# E03 — Customer Care

- **Vai trò:** HLV
- **Mục tiêu:** Chăm sóc KH sau chuyển đổi — 21 talking point + chuyên sâu bệnh lý, kỹ năng sống/mềm, điều chỉnh bữa ăn theo mốc trải nghiệm, nhắc tặng quà theo tuần, phân tích sức khỏe hằng ngày, cộng đồng/sự kiện, báo cáo hành trình, nhật ký infographic, nhắc kết nối 72h.
- **Nguồn:** feature-tree §2.3.

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E03-01 | Gửi talking point hằng ngày | Must |
| US-E03-02 | Kiểm tra kiến thức KH (2 câu hỏi) | Should |
| US-E03-03 | Điều chỉnh gợi ý bữa ăn theo mốc trải nghiệm | Must |
| US-E03-04 | Nhắc tặng quà theo tuần (theo nhu cầu) | Should |
| US-E03-05 | Phân tích sức khỏe hằng ngày + tư vấn nâng cấp SP | Should |
| US-E03-06 | Giao lưu cộng đồng / gợi ý sự kiện | Could |
| US-E03-07 | Báo cáo hành trình thay đổi | Should |
| US-E03-08 | Hỗ trợ KH tạo Nhật ký infographic | Could |
| US-E03-09 | Nhắc kết nối KH sau 72h | Must |

---

### US-E03-01 — Gửi talking point hằng ngày
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn mỗi ngày nhận sẵn 1 talking point dinh dưỡng kèm kiến thức & gợi ý giới thiệu sản phẩm phù hợp với giai đoạn của KH, để chăm sóc nhất quán mà không phải tự nhớ 21 bài.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (catalog 21 bài) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có KH đang active, When đến lượt chăm sóc, Then HLV thấy talking point hôm nay (khuôn T1) với 1 khối nội dung + CTA "Gửi cho KH".
  - AC2 — Given talking point đã gửi, When KH đọc, Then KH thấy 2 câu hỏi kiểm tra: *"Hôm nay bạn ấn tượng nhất điều gì?"* và *"Bạn sẽ chia sẻ cho ai?"*.
  - AC3 — Given KH trả lời, When HLV xem, Then câu trả lời lưu vào hồ sơ KH (T4) làm bằng chứng hành trình.
  - AC4 — Given không có KH active, When mở màn, Then trạng thái rỗng kèm gợi ý tạo KH.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-01_talking_point.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-01_talking_point.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Catalog 21 talking point — cần đặc tả (Open question).
- **Open question:** Catalog 21 talking point + chủ đề chuyên sâu bệnh lý cần đưa vào `docs/00-foundation/business-rules/`.

---

### US-E03-02 — Kiểm tra kiến thức KH (2 câu hỏi)
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem kết quả 2 câu hỏi phản tỉnh của KH sau mỗi talking point, để đánh giá mức hiểu & gợi ý điều chỉnh nội dung tiếp theo.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH đã trả lời 2 câu hỏi, When HLV xem, Then thấy câu trả lời + đánh giá nhanh (hiểu/chưa hiểu) trong hồ sơ KH (T4).
  - AC2 — Given KH chưa hiểu, When HLV đánh dấu, Then gợi ý talking point bổ sung hoặc gặp trực tiếp.
  - AC3 — Given KH muốn chia sẻ, When HLV xem "sẽ chia sẻ cho ai", Then gợi ý DMO giới thiệu (gắn E01).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-02_kiem_tra.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-02_kiem_tra.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: —
- **Open question:** Đánh giá "hiểu/chưa hiểu" do HLV chủ quan hay có rubric?

---

### US-E03-03 — Điều chỉnh gợi ý bữa ăn theo mốc trải nghiệm
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống nhắc & gợi ý điều chỉnh thực đơn khi đến mốc trải nghiệm (10 ngày → đo lại → điều chỉnh), để bữa ăn luôn phù hợp tiến độ KH mà không phải tự theo dõi.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given thực đơn 10 ngày sắp hết, When đến hạn, Then HLV & KH nhận nhắc "Đến hạn đo lại" (L4 — không nói "meal_plan hết hiệu lực").
  - AC2 — Given KH đo lại Tanita, When HLV nhập chỉ số mới, Then hệ thống so sánh & gợi ý điều chỉnh mục tiêu + sinh thực đơn phiên bản mới.
  - AC3 — Given phiên bản mới, When tạo, Then phiên bản cũ chuyển `expired`, phiên bản mới `active`; lịch sử giữ nguyên.
  - AC4 — Given HLV xem, When vào chi tiết KH, Then thấy lịch sử các phiên bản thực đơn (T4, gập).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-03_dieu_chinh_bua_an.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-03_dieu_chinh_bua_an.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (phiên bản 10 ngày + điều chỉnh).
- **Open question:** Mốc trải nghiệm có cố định 10 ngày hay tùy KH?

---

### US-E03-04 — Nhắc tặng quà theo tuần (theo nhu cầu)
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn được nhắc & gợi ý tặng quà cho KH theo tuần dựa trên nhu cầu, để giữ khách gắn bó mà không phải tự nhớ.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH đang active, When đến tuần tặng quà, Then HLV nhận nhắc kèm gợi ý quà theo nhu cầu KH (HOM dinh dưỡng, coaching, tư vấn nuôi dạy con, jumping…).
  - AC2 — Given gợi ý, When HLV chọn quà, Then ghi nhận & lên lịch tặng.
  - AC3 — Given đã tặng, When HLV đánh dấu, Then cập nhật timeline chăm sóc KH.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-04_tang_qua.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-04_tang_qua.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Lịch tặng quà (tuần 1/2/3/4…) & danh mục quà cần đặc tả.

---

### US-E03-05 — Phân tích sức khỏe hằng ngày + tư vấn nâng cấp SP
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem phân tích sức khỏe hằng ngày của KH & gợi ý hành động thay đổi / nâng cấp sản phẩm, để chăm sóc chủ động & tăng giá trị trị cho KH.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH check-in hằng ngày (E06-01), When HLV xem, Then thấy tổng hợp & cảnh báo (nước thiếu, ngủ trễ, bỏ bữa).
  - AC2 — Given cảnh báo, When HLV xem gợi ý, Then hiện hành động cần thay đổi + gợi ý nâng cấp SP (nếu cần) kèm "Vì sao?" (L7).
  - AC3 — Given gợi ý nâng cấp, When HLV gửi, Then KH nhận lời mời (không tạo áp lực — nguyên tắc đạo đức).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-05_phan_tich.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-05_phan_tich.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: Nguyên tắc AI hỗ trợ không thao túng — `docs/00-foundation/vision-and-values.md`.
- **Open question:** Ngưỡng cảnh báo (nước < ?, ngủ trễ > ?) cần đặc tả.

---

### US-E03-06 — Giao lưu cộng đồng / gợi ý sự kiện
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn gợi ý sự kiện & nhóm dinh dưỡng phù hợp cho KH tham gia, để KH giao lưu cộng đồng & tăng gắn bó.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH đang active, When HLV vào gợi ý sự kiện, Then thấy sự kiện + nhóm dinh dưỡng/Fit club phù hợp mục tiêu & vị trí KH.
  - AC2 — Given gợi ý, When HLV mời KH, Then KH nhận lời mời & đăng ký (gắn US-E00-05).
  - AC3 — Given chat nhóm cộng đồng, When KH tham gia, Then KH vào chat nhóm (gắn US-E06-05).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-06_cong_dong.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-06_cong_dong.html` *(chưa tạo)*
  - Khuôn màn: T2
  - Nghiệp vụ: —
- **Open question:** Danh mục sự kiện & nhóm lấy từ đâu (HLV tự tạo vs. tập trung)?

---

### US-E03-07 — Báo cáo hành trình thay đổi
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem báo cáo hành trình thay đổi của KH (thể chất, tinh thần, thói quen, kiến thức, lan tỏa), để đánh giá hiệu quả chăm sóc & thuyết phục KH tiếp tục.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (metric tinh thần) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH active, When HLV vào báo cáo, Then thấy 2 loại: (1) hành trình thể chất/tinh thần (đo lường được), (2) hành trình thói quen/kiến thức/lan tỏa.
  - AC2 — Given báo cáo thể chất, When xem, Then thấy biểu đồ chỉ số + mốc trải nghiệm (T4).
  - AC3 — Given báo cáo lan tỏa, When xem, Then thấy số người KH đã chia sẻ + kết quả chuyển đổi (nếu có).
  - AC4 — Given báo cáo, When HLV bấm "Xuất", Then xuất PDF/ảnh để gửi KH hoặc stakeholder.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-07_bao_cao.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-07_bao_cao.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: —
- **Open question:** Metric tinh thần/thói quen/lan tỏa cần chốt (từ check-in + câu trả lời talking point + chia sẻ).

---

### US-E03-08 — Hỗ trợ KH tạo Nhật ký infographic
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hỗ trợ KH tạo nội dung nhật ký infographic (kiến thức, hành trình, ảnh) để chia sẻ, để KH truyền cảm hứng dễ dàng & lan tỏa câu chuyện thành công.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (engine sinh) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH cần infographic, When HLV hỗ trợ, Then HLV chọn nội dung (tóm lược bài học, bữa ăn, thể chất, ảnh) & gửi template cho KH.
  - AC2 — Given KH nhận template, When KH chỉnh & chia sẻ, Then xuất ảnh kèm mã giới thiệu HLV.
  - AC3 — Given đã chia sẻ, When xem, Then ghi nhận vào báo cáo lan tỏa (US-E03-07).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-08_infographic.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-08_infographic.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Liên kết US-E06-08 (KH tự tạo) — đây là phiên HLV hỗ trợ.
- **Open question:** Template & engine sinh infographic cần PoC (gộp với E06-08).

---

### US-E03-09 — Nhắc kết nối KH sau 72h
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn được nhắc kết nối KH sau 72h từ mốc cuối cùng, để giữ nhịp chăm sóc & xử lý từ chối tiềm ẩn (rủ/chia sẻ thêm người khác).
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH không tương tác 72h, When đến hạn, Then HLV nhận nhắc "Kết nối lại với KH" kèm gợi ý hành động (rủ sự kiện, chia sẻ nội dung, hỏi thăm).
  - AC2 — Given nhắc, When HLV đánh dấu đã kết nối, Then reset bộ đếm 72h & ghi vào timeline.
    - AC3 — Given KH phản hồi tiêu cực/từ chối, When HLV đánh dấu, Then mở Objection Handler (gắn US-E02-06) hoặc gợi ý chuyển bảo trợ.
  - AC4 — Given KH muốn giới thiệu người khác, When HLV ghi nhận, Then tạo lead mới (gắn US-E01-02) & ghi nguồn giới thiệu.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-09_nhac_72h.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-09_nhac_72h.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Nhắc 72h: tự động gửi hay HLV xác nhận hành động?

---

## Open questions epic — đã chốt (xem `docs/00-foundation/decisions-log.md`)
- ✅ **D17** Chọn talking point → **hybrid** (tuần mặc định, HLV đổi theo Stage).
- ⏳ **D18** Catalog 21 talking point → PO cung cấp sau (placeholder `Content-Catalogs-Placeholder-v1.0.md` §2).
- ✅ **D19** Nhắc 72h → **tự động gửi nhắc đến HLV**; HLV đánh dấu hoàn thành.
- ✅ **D20** Metric báo cáo hành trình → tinh thần (talking point) + thói quen (tỷ lệ check-in) + lan tỏa (số người chia sẻ).
- ⏳ **D21** Ánh xạ 12 bước → PO cung cấp sau (placeholder `Content-Catalogs-Placeholder-v1.0.md` §3).

> Chi tiết đầy đủ: `docs/00-foundation/decisions-log.md`.
