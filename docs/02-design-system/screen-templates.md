# Khuôn mẫu màn hình (Screen Templates)

Mọi màn thuộc **1 trong 4 khuôn**. Khi thiết kế mockup, khai báo khuôn ở đầu file.

## T1 — Màn "Quyết định" (1 việc + 1 CTA)
**Dùng cho:** các bước trong luồng tư vấn (nhập Tanita, bản tư vấn, thiết lập mục tiêu, chốt gói, tạo tài khoản).
- **Cấu trúc**: AppBar (tên bước + ⓘ tùy chọn) → **1 khối nội dung chính** → (gập "Chỉnh"/"Xem thêm") → **CTA chính cố định chân màn** (+ 1 nút phụ tối đa).
- **Above-the-fold**: ≤ 3 khối.

## T2 — Màn "Danh sách"
**Dùng cho:** danh sách KH tiềm năng, KH hiện tại, thành viên, tài liệu.
- **Cấu trúc**: AppBar + tìm kiếm → (tab nếu cần) → **thẻ gọn (≤2 nhãn)** → FAB cố định (1 hành vi).
- **Above-the-fold**: thấy ≥ 3 thẻ.

## T3 — Màn "Bảng điều khiển / Tổng quan"
**Dùng cho:** Trang chủ HLV, Trang chủ KH.
- **Cấu trúc**: lời chào → **1 việc nổi bật nhất hôm nay (focus card)** → lối tắt (≤3) → danh sách cần chú ý. KPI phụ gom 1 hàng nhỏ, **không phải 4 ô lớn**.
- **Above-the-fold**: focus card phải nằm trong màn đầu.

## T4 — Màn "Chi tiết" (hồ sơ)
**Dùng cho:** chi tiết KH, chi tiết thành viên, chi tiết lead.
- **Cấu trúc**: header gọn → **hành động nhanh (≤3)** → các card thông tin **gập mặc định**, mở từng cái khi cần.
- **Above-the-fold**: chỉ header + hành động nhanh mở sẵn.

## Bảng map Module → Khuôn (gợi ý)

| Module (Epic) | Khuôn chủ yếu |
|---|---|
| E01 Lead Management | T2 (danh sách) + T4 (chi tiết lead) |
| E02 Consultation | T1 (mỗi bước tư vấn) |
| E03 Customer Care | T3 (tổng quan chăm sóc) + T1 (talking point) |
| E04 Team Operations | T2 (danh sách TV) + T4 (chi tiết TV) |
| E05 Self-Development | T2 (kho khóa học) + T1 (bài học) |
| E06 Personal Health | T3 (trang chủ KH) + T1 (check-in) |
| E00 Platform Shell | T3 (main screen) |

> Đây là gợi ý; mockup cụ thể có thể chọn khuôn khác nếu nghiệp vụ yêu cầu — nhưng phải giải thích lý do.
