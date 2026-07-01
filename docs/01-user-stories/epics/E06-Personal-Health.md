# E06 — Personal Health (Trải nghiệm KH · Thân–Tâm–Trí)

- **Vai trò:** KH (+ HLV làm gương)
- **Mục tiêu:** Trải nghiệm sống khỏe phía KH theo Thân–Tâm–Trí — trang chủ cá nhân hóa, "Sức khỏe tổng thể" (đồng hồ sinh học), cá nhân hóa thời gian biểu, gợi ý bữa ăn, chat HLV, chia sẻ. HLV cũng tự thực hiện lộ trình & chia sẻ.
- **Nguồn:** feature-tree §2.6 + trải nghiệm KH (README §A).

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E06-01 | Check-in đồng hồ sinh học 24h | Must |
| US-E06-02 | Trang chủ cá nhân hóa (% hoàn thành, tổng kết cuối ngày) | Must |
| US-E06-03 | Cá nhân hóa thời gian biểu (số bữa, giờ hoạt động) | Should |
| US-E06-04 | Gợi ý bữa ăn cá nhân hóa (3 nhóm + chụp ảnh AI) | Must |
| US-E06-05 | Chat với HLV | Must |
| US-E06-06 | Chia sẻ tiến bộ / truyền cảm hứng | Should |
| US-E06-07 | Xem kết quả cân quét & báo cáo hành trình | Should |
| US-E06-08 | Nhật ký infographic | Could |

---

### US-E06-01 — Check-in đồng hồ sinh học 24h
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn check-in từng nhiệm vụ trên đồng hồ sinh học 24h và được chấm điểm theo độ đúng giờ, để giữ nhịp sinh học & tích lũy streak phần thưởng.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH mở màn "Sức khỏe tổng thể", When xem, Then thấy vòng tròn 24h chia múi theo hoạt động, tô màu trạng thái (khuôn T3, focus card là đồng hồ).
  - AC2 — Given đến giờ nhiệm vụ, When KH bấm check-in, Then chấm điểm theo độ đúng giờ (3/2/1/0) — nền tảng streak & credit thưởng.
  - AC3 — Given nhiệm vụ "uống nước", When KH ghi nhận nhiều lần, Then mỗi cốc ~250ml cộng dồn; hiển thị tiến độ nước/ngày.
  - AC4 — Given danh sách nhiệm vụ, When xem, Then chia 2 vùng "đã thực hiện" / "chờ thực hiện" để tạo động lực.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-01_dong_ho_sinh_hoc.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-01_dong_ho_sinh_hoc.html` *(chưa tạo)*
  - Khuôn màn: T3 (widget trung tâm)
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (nước ≥ 0,4 L/10kg).
- **Open question:** Đồng hồ sinh học tham chiếu case study Huawei Health Clover (archive) — chưng cất quy tắc tô màu/quản gia ảo khi chốt.

---

### US-E06-02 — Trang chủ cá nhân hóa
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn một trang chủ cho biết % hoàn thành ngày/tuần, đánh giá sức khỏe 3 trụ cột, & tổng kết cuối ngày, để biết mình đang làm tốt chưa & cần cải thiện gì.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH đăng nhập, When mở trang chủ (T3), Then thấy lời chào + focus card "việc nổi bật hôm nay" + ≤3 lối tắt + danh sách cần chú ý.
  - AC2 — Given cuối ngày, When KH mở, Then thấy tổng kết: đủ đạm/calo/nước/ngủ, điểm ngày, lưu ý cải thiện.
  - AC3 — Given đánh giá 3 trụ cột, When xem, Then thấy Thân/Tâm/Trí ở 3 màu trụ cột, mỗi trụ cột 1 nhãn ngôn ngữ (Tốt/Cần lưu ý).
  - AC4 — Given lịch biểu, When xem, Then thấy sự kiện học tập/quiz/sự kiện sắp tới.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-02_trang_chu.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-02_trang_chu.html` *(chưa tạo)*
  - Khuôn màn: T3
  - Nghiệp vụ: —
- **Open question:** % hoàn thành tính từ đâu (check-in đồng hồ + bữa ăn + quiz)?

---

### US-E06-03 — Cá nhân hóa thời gian biểu
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn tự chọn số bữa ăn (3/4/5) & giờ từng hoạt động, để thời gian biểu vừa khả thi vừa tối ưu nhịp sinh học.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào "Cá nhân hóa thời gian biểu" (T1), When chọn số bữa (3/4/5) & giờ hoạt động, Then hệ thống hiển thị mức tối ưu đồng hồ sinh học + điểm tối đa.
  - AC2 — Given giờ lệch nhịp sinh học, When xem, Then hiển thị điểm giảm (nhãn ngôn ngữ "hơi lệch nhịp" — L4) & gợi ý giờ tối ưu.
  - AC3 — Given đã lưu, When xem đồng hồ, Then cập nhật theo thời gian biểu mới.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-03_thoi_gian_bieu.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-03_thoi_gian_bieu.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Điểm tối ưu tính từ quy tắc nhịp sinh học — cần đặc tả business-rule.

---

### US-E06-04 — Gợi ý bữa ăn cá nhân hóa (3 nhóm + chụp ảnh AI)
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn nhận thực đơn theo mục tiêu + số bữa, & ghi nhận bữa ăn bằng chụp ảnh AI bóc tách món, để theo dõi calo dễ dàng mà không nhập tay.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (AI bóc tách món) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào "Gợi ý bữa ăn" (T1), When xem, Then thấy thực đơn theo mục tiêu + số bữa, cấu trúc 3 nhóm (Đạm/Xơ/Đường-bột).
  - AC2 — Given bữa ăn, When KH chụp ảnh, Then AI bóc tách món + ước lượng đơn vị (bát/lạng); KH xác nhận/sửa.
  - AC3 — Given không chụp, When KH chọn "Nhập tay", Then mở form nhập → API tính calo.
  - AC4 — Given đã ghi nhận, When xem tổng kết ngày, Then cộng dồn calo/nước/đạm vào tổng kết (US-E06-02).
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-04_bua_an.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-04_bua_an.html` *(ch chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (3 nhóm + API calo).
- **Open question:** AI bóc tách món cần PoC (xem Feasibility). Catalog món + hệ số đơn vị `[TBD]`.

---

### US-E06-05 — Chat với HLV
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn chat trực tiếp với HLV (hỏi đáp thực đơn, được động viên), để có người đồng hành khi thắc mắc mà không phải đợi gặp trực tiếp.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào chat (T1), When gửi tin nhắn, Then HLV nhận notification & phản hồi.
  - AC2 — Given HLV bận, When KH gửi, Then trợ lý AI tạm trả lời (nếu bật) với nhãn "trợ lý AI" — không giả danh HLV.
  - AC3 — Given cuộc trò chuyện, When KH xem, Then lịch sử lưu & tìm được theo từ khóa.
  - AC4 — Given `ai_data_sharing_enabled = false`, When chat, Then chỉ chat với HLV, không có AI — app vẫn chạy.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-05_chat.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-05_chat.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Nguyên tắc minh bạch — `docs/00-foundation/vision-and-values.md`.
- **Open question:** AI companion chat có proactively gợi ý hay chỉ trả lời khi KH hỏi?

---

### US-E06-06 — Chia sẻ tiến bộ / truyền cảm hứng
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn chia sẻ tiến độ & câu chuyện của mình (ảnh, kết quả, bài học) với cộng đồng/MXH, để truyền cảm hứng & nhận động lực.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH có kết quả/tiến bộ, When bấm "Chia sẻ", Then chọn nội dung (ảnh trước–sau, kết quả, bài học) + nền tảng (cộng đồng app / MXH).
  - AC2 — Given chia sẻ cộng đồng, When đăng, Then hiện trong feed nhóm dinh dưỡng; thành viên tương tác (thích/bình luận).
  - AC3 — Given chia sẻ MXH, When đăng, Then sinh nội dung kèm mã giới thiệu HLV (Content-Attribution Matching).
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-06_chia_se.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-06_chia_se.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Content-Attribution Matching — `docs/00-foundation/vision-and-values.md` §Định hướng 4.
- **Open question:** Template chia sẻ MXH cần đặc tả (có sẵn vs tự do).

---

### US-E06-07 — Xem kết quả cân quét & báo cáo hành trình
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn xem kết quả cân quét Tanita & báo cáo hành trình thay đổi (thể chất, tinh thần, thói quen), để thấy tiến bộ & duy trì động lực.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào kết quả, When xem, Then thấy chỉ số Tanita hiện tại + so sánh với lần trước (T4, card gập).
  - AC2 — Given báo cáo hành trình, When xem, Then thấy biểu đồ thay đổi thể chất (cân nặng/mỡ/cơ) theo thời gian + mốc trải nghiệm.
  - AC3 — Given báo cáo thói quen/kiến thức, When xem, Then thấy tổng kết thói quen & sự lan tỏa (người đã chia sẻ).
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-07_bao_cao.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-07_bao_cao.html` *(chưa tạo)*
  - Khuôn màn: T4
  - Nghiệp vụ: —
- **Open question:** Báo cáo hành trình đo lường tinh thần/thói quen thế nào (cần metric).

---

### US-E06-08 — Nhật ký infographic
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn tạo nhật ký infographic (kiến thức tóm lược, hành trình bữa ăn/thể chất, ảnh) để chia sẻ, để lưu & truyền cảm hứng bằng hình ảnh sinh động.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (sinh infographic) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào "Nhật ký infographic", When chọn nội dung (bài học hôm nay, bữa ăn, thể chất, ảnh), Then hệ thống sinh infographic template.
  - AC2 — Given infographic, When xem, Then KH có thể chỉnh chữ/ảnh trước khi chia sẻ.
  - AC3 — Given đã chốt, When chia sẻ, Then xuất ảnh chất lượng cao kèm mã giới thiệu HLV.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-08_infographic.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-08_infographic.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Sinh infographic cần PoC (xem Feasibility).
- **Open question:** Template infographic & engine sinh cần PoC.

---

## Open questions epic — đã chốt (xem `docs/00-foundation/decisions-log.md`)
- ✅ **D24** Gamification → **gộp 1 hệ thống credit chung** (sức khỏe + học tập).
- ✅ **D27** Streak/credit → **P0 chỉ điểm check-in (3/2/1/0)**; credit/streak/badge sau.
- ✅ **D28** Đồng hồ sinh học → **tô màu trạng thái + gợi ý nhiệm vụ** (không quản gia ảo phức tạp ở P0).
- ✅ **D29** AI companion chat → **proactively gợi ý nhẹ** (phát hiện KH cần hỗ trợ, không phán xét).

> Chi tiết đầy đủ: `docs/00-foundation/decisions-log.md`. Câu kỹ thuật PoC (AI bóc tách món, sinh infographic) cần đội kỹ thuật — không thuộc open question nghiệp vụ.
