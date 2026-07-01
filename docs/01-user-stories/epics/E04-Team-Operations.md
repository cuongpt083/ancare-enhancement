# E04 — Team Operations

- **Vai trò:** HLV (vai trò dẫn dắt hệ thống KD)
- **Mục tiêu:** Chăm sóc hệ thống kinh doanh — danh sách thành viên, chi tiết thành viên kèm gợi ý DMO club bước tiếp, đào tạo thành viên.
- **Nguồn:** feature-tree §2.4.

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E04-01 | Xem danh sách thành viên | Must |
| US-E04-02 | Chi tiết thành viên + gợi ý DMO club | Should |
| US-E04-03 | Đào tạo thành viên | Could |

---

### US-E04-01 — Xem danh sách thành viên
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
- **Open question:** "Bước tiếp" lấy từ Process State Model — cần đặc tả state machine.

---

### US-E04-02 — Chi tiết thành viên + gợi ý DMO club bước tiếp
- **Epic:** E04 — Team Operations
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem chi tiết một thành viên kèm gợi ý DMO club phù hợp, gợi ý nhóm Dinh dưỡng/Fit club phù hợp, và bước tiếp theo trong Vòng tròn thành công, để dẫn dắt từng người đúng cách.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (state machine) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given mở chi tiết thành viên (T4), When xem, Then thấy header gọn + ≤3 hành động nhanh (Gọi · Nhắn · Gặp 2-1).
  - AC2 — Given thành viên ở bước N của PSM, When xem gợi ý, Then hiện DMO club phù hợp bước N + nhóm Dinh dưỡng/Fit club phù hợp + bước tiếp theo Vòng tròn thành công.
  - AC3 — Given gợi ý, When HLV bấm "Vì sao?", Then giải thích vì sao gợi ý này (gắn bằng chứng, chỉ ở điểm quyết định).
  - AC4 — Given lịch sử thành viên, When xem, Then timeline các mốc phát triển (gắn PSM) gập mặc định, mở khi cần.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-TEAM-02_chi_tiet.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/TEAM-02_chi_tiet.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: Quy trình 12 bước → `docs/99-archive/references/01.Quy-trinh-12-buoc-kinh-doanh.md` (chưng cất tiếp vào foundation).
- **Open question:** Ánh xạ 12 bước → DMO club / Vòng tròn thành công cần đặc tả business-rule.

---

### US-E04-03 — Đào tạo thành viên
- **Epic:** E04 — Team Operations
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn giao & theo dõi đào tạo cho thành viên tuyến dưới (kiểm tra, đánh giá, tài liệu), để đảm bảo họ phát triển đúng lộ trình.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given chi tiết thành viên (T4), When HLV bấm "Giao đào tạo", Then mở danh sách khóa học phù hợp bước PSM của thành viên.
  - AC2 — Given đã giao khóa, When thành viên hoàn thành, Then HLV thấy kết quả kiểm tra/đánh giá trong chi tiết thành viên.
  - AC3 — Given thành viên chưa hoàn thành, When đến hạn, Then nhắc HLV theo dõi.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-TEAM-03_dao_tao.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/TEAM-03_dao_tao.html` *(chưa tạo)*
  - Khuôn màn: T1 (giao) + T4 (theo dõi)
  - Nghiệp vụ: Liên kết E05 — Self-Development.
- **Open question:** Đào tạo thành viên dùng lại catalog micro-course của E05 hay tách bộ riêng cho tuyến dưới?

---

## Open questions epic
- DMO club "bước tiếp" ánh xạ thế nào từ quy trình 12 bước sang gợi ý hành động?
- Phân quyền: HLV thấy tuyến dưới đến bao nhiêu cấp?
- "Vòng tròn thành công" cần định nghĩa & đặc tả (chưa có trong glossary — thêm khi chốt).
