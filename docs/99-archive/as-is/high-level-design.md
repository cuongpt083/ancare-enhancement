# Current High Level Design (HLD)

*Hệ thống:* ANCARES / SmartLife — Nền tảng Herbalife AI Coaching
*Phạm vi:* High-Level Design (HLD) toàn hệ thống — kiến trúc, thành phần, luồng xử lý, cơ chế LLM, hạ tầng.
*Trạng thái:* Draft v1 · *Cập nhật:* 2026-06-15 · *Nguồn canonical (Markdown + sơ đồ Mermaid):* file đính kèm {{ancares-hld.md}}.

h2. Version history

||Version||Ngày||Người sửa||Thay đổi||
|v1.0 (draft)|2026-06-15|Engineering|Bản HLD đầu tiên — sinh từ codebase hiện trạng (backend + mobile + infra + LLM).|

*Tài liệu liên quan:* SPEC.md, ARCHITECTURE.md, docs/caching.md, docs/roadmap-v3-architecture.md, docs/DATABASE_SCHEMA.md.

h2. 1. Giới thiệu & phạm vi

ANCARES là nền tảng huấn luyện sức khỏe/dinh dưỡng cho hệ sinh thái Herbalife, kết hợp AI (LLM đa nhà cung cấp) để: phân tích tư vấn onboarding, sinh lộ trình (roadmap) N ngày, đánh giá tiến độ hằng ngày, phân tích ảnh bữa ăn/vận động, và hỗ trợ chat coach↔khách hàng.

*Actors:*

||Actor||Vai trò||
|CUSTOMER|Người dùng cuối — log bữa ăn/vận động, check-in, xem lộ trình & báo cáo, chat, hỏi đáp AI.|
|COACH (NPP)|Nhà phân phối — quản lý khách hàng, gói dịch vụ, sinh roadmap, review báo cáo, prospect.|
|ADMIN|Quản trị nền tảng — duyệt coach, quản lý khách, knowledge base, system settings, audit.|

*Phạm vi:* backend API (FastAPI), worker (arq), mobile (RN/Expo), admin-web (Next.js), hạ tầng GKE, cơ chế LLM. Ngoài phạm vi: chi tiết UI từng màn (MOBILE_APP_FLOW.md), spec nghiệp vụ (SPEC.md).

h2. 2. Tổng quan kiến trúc

h3. 2.1 Context diagram

{code}
   [Mobile App RN/Expo]          [Admin Web Next.js]
          |  HTTPS /api/v1 + JWT        |
          |  WSS /api/v1/events         |
          v                             v
   +----------------------------------------------+
   |        ANCARES Platform (GKE)                |
   |   FastAPI API (2 replicas)  <--->  Redis     |
   |        |        ^                  (cache/    |
   |        v        | enqueue/dequeue   queue/    |
   |   PostgreSQL17  +---- arq Worker    pubsub)   |
   |   + pgvector          (x1)                    |
   +----------------------------------------------+
          |            |          |          |
          v            v          v          v
   LLM providers   Firebase    Google      Resend
   Gemini/DeepSeek   (FCM)    Cloud Storage (email OTP)
   /Anthropic
{code}

h3. 2.2 Tech stack

||Tầng||Công nghệ||
|Backend|FastAPI, SQLAlchemy 2.0 async, Pydantic v2, uv|
|DB|PostgreSQL 17 + pgvector (HNSW, vector 3072 chiều)|
|Queue/Cache|Redis 7 (arq jobs + 3-layer cache + WS pub/sub)|
|Worker|arq (cron + on-demand jobs)|
|LLM|Anthropic Claude · Google Gemini · DeepSeek (multi-provider fallback)|
|Mobile|Expo SDK 54, RN 0.81, React 19, expo-router 6, TanStack Query 5, Zustand 5, NativeWind 4, Reanimated 4|
|Admin Web|Next.js App Router, Tailwind, shadcn/ui, TanStack Query, pnpm workspace|
|Hạ tầng|GKE, Kustomize, ArgoCD, GitHub Actions, Artifact Registry, External Secrets (GCP SM), Google Managed Prometheus|

h2. 3. Thành phần hệ thống

h3. 3.1 API (FastAPI)
* App: {{FastAPI(title="Herbalife Coaching API", version="0.1.0")}}, prefix {{/api/v1/}}.
* Middleware (thứ tự): ETag → GZip (min 500B, trừ /metrics) → CORS → Idempotency (POST/PUT/PATCH theo Idempotency-Key).
* Endpoint hệ thống: {{GET /health}} (200 không auth), {{GET /metrics}} (Prometheus).
* Lifespan: startup mở arq pool + đăng ký cache policies + ORM after-commit hook + LRU cross-pod subscriber; shutdown drain WebSocket (timeout 20s) + đóng pool.

h3. 3.2 Backend modules (23 routers)

||Module||Path||Chức năng||
|auth|/auth|Login, refresh, logout, forgot/reset password (OTP Resend), coach signup policy.|
|users|/users|Profile CRUD, đổi mật khẩu, avatar, danh sách/chi tiết khách của coach, xoá mềm.|
|agents|/agents|Q&A coaching (QnAAgent, tool-use + RAG), package sales (SSE).|
|onboarding|/onboarding|Tanita intake, ConsultationAgent (async polling).|
|progress|/progress|Log bữa ăn/vận động + vision (Nutrition/Activity VisionAgent).|
|reports|/reports|Báo cáo AI hằng ngày; coach review/annotate.|
|roadmaps|/coaches·/users|Sinh roadmap (trigger + polling), đọc roadmap.|
|packages|/packages|Mua/gán gói, quản lý hết hạn.|
|coaches|/coaches|Gói NPP, team khách, doanh thu.|
|prospects|/coaches|Lead NPP (phân tích + chuyển đổi).|
|chat|/chat|Phòng community/direct + WebSocket; AI-draft chờ coach duyệt.|
|events|/events|WebSocket hợp nhất (PDF status, badge, reminder, chat).|
|dashboard|/|Tổng hợp sức khỏe (Tanita + logs + scores).|
|routes|/|Lộ trình ngày (menu/exercise/water/shake) — PREMIUM.|
|programs|/|Chương trình huấn luyện nhiều ngày.|
|knowledge|/knowledge·/admin/knowledge|RAG pgvector, ingest curriculum, bulk import.|
|notifications|/notifications|Đăng ký device FCM.|
|gamification|/gamification|Thành tích, badge, streak.|
|health_reports|/health-reports|Báo cáo sức khỏe mới nhất.|
|admin/*|/admin/*|Duyệt coach, quản khách, analytics, audit, settings.|

h3. 3.3 Worker (arq)
StatefulSet 1 replica, on-demand jobs + cron (§9). Mỗi job tự mở AsyncSession, idempotent, max retries 5.

h3. 3.4 Mobile app
* Navigation (expo-router): nhóm (auth)/(customer)/(coach); 5 tab/role (phone) hoặc sidebar (tablet). Auth guard redirect theo role.
* Data: axios {{lib/api.ts}} (base EXPO_PUBLIC_API_URL + /api/v1, inject JWT + refresh-on-401), TanStack Query, Zustand + SecureStore.
* Realtime: {{useEventStream}} (WSS /api/v1/events) route pdf.job.done, badge.awarded, checkin.reminder, chat.*.
* Cross-cutting: typography token-hoá (body 17pt) + accessibility scale; ImageViewer gallery; push notifications.

h3. 3.5 Admin Web
Next.js App Router + Tailwind + shadcn/ui + TanStack Query, tiêu thụ /admin/*. Deploy Vercel.

h2. 4. Mô hình dữ liệu

h3. 4.1 ERD (rút gọn)

{code}
users 1--1 health_profiles
users 1--* tanita_records
users 1--* daily_logs 1--* meal_logs
                      1--* activity_logs
users 1--* daily_reports
users 1--* customer_roadmaps
users 1--* package_purchases *--1 coaching_packages
users *--* users  (coach_customers: 1 coach : N khách, customer UNIQUE)
chat_rooms 1--* chat_messages *--1 users (sender)
knowledge_documents 1--* knowledge_chunks  (embedding vector 3072, HNSW)
users 1--* analyze_jobs | roadmap_jobs
{code}

h3. 4.2 Bảng trọng yếu
* *users* (PK uuid): role (ADMIN/COACH/CUSTOMER), *subscription_status* (FREE/PREMIUM — SSOT gating), is_approved (cổng duyệt coach), is_prospect, is_free_trial + free_trial_ends_at, deleted_at (xoá mềm), ai_data_sharing_enabled (consent AI), herbalife_code, referral_code.
* *coach_customers*: 1 coach : N khách; customer_id UNIQUE.
* *health_profiles* (1-1): tanita_data, goal, onboarding_status, consultation_*; target calories/macro/water/shake.
* *daily_logs* (UNIQUE user_id+log_date) → *meal_logs* (ảnh + analysis_status + ai_analysis JSONB) + *activity_logs*.
* *customer_roadmaps* (uuid): status (active/expired/archived), llm_status (pending/generating/done/failed), start/end/total_days, days_json, tanita_targets_json.
* *package_purchases* + *coaching_packages*: index (customer_id,status) & (status,end_date) cho cron hết hạn.
* *daily_reports* (UNIQUE user_id+report_date): analysis_text + JSONB (who_report, consult_article, habit_findings), source, annotation coach.
* *chat_rooms/chat_messages*: status (pending_ai/pending_coach/sent/dismissed), ai_draft, event_type, read_by JSONB.
* *knowledge_documents/chunks*: embedding Vector(3072) HNSW.
* *analyze_jobs/roadmap_jobs*: trạng thái async + error code/detail.

bq. *Ràng buộc:* FK chủ yếu ON DELETE CASCADE; chat_messages.sender_id SET NULL; package_purchases.package_id RESTRICT. Partial index users.email/phone (WHERE NOT NULL) và customer_roadmaps (WHERE status='active').

h2. 5. Luồng xử lý chính (sequence)

h3. 5.1 Đăng nhập & phân quyền
{code}
Mobile -> API: POST /auth/login {email,password,role hint}
API   -> DB : verify bcrypt + is_active + is_approved(coach) + deleted_at
API   -> Mobile: 200 {access_token HS256 60m, refresh_token 30d}
Mobile-> API: GET /protected (Bearer JWT)
API   : get_current_user (decode + check)
API   : require_paid_tier? COACH/ADMIN bypass; CUSTOMER FREE -> 402 X-Upgrade-Required
{code}

h3. 5.2 Log bữa ăn + phân tích vision
{code}
Customer -> API: POST /progress/meals (ảnh + meal_type)
API: lưu ảnh (GCS/local) + MealLog(status=PENDING)
API -> Worker: enqueue NutritionVision
Worker -> Claude Vision: ảnh -> calories/macros/food_items
Worker -> API: update MealLog(status=COMPLETED, ai_analysis)
=> Coach + Customer thấy phân tích ở dashboard/báo cáo
{code}
Bản coach multi-photo: tất cả ảnh của 1 bữa gửi trong *1* vision call, model tự quyết same-dish vs khác món.

h3. 5.3 Đánh giá hằng ngày (cron 20:00 VNT)
{code}
arq cron 13:00 UTC -> run_daily_evaluations()
  for each khách PREMIUM active:
    gom Tanita + daily_logs 7 ngày
    DailyEvaluationAgent (Claude, <=6 vòng)
    chain ConsultArticle -> HabitFindings
    tạo DailyReport (who_report, consult_article, habit_findings)
{code}

h3. 5.4 Sinh roadmap (v3, 2 pha)
{code}
Coach -> API: POST /coaches/.../roadmap/generate
API -> Worker: RoadmapJob(QUEUED) + trả job_id
Worker: Pha 1 Engine — khung ngày + tanita_targets
        -> CustomerRoadmap(llm_status=PENDING) ~2s
Worker: enqueue content_job (4x, 1 tuần/lần)
  for tuần W: Claude sinh nội dung -> days_json[W]; llm_status=GENERATING
Worker: tuần cuối -> llm_status=DONE
Mobile: poll roadmap theo llm_status
{code}

h3. 5.5 Mua gói & gating tier
{code}
Coach gán gói -> PackagePurchase(ACTIVE) + users.subscription_status=PREMIUM
  => PREMIUM mở khoá AI/route/roadmap
Cron 09:10 VNT run_package_expiry: ACTIVE&end<today -> EXPIRED; free-trial -> auto-renew
Cron 09:15 VNT run_roadmap_expiry: roadmap end<today -> EXPIRED
{code}

h3. 5.6 Chat AI-draft (coach duyệt)
Khách gửi tin → chat_messages(status=pending_ai) → sinh ai_draft(status=pending_coach) → coach duyệt/sửa → sent. Cron mỗi 6h {{apply_insights_to_profiles}} trích tín hiệu sức khỏe từ chat vào health_profile.

h2. 6. Cơ chế LLM service

bq. *Đáp ứng yêu cầu ANCARE01-1:* xử lý input/prompt-injection, system/user prompt & skills, caching, nhà cung cấp & quota.

h3. 6.1 Kiến trúc đa nhà cung cấp (fallback chain)

||Vai trò||Mặc định||Model||Dùng cho||
|LLM_PRIMARY|gemini|gemini-2.5-flash|Mặc định, độ trễ thấp|
|LLM_SECONDARY|deepseek|deepseek-chat (OpenAI-compatible)|Fallback khi primary lỗi tạm thời|
|LLM_INTENTIONAL|anthropic|claude-sonnet-4-5 (+ haiku-4-5)|Tác vụ cần Claude: roadmap, route, vision, evaluation|

* {{_resolve_providers(use_intentional)}} trả (default, fallback). Tác vụ "intentional" buộc dùng Claude.
* {{_is_transient(exc)}} phân biệt lỗi tạm thời (rate/timeout/5xx) → fallback provider phụ; lỗi vĩnh viễn thì không.
* Clients: claude_client / gemini_client / deepseek_client (cùng interface system/messages/tools).

h3. 6.2 Catalog agent (giới hạn vòng lặp & token)

||Agent||max_iterations||max_tokens||Mục đích||
|ConsultationAgent|12|8192|Phân tích tư vấn onboarding (WHO + DISC)|
|DailyEvaluationAgent|6|—|Đánh giá tiến độ ngày|
|QnAAgent|6|~1000|Hỏi đáp coaching (RAG + tool-use)|
|PackageSalesAgent|8|—|Tư vấn bán gói (SSE)|
|Nutrition/Activity VisionAgent|4|1024|Phân tích ảnh bữa ăn/vận động|
|ConsultArticle/HabitFindings/ProgressArticle|2|2–4k|Bài viết cá nhân hoá, habit scoring|
|ChatInsightAgent|1|1024|Trích tín hiệu sức khỏe từ chat|

h3. 6.3 System prompt, user prompt & skills (tool-use)
* *System prompt:* mọi agent nhúng {{AI_SAFETY_PREAMBLE}} lên đầu — quy tắc an toàn bắt buộc: (1) không chẩn đoán y tế, (2) nội dung phải dựa trên Knowledge Base, không bịa, (3) trung thực khi ngoài phạm vi, (4) khuyên gặp bác sĩ khi nghiêm trọng, (5) trả lời tiếng Việt, (6) chuyên nghiệp.
* *User prompt:* ngữ cảnh (Tanita, daily logs, goal…) build qua *tools/skills* nội bộ ({{app/agents/tools/}}): ai_coach_context, daily_data, health_metrics, health_analysis_builder, calories, who_standards, consultation_catalog, qna_data, subscription, package_sales, vision. Agent gọi tool theo *tool-use* trong vòng lặp ≤ max_iterations.
* "Skill" ở đây = bộ tool nội bộ + RAG (không dùng skill marketplace ngoài).

h3. 6.4 Xử lý input & phòng prompt-injection
* *Sanitize:* {{_sanitize_messages_for_claude()}} chuẩn hoá block (text/tool_use/tool_result) về dict hợp lệ trước khi gửi — chặn payload dị dạng.
* *Tách kênh tin cậy:* chỉ thị hệ thống ở system prompt (kênh riêng), dữ liệu/ảnh người dùng ở user/tool content → giảm khả năng input lật ngược chỉ thị.
* *Guardrail:* AI_SAFETY_PREAMBLE + grounding bắt buộc theo Knowledge Base (RAG). Có quy ước review prompt (agent ai-safety-reviewer).
* *Giới hạn vòng lặp* chặn loop/abuse.
* (!) *Gap:* chưa có classifier phát hiện prompt-injection chuyên dụng — xem §14.

h3. 6.5 Prompt caching
{{claude_client.py}} đánh {{cache_control: ephemeral}} lên *system prompt* và *tool cuối* → Anthropic cache khối đó + mọi thứ trước nó. Lần đầu phí cache-write (+25%), các lần sau trong *TTL 5 phút* chỉ tốn cache-read (~10% giá gốc) — rẻ ~10× cho replay trong tool-loop và giữa các lượt. Gemini dùng system-instruction caching tương đương.

h3. 6.6 RAG — Knowledge Base (pgvector)
Document → chunk (markdown qua Claude) → embed Vector(3072) → knowledge_chunks (HNSW). Truy vấn {{KnowledgeService.search()}} threshold ~0.65, top_k=3 → nhồi vào ngữ cảnh agent (đảm bảo nội dung "dựa trên chuyên gia").

h3. 6.7 Quota, rate-limit & kiểm soát chi phí
* *Rate limit per-user/agent:* {{AgentRateLimiter}} (Redis sliding-window) — mặc định *20 req/phút/user/agent* ({{agent_rate_limit_per_minute}}), *fail-open* khi Redis lỗi.
* *Giới hạn cấp request:* max_iterations + max_tokens mỗi agent (§6.2).
* *PDF render:* slowapi limiter riêng → 429 ErrorResponse.
* *Consent gate:* 403 nếu ai_data_sharing_enabled=false (Apple 5.1.1(i)).
* *Provider quota:* nằm phía nhà cung cấp qua API key (GCP Secret Manager); chưa có hard cap chi phí nội bộ — xem §14.

h2. 7. Xác thực & phân quyền
* *JWT:* HS256, payload {sub,role,exp}, access 60′ + refresh 30 ngày, issuer nội bộ.
* *Roles:* ADMIN/COACH/CUSTOMER. *Tiers* (SSOT subscription_status): FREE vs PREMIUM; COACH/ADMIN bypass.
* *Gates:* get_current_user, require_admin, require_paid_tier (402 nếu FREE), require_role. Coach is_approved=false → login 403; có thể bật coach_auto_approve.

h2. 8. Caching layer
Ba tầng (docs/caching.md): (1) Policy Registry khai báo; (2) Repository + {{@cached}} dispatch Redis/LRU, swallow lỗi (degrade→miss); (3) Invalidation qua SQLAlchemy after_commit hook + LRU cross-pod Pub/Sub.

||Namespace||Layer||TTL||Mục đích||
|user.me|redis|300s|Profile người dùng|
|coach.customer.detail|redis|180s|Chi tiết khách + roadmap + 7-day logs|
|coach.customer.progress_reports|redis|120s|Báo cáo khách (phân trang)|
|static.kb_reference_tables|lru|3600s|Bảng tham chiếu KB (in-process)|

Cache là hint, không phải contract; payload >1MB bỏ qua; metrics Prometheus (cache_ops_total, cache_invalidation_total, cache_value_size_bytes).

h2. 9. Tác vụ bất đồng bộ & cron
*On-demand:* analyze_consultation, generate_roadmap_v3 (+content), generate_roadmap_v1, prospect_analyze, ingest_curriculum_pdf, finalize_curriculum, ingest_prechunked_zip, render_progress_report_pdf.

||UTC||VNT||Job||Mục đích||
|13:00|20:00|run_daily_evaluations|Đánh giá AI hằng ngày (PREMIUM)|
|11:30|18:30|run_upload_reminders|Nhắc log bữa ăn|
|17:05|00:05|nightly_engagement_decay|Giảm điểm engagement|
|17:30|00:30|cleanup_old_analyze_jobs|Xoá AnalyzeJob >7 ngày|
|20:00|03:00|cleanup_old_notifications|Xoá notification >90 ngày|
|02:00|09:00|notify_packages_expiring|Nhắc gói sắp hết hạn|
|02:10|09:10|run_package_expiry|Hết hạn gói + auto-renew free-trial|
|02:15|09:15|run_roadmap_expiry|Hết hạn roadmap|
|{0,6,12,18}:15|mỗi 6h|apply_insights_to_profiles|Trích insight chat → profile|

h2. 10. Hạ tầng & triển khai
* *Local* (docker-compose): db (pgvector pg17 5434), redis (6381), migrate (alembic), backend (uvicorn 8002), worker (arq). Mobile↔backend qua adb reverse + EXPO_PUBLIC_API_URL.
* *GKE* (Kustomize): base = api Deployment (2 replicas, graceful 130s), worker StatefulSet (1), redis, migration Job (PreSync), seed Job (PostSync), external-secrets (GCP SM/Workload Identity), monitoring (PodMonitoring), ingress + managed-certificate. Overlays dev (auto-sync) / prod (*manual-sync*).
* *ArgoCD:* app-of-apps; ancares-prod không auto-sync → bump image xong sync tay; PreSync migration → Sync → PostSync seed.
* *CI/CD:* backend-deploy (Test→Build→Bump tag), web-build-deploy (tsc+typography+jest+expo web→Vercel), eas-build (iOS), deploy-admin-dashboard (tsc+vitest+build→Vercel).

h2. 11. Observability
{{/metrics}} (Prometheus classic 0.0.4) → Google Managed Prometheus (PodMonitoring namespaced, scrape ancares-api 30s; worker không expose HTTP). Metrics cache/agent/chat/job. Logging theo domain (app.validation, app.cache.repo, app.orm_hook, app.agents — log token in/out).

h2. 12. Bảo mật & tuân thủ
* Apple 5.1.1(i): consent ai_data_sharing_enabled trước khi gửi PII cho LLM.
* Apple 5.1.1(v): xoá tài khoản mềm deleted_at; JWT cũ bị từ chối 401.
* GDPR: soft-delete + SET NULL; audit log mọi hành động admin.
* JWT HS256 (secret Secret Manager); rate limit agent 20/phút + PDF slowapi; CSV-injection safe cho export.

h2. 13. Yêu cầu phi chức năng
* *Scalability:* API stateless scale ngang (HPA); worker singleton (cron không trùng); Redis pub/sub đồng bộ cache đa pod.
* *Availability:* graceful drain WS 20s + headroom 120s; readiness /health; PDB.
* *Resilience:* LLM fallback đa provider; cache degrade→miss; job retry 5 + idempotent.
* *Performance:* prompt caching (~10× rẻ), ETag/GZip, 3-layer cache, roadmap engine trả khung ~2s rồi fill LLM async.

h2. 14. Rủi ro & nợ kỹ thuật
* *Prompt-injection:* chưa có classifier chuyên dụng; phụ thuộc tách kênh + safety preamble + grounding RAG. Đề xuất: thêm lớp phát hiện injection cho input QnA.
* *Chi phí LLM:* chưa có hard cap nội bộ (chỉ rate-limit req/phút). Đề xuất: budget/ngày theo user/tenant.
* *Worker đơn:* 1 replica + queue đơn — nghẽn khi nhiều job nặng. Đề xuất: queue riêng PDF/roadmap khi >500 job/ngày.
* *Rate limiter fail-open:* Redis lỗi → bỏ qua giới hạn (ưu tiên availability), cần theo dõi.
* *prod manual-sync:* cần thao tác tay sau mỗi deploy backend (chủ ý).

----

h2. Phụ lục A — Yêu cầu gốc

bq. Trích nguyên văn mô tả ban đầu của issue ANCARE01-1 (reporter: Cường Phạm Thanh) — tài liệu này được viết để đáp ứng các mục dưới đây.

* Thiết kế tổng quát các thành phần hệ thống → *§2, §3*
* Luồng xử lý của hệ thống (sequence diagram) → *§5*
* Cơ chế gọi LLM service → *§6*:
** xử lý input, prompt-injection → §6.4
** system-prompt, user-prompt, skill → §6.3
** caching → §6.5
** LLM provider nào, quota limit → §6.1, §6.7

----
*Sinh tự động từ codebase hiện trạng. Canonical Markdown (kèm sơ đồ Mermaid) ở file đính kèm {{ancares-hld.md}}.*
