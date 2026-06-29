# Software Requirements Specification (SRS) — AnCare DXP

**Phiên bản:** v0.1 (draft) · **Cập nhật:** 2026-06-18 · **Định dạng:** Hybrid (IEEE-830 rút gọn + Functional Requirements có mã + User Story & Acceptance Criteria).
**Phạm vi:** Toàn bộ cây chức năng (`docs/to-be/feature-tree.md`). Phần chưa thiết kế sâu được đánh dấu **`[TBD]`** / **Open question**.

> **Cách đọc:** Mỗi yêu cầu chức năng có mã `FR-<MODULE>-<n>`, độ ưu tiên (P0 bắt buộc / P1 / P2), trạng thái thiết kế (✅ đã thiết kế / 🔶 một phần / 🔜 TBD), và (khi đã rõ) User Story + Acceptance Criteria (AC, dạng Given/When/Then). Chi tiết logic/dữ liệu trỏ tới các tài liệu nguồn để tránh lặp.

**Tài liệu nguồn (canonical):**
- Hiện trạng kỹ thuật: `docs/as-is/high-level-design.md` (kiến trúc, auth, LLM, cron).
- Nghiệp vụ: `docs/to-be/Workflow-HLV.md`, `docs/to-be/Workflow-KH.md`.
- UI-UX: `docs/srs/UI-UX-HLV_v1.1.md`, `docs/srs/UI-UX-Lo-trinh-Dong-ho-sinh-hoc_v1.0.md`.
- Dữ liệu: `docs/technical/customer-persona-data-model_v1.0.md`.
- Quy tắc: `docs/business-rules/Calorie-Meal-Business-Rules-v1.0.md`, `docs/business-rules/packaged-service-advice-v1.0.md`.
- Cây chức năng: `docs/to-be/feature-tree.md`.

---

## 1. Giới thiệu

### 1.1 Mục đích
Đặc tả yêu cầu phần mềm cho **AnCare DXP** — nền tảng trải nghiệm số chăm sóc sức khỏe chủ động, đồng hành quy trình kinh doanh Nutrition Club (Herbalife), làm cơ sở để đội phát triển lập trình, kiểm thử và nghiệm thu.

### 1.2 Phạm vi sản phẩm
AnCare hỗ trợ hai vai trò chính — **Huấn luyện viên dinh dưỡng (HLV)** và **Khách hàng (KH)** — xuyên suốt: thu hút & tư vấn KH tiềm năng → chuyển đổi → chăm sóc theo lộ trình (Thân–Tâm–Trí) → phát triển bản thân & hệ thống kinh doanh. AnCare **không** làm POS/kho/quản trị KD (thuộc VNHUB) và **không** tích hợp kỹ thuật với VNHUB/Learning/SHOP/Pro2col (xem ràng buộc §7).

### 1.3 Định nghĩa & viết tắt (Glossary)
| Thuật ngữ | Ý nghĩa |
|---|---|
| HLV | Huấn luyện viên dinh dưỡng (nhà phân phối) |
| KH / KHTN | Khách hàng / Khách hàng tiềm năng (lead) |
| DISC | Mô hình tính cách D/I/S/C |
| Stage-of-Change | Giai đoạn sẵn sàng thay đổi |
| Persona | Chân dung khách hàng |
| Tanita | Cân phân tích thành phần cơ thể |
| TMR / RMR / AMR | Tổng/Nghỉ/Hoạt động — năng lượng tiêu hao |
| Đồng hồ sinh học | Widget 24h trên màn "Sức khỏe tổng thể" |
| Thân–Tâm–Trí | 3 trụ cột lộ trình (thể chất · lối sống/cảm xúc · kiến thức) |
| NBA | Next-Best-Action — gợi ý hành động kế tiếp |
| DMO | Daily Method of Operation — phương pháp vận hành hằng ngày |
| GNV | Giấy nhắc việc |
| HOM | Buổi sinh hoạt nhóm dinh dưỡng |

### 1.4 Vai trò người dùng (Actors)
- **CUSTOMER (KH):** xem lộ trình, check-in hằng ngày, gợi ý bữa ăn, chat, học tập.
- **COACH (HLV):** quản lý KH tiềm năng/KH, tư vấn, tạo tài khoản & gói, chăm sóc, phát triển bản thân & hệ thống; **đồng thời là một "người dùng sức khỏe"** (làm gương).
- **ADMIN:** duyệt HLV, quản trị nội dung/Knowledge Base, cấu hình, audit (chi tiết `high-level-design.md §3.2`).

### 1.5 Tổng quan hệ thống (tham chiếu)
Kiến trúc, hạ tầng, cơ chế LLM đa nhà cung cấp, caching, cron — xem `docs/as-is/high-level-design.md`. SRS này tập trung **yêu cầu chức năng & phi chức năng theo tính năng**.

---

## 2. Mô tả tổng thể

### 2.1 Bản đồ module → mã FR
| Module | Mã | Trạng thái |
|---|---|---|
| Xác thực & phân quyền | FR-AUTH | 🔶 (có ở HLD) |
| KH tiềm năng | FR-LEAD | ✅ |
| Chân dung KH + DISC | FR-PERSONA | ✅ |
| Tư vấn 15' (Tanita→Bản tư vấn→Mục tiêu→Gói→Tạo TK) | FR-CONSULT | ✅ |
| Gợi ý bữa ăn (3 nhóm, đa phiên bản) | FR-MEAL | ✅ |
| Sức khỏe của tôi (đồng hồ sinh học, check-in) — dùng chung KH & HLV | FR-HEALTH | ✅ |
| Cá nhân hóa thời gian biểu | FR-SCHEDULE | ✅ |
| Chăm sóc KH (HLV) | FR-CARE | 🔶 |
| Chat & Cộng đồng | FR-COMM | 🔶 (có ở HLD) |
| Báo cáo & Nhật ký (Infographic) | FR-REPORT | 🔜 |
| Đào tạo / micro-course / talking points | FR-TRAIN | 🔜 |
| Phát triển bản thân + Sơ đồ trả thưởng | FR-SELFDEV | 🔜 |
| Chăm sóc hệ thống KD / Thành viên / DMO | FR-BIZSYS | 🔜 |
| Kho sự kiện | FR-EVENT | 🔜 |
| Lịch 168 (tích hợp Google Calendar) | FR-CAL | 🔜 |
| Trợ lý AI & Xử lý từ chối | FR-AIASSIST | 🔶 |
| Mục tiêu (KH/HLV) | FR-GOAL | ✅ |
| Thông báo & Nhắc việc | FR-NOTIF | 🔶 (FCM ở HLD) |
| Màn hình chính & điều hướng | FR-UI | ✅ |

### 2.2 Nguyên tắc thiết kế ràng buộc (design constraints as requirements)
- **Hợp nhất "Sức khỏe của tôi":** Chăm sóc KH ∩ Chăm sóc bản thân dùng **chung một module sức khỏe** (FR-HEALTH). HLV dùng chính module này để **làm gương** và chia sẻ (xem FR-HEALTH & FR-COMM).
- **AI hỗ trợ, không thay người & không thao túng.** Mọi gợi ý AI phải để con người duyệt/chỉnh.
- **Consent-gated AI:** chỉ xử lý dữ liệu cá nhân qua LLM khi `ai_data_sharing_enabled=true`.
- **Tách nghiệp vụ vs trình bày:** logic (calo, gói, %) theo business-rules; DISC chỉ điều chỉnh tông giọng.

### 2.3 Giả định & phụ thuộc
- Có API/dịch vụ **OCR/Vision** đọc phiếu Tanita & ảnh món ăn; có **catalog món ăn** + API tính calo (`[TBD]` nguồn dữ liệu chính thức).
- Có **catalog gói dịch vụ** (`coaching_packages`) với thời lượng/sản phẩm (`[TBD]` dữ liệu thật).
- Tích hợp **Google Calendar** cho Lịch 168 (`[TBD]` phạm vi đồng bộ 2 chiều).
- LLM đa nhà cung cấp theo HLD.

---

## 3. Yêu cầu chức năng — phần ĐÃ THIẾT KẾ (chi tiết)

### FR-AUTH — Xác thực & phân quyền (P0, 🔶)
- **FR-AUTH-1** Đăng nhập/đăng ký/khôi phục mật khẩu (OTP email) theo role; JWT access 60' + refresh 30 ngày. *(HLD §5.1, §7)*
- **FR-AUTH-2** Phân quyền ADMIN/COACH/CUSTOMER; gating FREE/PREMIUM; HLV cần `is_approved`.
- **FR-AUTH-3** Consent `ai_data_sharing_enabled`: chặn gửi PII cho LLM nếu tắt (402/403 phù hợp).
- **AC:** Given KH FREE, When gọi tính năng PREMIUM, Then trả 402 kèm cờ nâng cấp.

### FR-LEAD — Danh sách KH tiềm năng (P0, ✅)
- **US:** *Là HLV, tôi muốn quản lý danh sách lead kèm chân dung/DISC/giai đoạn và việc cần làm tiếp, để biết hôm nay nên tiếp cận ai.*
- **FR-LEAD-1** Hiển thị danh sách lead: tên, thẻ DISC, Stage, nguồn (nóng/ấm/lạnh), `lead_score`, "việc cần làm tiếp".
- **FR-LEAD-2** Tìm kiếm + lọc theo nguồn/giai đoạn/cần theo dõi.
- **FR-LEAD-3** Nhóm "Hôm nay nên tiếp cận" theo `lead_score` + cadence.
- **FR-LEAD-4** Nút "+" tạo KH tiềm năng mới (→ FR-CONSULT-1).
- **FR-LEAD-5** Chống trùng lead; import danh bạ/MXH `[TBD nguồn import]`.
- **AC:** Given danh sách >0 lead, When mở màn, Then sắp xếp nhóm "hôm nay nên tiếp cận" theo điểm giảm dần; mỗi lead hiện đúng thẻ DISC & giai đoạn.
- **UI:** `prototypes/hlv/hlv_danh_sach_kh_tiem_nang.html`.

### FR-PERSONA — Chân dung KH + DISC (P0, ✅)
- **US:** *Là HLV, tôi muốn thu thập chân dung + nhận diện DISC qua bộ câu hỏi, lưu cả câu hỏi–câu trả lời để AI suy luận chính xác.*
- **FR-PERSONA-1** Mô hình **2 bảng**: `users` (cơ bản) + `customer_personas` (1:1, JSONB linh hoạt). *(data-model doc)*
- **FR-PERSONA-2** Lưu `survey_responses[]` gồm `qid` + **nguyên văn câu hỏi** + câu trả lời + nhãn (disc_signal/stage_signal/sp_category).
- **FR-PERSONA-3** Cột "nóng" có index: `disc_primary`, `stage`, `funnel_stage`, `lead_score`, `primary_goal`, `source`.
- **FR-PERSONA-4** AI suy luận DISC/Stage **từ Q&A**, ghi `provenance` kèm `evidence=[qid...]` + độ tin cậy (self_reported/inferred/coach_tagged); HLV xác nhận/ghi đè.
- **FR-PERSONA-5** Chỉ chạy suy luận AI khi consent bật.
- **AC:** Given KH trả lời ≥1 câu khảo sát, When lưu, Then tạo phần tử `survey_responses[]` và (nếu consent) sinh gợi ý DISC kèm evidence; HLV sửa được nhãn.

### FR-CONSULT — Tư vấn 15 phút (P0, ✅)
- **US:** *Là HLV mới, tôi muốn chuẩn bị tư vấn cá nhân hóa cho 1 KH trong vài phút thay vì 30–45 phút.*
- **FR-CONSULT-1** Màn "Tạo KH tiềm năng mới": Card *Thông tin cơ bản* (→`users`, gồm chiều cao, consent) + Card *Chân dung KH* (→`customer_personas`). Chỉ Họ tên bắt buộc; accordion/progressive disclosure.
- **FR-CONSULT-2** Màn "Nhập chỉ số Tanita": nhập tay **hoặc** chụp/chọn ảnh → OCR tự điền (đánh dấu giá trị AI, sửa được); chiều cao lấy từ hồ sơ; tự tính BMI. CTA bật khi đủ chỉ số.
- **FR-CONSULT-3** Màn "Bản tư vấn": Card *Những điểm cần cải thiện* (chi tiết Phân tích hiện trạng + Nguy cơ bệnh lý) + Card *Bảng phân tích chỉ số chi tiết* (đối chiếu chuẩn WHO/Tanita; mặc định 2 dòng + "xem thêm"; ghi nguồn). 2 nút: Tiếp tục / Hoàn tất (NBA).
- **FR-CONSULT-4** Màn "Thiết lập mục tiêu": thu thập mục tiêu + **thời hạn mong muốn** + thói quen + bệnh lý; tính **lộ trình**: chọn **gói (tên sản phẩm + thời gian, mặc định 3 tháng)** → tính lại **% đạt được mọi mục tiêu**; tinh chỉnh mục tiêu (đòn bẩy phụ). 2 nút: Tạo tài khoản KH / Hoàn tất.
- **FR-CONSULT-5** Màn "Tạo tài khoản KH": email, mật khẩu, mã giới thiệu; gói + **ngày bắt đầu (auto, sửa 1 lần)** + **ngày kết thúc (auto theo số tháng)**; lưu mục tiêu chỉ số; ảnh check-in (chân dung/toàn thân/vòng eo).
- **FR-CONSULT-6** Xử lý từ chối & chốt gói: gợi ý kịch bản theo nhóm phản đối (đắt/rẻ, phụ thuộc SP, tái béo, đa cấp, đói) `[TBD nội dung kịch bản — anh Đức]`.
- **FR-CONSULT-7** Disclaimer bắt buộc hiển thị: "không thần dược…".
- **AC:** Given đã nhập đủ Tanita, When bấm "Tạo bản Tư Vấn", Then hiển thị bản tư vấn đối chiếu chuẩn & danh sách điểm cần cải thiện; thời gian thao tác mục tiêu ≤ ~7 phút/KH.
- **UI:** `prototypes/hlv/hlv_tao_kh_tiem_nang.html`, `hlv_nhap_chi_so_tanita.html`, `hlv_ban_tu_van.html`, `hlv_thiet_lap_muc_tieu.html`, `hlv_tao_tai_khoan_kh.html`.

### FR-MEAL — Gợi ý bữa ăn (P0, ✅)
- **US:** *Là HLV/KH, tôi muốn thực đơn cá nhân hóa theo mục tiêu, cấu trúc 3 nhóm thực phẩm, cập nhật mỗi 10 ngày.*
- **FR-MEAL-1** Tính "con số kỳ diệu" (RMR+AMR+EX=TMR → magic calo theo mục tiêu/tuổi/bệnh lý) — `Calorie-Meal §I`.
- **FR-MEAL-2** Cấu trúc **mỗi bữa = 3 nhóm**: Đạm (calo + **đạm g mục tiêu**), Xơ (calo), Đường/bột (calo); chọn món từ catalog tương ứng — `Calorie-Meal §2.1b`.
- **FR-MEAL-3** Số bữa theo cấu hình KH (3/4/5).
- **FR-MEAL-4** **Đa phiên bản**: mỗi gợi ý hiệu lực **10 ngày**; lưu lịch sử; trạng thái active/expired; HLV "đánh giá lại → tạo phiên bản mới". Cấu trúc dữ liệu: `Workflow-HLV §3`.
- **FR-MEAL-5** Ghi nhận bữa ăn (KH): chụp ảnh → **AI bóc tách món + đơn vị (bát/lạng) + số lượng (sửa được)**; hoặc nhập tay form → **API tính calo/đạm**.
- **FR-MEAL-6** KH xem thực đơn hiện tại + phiên bản hiệu lực; hỏi HLV qua chat (→ FR-COMM).
- **FR-MEAL-7** Ràng buộc chế độ: hạn chế thịt đỏ/chiên-xào; nước ≥ 0,4 L/10 kg/ngày.
- **AC:** Given phiên bản #n hết 10 ngày, When HLV tạo phiên bản mới, Then #n chuyển `expired`, #n+1 `active`, lịch sử giữ nguyên; KH thấy phiên bản active.
- **Open question:** catalog món ăn & hệ số đơn vị chính thức (`[TBD]` — tham khảo của anh Hoàng).
- **UI:** `prototypes/hlv/hlv_goi_y_bua_an.html`, `prototypes/kh/goi_y_bua_an.html`.

### FR-SCHEDULE — Cá nhân hóa thời gian biểu (P1, ✅)
- **US:** *Là KH, tôi muốn tùy chỉnh số bữa & giờ từng hoạt động sao cho thực hiện được, hiểu rằng lệch nhịp sinh học sẽ giảm điểm.*
- **FR-SCHEDULE-1** Chọn số bữa (3/4/5) → sinh đúng số nhiệm vụ ăn.
- **FR-SCHEDULE-2** Chọn giờ bắt đầu/kết thúc từng hoạt động (thức dậy, thải độc, bữa ăn, ngủ trưa, thể dục, thư giãn/thiền, PTBT, ngủ tối).
- **FR-SCHEDULE-3** Tính **mức tối ưu (%)** + **điểm tối đa/ngày**: lệch khung tối ưu → giảm trần điểm (3/2/1).
- **AC:** Given KH đổi giờ lệch khung, When cập nhật, Then % tối ưu & điểm tối đa giảm tương ứng; lưu cho màn hằng ngày.
- **UI:** `prototypes/kh/ca_nhan_hoa_thoi_gian_bieu.html`.

### FR-HEALTH — "Sức khỏe của tôi" (đồng hồ sinh học) — dùng chung KH & HLV (P0, ✅)
> Hợp nhất *Chăm sóc bản thân* + phần sức khỏe của *Chăm sóc KH*; HLV dùng để làm gương.
- **US (KH):** *Tôi muốn check-in nhiệm vụ ngày theo đồng hồ sinh học, được chấm điểm và tổng kết cuối ngày.*
- **US (HLV):** *Tôi muốn tự thực hiện & chia sẻ kết quả như một KH để làm gương.*
- **FR-HEALTH-1** Widget **đồng hồ sinh học 24h** chia múi theo hoạt động, tô màu trạng thái; kim thời gian thực; quick stats (điểm/Calo/nước).
- **FR-HEALTH-2** Danh sách hoạt động chia **2 vùng** "đã/chờ thực hiện"; tick xong → chuyển vùng.
- **FR-HEALTH-3** **Chấm điểm mỗi lần tick** (3 đúng lịch / 2 trễ / 1 một phần / 0 chưa) = **bản ghi nhật ký**; tổng điểm ngày lũy kế (nền tảng streak & credit — *credit chưa triển khai*).
- **FR-HEALTH-4** **Uống nước ghi nhận nhiều lần** (mỗi cốc ~250ml), mục tiêu `0.4–0.7 × kg`.
- **FR-HEALTH-5** Tự phân tích Calo in/out, nước (đối chiếu mục tiêu R).
- **FR-HEALTH-6** **Trang chủ tổng kết cuối ngày (~22h)**: đủ đạm/calo/nước/ngủ, % hoàn thành, chấm điểm từng hoạt động, lưu ý cải thiện; đánh giá % theo ngày/tuần (6 yếu tố).
- **FR-HEALTH-7** **HLV làm gương**: HLV thực hiện cùng module và **chia sẻ ảnh/kết quả** qua chat/cộng đồng (→ FR-COMM).
- **AC:** Given KH tick 1 nhiệm vụ đúng khung giờ, When xác nhận, Then +3 điểm, thẻ chuyển sang "đã thực hiện", đồng hồ cập nhật màu & tổng điểm.
- **UI:** `prototypes/kh/suc_khoe_tong_the.html`, `trang_chu.html`.

### FR-GOAL — Mục tiêu (P1, ✅)
- **FR-GOAL-1** Mục tiêu KH (cân nặng/chỉ số/thói quen) + thời hạn; là đầu vào FR-MEAL & FR-HEALTH.
- **FR-GOAL-2** Mục tiêu HLV (kinh doanh/phát triển) `[TBD chi tiết]`.

### FR-UI — Màn hình chính & điều hướng (P0, ✅)
- **FR-UI-1** Điều hướng KH: Trang chủ · Chăm sóc · Chat · Hồ sơ (`prototypes/kh/`).
- **FR-UI-2** Điều hướng HLV: Tổng quan · KH tiềm năng · Chat · Hồ sơ (`prototypes/hlv/`).
- **FR-UI-3** Màn hình chính có **menu shortcut**; cân nhắc **floating-bubble tùy biến** (tư vấn 15', CSKH, đào tạo hệ thống, kết nối cộng đồng, xử lý từ chối) `[TBD chi tiết hành vi bubble]`.
- **FR-UI-4** Dashboard HLV: KPI (KH/lead/hôm nay nên tiếp cận/**gợi ý bữa ăn cần làm mới**), cảnh báo, KH cần chú ý.
- **FR-UI-5** Chi tiết KH: hồ sơ, Tanita, mục tiêu, ảnh check-in, gợi ý bữa ăn (phiên bản + lịch sử), hành động (tiến độ/điều chỉnh mục tiêu/chat).
- **UI:** `prototypes/hlv/hlv_tong_quan.html`, `hlv_chi_tiet_kh.html`, `prototypes/kh/trang_chu.html`.

---

## 4. Yêu cầu chức năng — phần MỘT PHẦN / TBD

### FR-CARE — Chăm sóc KH (HLV) (P1, 🔶)
- **FR-CARE-1** ✅ Phân tích sức khỏe hằng ngày → tư vấn hành động, gợi ý nâng cấp SP (một phần qua FR-HEALTH/FR-MEAL).
- **FR-CARE-2** 🔜 **Nhắc HLV kết nối KH sau [N] giờ/ngày chưa liên lạc** (mặc định 72h) + hoạt động tiếp theo. `[TBD ngưỡng cấu hình]`.
- **FR-CARE-3** 🔜 **Nhắc tặng quà theo tuần** (quà theo nhu cầu: HOM, coaching, nuôi dạy con, jumping…). `[TBD danh mục quà & logic]`.
- **FR-CARE-4** 🔜 **Cảnh báo KH chưa tương tác trong ngày**.
- **FR-CARE-5** ✅ AI tự phân tích ảnh bữa ăn KH & gửi lại (gắn FR-MEAL-5).
- **FR-CARE-6** 🔜 21 talking points đi kèm kiến thức + kiểm tra 2 câu hỏi (gắn FR-TRAIN).
- **Open question:** kênh nhắc (push/zalo?), nội dung mẫu, quyền riêng tư khi theo dõi tương tác.

### FR-COMM — Chat & Cộng đồng (P1, 🔶)
- **FR-COMM-1** ✅ Chat KH ↔ HLV (có ở HLD: AI-draft chờ HLV duyệt); hỏi đáp về thực đơn (gắn FR-MEAL-6).
- **FR-COMM-2** 🔶 Chat cộng đồng/nhóm dinh dưỡng; chia sẻ ảnh/kết quả (HLV làm gương, KH khoe tiến bộ).
- **FR-COMM-3** 🔜 Gợi ý sự kiện/nhóm dinh dưỡng phù hợp trong hội thoại.
- **Open question:** mô hình nhóm (1 club/nhiều club), kiểm duyệt nội dung.

### FR-AIASSIST — Trợ lý AI & Xử lý từ chối (P1, 🔶)
- **FR-AIASSIST-1** 🔶 **NBA**: gợi ý hành động kế tiếp theo DISC + Stage (gặp 2:1 với ai, câu hỏi theo DISC, câu chuyện tương đồng, tài liệu/sự kiện/nhóm phù hợp, kịch bản tư vấn/chốt).
- **FR-AIASSIST-2** 🔜 Trợ lý AI trả lời câu hỏi KH theo **Sơ đồ dẫn** (thời điểm nâng cấp SP, nên gặp 2:1 ai, sự kiện/tài liệu nào).
- **FR-AIASSIST-3** 🔜 **Engine xử lý từ chối**: bộ câu hỏi + kịch bản theo nhóm phản đối.
- **Ràng buộc:** AI hỗ trợ, HLV duyệt; consent-gated; chống prompt-injection (HLD §6.4).
- **Open question:** nguồn tri thức Sơ đồ dẫn, mức tự động hóa cho phép.

### FR-NOTIF — Thông báo & Nhắc việc (P1, 🔶)
- **FR-NOTIF-1** ✅ Hạ tầng push FCM (HLD).
- **FR-NOTIF-2** ✅ Nhắc theo mốc giờ hoạt động (FR-HEALTH) + loại xác nhận (ảnh/tick).
- **FR-NOTIF-3** 🔜 Nhắc HLV (FR-CARE-2/3/4), nhắc KH công việc/sự kiện.
- **Open question:** ma trận loại thông báo × kênh × tần suất.

### FR-REPORT — Báo cáo & Nhật ký Infographic (P2, 🔜)
- **FR-REPORT-1** 🔜 Báo cáo hành trình thay đổi thể chất/tinh thần (đo lường được) + thói quen/kiến thức/lan tỏa.
- **FR-REPORT-2** 🔜 **Biểu đồ cải thiện chỉ số** theo thời gian (KH).
- **FR-REPORT-3** 🔜 **Trình tạo Nhật ký (Infographic)** để chia sẻ: tóm lược bài học, hành trình bữa ăn/thể chất, ảnh.
- **Open question:** bộ chỉ số báo cáo chuẩn, template infographic, công cụ render.

### FR-TRAIN — Đào tạo / Micro-course / Talking points (P1, 🔜)
- **FR-TRAIN-1** 🔜 Micro-course (khóa ngắn) đa chủ đề (dinh dưỡng, sản phẩm, kỹ năng, nhóm bệnh lý) + **gamification** (thi đua).
- **FR-TRAIN-2** 🔜 **21 bài kiến thức cơ bản** + chủ đề chuyên sâu; talking points kèm giới thiệu SP.
- **FR-TRAIN-3** 🔜 Kiểm tra kiến thức: trả lời các câu hỏi ("ấn tượng nhất điều gì", "chia sẻ cho ai", "hành động là gì").
- **FR-TRAIN-4** 🔜 Điều kiện hoàn thành trước khi học bài tiếp.
- **Open question:** cấu trúc khóa học, nguồn nội dung (chị Mai/Hương/Đức), cơ chế chấm/điểm thưởng.

### FR-SELFDEV — Phát triển bản thân + Sơ đồ trả thưởng (P2, 🔜)
- **FR-SELFDEV-1** 🔜 Lộ trình đào tạo HLV (kỹ năng KD/tâm thế/SP/mạng lưới/thấu hiểu).
- **FR-SELFDEV-2** 🔜 **Sơ đồ trả thưởng (comp plan)** — hiển thị/định hướng thăng tiến.
- **Cảnh báo:** comp plan **nhạy cảm pháp lý (đa cấp)** — cần rà tuân thủ; có thể chỉ hiển thị thông tin, không tính thưởng. **Open question** lớn.

### FR-BIZSYS — Chăm sóc hệ thống KD / Thành viên / DMO (P2, 🔜)
- **FR-BIZSYS-1** 🔜 Danh sách thành viên (tuyến dưới) + chi tiết.
- **FR-BIZSYS-2** 🔜 Gợi ý DMO / nhóm dinh dưỡng-Fit club / bước tiếp theo (Vòng tròn thành công).
- **FR-BIZSYS-3** 🔜 Đào tạo thành viên (kiểm tra, tài liệu).
- **Open question:** ranh giới với VNHUB (tránh trùng), mô hình tuyến.

### FR-EVENT — Kho sự kiện (P2, 🔜)
- **FR-EVENT-1** 🔜 Danh mục sự kiện (HOM, workshop…), đăng ký/nhắc, gợi ý sự kiện phù hợp KH.
- **Open question:** nguồn sự kiện, lịch, điểm danh.

### FR-CAL — Lịch 168 (tích hợp Google Calendar) (P2, 🔜)
- **FR-CAL-1** 🔜 Tích hợp Google Calendar (đồng bộ `[TBD 1 chiều/2 chiều]`).
- **FR-CAL-2** 🔜 Nhắc **5 việc lặp lại hằng ngày** (lên lịch+biết ơn+ghi âm; đăng MXH 3 lần/ngày; nhắn hỏi thăm; phát triển bản thân; học kỹ năng).
- **FR-CAL-3** 🔜 3 danh sách "5 người/ngày" (KH cần chăm · TV cần dẫn · KH tiềm năng cần nói chuyện) + lịch sự kiện.
- **Open question:** OAuth Google, quyền riêng tư lịch cá nhân.

---

## 5. Yêu cầu giao diện ngoài (External Interfaces)
- **OCR/Vision API:** đọc phiếu Tanita (FR-CONSULT-2) & ảnh món ăn (FR-MEAL-5). `[TBD nhà cung cấp/độ chính xác]`.
- **API tính Calo / Catalog món ăn:** (FR-MEAL-5). `[TBD]`.
- **LLM đa nhà cung cấp** (Gemini/DeepSeek/Anthropic) — HLD §6.
- **FCM** (push), **GCS** (ảnh), **Email OTP** — HLD.
- **Google Calendar** (FR-CAL). `[TBD]`.
- **Catalog gói** `coaching_packages`.

## 6. Yêu cầu phi chức năng (NFR) — *nhiều mục cần chốt ngưỡng*
- **NFR-PERF-1** Bản tư vấn/gợi ý bữa ăn tạo trong **≤ vài giây**; thao tác chuẩn bị 1 KH **≤ ~7 phút** (mục tiêu sản phẩm). `[TBD số đo thật]`.
- **NFR-SEC-1** JWT, mã hóa bí mật (Secret Manager), rate-limit agent; CSV-injection safe — HLD §12.
- **NFR-PRIV-1** Consent AI bắt buộc trước khi gửi PII; xóa mềm tài khoản; audit hành động admin (GDPR-like) — HLD §12.
- **NFR-COMPLIANCE-1** Tuân thủ quảng cáo sức khỏe & quy định bán hàng đa cấp; **không chẩn đoán y tế**; disclaimer bắt buộc (FR-CONSULT-7). Comp plan (FR-SELFDEV-2) cần rà pháp lý.
- **NFR-SCALE-1** API stateless scale ngang; worker/cron không trùng — HLD §13.
- **NFR-AVAIL-1** LLM fallback đa provider; cache degrade→miss — HLD §13.
- **NFR-USABILITY-1** Mobile-first ≤460px; thân thiện người **chưa quen công nghệ** (thao tác tối thiểu, ánh xạ thói quen offline).
- **NFR-I18N-1** Tiếng Việt mặc định.

## 7. Ràng buộc thiết kế (Constraints)
- Không tích hợp kỹ thuật với VNHUB/Learning/SHOP/Pro2col; không làm POS/kho/quản trị KD.
- AI hỗ trợ không thay người & không thao túng; consent là ràng buộc thiết kế.
- Logic nghiệp vụ tách khỏi tầng trình bày (DISC chỉ chỉnh tông giọng).

## 8. Phụ lục
- **A. Ma trận truy vết:** mỗi FR ↔ tài liệu nguồn ↔ prototype (rút gọn ở §2.1; chi tiết bổ sung sau).
- **B. Danh sách Open Questions tổng hợp:** catalog món ăn & API calo; catalog gói thật; số đo thời gian "after"; phạm vi Google Calendar; comp plan & pháp lý; nội dung đào tạo/talking points/xử lý từ chối; template báo cáo/infographic; mô hình cộng đồng/tuyến.
- **C. Lịch sử phiên bản:** v0.1 — bản SRS đầu tiên, hybrid, toàn cây chức năng + TBD.

---
*SRS v0.1 — draft để khởi động phát triển. Các mục `[TBD]`/Open question cần đội nghiệp vụ bổ sung trước khi đặc tả mức triển khai (API contract, schema chi tiết) cho các module 🔜.*
