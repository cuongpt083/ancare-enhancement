# 03 — Mockups

Tầng **Mockup** (thiết kế tĩnh từng màn). Mỗi mockup truy vết lên **1 user story** và tuân thủ **1 khuôn màn** của design system.

## Quy ước đặt tên

`S-<MODULE>-<nn>_<tên_gọn>.<png|fig|svg>`

- **MODULE code**: `AUTH · LEAD · CONS · CARE · TEAM · DEV · HLTH` (khớp epic).
- **nn**: số thứ tự màn trong module (01, 02…).
- Ví dụ: `S-LEAD-01_danh_sach.png`, `S-CONS-03_ban_tu_van.png`.

## Lưu trữ
- `coach/` — màn phía HLV.
- `customer/` — màn phía KH.

## Bắt buộc kèm mỗi mockup
Một file `.md`同名 khai báo:
```markdown
# S-LEAD-01 — Danh sách KH tiềm năng
- User story: US-E01-01
- Khuôn màn: T2
- Tokens: --accent-coach, --state-good, --radius-md
- Ghi chú thiết kế: <chú thích wireframe → hi-fi>
```

## Tiến trình
1. **Wireframe** (thấp cam) → chốt bố cục theo khuôn.
2. **Hi-fi** — áp tokens + component từ `docs/02-design-system/`.
3. **Review chéo** (gate): story nào chưa có mockup? mockup nào sai khuôn? → sửa trước khi sang prototype.

> Bản mockup tham chiếu cũ: `docs/99-archive/srs/mockups/` (S-LEAD-01, S-LEAD-02) — dùng làm gợi ý, **không** copy nguyên.
