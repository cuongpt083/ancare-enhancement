# 99 — Archive (hiện trạng trước khi khởi động lại)

> **Chỉ đọc, không chỉnh sửa.** Toàn bộ nội dung đây là trạng thái **trước cột mốc khởi động lại** (commit `47905ed` — baseline freeze). Giữ để tham chiếu & truy vết; mọi tác động mới diễn ra ở `docs/00-foundation/` → `04-prototypes/`.

## Vì sao tồn tại
Repo sau nhiều lần chỉnh sửa bị phân mảnh: trùng lặp phiên bản (To-be v1.0 + v2.1 + draft; GAP v1.0 + v2.0; To-do v1.0 + v2.0), trùng định dạng (.md + .docx), trùng prototype (`hlv-old/` + `hlv/` + `old_*.html` + zip), trộn lẫn UI-UX giữa `to-be/` và `srs/`, không có nguồn sự thật duy nhất. Khởi động lại chọn chiến lược **Lưu trữ & Tái lập nền**: đóng băng toàn bộ vào đây, xây nền tảng mới sạch.

## Mục lục & giá trị tham chiếu

| Thư mục | Vẫn còn giá trị tham chiếu? |
|---|---|
| `as-is/` | **Có** — khảo sát hiện trạng + screenshots HLV/KH vẫn là baseline hợp lệ. |
| `to-be/` | **Một phần** — `Workflow-HLV.md`, `Workflow-KH.md`, `customer-persona-disc-framework_v1.0.md` (Phần IV: 3 persona lõi), `Empathy-Consultation_v1.0.md` (5 lớp đồng cảm) còn dùng để chưng cất tiếp vào foundation. Bản v1.0/v2.1 trùng nhau — lấy consolidated. |
| `srs/` | **Một phần** — `UI-UX-Design-Language-Lean_v1.0.md` (đã chưng cất vào `docs/02-design-system/`); `Objection-Handler_v1.0.md`, `Conversational-Explainable-UX_v1.0.md` còn tham chiếu. |
| `references/` | **Có** — Quy trình 12 bước (`01.…`), Tính Calories (`02.…`), Tư vấn 15p (`03.…`) là tài liệu gốc domain. |
| `technical/` | **Có** — `customer-persona-data-model_v1.0.md`, rule engine — đầu vào thiết kế kỹ thuật sau này. |
| `business-rules/` | **Đã chuyển** vào `docs/00-foundation/business-rules/` (bản duy nhất). |
| `gap/`, `to-do/`, `feasibility/` | Tham chiếu lịch sử — định hướng DXP hiện tại đã vượt các bản v1.0. |
| `reviews/` | Ghi chú review 2026-06-14 — tham chiếu quyết định. |
| `prototypes-old/` | Tham chiếu điều hướng; **không** là điểm xuất phát mới. |
| `tools/` | `capture_robust.js`, `capture_subpages.js` — script chụp ảnh prototype (playwright). |
| `README.docx` | Bản xuất cũ của README. |

## Cách dùng
- Cần chi tiết gốc → mở file tại đây, **không** copy vào tầng mới (tránh tái phân mảnh).
- Khi chưng cất một khái niệm vào foundation, ghi nguồn tại cuối file foundation.
