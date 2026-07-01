# Personas — Vai trò người dùng & Chân dung khách hàng

> Chưng cất từ SRS §1.4, As-Is v1.2 và `customer-persona-disc-framework_v1.0` (trong archive).

## 1. Ba vai trò người dùng (Actors)

| Actor | Viết tắt | Mục tiêu chính | Ngữ cảnh sử dụng | Quen công nghệ |
|---|---|---|---|---|
| **Huấn luyện viên dinh dưỡng** | HLV / COACH | Quản lý KH tiềm năng & KH hiện tại, tư vấn chuyển đổi, chăm sóc, phát triển hệ thống KD; đồng thời là "người dùng sức khỏe" (làm gương). | Trung niên, **bận**, thường dùng máy **khi đang ngồi cạnh khách thật**. Sợ *"tốn thời gian – không hiệu quả"*. | Thấp–trung |
| **Khách hàng** | KH / KHTN | Sống khỏe theo Thân–Tâm–Trí; theo dõi sức khỏe, dinh dưỡng, thói quen; được HLV đồng hành; chia sẻ tiến bộ. | Onboarding do HLV mời; dùng tại nhà + tại club. | Trung |
| **Founder / Admin** | ADMIN | Quản trị nền tảng: duyệt HLV, quản trị nội dung/Knowledge Base, cấu hình, audit. (Founder: dashboard riêng 1/nhiều club, tài chính 3 tầng, chân dung KH giá trị.) | Web, dashboard quản trị. | Cao |

> **HLV đồng thời là persona "người dùng sức khỏe"**: tự thực hiện lộ trình, chia sẻ ảnh/kết quả qua chat tới KH/cộng đồng (làm gương).

## 2. Khung chân dung khách hàng (Customer Persona)

### Nguyên tắc nền
- **DISC là thẻ phụ** — giúp chọn *tông giọng & cách trình bày*, **không** phải trung tâm.
- **Trục quyết định chuyển đổi** = **Aim (mục tiêu sức khỏe) + Pain point + Giai đoạn sẵn sàng thay đổi (Stage-of-Change)**.
- DISC điều chỉnh *cách nói*; Stage-of-Change quyết định *nói gì và khi nào chốt*.

### Schema (trường dữ liệu mỗi lead/persona)
- **Định danh & nhân khẩu**: `persona_name`, `age_range`, `gender`, `occupation`, `location`, `family_status`.
- **Aim & nỗi đau (trục chính)**: `primary_goal`, `pain_points[]`, `trigger_event`, `success_definition`, `health_metrics` (Tanita khi có).
- **Hành vi & bối cảnh**: `lifestyle`, `channels[]`, `tech_comfort`, `budget_sensitivity`, `decision_factors[]`, `objections[]`.
- **Persona-fit bữa ăn**: `diet_type`, `daily_budget`, `liked_foods[]`/`disliked_foods[]`, `meal_autonomy`.
- **Thẻ phụ**: `disc_primary` (D/I/S/C), `disc_secondary`, `stage_of_change`.

### 4 thẻ DISC (chỉ đổi *cách trình bày*, không in ra UI)
| Thẻ | Đặc trưng | Hướng trình bày |
|---|---|---|
| **D** | Quyết đoán, kết quả | Ngắn gọn, con số mục tiêu, đi thẳng vấn đề |
| **I** | Cảm xúc, quan hệ | Câu chuyện người thật, hình ảnh trước–sau, truyền cảm hứng |
| **S** | Kiên định, an toàn | Bằng chứng khoa học, lộ trình từng bước, cam kết đồng hành |
| **C** | Phân tích, chi tiết | Số liệu chi tiết, đối chiếu chuẩn, so sánh lựa chọn |

### Stage-of-Change (khi nào nói gì)
`precontemplation` → `contemplation` → `preparation` → `action` → `maintenance`. Giai đoạn càng sớm → càng cần làm ấm/đồng cảm, chưa chốt gói.

> **TODO chưng cất tiếp**: 3 persona lõi có tên + avatar (Phần IV của `docs/99-archive/to-be/customer-persona-disc-framework_v1.0.md`) — cần đưa vào đây sau khi rà soát. Hiện đã có schema & nguyên tắc đủ để bắt đầu viết user stories.
