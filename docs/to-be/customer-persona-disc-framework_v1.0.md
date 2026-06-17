# KHUNG CHÂN DUNG KHÁCH HÀNG + DISC — ANCARE / SmartLife

**Phiên bản:** v1.0 (draft) · **Cập nhật:** 2026-06-17
**Mục đích:** Chuẩn hóa bộ dữ liệu chân dung khách hàng (customer persona) **tích hợp tính cách DISC + giai đoạn sẵn sàng thay đổi (Stage-of-Change)**, làm đầu vào cho việc lên kịch bản và phương pháp tư vấn nhằm **tối ưu tỷ lệ chuyển đổi** (khách hàng mục tiêu → mua gói dịch vụ).
**Bám sát:**
- HLD hiện trạng (`docs/as-is/high-level-design.md`) — `ConsultationAgent` đã dùng *WHO + DISC*; bảng `health_profiles`, `users.is_prospect`.
- To-do v2.0 — **TD-AC4** (chấm điểm/ưu tiên lead), **TD-AC5-P1/P2** (thư viện kịch bản gắn thẻ DISC + Stage-of-Change, copilot MI).
- Quy trình 5 bước xây dựng chân dung khách hàng (Vietnam Business Insider).

> **Nguyên tắc nền:** DISC là **một thẻ phụ** giúp chọn *tông giọng & cách trình bày*, **không** phải trung tâm. Trục quyết định chuyển đổi là **Aim (mục tiêu sức khỏe) + Pain point + Giai đoạn sẵn sàng thay đổi**. DISC điều chỉnh *cách nói*, Stage-of-Change quyết định *nói gì và khi nào chốt*.

---

## Phần I — Quy trình 5 bước (ánh xạ sang AnCare)

Tài liệu nguồn nêu 5 bước; dưới đây là cách AnCare hiện thực hóa từng bước:

| Bước (nguồn) | Diễn giải | Hiện thực trong AnCare |
|---|---|---|
| **1. Xác định mục tiêu** xây dựng persona | Persona phục vụ mục đích gì trong bán hàng; nhu cầu cơ bản | Mục tiêu = tăng tỷ lệ chuyển đổi Bước 1→2 (làm ấm → mời → đến 2/1 → trải nghiệm → mua gói). Mỗi persona gắn 1 *mục tiêu sức khỏe trội*. |
| **2. Thu thập dữ liệu** | Nội bộ, công cụ khảo sát, social listening, phỏng vấn trực tiếp | Import danh bạ/MXH (TD-AC1 DSKHTN), khảo sát onboarding (bộ câu hỏi Phần V), Tanita intake, chat insight (`apply_insights_to_profiles`). |
| **3. Xử lý thông tin** | Phân loại theo tâm lý/hành vi/nhân khẩu/sở thích; 2–4 persona; tiêu chí: tuổi, giới, thu nhập, vấn đề, kênh, yếu tố quyết định mua | Phân tầng thành **3 persona lõi** (Phần IV) + thẻ DISC + thẻ Stage-of-Change. Chấm điểm ưu tiên (TD-AC4). |
| **4. Tạo danh tính & khuôn mặt** | Tên 1–2 chữ, giới tính, hình dung khuôn mặt | Mỗi persona có tên + avatar đại diện (Phần IV). |
| **5. Bổ sung chi tiết** | Phong cách sống, nhân khẩu, sở thích, mối quan tâm sản phẩm | Trường chi tiết trong schema (Phần II) + kịch bản tiếp cận (Phần III). |

---

## Phần II — Schema bộ dữ liệu chân dung khách hàng

Cấu trúc đề xuất cho mỗi bản ghi persona/lead (gợi ý lưu trong `health_profiles` mở rộng hoặc bảng `lead_profiles` mới của module Thu hút TD-AC1). Đánh dấu **[lead]** = thu thập sớm cho lead, **[KH]** = bổ sung sau khi onboarding.

### 1. Định danh & nhân khẩu (bước 4–5)
- `persona_name` — tên gợi nhớ (vd "Chị Lan văn phòng"). **[lead]**
- `age_range`, `gender`, `occupation`, `location`, `income_band` (tham khảo, không bắt buộc). **[lead]**
- `family_status` — độc thân / có con nhỏ / chăm cha mẹ… (ảnh hưởng thời gian & động lực). **[lead]**

### 2. Mục tiêu & nỗi đau sức khỏe (trục Aim — quan trọng nhất)
- `primary_goal` — giảm cân / tăng cơ / kiểm soát đường huyết / tăng năng lượng / cải thiện tiêu hóa / làm đẹp da. **[lead]**
- `pain_points[]` — danh sách nỗi đau (vd: mệt mỏi buổi chiều, mặc cảm ngoại hình, bác sĩ cảnh báo mỡ máu). **[lead]**
- `health_metrics` — Tanita (cân nặng, BMI, mỡ, cơ, tuổi sinh học…) khi có. **[KH]**
- `trigger_event` — sự kiện châm ngòi (khám sức khỏe, sắp cưới, sau sinh, bạn bè rủ). **[lead]**
- `success_definition` — khách định nghĩa "thành công" thế nào (mặc vừa váy cũ / leo cầu thang không hụt hơi). **[lead]**

### 3. Hành vi & bối cảnh (bước 5)
- `lifestyle` — lịch sinh hoạt, mức vận động, thói quen ăn uống.
- `channels[]` — kênh hay dùng (Zalo, Facebook, TikTok, gặp trực tiếp). **[lead]**
- `tech_comfort` — mức quen công nghệ (thấp/trung/cao).
- `budget_sensitivity` — nhạy giá (cao/trung/thấp) + khả năng chi cho sức khỏe. **[lead]**
- `decision_factors[]` — yếu tố quyết định mua (bằng chứng khoa học, người thật-việc thật, giá, sự đồng hành, thương hiệu). **[lead]**
- `objections[]` — phản đối thường gặp (sợ sản phẩm "đa cấp", từng thất bại giảm cân, không có thời gian, hỏi ý kiến chồng/vợ).

### 4. Thẻ tính cách DISC (thẻ phụ — điều chỉnh tông giọng)
- `disc_primary` — D / I / S / C (xem Phần III).
- `disc_secondary` — kiểu phụ (đa số người là tổ hợp 2 chữ).
- `disc_confidence` — `self_reported` | `inferred` (suy luận từ hành vi chat/khảo sát) | `coach_tagged`.
- `communication_pref` — nhịp nhanh/chậm, thích số liệu hay cảm xúc, thích chốt nhanh hay cần thời gian.

### 5. Thẻ giai đoạn sẵn sàng thay đổi (Stage-of-Change — quyết định chiến thuật chốt)
- `stage` — `precontemplation` (chưa nghĩ tới) / `contemplation` (đang cân nhắc) / `preparation` (chuẩn bị) / `action` (bắt đầu) / `maintenance` (duy trì).
- `readiness_score` — 0–100 (kết hợp với lead score TD-AC4).
- `motivation_quotes[]` — "câu nói thay đổi" do khách tự nói (dùng cho MI copilot TD-AC5-P2).

### 6. Trạng thái phễu & vận hành (liên kết TD-AC1/AC2)
- `funnel_stage` — Mới → Làm ấm → Đã mời → Nhận lời → Đến 2/1 → Trải nghiệm → Mua gói.
- `lead_score`, `next_best_action`, `source` (nóng/ấm/lạnh), `assigned_coach`.
- `consent_ai` — `ai_data_sharing_enabled` (bắt buộc trước khi đưa PII cho LLM — Apple 5.1.1(i)).

> **Gợi ý kỹ thuật:** Cụm DISC + Stage có thể lưu JSONB `persona_tags` trong `health_profiles`, để `ConsultationAgent` và thư viện kịch bản (TD-AC5) đọc qua tool `ai_coach_context`.

---

## Phần III — DISC × Stage-of-Change → Kịch bản & cách tư vấn

### 3.1 Bốn kiểu DISC trong bối cảnh tư vấn sức khỏe

| Kiểu | Đặc điểm | Động lực mua | Nên làm | Tránh |
|---|---|---|---|---|
| **D — Quyết đoán** (Dominance) | Nhanh, thẳng, hướng kết quả, bận rộn, thích kiểm soát | Kết quả nhanh, hiệu quả, tiết kiệm thời gian | Vào thẳng vấn đề; nói kết quả & lộ trình ngắn gọn; đưa 2 lựa chọn để họ quyết; tôn trọng thời gian | Nói dài dòng, lan man cảm xúc, ép buộc |
| **I — Ảnh hưởng** (Influence) | Cởi mở, cảm xúc, thích xã hội, sợ nhàm chán, thích được công nhận | Trải nghiệm vui, cộng đồng, được khen, câu chuyện truyền cảm hứng | Kể câu chuyện người thật, ảnh before/after; mời vào cộng đồng/nhóm; khen ngợi chân thành; tạo hứng khởi | Quá nhiều số liệu khô khan, quy trình cứng nhắc |
| **S — Ổn định** (Steadiness) | Điềm đạm, ngại thay đổi, trung thành, cần an toàn, quyết định chậm | Sự đồng hành, cam kết hỗ trợ, không rủi ro, được dẫn dắt từng bước | Trấn an, đi từng bước nhỏ; nhấn mạnh hỗ trợ 1-1 liên tục; cho thời gian; bảo chứng an toàn | Hối thúc chốt, tạo áp lực, thay đổi đột ngột |
| **C — Tuân thủ/Phân tích** (Conscientiousness) | Cẩn trọng, hoài nghi, cần bằng chứng, đọc kỹ, hỏi nhiều | Dữ liệu, cơ chế khoa học, minh bạch thành phần & cam kết | Cung cấp số liệu, nghiên cứu, thành phần, FAQ chi tiết; cho thời gian tự kiểm chứng; trung thực về hạn chế | Nói cảm tính, phóng đại, giấu thông tin, giục |

### 3.2 Stage-of-Change → trọng tâm hội thoại (theo tinh thần MI — Motivational Interviewing)

| Giai đoạn | Tâm lý khách | Mục tiêu của TV | Việc nên làm | **Tuyệt đối KHÔNG** |
|---|---|---|---|---|
| **Precontemplation** | Chưa thấy vấn đề | Gieo nhận thức | Hỏi mở, chia sẻ thông tin nhẹ nhàng, gương người quen | Pitch bán hàng, dọa dẫm |
| **Contemplation** | Lưỡng lự, "có nên không" | Cân lợi–hại, khơi "lý do thay đổi" | Phản chiếu, hỏi về hình dung tương lai, gỡ rào cản | Chốt sớm |
| **Preparation** | Sẵn sàng, tìm cách | Đưa lộ trình cụ thể & đề nghị 2/1 | Đề xuất buổi đo Tanita/2-1, gói phù hợp, kế hoạch | Để khách tự bơi |
| **Action** | Bắt đầu làm | Hỗ trợ sát, củng cố | Theo dõi GNV, khen tiến bộ, xử lý trở ngại sớm | Bỏ mặc sau khi bán |
| **Maintenance** | Đã quen | Giữ thói quen, mở rộng | Cộng đồng, mục tiêu mới, giới thiệu người mới | Coi như "xong việc" |

### 3.3 Ma trận kết hợp — "nói gì × nói thế nào"

> **Stage quyết định *nói gì* (nội dung & thời điểm chốt). DISC quyết định *nói thế nào* (tông giọng & hình thức).**

Ví dụ ô giao nhau (dùng làm thẻ cho thư viện kịch bản TD-AC5-P1):

- **C × Contemplation:** gửi tài liệu cơ chế khoa học + bảng so sánh, hẹn "khi nào anh xem xong mình trao đổi"; *không* giục. Câu chốt mềm: *"Anh cần thêm dữ liệu gì để yên tâm quyết định?"*
- **I × Preparation:** mời tham gia buổi trải nghiệm nhóm vui vẻ + khoe câu chuyện thành công; chốt bằng cảm xúc & cộng đồng: *"Tuần này nhóm mình có buổi đo chỉ số, chị tham gia cho vui rồi mình xem kết quả nhé!"*
- **D × Preparation:** đề nghị thẳng 2 phương án gói + kết quả kỳ vọng theo mốc thời gian; *"Anh chọn gói 3 tháng hay 6 tháng để em set lộ trình luôn?"*
- **S × Contemplation:** trấn an, cam kết đồng hành từng bước, không rủi ro: *"Mình bắt đầu nhẹ nhàng, em theo sát chị mỗi ngày, không ổn mình điều chỉnh ngay."*

---

## Phần IV — 3 Persona lõi mẫu (có thể mở rộng 2–4)

> Bám tiêu chí phân loại của bài viết: tuổi, giới, thu nhập, vấn đề, kênh, yếu tố quyết định mua. Số liệu mang tính minh họa, cần hiệu chỉnh theo dữ liệu thực của đội nhóm.

### Persona 1 — "Chị Lan văn phòng" (giảm cân sau sinh)
- **Nhân khẩu:** Nữ, 32, nhân viên văn phòng, TP.HCM, thu nhập trung bình-khá; có con nhỏ.
- **Mục tiêu trội:** Giảm 5–7 kg sau sinh, lấy lại tự tin & năng lượng.
- **Pain points:** Mặc cảm ngoại hình, mệt mỏi, không có thời gian tập.
- **DISC:** I/S — cảm xúc, thích cộng đồng nhưng cần được trấn an.
- **Stage điển hình:** Contemplation → Preparation.
- **Kênh:** Facebook, Zalo. **Yếu tố quyết định:** người thật-việc thật, sự đồng hành, không quá đắt.
- **Objection:** "Sợ không có thời gian", "từng thất bại giảm cân".
- **Cách tiếp cận:** Kể câu chuyện mẹ bỉm thành công + cam kết đồng hành sát; lộ trình nhẹ nhàng theo ngày (GNV).

### Persona 2 — "Anh Minh quản lý" (cảnh báo sức khỏe, bận rộn)
- **Nhân khẩu:** Nam, 41, quản lý/kinh doanh, thu nhập cao, rất bận.
- **Mục tiêu trội:** Giảm mỡ máu/mỡ bụng, kiểm soát chỉ số sau khám sức khỏe.
- **Pain points:** Bác sĩ cảnh báo, ít thời gian, ăn ngoài nhiều.
- **DISC:** D/C — quyết đoán nhưng cần bằng chứng.
- **Stage:** Preparation (đã có trigger từ kết quả khám).
- **Kênh:** Gặp trực tiếp/Zalo. **Yếu tố quyết định:** hiệu quả nhanh + cơ chế khoa học + tiết kiệm thời gian.
- **Objection:** "Liệu có thật sự hiệu quả?", "tôi không có thời gian".
- **Cách tiếp cận:** Vào thẳng kết quả + dữ liệu Tanita; đề nghị 2 phương án gói; lộ trình tối giản, đo lường được.

### Persona 3 — "Cô Hạnh trung niên" (sức khỏe & tuổi sinh học)
- **Nhân khẩu:** Nữ, 55, nội trợ/về hưu, con cái trưởng thành.
- **Mục tiêu trội:** Tăng năng lượng, cải thiện tiêu hóa/giấc ngủ, "trẻ hóa" tuổi sinh học.
- **Pain points:** Mệt mỏi, lo bệnh tuổi già, cô đơn.
- **DISC:** S/C — điềm đạm, ngại thay đổi, cần an toàn & bằng chứng.
- **Stage:** Precontemplation → Contemplation (cần gieo nhận thức).
- **Kênh:** Zalo, gặp trực tiếp, cộng đồng. **Yếu tố quyết định:** an toàn, đồng hành, người quen giới thiệu.
- **Objection:** "Lớn tuổi dùng có sao không", "để hỏi con đã".
- **Cách tiếp cận:** Trấn an, đi từng bước rất nhỏ; mời vào cộng đồng ấm áp; bảo chứng an toàn; không hối thúc.

---

## Phần V — Bộ câu hỏi khảo sát chân dung khách hàng (đề xuất)

Bộ câu hỏi gắn nhãn theo **mục đích** và **SP-category** (Aim/People/Resource…) + cờ **[DISC]** cho câu suy luận tính cách, **[Stage]** cho câu định vị giai đoạn. Thiết kế để dùng ở **2 thời điểm**: (A) Làm ấm lead — hỏi tự nhiên trong hội thoại; (B) Onboarding — khảo sát có cấu trúc trước/trong buổi 2/1.

### Nhóm 1 — Mục tiêu & nỗi đau (Aim — bắt buộc, hỏi sớm)
1. Điều gì khiến anh/chị bắt đầu quan tâm đến sức khỏe/vóc dáng lúc này? *(trigger event)* **[Stage]**
2. Nếu 3 tháng tới mọi thứ tiến triển tốt, anh/chị hình dung mình thay đổi thế nào? *(success_definition)* **[Stage]**
3. Vấn đề sức khỏe nào đang làm phiền an/chị nhất hiện nay? *(pain_point)*
4. Anh/chị đã từng thử cách nào trước đây chưa? Kết quả ra sao? *(lịch sử & objection)*
5. Trên thang 0–10, anh/chị sẵn sàng thay đổi đến mức nào — và vì sao không thấp hơn? *(MI — khơi lời nói thay đổi)* **[Stage]**

### Nhóm 2 — Bối cảnh & lối sống (People/Resource)
6. Một ngày của anh/chị thường diễn ra thế nào (giờ giấc, vận động, ăn uống)? *(lifestyle)*
7. Anh/chị có ràng buộc gì về thời gian/công việc/gia đình không? *(family_status, time)*
8. Anh/chị thường tìm hiểu thông tin sức khỏe qua kênh nào? *(channels)*

### Nhóm 3 — Yếu tố quyết định & rào cản (Resource/Objection)
9. Khi quyết định dùng một sản phẩm/dịch vụ sức khỏe, điều gì quan trọng nhất với anh/chị: kết quả nhanh, bằng chứng khoa học, chi phí, hay có người đồng hành? *(decision_factors)* **[DISC]**
10. Điều gì khiến anh/chị còn băn khoăn/chưa quyết định? *(objections)* **[Stage]**
11. Ngân sách anh/chị thấy hợp lý để đầu tư cho sức khỏe là khoảng nào? *(budget_sensitivity — hỏi tế nhị, giai đoạn sau)*
12. Quyết định này anh/chị tự quyết hay cần trao đổi với ai? *(người ảnh hưởng)*

### Nhóm 4 — Câu hỏi suy luận DISC (đan vào hội thoại, không hỏi lộ liễu)
13. Anh/chị thích em trình bày ngắn gọn trọng tâm, hay chi tiết đầy đủ? → ngắn gọn = **D**; chi tiết/số liệu = **C**. **[DISC]**
14. Anh/chị thấy hứng thú với câu chuyện người thật đã thành công, hay với số liệu & cơ chế khoa học? → câu chuyện = **I**; số liệu = **C**. **[DISC]**
15. Anh/chị thích bắt đầu ngay rồi điều chỉnh dần, hay muốn chuẩn bị kỹ rồi mới bắt đầu? → ngay = **D/I**; chuẩn bị kỹ = **S/C**. **[DISC]**
16. Khi thay đổi điều gì đó, anh/chị thấy thoải mái khi làm nhanh hay cần thời gian làm quen? → nhanh = **D**; cần thời gian = **S**. **[DISC]**

> *Cách dùng DISC:* TV/HLV (hoặc LLM với cờ `disc_confidence=inferred`) tổng hợp tín hiệu từ câu 13–16 **và** quan sát nhịp nhắn tin để gán `disc_primary/secondary`. Không bắt khách "làm test DISC" — gây mất tự nhiên.

### Nhóm 5 — Định vị giai đoạn sẵn sàng (Stage — chọn chiến thuật chốt)
17. Anh/chị đang ở giai đoạn nào: chưa nghĩ tới / đang cân nhắc / muốn bắt đầu sớm / đã đang làm? **[Stage]**
18. Nếu có một lộ trình phù hợp và người đồng hành, anh/chị muốn bắt đầu khi nào? **[Stage]**

### (Tùy chọn) Câu hỏi định lượng cho onboarding có cấu trúc
- Thang Likert 1–5 cho: mức độ ưu tiên sức khỏe, mức tin vào sản phẩm bổ sung, mức sẵn sàng đầu tư, mức cần đồng hành.
- Tanita intake (cân nặng, BMI, mỡ, cơ, tuổi sinh học) — đã có trong onboarding hiện tại.

---

## Phần VI — Liên kết hệ thống & bước tiếp theo

- **Đầu vào `ConsultationAgent`:** map kết quả khảo sát → JSONB `persona_tags` (DISC + Stage + pain) để agent cá nhân hóa tư vấn onboarding (hiện đã dùng WHO + DISC).
- **Thư viện kịch bản TD-AC5-P1:** mỗi mẫu tin làm ấm/mời gắn thẻ `(DISC, Stage)` → LLM chỉ viết lại cho mượt, HLV chọn & duyệt (giữ "lập trường" kết nối, không pitch).
- **MI Copilot TD-AC5-P2:** dùng `motivation_quotes[]` + `stage` để gợi ý hỏi mở/phản chiếu đúng giai đoạn.
- **Lead scoring TD-AC4:** `lead_score = phù hợp(persona×gói) × ấm(funnel) × readiness(stage)`.
- **Đề xuất triển khai dữ liệu:** (1) thêm bảng/JSONB persona; (2) số hóa bộ câu hỏi thành form onboarding + gợi ý câu hỏi làm ấm trong chat; (3) dashboard phễu theo persona để đo tỷ lệ chuyển đổi từng nhóm.

> **Cảnh báo đạo đức & tuân thủ:** DISC/persona chỉ để *phục vụ khách tốt hơn*, không thao túng. Tuân thủ consent AI (`ai_data_sharing_enabled`) trước khi đưa dữ liệu cá nhân cho LLM; không chẩn đoán y tế; nội dung bám Knowledge Base.

---
*Tài liệu nháp v1.0 — cần đội nhóm hiệu chỉnh persona & ngưỡng theo dữ liệu thực tế.*
