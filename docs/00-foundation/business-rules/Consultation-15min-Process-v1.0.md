# Quy trình Tư vấn 15 phút — Tiêu chuẩn (v1.0)

> **Nguồn:** trích xuất từ file ghi âm thực tế — `docs/00-foundation/consultation-sample-15-minutes.md`.
> **Vai trò:** làm nền tảng nghiệp vụ cho Epic E02 — Consultation (`docs/01-user-stories/epics/E02-Consultation.md`).
> **Nguyên tắc nền:** bám nguyên tắc README *"AI hỗ trợ không thao túng; con người ở vòng quyết định"*; mọi gợi ý là **gợi ý chỉnh sửa được**, không auto-gửi.

---

## 1. Tổng quan 5 giai đoạn

| Giai đoạn | Tên | Mục đích | Story AnCare |
|---|---|---|---|
| 1 | **Phá băng & Xây dựng thiện cảm** | Tạo niềm tin trong 1–2 phút đầu | US-E02-01 |
| 2 | **Khảo sát & Khai thác thông tin** | Thu thập mục tiêu, tiền sử, thói quen; tạo động lực trước khi đo | US-E02-02 |
| 3 | **Hướng dẫn đo lường chỉ số cơ thể** | Đo Tanita đúng tư thế, nhập chỉ số | US-E02-03 |
| 4 | **Phân tích chỉ số & Cảnh báo sức khỏe** | Đối chiếu chuẩn 5 bước, cảnh báo mỡ nội tạng | US-E02-04 |
| 5 | **Tư vấn giải pháp & Chốt chương trình** | Đề xuất giải pháp theo mục tiêu, chốt gói | US-E02-05 + US-E02-06 |

---

## 2. Giai đoạn 1 — Phá băng & Xây dựng thiện cảm

**Trình tự chuẩn:**
1. Hỏi thăm cá nhân (vd: năm sinh → liên hệ bản thân/đồng cảm).
2. Khen ngợi đặc điểm tích cực của khách.
3. Giới thiệu bản thân & vai trò.
4. Giới thiệu đội ngũ kèm **kết quả tiêu biểu** đã đạt được (vd: cải thiện trào ngược dạ dày, giảm 5 cân, giúp người thân cải thiện sức khỏe) → tạo niềm tin bằng bằng chứng người thật.

---

## 3. Giai đoạn 2 — Khảo sát & Khai thác thông tin

**Trình tự 7 nhóm câu hỏi (theo thứ tự chuẩn):**

| # | Nhóm | Câu hỏi mẫu | Dữ liệu ghi vào |
|---|---|---|---|
| 1 | **Mục tiêu** | "Anh/chị mong muốn cải thiện điều gì nhất?" (giảm cân / tăng cơ / đẹp da / kiểm soát bệnh lý) | `primary_goal` |
| 2 | **Tiền sử bệnh lý** | "Lần khám sức khỏe gần nhất? Vấn đề tim mạch, huyết áp, đại tràng, dạ dày?" | `pain_points[]` |
| 3 | **Giấc ngủ** | "Giờ đi ngủ? Giờ thức dậy? Độ sâu giấc ngủ?" | `lifestyle.sleep` |
| 4 | **Ăn sáng** | "Thường ăn gì vào bữa sáng?" | `lifestyle.diet` |
| 5 | **Uống nước** | "Lượng nước mỗi ngày? Uống đều đặn không?" | `lifestyle.water` |
| 6 | **Vận động & sinh hoạt** | "Tập thể dục mấy buổi/tuần? Hút thuốc? Uống rượu bia?" | `lifestyle.exercise`, `lifestyle.habits` |
| 7 | **Tạo động lực trước khi đo** | Chia sẻ câu chuyện thành công của HLV + hàng nghìn người đã giúp | (động viên, không lưu dữ liệu) |

> **Quy tắc:** KH trả lời ngắn gọn (vd "tôi chỉ bị mất insomnia, còn lại bình thường"). HLV đồng cảm/khen ngợi sau mỗi câu (vd: khen "người đàn ông tuyệt vời" nếu không hút thuốc).

---

## 4. Giai đoạn 3 — Hướng dẫn đo lường chỉ số cơ thể

**Thu thập trước khi đo:** tên, tuổi, chiều cao → cài đặt thông số trên cân.

**Chuẩn bị đo:** yêu cầu KH tháo chìa khóa, bỏ điện thoại ra khỏi người.

**Hướng dẫn tư thế đứng lên cân Tanita:**
1. Chạm gót chân vào sát tường / điện cực.
2. Đứng thẳng người, nhìn thẳng phía trước.
3. **Tuyệt đối không cúi đầu nhìn xuống.**

**Tác phong chuyên viên (chuẩn nội bộ):**
- Không đứng che khuất tầm nhìn KH.
- Không tì nách/tay vào mặt KH.
- Dùng bút che hờ hoặc chỉ số → tinh tế, lịch sự.

**Chỉ số thu thập:** cân nặng, mỡ %, cơ kg, nước %, mỡ nội tạng, xương, tuổi sinh học, BMR.

---

## 5. Giai đoạn 4 — Phân tích chỉ số & Cảnh báo sức khỏe

### 5.1. Thứ tự phân tích 5 bước (bắt buộc)

| Bước | Hành động | Output |
|---|---|---|
| **1** | Đọc cân nặng + tỷ lệ % mỡ → tính số kg mỡ (`kg mỡ = cân nặng × % mỡ / 100`) | kg mỡ thực tế |
| **2** | So sánh với bảng tiêu chuẩn theo tuổi & giới tính → nhận xét thừa/thiếu bao nhiêu | chênh lệch vs lý tưởng |
| **3** | Phân tích 2 loại mỡ: (1) mỡ dưới da — trao đổi thân nhiệt, giữ ấm, sờ nắn được; (2) mỡ nội tạng — trong ổ bụng, bao bọc nội tạng, không sờ được + bảng tham chiếu mỡ lý tưởng theo tuổi/giới | phân biệt 2 loại mỡ |
| **4** | Đọc chiều cao, đối chiếu cân nặng lý tưởng theo chiều cao/giới → hỏi KH có hài lòng với cân nặng hiện tại không, số cân mong muốn | cân mục tiêu |
| **5** | So sánh cân mục tiêu vs hiện tại → kết luận nhu cầu: **tăng cân / giảm cân / giữ cân** | loại nhu cầu |

### 5.2. Phân tích sâu — Mỡ nội tạng (cảnh báo nguy cơ)

- **Ngưỡng:** mỡ nội tạng lý tưởng nam = 1–7; nữ = 1–4 (theo Tanita). Vượt ngưỡng = thừa cấp độ.
- **Cơ chế gây bệnh:** mỡ quấn vào tim, gan, phổi & chui vào lòng mạch máu (so sánh: mạch máu bị mỡ bám giống cống/rãnh bị tắc).
- **Hậu quả:** nguyên nhân gốc rễ gây tiểu đường, tim mạch, huyết áp, xương khớp, **đặc biệt tai biến, đột quỵ**.
- **Triệu chứng lâm sàng cần hỏi:** tê bì chân tay, mỏi cổ vai gáy, đau lưng (do máu không lưu thông vì mạch bị tắc/hẹp).

### 5.3. Phân tích nước
- Mức nước tốt: nam > 50%, nữ > 45%.
- Công thức uống nước: **0,4 lít / 10 kg cân nặng / ngày**.

### 5.4. Phân tích tuổi sinh học
- Tuổi sinh học (tuế bào) vs tuổi thật: nếu trẻ hơn → chúc mừng (vd: tuổi thật 42, sinh học 37 = trẻ hơn 5 tuổi).

---

## 6. Giai đoạn 5 — Tư vấn giải pháp & Chốt chương trình

### 6.1. Logic tư vấn giải pháp theo mục tiêu

| Mục tiêu (từ Bước 5) | Chương trình áp dụng |
|---|---|
| **Giảm cân** | **Cân bằng Cơ — Nước — Mỡ** |
| **Tăng cân** | **Dinh dưỡng tế bào** |
| **Giữ cân** | **Bữa ăn lành mạnh** |

### 6.2. Chốt mục tiêu
- Xác nhận lại mục tiêu cuối cùng (vd: giảm từ 64,8kg → 62kg, giảm ~3kg).

### 6.3. Giới thiệu giải pháp (ví dụ: chương trình "Cơ — Nước — Mỡ")
1. **Phân tích sai lầm khi tự giảm cân:** đa số tự giảm (nhịn ăn, tập quá sức) → mất cơ + mất nước, mỡ vẫn giữ nguyên hoặc tăng.
2. **Giải thích cơ chế chương trình VIP:** cá nhân hóa, giảm **đúng mỡ thừa**, giữ nguyên hoặc tăng cơ bắp + nước.
3. **Khẳng định giá trị:** dùng tài liệu trực quan (3 khối cơ thể), cam kết chương trình độc quyền giúp KH đạt mục tiêu giảm cân + tăng cơ + khỏe mạnh từ bên trong.

---

## 7. Quy tắc đạo đức (xuyên suốt)
- **Disclaimer bắt buộc:** "Không có gì là thần dược; để có kết quả cần kiến thức dinh dưỡng, kỷ luật bản thân, hiểu nguyên lý để không phụ thuộc vào HLV hoặc sản phẩm."
- **AI hỗ trợ, không thay người:** mọi gợi ý phân tích/giải pháp là gợi ý, HLV xác nhận & điều chỉnh.
- **Không thao túng:** cảnh báo sức khỏe dựa trên chỉ số thật, không phóng đại; tôn trọng quyết định "để sau" của KH.
