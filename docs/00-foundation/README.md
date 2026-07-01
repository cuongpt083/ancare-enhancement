# 00 — Foundation (Nguồn sự thật duy nhất)

Đây là **bộ nền tảng canonical** của dự án AnCare DXP. Mỗi khái niệm chỉ tồn tại **một phiên bản** tại đây. Mọi tài liệu ở các tầng sau (user stories, design system, mockups, prototypes) **phai tham chiếu về đây**, không định nghĩa lại.

## Mục lục

| File | Vai trò |
|---|---|
| `vision-and-values.md` | Tầm nhìn, sứ mệnh, 4 giá trị cốt lõi (module), định hướng thiết kế, giới hạn phạm vi, nguyên tắc đạo đức. |
| `personas.md` | 3 vai trò người dùng (HLV, KH, Founder/Admin) + khung chân dung khách hàng (DISC + Stage-of-Change). |
| `glossary.md` | Thuật ngữ & viết tắt dùng xuyên suốt dự án. |
| `feature-tree.md` | Cây chức năng — **xương sống để sinh epics & user stories** (giữ nguyên từ bản gốc). |
| `business-rules/` | Quy tắc nghiệp vụ thật (logic tính toán): `Calorie-Meal-Business-Rules-v1.1.md`, `packaged-service-advice-v1.0.md`, `Consultation-15min-Process-v1.0.md` (quy trình tư vấn 15 phút — 5 giai đoạn, 5 bước phân tích, logic giải pháp). |
| `consultation-sample-15-minutes.md` | Trích xuất nội dung tư vấn thực tế từ file ghi âm — nguồn gốc của `business-rules/Consultation-15min-Process-v1.0.md`. |

## Quy ước

- **Một phiên bản duy nhất**: khi cần cập nhật, sửa tại đây rồi tăng phiên bản trong file; không tạo bản song song.
- **Tham chiếu, không lặp**: tầng 01–04 trỏ tới foundation bằng đường dẫn tương đối, không chép nội dung.
- **Ngôn ngữ**: tiếng Việt. Định dạng: Markdown.
- **Lịch sử**: bản đầy đủ trước khi khởi động lại nằm trong `docs/99-archive/` và git history (commit `895e4dd` trở về trước).
