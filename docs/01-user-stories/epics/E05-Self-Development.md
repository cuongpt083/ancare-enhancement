# E05 — Self-Development

- **Vai trò:** HLV + KH
- **Mục tiêu:** Phát triển bản thân — sơ đồ trả thưởng, đào tạo kinh doanh/tâm thế/sản phẩm/mạng lưới/thấu hiểu, 3 câu hỏi trước & sau khi học (micro-course).
- **Nguồn:** feature-tree §2.5; gắn Module Đào tạo (README §3).

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E05-01 | Học 1 micro-course (3 câu hỏi trước/sau) | Must |
| US-E05-02 | Xem sơ đồ trả thưởng | Should |
| US-E05-03 | Gợi ý khóa học cá nhân hóa | Should |
| US-E05-04 | Theo dõi lộ trình đào tạo (điều kiện + chứng nhận) | Could |

---

### US-E05-01 — Học 1 micro-course (3 câu hỏi trước/sau)
- **Epic:** E05 — Self-Development
- **Vai trò:** KH (và HLV)
- **Story:** Là người học, tôi muốn học 1 micro-course ngắn với 3 câu hỏi định hướng trước & 3 câu phản tỉnh sau, để nắm được điều đáng nhớ & việc sẽ áp dụng.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given người học mở micro-course, When bắt đầu, Then hiện 3 câu hỏi trước học (mục tiêu/ky vọng/câu hỏi mang theo).
  - AC2 — Given đã trả lời trước, When vào nội dung, Then trình bày ngắn (khuôn T1, ≤3 khối above-the-fold) + CTA "Hoàn thành".
  - AC3 — Given hoàn thành nội dung, When kết thúc, Then hiện 3 câu hỏi sau: *"Hôm nay bạn ấn tượng nhất điều gì?"*, *"Bạn sẽ chia sẻ cho ai?"*, *"Bạn sẽ áp dụng điều gì?"*.
  - AC4 — Given đã trả lời sau, When lưu, Then cập nhật lộ trình đào tạo & ghi nhận hoàn thành.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-DEV-01_microcourse.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/DEV-01_microcourse.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Module Đào tạo micro-course — cần đặc tả catalog (Open question).
- **Open question:** Catalog micro-course + điều kiện tiên quyết cần đưa vào foundation.

---

### US-E05-02 — Xem sơ đồ trả thưởng
- **Epic:** E05 — Self-Development
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem sơ đồ trả thưởng Herbalife & vị trí hiện tại của mình/tuyến dưới, để biết cần đạt gì để lên cấp tiếp theo.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (dữ liệu trả thưởng) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV vào sơ đồ trả thưởng, When xem, Then thấy sơ đồ cấp bậc + vị trí hiện tại + điều kiện lên cấp tiếp theo (đơn vị:Vol / số TV / doanh thu).
  - AC2 — Given vị trí hiện tại, When xem "cần thêm", Then hiện khoảng cách tới cấp tiếp theo & gợi ý hành động (gắn PSM).
  - AC3 — Given có tuyến dưới, When xem sơ đồ tuyến, Then thấy cấu trúc tuyến (không lộ chi tiết thu nhập của từng người).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-DEV-02_tra_thuong.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/DEV-02_tra_thuong.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: Sơ đồ trả thưởng Herbalife — nội dung tĩnh hay tính động? (Open question).
- **Open question:** Sơ đồ tĩnh (hiển thị cấu trúc Herbalife) hay động (tính từ dữ liệu tuyến)?

---

### US-E05-03 — Gợi ý khóa học cá nhân hóa
- **Epic:** E05 — Self-Development
- **Vai trò:** KH + HLV
- **Story:** Là người học, tôi muốn được gợi ý khóa học phù hợp với sức khỏe, thói quen, mục tiêu & giai đoạn phát triển của mình, để học đúng thứ cần thay vì lướt danh sách dài.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given vào kho học, When xem, Then thấy danh sách (khuôn T2) với khóa "Nên học tiếp" ở đầu (dựa mục tiêu + Stage + lịch sử học).
  - AC2 — Given gợi ý, When bấm "Vì sao?", Then giải thích vì sao khóa này phù hợp (gắn bằng chứng ngắn).
  - AC3 — Given `ai_data_sharing_enabled = false`, When gợi ý, Then dùng gợi ý tĩnh (theo bước PSM) thay vì AI.
  - AC4 — Given đã hoàn thành khóa, When xem gợi ý, Then không lặp khóa đã học; gợi ý khóa tiếp theo trong lộ trình.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-DEV-03_goi_y_khoa_hoc.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/DEV-03_goi_y_khoa_hoc.html` *(chưa tạo)*
  - Khuôn màn: T2
  - Nghiệp vụ: Persona framework — `docs/00-foundation/personas.md`.
- **Open question:** Thuật toán gợi ý thuộc P1 (rule-based) hay P3 (RAG) — phân tầng AI.

---

### US-E05-04 — Theo dõi lộ trình đào tạo (điều kiện + chứng nhận)
- **Epic:** E05 — Self-Development
- **Vai trò:** HLV + KH
- **Story:** Là người học, tôi muốn xem lộ trình đào tạo với điều kiện tiên quyết & chứng nhận hoàn thành, để biết mình ở đâu và cần gì để đạt chứng nhận tiếp theo.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given vào lộ trình đào tạo, When xem, Then thấy cây lộ trình (khuôn T4) với các mốc: khóa đã hoàn thành / đang học / bị khóa (chưa đủ tiên quyết).
  - AC2 — Given khóa bị khóa, When bấm, Then hiện điều kiện tiên quyết cần hoàn thành trước.
  - AC3 — Given hoàn thành đủ điều kiện chứng nhận, When hệ thống kiểm tra, Then cấp chứng nhận (hiển thị trong hồ sơ).
  - AC4 — Given HLV xem lộ trình thành viên, When mở, Then thấy tiến độ của thành viên (gắn E04-03).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-DEV-04_lo_trinh.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/DEV-04_lo_trinh.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: Catalog micro-course + điều kiện tiên quyết (Open question epic).
- **Open question:** Chứng nhận có giá trị trong app (badge) hay liên kết bên ngoài?

---

## Open questions epic — đã chốt (xem `docs/00-foundation/decisions-log.md`)
- ✅ **D24** Gamification → **gộp 1 hệ thống credit chung** (sức khỏe + học tập).
- ✅ **D25** Sơ đồ trả thưởng → **tĩnh** (P0).
- ⏳ **D26** Catalog micro-course 5 mảng → PO cung cấp sau (placeholder `Content-Catalogs-Placeholder-v1.0.md` §4).

> Chi tiết đầy đủ: `docs/00-foundation/decisions-log.md`.
