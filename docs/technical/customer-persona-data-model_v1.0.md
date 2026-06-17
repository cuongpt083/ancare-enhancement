# MÔ HÌNH DỮ LIỆU CHÂN DUNG KHÁCH HÀNG (2 BẢNG) — ANCARE / SmartLife

**Phiên bản:** v1.0 (draft) · **Cập nhật:** 2026-06-17
**Mục đích:** Đặc tả mô hình dữ liệu cho **Khách hàng tiềm năng (lead)** theo 2 nhóm thông tin:
1. **Thông tin cơ bản** — lấy từ bảng `users` (đã có).
2. **Chân dung khách hàng** — bảng mới `customer_personas`, tham chiếu **1:1** với `users`, cấu trúc linh hoạt (JSONB) phản ánh persona thu thập được.

**Liên quan:**
- Khung nội dung persona: `docs/to-be/customer-persona-disc-framework_v1.0.md`.
- HLD hiện trạng: `docs/as-is/high-level-design.md` (pattern `health_profiles` 1:1; `users.is_prospect`; consent `ai_data_sharing_enabled`).
- To-do v2.0: TD-AC1 (DSKHTN), TD-AC4 (lead scoring), TD-AC5 (kịch bản theo DISC × Stage).

---

## 1. Nguyên tắc thiết kế

| Nguyên tắc | Diễn giải |
|---|---|
| **1:1 với `users`** | Đồng nhất pattern `health_profiles`. Mỗi user (kể cả prospect) có tối đa 1 persona. |
| **Lead = user shadow** | Lead nhập từ danh bạ/MXH được tạo `users` với `is_prospect=true` ngay khi import → đủ điều kiện 1:1. (Khớp `is_prospect` sẵn có.) |
| **Hot columns + JSONB** | Trường dùng để **lọc/sắp xếp/chấm điểm hằng ngày** = cột thật có index; phần mô tả chi tiết & tiến hóa = JSONB. |
| **Không trùng lặp** | Không copy Tanita/goal/calo (đã ở `health_profiles`). Persona giữ phần *tâm lý – hành vi – DISC – Stage – phễu*. |
| **Provenance + consent** | Mỗi cụm dữ liệu kèm độ tin cậy (`self_reported`/`inferred`/`coach_tagged`) + thời điểm. Tôn trọng `ai_data_sharing_enabled` trước khi đưa cho LLM. |
| **SSOT một nguồn sự thật** | `users` = định danh; `health_profiles` = số liệu sức khỏe; `customer_personas` = chân dung. Tham chiếu, không sao chép. |

---

## 2. ERD

```mermaid
erDiagram
    users ||--o| health_profiles : "1:1 (đã có)"
    users ||--o| customer_personas : "1:1 (MỚI)"
    users ||--o{ coach_customers : "coach quản lý"
    users {
        uuid id PK
        string role "ADMIN/COACH/CUSTOMER"
        bool is_prospect "lead shadow"
        string subscription_status "FREE/PREMIUM"
        bool ai_data_sharing_enabled "consent AI"
        string herbalife_code
        string referral_code
        timestamp deleted_at "xoá mềm"
    }
    health_profiles {
        uuid user_id PK_FK
        jsonb tanita_data
        string goal
        string onboarding_status
        int target_calories
    }
    customer_personas {
        uuid user_id PK_FK "1:1 -> users.id"
        string disc_primary "D/I/S/C (index)"
        string disc_secondary
        string stage "precontemplation..maintenance (index)"
        string funnel_stage "Mới..Mua gói (index)"
        int lead_score "0-100 (index)"
        string primary_goal "index"
        string source "nóng/ấm/lạnh (index)"
        uuid assigned_coach_id FK
        jsonb persona_data "chi tiết linh hoạt"
        jsonb provenance "độ tin cậy theo cụm"
        int schema_version
        timestamp created_at
        timestamp updated_at
    }
```

> `||--o|` = quan hệ 1:1 tùy chọn (user có thể chưa có persona). `customer_personas.user_id` vừa là **PK vừa là FK** tới `users.id` (đúng kiểu `health_profiles`).

---

## 3. Cột "nóng" (queryable) vs JSONB

### 3.1 Cột thật + index — phục vụ lọc/sắp xếp/scoring hằng ngày

| Cột | Kiểu | Mục đích | Index |
|---|---|---|---|
| `user_id` | uuid PK/FK | 1:1 tới `users` | PK |
| `disc_primary` | varchar(2) | Lọc theo kiểu DISC chọn kịch bản (TD-AC5) | ✅ |
| `disc_secondary` | varchar(2) | Tổ hợp phụ | — |
| `stage` | varchar(20) | Định vị giai đoạn → chiến thuật chốt | ✅ |
| `funnel_stage` | varchar(20) | Vị trí phễu (TD-AC2) | ✅ |
| `lead_score` | smallint | "Hôm nay nên tiếp cận ai" (TD-AC4) | ✅ |
| `primary_goal` | varchar(40) | Khớp persona × gói | ✅ |
| `source` | varchar(12) | Nóng/ấm/lạnh | ✅ |
| `assigned_coach_id` | uuid FK | Phân công HLV | ✅ |
| `schema_version` | smallint | Versioning JSONB | — |
| `created_at`/`updated_at` | timestamptz | Audit | — |

> Gợi ý composite index cho TD-AC4: `(assigned_coach_id, funnel_stage, lead_score DESC)`.

### 3.2 `persona_data` JSONB — chi tiết linh hoạt, tiến hóa theo bộ câu hỏi

```json
{
  "demographics": {
    "age_range": "30-39", "gender": "female",
    "occupation": "office", "location": "HCM",
    "income_band": "mid", "family_status": "có con nhỏ"
  },
  "aim": {
    "pain_points": ["mệt mỏi buổi chiều", "mặc cảm ngoại hình"],
    "trigger_event": "sau sinh",
    "success_definition": "mặc vừa váy cũ",
    "secondary_goals": ["tăng năng lượng"]
  },
  "behavior": {
    "lifestyle": "ít vận động, ăn ngoài trưa",
    "channels": ["facebook", "zalo"],
    "tech_comfort": "medium",
    "budget_sensitivity": "high",
    "decision_factors": ["người thật-việc thật", "đồng hành"],
    "objections": ["không có thời gian", "từng thất bại giảm cân"]
  },
  "disc": {
    "communication_pref": "thích câu chuyện, nhịp chậm, cần trấn an"
  },
  "stage_of_change": {
    "readiness_score": 65,
    "motivation_quotes": ["mình muốn khỏe lại để chơi với con"]
  },
  "survey_responses": [
    {
      "qid": "Q1",
      "question_text": "Điều gì khiến anh/chị bắt đầu quan tâm đến sức khỏe/vóc dáng lúc này?",
      "group": "aim",
      "sp_category": "Aim",
      "disc_signal": false,
      "stage_signal": true,
      "answer_type": "free_text",
      "answer": "Sau sinh em tăng cân, mệt và mặc đồ không vừa",
      "asked_at": "2026-06-16T15:00:00Z",
      "channel": "zalo_warmup",
      "asked_by": "coach"
    },
    {
      "qid": "Q5",
      "question_text": "Trên thang 0–10, anh/chị sẵn sàng thay đổi đến mức nào — và vì sao không thấp hơn?",
      "group": "aim",
      "sp_category": "Aim",
      "stage_signal": true,
      "answer_type": "scale_text",
      "answer_value": 7,
      "answer": "7, vì em thực sự muốn khỏe lại để chơi với con",
      "asked_at": "2026-06-16T15:02:00Z",
      "channel": "zalo_warmup"
    },
    {
      "qid": "Q13",
      "question_text": "Anh/chị thích em trình bày ngắn gọn trọng tâm, hay chi tiết đầy đủ?",
      "group": "disc_probe",
      "disc_signal": true,
      "answer_type": "choice",
      "answer": "chi tiết đầy đủ",
      "asked_at": "2026-06-16T15:05:00Z",
      "channel": "onboarding_form"
    }
  ]
}
```

> **Vì sao lưu cả `question_text`, không chỉ `qid`?** Bộ câu hỏi sẽ tiến hóa (đổi từ ngữ, thêm/bớt câu). Lưu nguyên văn câu hỏi tại thời điểm hỏi giúp: (1) AI hiểu đúng ngữ cảnh câu trả lời dù bộ câu hỏi đã đổi; (2) tránh "diễn giải sai" khi `qid` bị tái sử dụng cho câu khác về sau. `survey_version` (trong `provenance`) ghi nhận phiên bản bộ câu hỏi đã dùng.

### 3.3 `provenance` JSONB — độ tin cậy, nguồn & bằng chứng

Mỗi nhận định persona **trỏ ngược về các `qid`** đã dẫn tới kết luận đó (`evidence`). Đây là cơ sở để AI/HLV giải thích "vì sao gán DISC=C" và để kiểm toán.

```json
{
  "survey_version": "persona-survey-v1.0",
  "disc":   { "confidence": "inferred",      "by": "llm",   "at": "2026-06-17T09:00:00Z",
              "evidence": ["Q13", "Q14", "chat_tempo"] },
  "stage":  { "confidence": "coach_tagged",  "by": "coach", "at": "2026-06-17T10:00:00Z",
              "evidence": ["Q5", "Q17"] },
  "aim":    { "confidence": "self_reported", "by": "survey","at": "2026-06-16T15:00:00Z",
              "evidence": ["Q1", "Q3"] }
}
```

---

## 3.4 Cách AI suy luận chân dung TỪ câu hỏi & câu trả lời

Nguyên tắc: **AI xuất phát từ `survey_responses[]` (dữ liệu thô) → suy ra các thẻ, không nhận thẻ "có sẵn".** Quy trình đề xuất cho `ConsultationAgent`:

1. **Đọc nguyên văn Q&A**: nạp `survey_responses[]` (cả `question_text` + `answer`) + tín hiệu hành vi (nhịp chat) vào ngữ cảnh — *sau khi* kiểm tra `ai_data_sharing_enabled`.
2. **Suy luận có dẫn chứng**: với mỗi thẻ (`disc_primary`, `stage`, `pain_points`…), model phải nêu `evidence` là các `qid` đã dựa vào → ghi vào `provenance`.
3. **Gán độ tin cậy**: chỉ từ survey/chat = `inferred`; khách tự khẳng định = `self_reported`; HLV duyệt = `coach_tagged` (ưu tiên cao nhất, ghi đè được suy luận máy).
4. **Tái suy luận khi có câu trả lời mới**: thêm phần tử vào `survey_responses[]` → trigger phân tích lại; thẻ cũ chỉ bị ghi đè nếu độ tin cậy mới ≥ cũ.

> Lợi ích: quyết định của AI **chính xác và giải thích được** vì luôn neo vào câu hỏi–câu trả lời gốc, thay vì một nhãn rời rạc không rõ căn cứ.

---

## 4. DDL phác thảo (PostgreSQL 17)

```sql
CREATE TABLE customer_personas (
    user_id           uuid PRIMARY KEY
                       REFERENCES users(id) ON DELETE CASCADE,
    disc_primary      varchar(2),          -- D/I/S/C
    disc_secondary    varchar(2),
    stage             varchar(20),         -- precontemplation..maintenance
    funnel_stage      varchar(20),         -- Mới..Mua gói
    lead_score        smallint DEFAULT 0,
    primary_goal      varchar(40),
    source            varchar(12),         -- hot/warm/cold
    assigned_coach_id uuid REFERENCES users(id) ON DELETE SET NULL,
    persona_data      jsonb NOT NULL DEFAULT '{}'::jsonb,
    provenance        jsonb NOT NULL DEFAULT '{}'::jsonb,
    schema_version    smallint NOT NULL DEFAULT 1,
    created_at        timestamptz NOT NULL DEFAULT now(),
    updated_at        timestamptz NOT NULL DEFAULT now()
);

-- Index phục vụ phễu & lead scoring (TD-AC2 / TD-AC4)
CREATE INDEX idx_personas_coach_funnel_score
    ON customer_personas (assigned_coach_id, funnel_stage, lead_score DESC);
CREATE INDEX idx_personas_stage       ON customer_personas (stage);
CREATE INDEX idx_personas_disc        ON customer_personas (disc_primary);
CREATE INDEX idx_personas_goal_source ON customer_personas (primary_goal, source);

-- Index JSONB khi cần truy vấn sâu (vd lọc theo pain_point)
CREATE INDEX idx_personas_data_gin ON customer_personas USING gin (persona_data);
```

> **Ràng buộc & quy ước:** `ON DELETE CASCADE` theo user (đồng nhất HLD); `assigned_coach_id` `SET NULL` khi coach bị xoá. `updated_at` cập nhật qua ORM hook hoặc trigger.

---

## 5. Vòng đời dữ liệu (data lifecycle)

```
Import lead (TD-AC1)
   └─> tạo users(is_prospect=true) + customer_personas(rỗng, source=...)
Làm ấm / khảo sát (Phần V bộ câu hỏi)
   └─> append vào persona_data.survey_responses[] (câu hỏi + câu trả lời gốc)
   └─> ghi persona_data.aim / behavior + provenance(self_reported)
Hội thoại chat / quan sát
   └─> LLM đọc survey_responses[] → suy luận disc_primary, stage
       (provenance=inferred + evidence=[qid...])  [cần consent]
HLV xác nhận / chỉnh
   └─> coach_tagged (độ tin cậy cao nhất)
Onboarding (Tanita)
   └─> số liệu vào health_profiles; persona tham chiếu, không copy
Chuyển đổi
   └─> funnel_stage tiến; khi mua gói: users.subscription_status=PREMIUM
       is_prospect=false (lead → khách)
```

---

## 6. Tích hợp & lưu ý

- **`ConsultationAgent` / TD-AC5:** đọc `disc_primary`, `stage`, `persona_data` qua tool `ai_coach_context` để chọn & cá nhân hóa kịch bản. **Bắt buộc kiểm tra `users.ai_data_sharing_enabled` trước khi gửi cho LLM.**
- **Lead scoring TD-AC4:** `lead_score = f(primary_goal × gói phù hợp, source, stage_of_change.readiness_score)`. Lưu kết quả vào cột `lead_score` để sắp xếp nhanh.
- **Versioning:** đổi bộ câu hỏi/cấu trúc → tăng `schema_version`; migration JSONB chạy nền, không cần đổi cột.
- **Đạo đức:** persona phục vụ tư vấn tốt hơn, không thao túng; DISC là thẻ phụ chỉnh tông giọng.

---
*Draft v1.0 — cần review cùng team Engineering (đặt tên cột/migration alembic) và team nghiệp vụ (chuẩn enum funnel_stage, primary_goal).*
