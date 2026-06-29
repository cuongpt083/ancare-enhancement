# Các workflow chính dành cho đối tượng HLV

## A. Workflow dành cho HLV

### 1. Tạo KH tiềm năng và Chuyển đổi thành KH chính thức

**Mục tiêu:** Rút gọn và chuẩn hóa luồng tạo KH tiềm năng và Tư vấn, chuyển đổi thành KH chính thức.

```mermaid
graph TD
    A[Start] --> B["Truy cập mục HLV"]
    B --> C["Bấm mục 'KH tiềm năng'"]
    C --> D["Bấm nút '+' / Tạo KH mới"]
    D --> E["Hệ thống hiển thị màn hình 'Tạo KH tiềm năng mới'"]
    E --> F["HLV nhập 'Thông tin cơ bản', 'Chân dung khách hàng'"]
    F --> G{"HLV bấm nút 'Hoàn tất | 'Tiếp tục'"}
    G -- "Hoàn tất" --> H["Trở về màn hình 'Danh sách KH tiềm năng'"]
    H --> I[End]
    G -- "Tiếp tục" --> J["Hiển thị màn hình 'Nhập chỉ số Tanita'"]
    J --> K{"HLV nhập chỉ số Tanita hoặc chụp ảnh sổ theo dõi"}
    K -- "Nhập chỉ số Tanita" --> L["HLV nhập các thông số từ cân Tanita vào form"]
    K -- "Chụp ảnh" --> M["HLV chụp ảnh trang kết quả cân Tanita"]
    K -- "Chọn ảnh" --> N["HLV chọn ảnh từ thư viện thiết bị"]
    L --> O["Phân tích & tư vấn"]
    M --> O
    N --> O
    O --> P["Hiển thị 'Bản tư vấn' bao gồm các Card thông tin: 'Bảng phân tích chỉ số', 'Bảng tổng hợp mục tiêu cần cải thiện'"]
    P --> Q{"KH có nhu cầu trải nghiệm Giải pháp không?"}
    Q --"Có"--> R["HLV giới thiệu Giải pháp, Lộ trình (10 ngày, 30 ngày, 90 ngày), Sản phẩm phù hợp"]
    Q --"Không"--> I
    R --> S["HLV Tạo tài khoản cho KH, Đặt mua Gói dịch vụ"]
    S --> T["Lưu Mục tiêu chỉ số, Cập nhật Ảnh check-in: Ảnh chân dung, toàn thân, vòng eo"]
    T --> U["Tạo gợi ý bữa ăn dựa trên 'Mục tiêu' thay đổi số Calo/ngày,'Số bữa ăn/ngày' " ]
    V --> I
```

#### 1.1. Màn hình "Tạo KH tiềm năng mới"

Màn hình này sử dụng cho việc Tạo, Sửa thông tin KH tiềm năng. Để phù hợp cho việc hiển thị trên màn hình điện thoại cũng như màn hình máy tính bảng, màn hình này được chia thành các Card thông tin như sau:
- Card **Thông tin cơ bản** → ghi vào bảng `users`.
- Card **Chân dung khách hàng** → ghi vào bảng `customer_personas` (xem `docs/technical/customer-persona-data-model_v1.0.md`).

> **Nguyên tắc UX:** Chỉ **Họ tên** bắt buộc; mọi trường còn lại tùy chọn để HLV tạo nhanh trong lúc làm ấm và *bổ sung dần*. Mỗi câu hỏi ở Card Chân dung khách hàng khi được trả lời sẽ sinh 1 phần tử trong `persona_data.survey_responses[]` (kèm `qid` + nguyên văn câu hỏi), đồng thời cập nhật trường suy luận tương ứng. Prototype: `prototypes/hlv/hlv_tao_kh_tiem_nang.html`.

> **Tối ưu hiển thị (progressive disclosure):** Vì cả 2 Card đều dài, áp dụng cơ chế **accordion theo Card**:
> - Mặc định **chỉ mở Card "Thông tin cơ bản"**; Card "Chân dung khách hàng" **gập sẵn** (chỉ hiện tiêu đề + chú thích "Tùy chọn · bổ sung dần").
> - Mở một Card sẽ tự gập Card kia để giữ tập trung trên màn hình điện thoại.
> - Bên trong Card Chân dung khách hàng, mỗi **nhóm câu hỏi** cũng gập/mở riêng; mặc định mở 2 nhóm ưu tiên (Nguồn, Mục tiêu & nỗi đau — Aim).
> - Card Chân dung khách hàng hiển thị **dấu ✓** khi đã có ít nhất 1 thông tin, giúp HLV biết đã bắt đầu điền mà không cần mở ra.
> - HLV luôn có thể bấm **Hoàn tất** ngay sau khi nhập Họ tên (tạo lead tối thiểu), rồi quay lại bổ sung chân dung sau.

##### a) Card "Thông tin cơ bản" (→ `users`)

| Trường | Bắt buộc | Kiểu nhập | Map `users` |
|---|---|---|---|
| Họ tên | ✅ | text | `full_name` |
| Số điện thoại | — | tel | `phone` |
| Ngày sinh | — | date | `dob` |
| Giới tính | — | chọn (Nam/Nữ/Khác) | `gender` |
| Chiều cao | — | số (cm) | `health_profiles` / hồ sơ KH |
| Email | — | email | `email` |
| Mã giới thiệu (nếu có) | — | text | `referral_code` |
| Đồng ý chia sẻ dữ liệu cho AI | — | toggle | `ai_data_sharing_enabled` |

> Khi lưu, hệ thống tạo `users` với `is_prospect=true` và bản ghi `customer_personas` 1:1. Toggle consent điều khiển việc có đưa dữ liệu cho LLM phân tích hay không (Apple 5.1.1(i)).

##### b) Card "Chân dung khách hàng" (→ `customer_personas`)

Bố cục theo nhóm câu hỏi (gập/mở để gọn trên điện thoại). `qid` khớp Bộ câu hỏi Phần V của khung persona. Cột **Map** ghi đích trong `persona_data` / cột nóng.

**Nhóm 0 — Nguồn & phân công**

| Trường | Kiểu nhập | Map |
|---|---|---|
| Nguồn lead | chọn: Nóng / Ấm / Lạnh | cột `source` |
| Kênh tiếp cận | chip nhiều lựa chọn: Zalo, Facebook, TikTok, Gặp trực tiếp, Giới thiệu | `persona_data.behavior.channels[]` |
| HLV phụ trách | chọn (mặc định HLV hiện tại) | cột `assigned_coach_id` |

**Nhóm 1 — Mục tiêu & nỗi đau (Aim)** *(quan trọng nhất, nên hỏi sớm)*

| qid | Câu hỏi | Kiểu nhập | Map |
|---|---|---|---|
| Q-goal | Mục tiêu sức khỏe trội | chọn: Giảm cân / Tăng cơ / Kiểm soát đường huyết / Tăng năng lượng / Tiêu hóa / Làm đẹp da | cột `primary_goal` |
| Q1 | Điều gì khiến anh/chị bắt đầu quan tâm lúc này? | text ngắn | `survey_responses[]` + `aim.trigger_event` |
| Q3 | Vấn đề sức khỏe nào làm phiền nhất? | chip + text | `aim.pain_points[]` |
| Q2 | 3 tháng tới mọi thứ tốt thì anh/chị hình dung mình thế nào? | text | `aim.success_definition` |
| Q4 | Đã từng thử cách nào trước đây? Kết quả? | text | `survey_responses[]` |

**Nhóm 2 — Bối cảnh & lối sống (People/Resource)**

| qid | Câu hỏi | Kiểu nhập | Map |
|---|---|---|---|
| Q-demo | Độ tuổi / Nghề nghiệp / Khu vực | chọn + text | `persona_data.demographics` |
| Q7 | Ràng buộc thời gian/công việc/gia đình | text | `demographics.family_status` |
| Q6 | Một ngày thường diễn ra thế nào? | text | `behavior.lifestyle` |

**Nhóm 3 — Yếu tố quyết định & rào cản (Resource/Objection)**

| qid | Câu hỏi | Kiểu nhập | Map |
|---|---|---|---|
| Q9 | Điều gì quan trọng nhất khi quyết định? | chọn nhiều: Kết quả nhanh / Bằng chứng khoa học / Chi phí / Có người đồng hành | `behavior.decision_factors[]` (+ tín hiệu DISC) |
| Q10 | Điều gì còn khiến anh/chị băn khoăn? | chip + text | `behavior.objections[]` |
| Q11 | Ngân sách hợp lý cho sức khỏe | chọn dải (tùy chọn, hỏi sau) | `behavior.budget_sensitivity` |
| Q12 | Tự quyết hay cần trao đổi với ai? | chọn: Tự quyết / Hỏi vợ-chồng / Hỏi con / Khác | `survey_responses[]` |

**Nhóm 4 — Tín hiệu DISC** *(đan vào hội thoại, ngắn, tùy chọn — KHÔNG gọi là "test")*

| qid | Câu hỏi | Kiểu nhập | Tín hiệu |
|---|---|---|---|
| Q13 | Thích trình bày ngắn gọn hay chi tiết đầy đủ? | chọn | ngắn=D · chi tiết=C |
| Q14 | Hứng thú với câu chuyện người thật hay số liệu khoa học? | chọn | chuyện=I · số liệu=C |
| Q15 | Thích bắt đầu ngay hay chuẩn bị kỹ rồi mới làm? | chọn | ngay=D/I · kỹ=S/C |
| Q16 | Thay đổi: làm nhanh hay cần thời gian làm quen? | chọn | nhanh=D · cần thời gian=S |
| — | DISC gợi ý (hệ thống suy luận, HLV xác nhận/sửa) | chọn D/I/S/C + phụ | cột `disc_primary`/`disc_secondary`, provenance |

**Nhóm 5 — Giai đoạn sẵn sàng (Stage)**

| qid | Câu hỏi | Kiểu nhập | Map |
|---|---|---|---|
| Q17 | Đang ở giai đoạn nào? | chọn: Chưa nghĩ tới / Đang cân nhắc / Muốn bắt đầu sớm / Đã đang làm | cột `stage` |
| Q5 | Thang 0–10 sẵn sàng thay đổi — vì sao không thấp hơn? | slider 0–10 + text | `stage_of_change.readiness_score` + `motivation_quotes[]` |
| Q18 | Nếu có lộ trình phù hợp, muốn bắt đầu khi nào? | chọn: Ngay / Tuần này / Trong tháng / Chưa rõ | `survey_responses[]` |

**Khu vực gợi ý của AI (chỉ hiển thị khi đã bật consent):**
Sau khi nhập, nếu `ai_data_sharing_enabled=true`, hệ thống có thể hiển thị thẻ gợi ý "DISC dự đoán / Giai đoạn / Cách tiếp cận đề xuất" kèm các `qid` làm bằng chứng (`provenance.evidence`); HLV xác nhận hoặc chỉnh trước khi lưu.

**Hành động cuối màn hình:** `Hoàn tất` (lưu, về Danh sách) · `Tiếp tục` (lưu, sang màn "Nhập chỉ số Tanita"). Nếu HLV bấm `Hoàn tất`, hệ thống sẽ quay về màn Danh sách. Nếu HLV bấm `Tiếp tục`, hệ thống sẽ lưu thông tin KH tiềm năng và chuyển sang màn "Nhập chỉ số Tanita".

#### 1.2. Màn hình "Nhập chỉ số Tanita"

Truy cập khi HLV bấm **"Tiếp tục"** ở màn 1.1. Mục đích: nhập kết quả đo Tanita của KH tiềm năng để tạo **Bản tư vấn**. Cho phép **nhập tay** hoặc **chụp/chọn ảnh** phiếu cân → hệ thống OCR/Vision tự nhận diện và điền chỉ số. Prototype: `prototypes/hlv/hlv_nhap_chi_so_tanita.html`.

**Cải tiến UI-UX so với thiết kế ban đầu:**

1. **Chiều cao lấy sẵn từ hồ sơ KH** (đã nhập ở Card Thông tin cơ bản, màn 1.1) — hiển thị **read-only** với nhãn "từ hồ sơ", HLV không phải nhập lại. Bản chất màn này chỉ nhập **các chỉ số đo được từ cân Tanita**. BMI **tự tính** từ chiều cao (hồ sơ) + cân nặng, hiển thị read-only kèm phân loại (Thiếu cân / Bình thường / Thừa cân / Béo phì).
2. **Nhóm trường** thay vì danh sách phẳng 9 dòng:
   - *Cơ bản*: Cân nặng (kg) · Chiều cao (cm, từ hồ sơ) · BMI (tự tính).
   - *Thành phần cơ thể*: Tỷ lệ mỡ (%) · Khối lượng cơ (kg) · Tỷ lệ nước (%) · Khối lượng xương (kg) · Mỡ nội tạng (mức).
   - *Chỉ số khác*: Vóc dáng (1–9) · Tuổi sinh học (tuổi) · Năng lượng nghỉ ngơi (kcal).
3. **Đơn vị hiển thị dạng hậu tố** ngay trong ô nhập; ô có viền rõ + focus ring (khắc phục cảm giác "bị khóa" của nền xám ở bản gốc); **bàn phím số** (`inputmode`).
4. **Luồng OCR rõ ràng**: sau khi chụp/chọn ảnh → banner "Đã nhận diện N chỉ số", các ô tự điền được **tô xanh + nhãn "AI"** để HLV phân biệt với giá trị nhập tay và đối chiếu phiếu cân.
5. **Chú thích chỉ số mơ hồ**: "Mỡ nội tạng" (mức 1–12 bình thường, ≥13 cao), "Vóc dáng" (physique rating 1–9) có icon ⓘ tooltip.
6. **Nút "Tạo bản Tư Vấn"** chỉ kích hoạt khi đã nhập **đầy đủ tất cả chỉ số Tanita** (Cân nặng, Tỷ lệ mỡ, Khối lượng cơ, Tỷ lệ nước, Khối lượng xương, Mỡ nội tạng, Vóc dáng, Tuổi sinh học, Năng lượng nghỉ ngơi); khi disable có dòng nhắc lý do. Chiều cao đã có sẵn từ hồ sơ nên không tính vào điều kiện nhập.
7. Nút **Quay lại** dạng icon tròn ở góc trái footer, CTA chiếm phần còn lại.

**Map dữ liệu:** các chỉ số ghi vào `health_profiles.tanita_data` (JSONB) như hiện trạng; BMI có thể lưu hoặc tính lại khi đọc. Nguồn giá trị (OCR vs nhập tay) nên ghi nhận để kiểm chứng.

**Hành động:** `Tạo bản Tư Vấn` → chạy phân tích & sinh "Bản tư vấn" (Card *Bảng phân tích chỉ số* + *Bảng tổng hợp mục tiêu cần cải thiện*) theo workflow ở mục 1.

Màn hình này sử dụng cho việc Nhập thủ công, Nhập tự động (qua việc chụp ảnh form thông tin trên Sổ theo dõi tại Nhóm dinh dưỡng, hoặc upload file ảnh chụp từ thư viện hình ảnh trên thiết bị). 

#### 1.3. Màn hình "Bản tư vấn"

Truy cập khi HLV bấm **"Tạo bản Tư Vấn"** ở màn 1.2. Hệ thống tính toán & phân tích các chỉ số (đối chiếu chuẩn WHO/Tanita), sau đó hiển thị màn này. Prototype: `prototypes/hlv/hlv_ban_tu_van.html`.

**Nhiệm vụ màn hình:** kể về **hiện trạng thông số sức khỏe** của KH, **đối chiếu mức tiêu chuẩn** để KH hiểu trạng thái hiện tại và **các nguy cơ tiềm ẩn** — làm cơ sở để KH thấy nhu cầu cải thiện (hỗ trợ chuyển đổi).

> 💬 **Tích hợp Objection Handler:** màn này có **FAB "Khách đang băn khoăn"** — khi KH nêu từ chối (giá / thời gian / "để suy nghĩ"…), HLV bấm để nhận mẫu câu 3 lớp (Thấu hiểu → Lật khung → Tiến tới) cá nhân hóa theo DISC + Stage. Xem `docs/srs/Objection-Handler_v1.0.md`.

> ❤️ **Tùy chọn Empathy layer:** trình bày bản tư vấn theo **cấu trúc 5 lớp đồng cảm** (Mở đồng cảm → Điểm đang ổn → Điểm cần quan tâm → Nguy cơ giấu sau 1 lớp bấm → Tin vui khả thi), đổi tông theo DISC + Stage. Dành cho khách có nỗi đau sức khỏe & khách đa nghi. Đặc tả: `docs/srs/Empathy-Consultation_v1.0.md`.

**Đầu trang:** thông tin KH — Tên/Mã (vd "KH03"), giới tính · tuổi · chiều cao, số điện thoại.

**Card 1 — "Những điểm cần cải thiện"**
- Liệt kê **các chỉ số chưa tốt** (severity vàng/đỏ), mỗi dòng: tên chỉ số + giá trị hiện tại + chấm màu mức độ.
- **Bấm vào mỗi chỉ số** → mở bảng chi tiết gồm 2 phần:
  - **Phân tích hiện trạng** — diễn giải chỉ số so với chuẩn, mức chênh, định hướng cải thiện.
  - **Nguy cơ bệnh lý** — các rủi ro sức khỏe liên quan nếu không cải thiện.
- Ví dụ các mục: Cân nặng (60 kg), Mỡ nội tạng (8 điểm), Chỉ số cân đối (3 điểm), Tuổi sinh học (50 tuổi), BMI (23.1).

**Card 2 — "Bảng phân tích chỉ số chi tiết"**
- Mỗi dòng gồm: **Tên chỉ số · chuẩn tham chiếu (WHO/Tanita)** · **Giá trị** (tô màu theo mức độ) · **Phân tích ngắn**.
- Danh sách đầy đủ: Cân nặng, Mỡ cơ thể, Mỡ nội tạng, Lượng cơ bắp, Chỉ số cân đối, Năng lượng nghỉ ngơi, Tuổi sinh học, Lượng xương, Nước, BMI.
- **Mặc định chỉ hiển thị 2 dòng đầu**; phần còn lại ẩn sau nút **"Xem thêm"** (bấm để mở/thu gọn — đổi nhãn "Thu gọn").
- Cuối bảng có **ghi chú nguồn** (các bảng tham chiếu chuẩn, WHO Expert Consultation 2004, Mifflin–St Jeor, Tanita BC-series…).

**Khối "Bài phân tích chi tiết các chỉ số":** dẫn nhập rằng hệ thống sẽ sinh bài tư vấn cá nhân hóa dựa trên bảng phân tích trên.

**Hành động — 2 nút (HLV chọn theo quyết định của KH):**

Sau khi trình bày bản tư vấn, HLV hỏi KH có muốn **trải nghiệm giải pháp** không, rồi chọn 1 trong 2 nút:

1. **CTA "Tiếp tục"** — bấm khi **KH quyết định trải nghiệm**. Hệ thống chuyển sang màn **"Thiết lập mục tiêu"** (mục 1.4) để thu thập nốt các thông tin còn thiếu của **Chân dung khách hàng**: thói quen hiện tại, mục tiêu ưu tiên của KH, và các vấn đề/bệnh lý đang gặp. (Các thông tin này tiếp tục ghi vào `customer_personas` — `persona_data.behavior`, `aim`, kèm `survey_responses[]`.)
2. **"Hoàn tất"** — bấm khi **KH chưa ra quyết định trải nghiệm**. Hệ thống **tính toán hành động kế tiếp dựa trên DISC** (và giai đoạn sẵn sàng — Stage) để **đề xuất cho HLV** việc nên làm tiếp, ví dụ:
   - Tiếp tục làm ấm (nội dung/tông giọng theo DISC).
   - Chia sẻ video/bài học phù hợp.
   - Dẫn tới cuộc gặp 2/1 với người phù hợp (TAB/chuyên gia).
   - Đặt lịch nhắc theo cadence.

   > Gợi ý này lấy từ engine **Next-Best-Action** (To-do TD-AC5 / TD-AC2): kết hợp `disc_primary` + `stage` + `funnel_stage` → đề xuất bước kế tiếp; chỉ sinh khi `ai_data_sharing_enabled=true`. KH được đưa về Danh sách KH tiềm năng kèm "việc cần làm tiếp".

**Map dữ liệu:** kết quả phân tích lấy từ `health_profiles.tanita_data` + bảng chuẩn tham chiếu; nội dung diễn giải sinh bởi `ConsultationAgent` (WHO + DISC) — bám Knowledge Base, không chẩn đoán y tế.

#### 1.4. Màn hình "Thiết lập mục tiêu"

Truy cập khi HLV bấm **"Tiếp tục"** ở màn 1.3 (KH đồng ý trải nghiệm). Prototype: `prototypes/hlv/hlv_thiet_lap_muc_tieu.html`. Màn gồm **2 phần**: (A) thu thập thông tin, (B) lộ trình trải nghiệm hệ thống tính ra.

> 💬 **Tích hợp Objection Handler:** FAB "Khách đang băn khoăn" cũng có ở màn này (giai đoạn chốt gói thường phát sinh từ chối về giá/ngân sách). Nếu `stage` thấp (Chưa nghĩ tới / Đang cân nhắc), các nhánh chốt gói bị **ẩn**, chỉ hiện gợi ý làm ấm. Xem `docs/srs/Objection-Handler_v1.0.md`.

**A. Thu thập thông tin (bổ sung chân dung khách hàng)**

- **Card "Mục tiêu cần cải thiện"** — danh sách chỉ số chưa tốt (kế thừa từ Bản tư vấn). Mỗi mục tiêu **bổ sung câu hỏi "Bao giờ bạn muốn có kết quả?"** (chọn mốc: 10/30/60/90 ngày, 6 tháng, dài hạn) và cho phép **đánh dấu ưu tiên**. → `persona_data.aim` (mục tiêu + `desired_timeframe`), cột `primary_goal`.
- **Card "Thói quen hiện tại"** — ăn uống, vận động, giấc ngủ (chọn nhanh dạng chip). → `persona_data.behavior.lifestyle`.
- **Card "Vấn đề/bệnh lý đang gặp"** — chip + ghi chú (tiền sử, dị ứng, lưu ý). → `persona_data.aim.pain_points[]` + ghi chú y tế. *(Chỉ ghi nhận để cá nhân hóa & cảnh báo HLV — không chẩn đoán y tế.)*
- **Card "Khả thi bữa ăn" (mới)** — 4 chip chọn nhanh để gợi ý bữa ăn vừa đời sống thật & không gây áp lực, đồng thời thể hiện hệ thống hiểu chân dung KH:
  - **Chế độ ăn** (`diet_type`): Ăn mặn / Bán chay / Chay trứng-sữa / Thuần chay → `behavior.diet_type`.
  - **Ngân sách/ngày** (`daily_budget`): Tiết kiệm / Trung bình / Thoải mái → `behavior.budget_sensitivity` (tái dùng Q11).
  - **Món thích / không thích** (`liked_foods` / `disliked_foods`) → `behavior.food_preferences`.
  - **Quyền chủ động bữa ăn** (`meal_autonomy`): Tự nấu / Phụ thuộc người nấu / Ăn ngoài → `behavior.meal_autonomy`.

  > 4 trường này là **đầu vào của Process 2.0 (Persona-fit)** và **Feasibility Score** trong `docs/business-rules/Calorie-Meal-Business-Rules-v1.1.md`.

> Thời hạn mong muốn (`desired_timeframe`) là **đầu vào bắt buộc** để hệ thống sang bước tính toán & cá nhân hóa lộ trình. Mọi câu trả lời ghi kèm `survey_responses[]`.

**B. Lộ trình trải nghiệm (hệ thống tính & trả về)**

Sau khi HLV bấm **"Tính lộ trình trải nghiệm"**, hệ thống lưu bổ sung chân dung và tính lộ trình. Card "Lộ trình trải nghiệm đề xuất" lấy **gói làm đòn bẩy chính** và **tinh chỉnh mục tiêu làm đòn bẩy phụ**:

1. **Gói giải pháp đề xuất** — gồm **2 thông tin tách biệt**:
   - **Tên gói** — đại diện **bộ sản phẩm hỗ trợ** KH được hưởng (vd "Gói Khởi đầu / Tăng cường / Toàn diện"). Gói phù hợp theo Business Logic được **đánh dấu "Đề xuất"**, chọn sẵn. Chỉ hiện **tên gói**, không hiện giá/chi tiết (HLV chia sẻ trực tiếp).
   - **Thời gian** — **thời gian mua** (1 / 2 / 3 tháng), **mặc định 3 tháng** (đánh dấu "Tốt nhất" để có kết quả tối ưu). Đổi Thời gian → hệ thống **tính lại % thành công cho TẤT CẢ mục tiêu**.
   - **Số ngày lộ trình** — hiển thị **dựa trên mục tiêu KH đã chọn trước đó** (thời hạn mong muốn ở Card "Mục tiêu cần cải thiện"), vd "Lộ trình 90 ngày". Số ngày này gắn với mục tiêu, hiển thị kèm thời gian gói đang chọn.
2. **Mục tiêu & mức đạt được (theo gói đang chọn)** — liệt kê từng mục tiêu kèm **% đạt được** dưới gói đã chọn (vd: Giảm cân 100% · Mỡ nội tạng 80% · Tuổi sinh học 60%). Với mỗi mục tiêu:
   - **Đòn bẩy phụ — tinh chỉnh mục tiêu:** nút **− / +** để giảm tính thách thức từng mục tiêu; link **"đặt về khả thi"** đưa mục tiêu về mức khả thi 100% của gói. Mức khả thi (`cap`) = **tốc độ an toàn** (business-rules, Decision Table 1) × thời lượng gói; không vượt trần an toàn.
   - Mục tiêu sau điều chỉnh lưu vào `customer_personas` (`persona_data.aim.adjusted_target` theo từng mục tiêu + gói đã chọn).
3. **Lợi ích khi tham gia chương trình** — lấy từ database hoặc nội dung tĩnh.

> 🍽️ **Liên kết chức năng tiếp theo:** Mục tiêu **cân nặng sau điều chỉnh (giảm/tăng X kg)** chính là **đầu vào** của chức năng *Tính & gợi ý bữa ăn* (số Calo/ngày, số bữa/ngày) — xem `docs/business-rules/Calorie-Meal-Business-Rules-v1.1.md`. Vì vậy mục tiêu cân nặng được đánh dấu rõ trên màn hình.

> ⚠️ **Lưu ý nghiệp vụ:** Việc đề xuất & chọn gói cũng như tính % đạt được **KHÔNG** suy luận tùy ý mà căn cứ **Business Logic** dựa trên *mục tiêu*, *thời gian trải nghiệm* và *chân dung khách hàng* (DISC/Stage/ngân sách…). Bộ quy tắc đặc tả tại `docs/business-rules/packaged-service-advice-v1.0.md` (cần bổ sung catalog gói + ngưỡng thực tế).

**Hành động — 2 nút:**

1. **CTA "Tạo tài khoản KH"** — bấm khi **KH đồng ý với lộ trình đề xuất**. Chuyển sang màn **"Tạo tài khoản KH"** (đặt mua gói, lưu mục tiêu chỉ số, ảnh check-in… theo workflow mục 1).
2. **"Hoàn tất"** — bấm khi **KH chưa quyết định mua gói nào**. Hệ thống **lưu chân dung KH kèm mục tiêu mong muốn**, rồi **tính & đề xuất hành động kế tiếp** dựa trên DISC + Stage. Hành động này **không hiển thị ngay trên màn hình**, mà được lưu vào chân dung khách hàng như một **memory-note cho HLV** (vd: tiếp tục làm ấm, gửi video bài học, dẫn tới gặp 2/1…). → ghi `persona_data` + ghi chú Next-Best-Action (TD-AC5/TD-AC2); KH về Danh sách KH tiềm năng kèm "việc cần làm tiếp".

#### 1.5. Màn hình "Tạo tài khoản KH"

Truy cập khi bấm **"Tạo tài khoản KH"** ở màn 1.4. Prototype: `prototypes/hlv/hlv_tao_tai_khoan_kh.html`. Cho phép nhập: họ tên, SĐT, **email, mật khẩu**, mã giới thiệu; **gói dịch vụ** (tên + thời gian, lấy từ 1.4); **ngày gói bắt đầu** (tự lấy theo thời điểm bấm nút, HLV chỉ chỉnh 1 lần), **ngày gói kết thúc** (tự tính theo số tháng gói); **lưu mục tiêu chỉ số**; **ảnh check-in** (chân dung, toàn thân, vòng eo).

> 💬 **Tích hợp Objection Handler:** điểm chốt cuối — FAB hỗ trợ xử lý từ chối phút chót (thanh toán/cam kết). Mọi mẫu câu là **gợi ý chỉnh sửa được, không ép**; tinh thần đồng hành, không thu trước gây áp lực. Xem `docs/srs/Objection-Handler_v1.0.md`.

#### 1.6. Màn hình "Gợi ý bữa ăn"

Sau khi tạo tài khoản, hệ thống tính **"Gợi ý bữa ăn"** dựa trên mục tiêu cân nặng + số bữa (xem `docs/business-rules/Calorie-Meal-Business-Rules-v1.1.md`). Prototype: `prototypes/hlv/hlv_goi_y_bua_an.html`. Hiển thị **Calo/ngày**, **phân bổ theo bữa** và **thực đơn gợi ý mỗi bữa**; rồi quay về màn chi tiết KH / Danh sách KH tiềm năng.

> 🍽️ **Cá nhân hóa & khả thi (v1.1):** thực đơn được lọc qua **Process 2.0 (Persona-fit)** theo 4 tiêu chí ở §1.4 (chế độ ăn, ngân sách, sở thích, quyền chủ động). Màn này hiển thị thêm: **badge "Độ khả thi áp dụng" (Feasibility Score)**, **chi phí ước tính/ngày**, và — nếu KH thuộc nhóm *phụ thuộc* — nút **"Xuất hướng dẫn cho người nấu/đi chợ"**. Nếu điểm khả thi thấp, hệ thống nhắc HLV chỉnh trước khi giao. Chi tiết: `docs/business-rules/Calorie-Meal-Business-Rules-v1.1.md` §IX.

#### 1.0. Màn hình "Danh sách KH tiềm năng" (điểm vào)

Prototype: `prototypes/hlv/hlv_danh_sach_kh_tiem_nang.html`. Danh sách lead (tên, thẻ DISC, giai đoạn, nguồn nóng/ấm/lạnh, lead score, "việc cần làm tiếp"), bộ lọc, nút **"+"** tạo KH mới.

#### Chuỗi điều hướng (đã nối trong prototype)

```mermaid
graph LR
    DS["Danh sách KH tiềm năng"] -->|"+"| TKN["Tạo KH tiềm năng mới"]
    TKN -->|"Tiếp tục"| TAN["Nhập chỉ số Tanita"]
    TKN -->|"Hoàn tất"| DS
    TAN -->|"Tạo bản Tư Vấn"| BTV["Bản tư vấn"]
    BTV -->|"Tiếp tục"| TLM["Thiết lập mục tiêu"]
    BTV -->|"Hoàn tất"| DS
    TLM -->|"Tạo tài khoản KH"| TTK["Tạo tài khoản KH"]
    TLM -->|"Hoàn tất"| DS
    TTK --> GYB["Gợi ý bữa ăn"]
    GYB -->|"Hoàn tất"| DS
```

### 2. Chăm sóc Khách hàng (KH của tôi)

**Điểm vào ứng dụng HLV — màn "Tổng quan" (Dashboard).** Prototype: `prototypes/hlv/hlv_tong_quan.html`. Hiển thị KPI (số KH, lead, "hôm nay nên tiếp cận", **gợi ý bữa ăn cần làm mới**), cảnh báo, **truy cập nhanh (v1.1): Danh sách KH · Kho tài liệu · Chat**, danh sách KH cần chú ý → mở **"Chi tiết KH"**.

> 🔁 **Thay đổi v1.1 (Truy cập nhanh):**
> - Gộp 2 nút "KH tiềm năng" + "KH của tôi" thành **một nút "Danh sách KH"** → mở màn 2 tab (tab **KH tiềm năng mở mặc định**, tab **KH của tôi**). Xem `UI-UX-HLV_v1.1.md §1.0`.
> - Bổ sung nút **"Kho tài liệu"** → màn khai thác kho tri thức (xem §4 dưới đây).

**Màn "Chi tiết KH".** Prototype: `prototypes/hlv/hlv_chi_tiet_kh.html`. Gồm: hồ sơ + gói (ngày X/Y), **Gợi ý bữa ăn (đa phiên bản — §3)**, Tanita mới nhất, mục tiêu chỉ số, ảnh check-in; hành động: Tiến độ, **Điều chỉnh mục tiêu**, Chat. Đây là màn quay về sau khi tạo tài khoản & gợi ý bữa ăn (hoàn thiện vòng lặp).

```mermaid
graph LR
    TQ["Tổng quan (Dashboard)"] -->|"Danh sách KH"| DS["Danh sách KH<br/>(tab KH tiềm năng | KH của tôi)"]
    TQ -->|"Kho tài liệu"| KTL["Kho tài liệu"]
    TQ --> CT["Chi tiết KH"]
    DS -->|"tab KH của tôi"| CT
    CT -->|"Xem / làm mới"| GYB["Gợi ý bữa ăn"]
    GYB -->|"Lưu"| CT
    CT -->|"Điều chỉnh mục tiêu → tạo bản mới"| TLM["Thiết lập mục tiêu"]
```

### 3. Quản lý "Gợi ý bữa ăn" đa phiên bản (multi-version)

Mỗi gợi ý bữa ăn **chỉ có hiệu lực 10 ngày**. Sau 10 ngày, nếu kết quả sức khỏe thay đổi, HLV **đánh giá lại Tanita → điều chỉnh mục tiêu → tạo phiên bản mới**. Hệ thống **lưu lịch sử các phiên bản** (xem được phiên bản cũ).

- Màn HLV (`hlv_goi_y_bua_an.html`): có **thanh phiên bản** (số hiệu + trạng thái *Đang hiệu lực/Hết hiệu lực* + khoảng ngày) và **bộ chọn phiên bản** (xem lại bản cũ).
- Màn Chi tiết KH: hiển thị **phiên bản hiện tại + lịch sử**, nút **"Đánh giá lại & tạo phiên bản mới"**.
- Dashboard: đếm số KH có gợi ý bữa ăn **đã hết hiệu lực** cần làm mới.

> ⚠️ **Cần xác nhận cấu trúc dữ liệu.** Chưa có đặc tả chính thức cho "gợi ý bữa ăn". **Cấu trúc đề xuất (chờ anh/chị cung cấp mẫu để chốt):**
>
> ```
> meal_plan (gắn 1 KH)
>  └─ versions[]            // đa phiên bản
>      ├─ version_no        // #1, #2, #3…
>      ├─ status            // active | expired | superseded
>      ├─ valid_from / valid_to   // 10 ngày
>      ├─ target_snapshot   // calo/ngày, đạm, nước, số bữa, mục tiêu cân nặng tại thời điểm tạo
>      ├─ meals[]           // mỗi bữa: tên, giờ, kcal mục tiêu
>      │    └─ groups[]      // 3 NHÓM/bữa (xem Calorie-Meal §2.1b)
>      │         ├─ type            // protein | fiber_vitamin | carb
>      │         ├─ target_calo     // calo mục tiêu của nhóm
>      │         ├─ target_protein  // (g) — CHỈ nhóm protein
>      │         └─ dishes[]        // món từ catalog của nhóm: tên, khẩu phần/đơn vị, calo
>      ├─ notes              // hạn chế thịt đỏ/chiên-xào; nước 0.4L/10kg/ngày
>      ├─ created_by_coach / created_at
>      └─ tanita_ref        // bản Tanita căn cứ để tạo
> ```
>
> Cấu trúc trên đã cập nhật theo **mẫu phiếu Nutrition club** (3 nhóm: đạm/xơ/đường-bột) — logic chi tiết ở `docs/business-rules/Calorie-Meal-Business-Rules-v1.1.md §2.1b`.

### 4. Kho tài liệu — khai thác kho tri thức *(mới v1.1)*

**Điểm vào:** nút **"Kho tài liệu"** ở màn Tổng quan (Truy cập nhanh). Mục đích: không gian để HLV **tự học** và **lấy nội dung chia sẻ** cho KH/cộng đồng. Tổ chức theo **micro-course** (gắn Module Đào tạo — README §3). UI-UX chi tiết: `UI-UX-HLV_v1.1.md §3`.

**6 chủ đề:**

1. **Kiến thức dinh dưỡng** — video, slide bài giảng.
2. **Kiến thức vận động** — video, slide bài giảng.
3. **Phát triển bản thân** — slide đào tạo, video, tài liệu, sách.
4. **Kỹ năng kinh doanh** — slide đào tạo, video, tài liệu, sách.
5. **Câu chuyện bản thân** — video, slide (testimonial/câu chuyện thành công, để truyền cảm hứng & làm "bằng chứng người thật").
6. **Danh mục Nhóm dinh dưỡng / CLB** (Gym, Fit dinh dưỡng…) **& danh sách Huấn luyện viên** — tra cứu & kết nối.

**Hành vi chính:** tìm kiếm toàn kho + lọc theo định dạng (Video/Slide/Tài liệu/Sách); mở mục → trình xem tương ứng; mỗi mục có **"Chia sẻ cho KH"** (qua Chat) và **"Lưu"**. Chủ đề 1–5 là **thư viện nội dung**; chủ đề 6 là **danh mục Nhóm/CLB + HLV** (cấu trúc khác — xem `UI-UX-HLV_v1.1.md §3.1b`).

```mermaid
graph LR
    TQ["Tổng quan"] -->|"Kho tài liệu"| KTL["Kho tài liệu (lưới 6 chủ đề)"]
    KTL -->|"Chủ đề 1–5"| LIB["Thư viện nội dung<br/>(video/slide/tài liệu/sách)"]
    KTL -->|"Chủ đề 6"| DIR["Danh mục Nhóm/CLB + HLV"]
    LIB -->|"mở mục"| VIEW["Trình xem + Chia sẻ cho KH / Lưu"]
    DIR -->|"chọn"| DETAIL["Chi tiết Nhóm / Hồ sơ HLV"]
```

> **Tuân thủ:** gợi ý "đề xuất cho bạn" (nếu có) chỉ chạy khi `ai_data_sharing_enabled = true`; danh mục Nhóm/HLV lấy từ dữ liệu vận hành AnCare, **không trùng lặp VNHUB** (chỉ phục vụ tra cứu & kết nối, theo định hướng độc lập ở README).             