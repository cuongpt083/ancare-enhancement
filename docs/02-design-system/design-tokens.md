# Design Tokens

> Một ý nghĩa = một màu/một khoảng. Dùng nhất quán mọi màn. Không dùng trang trí gây nhiễu.

## Màu

| Token | Giá trị | Dùng cho |
|---|---|---|
| `--accent-coach` | `#2f6f4f` | CTA chính phía HLV, nhấn thương hiệu HLV |
| `--accent-customer` | `#2f9e6e` | CTA chính phía KH, nhấn thương hiệu KH |
| `--state-good` | `#16a34a` | trạng thái tốt / hoàn thành đúng |
| `--state-warn` | `#d99a14` | một phần / trễ / hơi khó |
| `--state-alert` | `#c5402f` | bỏ lỡ / vượt ngưỡng / đến hạn |
| `--state-idle` | `#cdd4db` | chưa tới / không liên quan / chờ |
| `--pillar-than` | `#16a34a` | trụ cột Thân (chỉ ngữ cảnh Thân–Tâm–Trí) |
| `--pillar-tam` | `#8b5cf6` | trụ cột Tâm |
| `--pillar-tri` | `#f97316` | trụ cột Trí |
| `--bg` | `#ffffff` | nền màn |
| `--bg-subtle` | `#f6f8f7` | nền card/khu vực phụ |
| `--text` | `#1f2933` | chữ chính |
| `--text-muted` | `#6b7780` | chữ phụ |

**Chip/nhãn**: nền nhạt + chữ đậm cùng tông; **không quá 2 chip/thẻ**.

## Typography

- Cỡ chữ tối thiểu nội dung: **13px** (người trung niên); tiêu đề **15–18px**; tránh 9–10px cho thông tin quan trọng.
- Font: hệ sans-serif, dễ đọc (Inter / Be Vietnam Pro đề xuất).
- Mỗi mục **≤ 1 dòng**; mô tả **≤ 2 dòng**. Ưu tiên động từ ("Tạo bản tư vấn", "Lưu & gửi khách").

## Spacing (bội số 4)

`4 · 8 · 12 · 16 · 24 · 32 · 48` (px). Padding card 16; gap giữa khối 12–16; margin màn 16.

## Vùng chạm & nút

- Vùng chạm tối thiểu **44px**.
- Nút chính: to, rõ, có **icon + chữ**, full-width hoặc rộng, cố định chân màn (khuôn T1).

## Radii

`--radius-sm: 6px` (chip/input) · `--radius-md: 12px` (card) · `--radius-lg: 20px` (sheet/modal).

## Icon

- Bộ icon: **Tabler Icons** (đã có sẵn `tabler-icons.min.css` trong `docs/99-archive/prototypes-old/` — copy vào prototype mới khi cần).
- 1 icon = 1 ý nghĩa; không dùng icon trùng ý nghĩa khác nhau.

## Elevație

`--shadow-card: 0 1px 3px rgba(0,0,0,.08)` · `--shadow-fab: 0 4px 12px rgba(0,0,0,.18)`.
