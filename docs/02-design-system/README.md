# 02 — Design System (UI-UX System Design)

Bộ thiết kế thống nhất cho **mọi màn hình HLV & KH**. Mọi mockup (`docs/03-mockups/`) và prototype (`docs/04-prototypes/`) **bắt buộc** tuân thủ hệ thống này trước khi đào sâu luồng.

> Nguồn gốc: chưng cất & nâng cấp từ `UI-UX-Design-Language-Lean_v1.0.md` (trong `docs/99-archive/srs/`).

## Mục lục

| File | Nội dung |
|---|---|
| `principles.md` | 7 nguyên tắc Lean (L1–L7) — luật bắt buộc. |
| `design-tokens.md` | Màu, typography, spacing, vùng chạm, radii, icon. |
| `screen-templates.md` | 4 khuôn màn (T1 Quyết định · T2 Danh sách · T3 Tổng quan · T4 Chi tiết). |
| `voice-and-tone.md` | Bảng "dịch khái niệm hệ thống → ngôn ngữ người dùng" + tông giọng. |
| `components.md` | Kho component (atoms → molecules → organisms). Mầm — lớn dần theo mockup. |

## Tuyên ngôn

> *"Mỗi màn hỏi một điều. Hệ thống quyết sẵn — người dùng chỉ xác nhận. Chi tiết ẩn cho tới khi cần."*

## Quy tắc truy vết (bắt buộc)

Mỗi mockup/prototype phải khai báo ở đầu file:
- **User story**: `US-<EPIC>-<nn>` (tham chiếu `docs/01-user-stories/`)
- **Khuôn màn**: `T1` / `T2` / `T3` / `T4`
- **Tokens dùng**: (tham chiếu `design-tokens.md`)

→ Đảm bảo tính nhất quán và dễ review chéo (gate sau mỗi giai đoạn).
