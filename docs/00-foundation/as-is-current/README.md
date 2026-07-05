# As-Is Hiện tại (bản sống) — App AnCare đang chạy

> **Vai trò:** Nơi PO nộp **ảnh chụp app hiện tại + mô tả tổng quát**; AI sẽ phân tích As-Is chi tiết để đưa vào GAP analysis (`docs/03-mockups/screen-gap-analysis.md`).
> **Khác archive:** `docs/99-archive/as-is/` là bản cũ đã **đóng băng** (có thể lỗi thời). Thư mục này là **bản sống**, cập nhật được khi app thay đổi.
> **Nguyên tắc kế thừa:** app đã có nhiều thứ ổn (logic, data, layout) → tối đa kế thừa, chỉ đánh GAP phần cần đổi.

## Cách PO nộp As-Is

### Bước 1 — Chụp ảnh
- Chụp theo **trình tự thao tác thật** (luồng nghiệp vụ), vd: đăng nhập → dashboard → vào tư vấn → nhập Tanita →...
- Ưu tiên **luồng trọng tâm trước**: E02 (tư vấn 15p), E01 (KH tiềm năng), E06 (KH trang chủ).
- Đặt ảnh vào:
  - `screenshots-hlv/` — màn HLV
  - `screenshots-kh/` — màn Khách hàng
- **Quy ước tên:** `<nn>_<tên_ngắn>.png` theo thứ tự thao tác, vd:
  - `01_dang_nhap.png` · `02_dashboard.png` · `03_tao_kh_tiem_nang.png` · `04_nhap_tanita.png` · `05_ban_tu_van.png`...

### Bước 2 — Mô tả tổng quát
- Mở `as-is-notes.md` (cùng thư mục) → điền theo template:
  - **Sơ đồ luồng tổng quát** (đầu file): các màn nối nhau thế nào (vd `dang_nhap → dashboard → tao_kh → nhap_tanita → ...`)
  - **Mỗi màn 1 mục**: tên + path ảnh + vai trò + từ đâu tới/đi đâu + các trường thông tin hiển thị + nhận xét (gì ổn/gì cần cải thiện — optional)
- **Không cần mô tả chi tiết từng pixel** — tôi sẽ đọc ảnh + phân tích. Bạn chỉ cần mô tả **ngữ cảnh luồng + trường thông tin + ý định nghiệp vụ** (thứ mà ảnh không nói hết).

### Bước 3 — Báo AI phân tích
- Sau khi nộp ảnh + mô tả, báo tôi (vd “đã nộp E02, 8 ảnh”).
- Tôi sẽ: đọc ảnh + mô tả → phân tích As-Is chi tiết → điền vào `as-is-notes.md` (phần “AI phân tích”) + cập nhật `screen-gap-analysis.md` (cột As-Is).

## Mẹo mô tả để AI phân tích tốt
1. **Luồng quan trọng hơn màn lẻ**: mô tả sơ đồ luồng tổng thể trước, rồi từng màn — tôi nắm được hành trình.
2. **Trường thông tin**: liệt kê nhanh các trường hiển thị + nguồn (HLV nhập/KH nhập/động/tĩnh) nếu biết — ảnh đôi khi thiếu ngữ cảnh.
3. **Điểm “đã ổn” vs “cần cải thiện”**: ghi nhận xét ngắn nếu có — giúp tôi đánh GAP chính xác (KẾ THỪA vs SỬA).
4. **Nơi dữ liệu tới**: vd “chỉ số này lấy từ cân Tanita qua API” / “HLV gõ tay” / “tự sinh” — tôi biết kế thừa logic nào.
5. **Có thể nộp từng nhóm** (vd “E02 trước”) — không cần chụp hết app cùng lúc.

## Trạng thái nộp
| Nhóm | Số màn | Trạng thái |
|---|---|---|
| E02 Tư vấn 15p (HLV) | — | ⏳ chờ PO |
| E01 KH tiềm năng (HLV) | — | ⏳ chờ PO |
| E00 Shell/Auth (HLV) | — | ⏳ chờ PO |
| E03 Chăm sóc KH (HLV) | — | ⏳ chờ PO |
| E06 Khách hàng (KH) | — | ⏳ chờ PO |
