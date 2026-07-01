# E04 — Team Operations

- **Vai trò:** HLV (vai trò dẫn dắt hệ thống KD)
- **Mục tiêu:** Chăm sóc hệ thống kinh doanh — danh sách thành viên, chi tiết thành viên kèm gợi ý DMO club bước tiếp, đào tạo thành viên.
- **Nguồn:** feature-tree §2.4.

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E04-01 | Xem danh sách thành viên | Must |
| US-E04-02 | Chi tiết thành viên + gợi ý DMO club bước tiếp | Should |
| US-E04-03 | Đào tạo thành viên (gắn E05) | Could |

## Exemplar — US-E04-01
- **Epic:** E04 — Team Operations
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem danh sách thành viên hệ thống kinh doanh với trạng thái & bước phát triển tiếp theo, để biết ai cần dẫn dắt gì trong tuần.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có ≥1 thành viên, When HLV mở màn thành viên, Then thấy danh sách (khuôn T2) sắp xếp theo "cần chú ý tuần này".
  - AC2 — Given danh sách, When xem mỗi thẻ, Then thẻ hiện tối đa 2 nhãn (vd vai trò + bước PSM); chi tiết ở T4.
  - AC3 — Given thẻ, When bấm, Then mở chi tiết thành viên (T4) với gợi ý DMO club bước tiếp (≤3 hành động nhanh).
  - AC4 — Given không có thành viên, When mở màn, Then trạng thái rỗng kèm gợi ý "Mời thành viên".
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-TEAM-01_danh_sach.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/TEAM-01_danh_sach.html` *(chưa tạo)*
  - Khuôn màn: T2 (+ T4 cho chi tiết)
  - Nghiệp vụ: La bàn quy trình (PSM) — `docs/00-foundation/vision-and-values.md` §Định hướng 2.
- **Open question:** "Bước tiếp" của thành viên lấy từ Process State Model — cần đặc tả state machine.

## Open questions epic
- DMO club "bước tiếp" ánh xạ thế nào từ quy trình 12 bước sang gợi ý hành động?
- Phân quyền: HLV thấy tuyến dưới đến bao nhiêu cấp?
