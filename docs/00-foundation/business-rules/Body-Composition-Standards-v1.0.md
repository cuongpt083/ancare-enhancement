# Tiêu chuẩn thành phần cơ thể (WHO/Tanita) — v1.0

> **Quyết định:** D05 (AI tìm/đề xuất bảng chuẩn). Nguồn: file sample `consultation-sample-15-minutes.md` + khuyến nghị phổ biến Tanita/WHO. **Cần PO xác nhận lại số liệu chính thức** trước khi triển khai.
> **Vai trò:** nền tảng cho US-E02-04 (Phân tích chỉ số & Cảnh báo sức khỏe — 5 bước).
> **Quy tắc UX:** chỉ số kỹ thuật (điểm 0-100) **không in ra UI** (L4); quy về nhãn ngôn ngữ (Tốt/Cần lưu ý/Cảnh báo). Số chi tiết chỉ hiện khi "Xem chi tiết".

## 1. Mỡ cơ thể (% body fat) — lý tưởng theo tuổi & giới

| Nhóm tuổi | Nam (lý tưởng) | Nam (mức tốt) | Nữ (lý tưởng) | Nữ (mức tốt) |
|---|---|---|---|---|
| 20-39 | 8-19% | ≤20% | 21-32% | ≤33% |
| 40-59 | 11-21% | ≤22% | 23-33% | ≤34% |
| 60-79 | 13-24% | ≤25% | 24-35% | ≤36% |

> Mốc lý tưởng (Tanita) = cột dưới của khoảng lý tưởng. Vd: nam 42 tuổi → lý tưởng 17.5%, mức tốt 20.5% (theo sample). Thừa = chỉ số thực − mốc lý tưởng.

## 2. Mỡ nội tạng (visceral fat rating)

| Mức | Nam | Nữ | Ý nghĩa / hiển thị |
|---|---|---|---|
| **Lý tưởng** | 1-7 | 1-4 | "Tốt" (xanh) |
| **Cần lưu ý** | 8-9 | 5-6 | "Hơi cao" (vàng) — cảnh báo nhẹ |
| **Cảnh báo** | 10-14 | 7-12 | "Cao — nguy cơ" (đỏ) — cảnh báo mỡ quấn tim/gan/phổi/mạch máu |
| **Nguy hiểm** | ≥15 | ≥13 | "Rất cao — nguy cơ đột quỵ" (đỏ) |

> **Cơ chế gây bệnh** (sample): mỡ quấn tim, gan, phổi & chui vào lòng mạch máu (so sánh: mạch máu bị mỡ bám giống cống/rãnh bị tắc). Hậu quả: tiểu đường, tim mạch, huyết áp, xương khớp, **đặc biệt tai biến, đột quỵ**.
> **Triệu chứng lâm sàng cần hỏi**: tê bì chân tay, mỏi cổ vai gáy, đau lưng (do máu không lưu thông vì mạch bị tắc/hẹp).

## 3. Nước cơ thể (% body water)

| Giới | Lý tưởng | Cần lưu ý |
|---|---|---|
| Nam | > 50% | 45-50% |
| Nữ | > 45% | 40-45% |

> Công thức uống nước: **0,4 lít / 10 kg cân nặng / ngày**. Vd: 65kg → 2,6 lít/ngày.

## 4. Khối lượng cơ (muscle mass)

| Giới | Lý tưởng (tỉ lệ) | Cần lưu ý |
|---|---|---|
| Nam | 38-54% | < 38% |
| Nữ | 29-35% | < 29% |

> Khối lượng cơ tuyệt đối (kg) tùy chiều cao; tỉ lệ % ổn định hơn để đánh giá.

## 5. Tuổi sinh học (metabolic age)

- Tuổi sinh học < tuổi thật → cơ thể khỏe (chúc mừng).
- Tuổi sinh học > tuổi thật → cơ thể già hơn tuổi thật (cần cải thiện).
- Hiển thị: "Cơ thể trẻ hơn X tuổi" / "Cơ thể lớn hơn X tuổi".

## 6. BMI (WHO)

| Phân loại | BMI (kg/m²) |
|---|---|
| Thiếu cân | < 18.5 |
| Bình thường | 18.5 - 24.9 |
| Thừa cân | 25.0 - 29.9 |
| Béo phì độ I | 30.0 - 34.9 |
| Béo phì độ II | 35.0 - 39.9 |
| Béo phì độ III | ≥ 40.0 |

> BMI chỉ là chỉ số phụ; Tanita dùng cân nặng lý tưởng theo chiều cao & giới (mục 7).

## 7. Cân nặng lý tưởng theo chiều cao (Tanita, tham chiếu)

Cân nặng lý tưởng ≈ dựa chiều cao + giới; HLV dùng cân mục tiêu KH tự nêu (Bước 4 US-E02-04) làm mốc chính. Bảng chi tiết theo Tanita — `[cần PO xác nhận bảng đầy đủ]`.

---
*TODO D05: PO xác nhận lại số liệu chính thức (đặc biệt mục 2 mỡ nội tạng + mục 7 cân lý tưởng) trước khi triển khai US-E02-04. Các giá trị trên lấy từ file sample + khuyến nghị phổ biến Tanita.*
