# 04 — Prototypes

Tầng **Prototype** (HTML tương tác). Chuyển mockup thành màn chạy được, nối điều hướng đầy đủ giữa các màn.

## Quy ước đặt tên

`<MODULE>-<nn>_<tên_gọn>.html` — khớp với mockup tương ứng.

- Ví dụ: `LEAD-01_danh_sach.html` ↔ `docs/03-mockups/coach/S-LEAD-01_danh_sach.png`.

## Lưu trữ
- `coach/` — prototype phía HLV.
- `customer/` — prototype phía KH.

## Bắt buộc
- **Khai báo đầu file** (HTML comment): user story `US-…`, khuôn màn `T…`, mockup tham chiếu.
- **Dùng tokens/system**: nhúng CSS tokens từ `docs/02-design-system/design-tokens.md` (inline `<style>` hoặc shared `_tokens.css`). Không dùng màu/giá trị ngoài token.
- **Icon**: Tabler Icons — copy `tabler-icons.min.css` từ `docs/99-archive/prototypes-old/` vào `_assets/` khi bắt đầu.
- **Điều hướng**: mọi CTA/nút phải dẫn tới màn tiếp theo (có thể dùng màn giả "chưa làm"). Không có nút chết.

## Tiến trình
1. Bắt đầu từ mockup đã chốt (đã qua gate review).
2. dựng HTML tĩnh theo khuôn + tokens.
3. Nối điều hướng; chạy thử click-through.
4. Gate: mọi story P0 phải có prototype điều hướng đến nơi.

> Prototype cũ (HLV/KH) nằm trong `docs/99-archive/prototypes-old/` — tham chiếu cách nối điều hướng, **không** dùng làm điểm xuất phát (vi phạm nhiều nguyên tắc Lean v1.1).
