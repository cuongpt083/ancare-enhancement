# E02 — Consultation 15 phút

- **Vai trò:** HLV (với khách ngồi cạnh)
- **Mục tiêu:** Số hóa buổi tư vấn 15 phút theo **quy trình tiêu chuẩn** (Khảo sát Chân dung KH → Đo lường Tanita → Phân tích & Cảnh báo → Tư vấn giải pháp & Chốt chương trình) → Tạo tài khoản KH → Gợi ý bữa ăn → Disclaimer.
- **Ghi chú:** Giai đoạn "Phá băng & xây thiện cảm" đã **bỏ khỏi luồng app** (Q33) — nội dung chuyển vào kho đào tạo (E05). Quy trình xử lý từ chối tạm **"Đóng về DS KH"** (Q34, man-to-man, hạn chế nhìn màn hình) — Objection Handler FAB để P1+.
- **Nguồn:** feature-tree §2.2; **quy trình chuẩn:** `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` (chưng cất từ `docs/00-foundation/consultation-sample-15-minutes.md`); tham chiếu `docs/99-archive/srs/Objection-Handler_v1.0.md`.

## Danh sách stories
| ID | Bước | Tên ngắn | Ưu tiên |
|---|---|---|---|
| US-E02-02 | Giai đoạn 1 | Chân dung KH (gộp khảo sát mục tiêu) | Must |
| US-E02-03 | Giai đoạn 2 | Hướng dẫn đo lường Tanita (OCR + tư thế) | Must |
| US-E02-04 | Giai đoạn 3 | Phân tích chỉ số & Cảnh báo sức khỏe (5 bước) | Must |
| US-E02-05 | Giai đoạn 4 | Xem lộ trình (giải pháp + lộ trình 3 tháng) | Must |
| US-E02-06 | Giai đoạn 4 | Chốt gói (đơn giản — Q34) | Must |
| US-E02-07 | Sau chốt | Gợi ý bữa ăn 10 ngày đầu | Must |
| US-E02-08 | Sau chốt | Tạo tài khoản KH | Must |
| US-E02-09 | Xuyên suốt | Disclaimer "không thần dược" | Must |

> **Đã xóa:** US-E02-01 Phá băng (Q33 — chuyển nội dung vào E05 đào tạo). Mockup S-CONS-01 xóa.

---

### US-E02-02 — Chân dung KH (gộp khảo sát mục tiêu)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn thu thập Chân dung KH qua bộ câu hỏi (mục tiêu mong muốn + tiền sử bệnh lý + thói quen ăn/uống/ngủ/vận động) với ô trả lời ngắn gọn, để hệ thống tự phân tích & ghi chân dung, làm đầu vào cho bản phân tích Tanita.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào buổi tư vấn (sau Thêm mới KH), When HLV mở "Chân dung KH", Then hiện Card gồm 2 phần: (a) danh sách câu hỏi cơ bản (vd 10 câu — hiện thị để HLV đọc hỏi, không cần tương tác), (b) ô trả lời cho HLV (nhập text, độ dài tối đa 500 ký tự, tập trung kết quả KH mong muốn vd "Tất cả bình thường/ngoại trừ bệnh tiểu đường/mong muốn tăng cơ giảm mỡ"), HLV điền câu trả lời theo mẫu trên để hệ thống dễ dàng tổng hợp và phân tích & ghi vào `pain_points[]`, `lifestyle` (sleep, diet, water, exercise, habits).
  - AC2 — Given hoàn thành Chân dung, When HLV bấm "Lưu → Khảo sát Tanita", Then chuyển sang US-E02-03.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-02_chan_dung_kh.png` *(đổi tên từ S-CONS-02_khao_sat)*
  - Prototype: `docs/04-prototypes/coach/CONS-02_chan_dung_kh.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §3; Persona framework — `docs/00-foundation/personas.md` (DISC/Stage HLV tự đánh giá ngoài form — D06).
- **Reference:** [Bộ câu hỏi Chân dung KH](./../00-foundation/survey-questions.md)

---

### US-E02-03 — Hướng dẫn đo lường Tanita (OCR + tư thế)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chụp ảnh màn hình cân Tanita & hệ thống OCR nhận diện chỉ số, đồng thời có checklist hướng dẫn tư thế đo chuẩn, để nhập dữ liệu ≤1 phút & đảm bảo đo đúng.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (OCR) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given vào bước đo lường, When HLV thu thập thông tin cơ bản (tên, tuổi, chiều cao), Then cài đặt thông số trên cân.
  - AC2 — Given chuẩn bị đo, When HLV xem checklist tư thế, Then hiện: tháo chìa khóa/điện thoại → chạm gót chân vào điện cực → đứng thẳng nhìn thẳng → **không cúi đầu nhìn xuống**.
  - AC3 — Given chụp ảnh cân Tanita, When OCR, Then nhận diện: cân nặng, mỡ %, cơ kg, nước %, mỡ nội tạng, xương, tuổi sinh học, BMR.
  - AC4 — Given OCR xong, When HLV kiểm tra, Then giá trị điền sẵn vào form (T1); HLV có thể sửa nếu nhận sai.
  - AC5 — Given không chụp được ảnh, When HLV chọn "Nhập tay", Then mở form nhập tay với cùng trường.
  - AC6 — Given đã lưu chỉ số, When chuyển bước, Then dữ liệu gắn vào phiên tư vấn & chuyển sang phân tích (US-E02-04).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-03_tanita.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-03_tanita.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §4.
- **Open question:** OCR Tanita cần PoC (xem Feasibility — đồng bộ dữ liệu lai Tanita). Có API Tanita?

---

### US-E02-04 — Phân tích chỉ số & Cảnh báo sức khỏe (5 bước)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn bản phân tích chỉ số tự động theo **thứ tự 5 bước chuẩn** (cân nặng+mỡ → so sánh chuẩn → 2 loại mỡ → chiều cao/cân lý tưởng → kết luận tăng/giảm/giữ), kèm cảnh báo mỡ nội tạng, để thuyết phục khách trong khi ngồi cạnh họ mà không phải tự tra cứu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ (5 bước đã chốt) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã nhập Tanita + khảo sát, When HLV bấm "Tạo bản tư vấn", Then hiện phân tích (khuôn T1) theo **thứ tự 5 bước**:
    - **Bước 1:** đọc cân nặng + % mỡ → tính kg mỡ (= cân nặng × % mỡ / 100).
    - **Bước 2:** so sánh với bảng tiêu chuẩn theo tuổi & giới → nhận xét thừa/thiếu bao nhiêu.
    - **Bước 3:** phân tích 2 loại mỡ (dưới da — sờ được; nội tạng — trong ổ bụng, không sờ được) + bảng tham chiếu mỡ lý tưởng.
    - **Bước 4:** đọc chiều cao, đối chiếu cân nặng lý tưởng → hỏi KH có hài lòng không + số cân mong muốn.
    - **Bước 5:** so sánh cân mục tiêu vs hiện tại → kết luận nhu cầu **tăng cân / giảm cân / giữ cân**.
  - AC2 — Given mỡ nội tạng vượt ngưỡng (nam >7, nữ >4), When phân tích, Then **cảnh báo nguy cơ** (mỡ quấn tim/gan/phổi/mạch máu → tiểu đường/tim mạch/huyết áp/xương khớp/tai biến/đột quỵ) + hỏi triệu chứng (tê bì chân tay, mỏi cổ vai gáy, đau lưng).
  - AC3 — Given phân tích nước, When xem, Then chúc mừng nếu tốt (>50% nam / >45% nữ) + hiện công thức 0,4 lít/10kg/ngày.
  - AC4 — Given tuổi sinh học < tuổi thật, When xem, Then chúc mừng "cơ thể trẻ hơn X tuổi".
  - AC5 — Given above-the-fold, When xem, Then thấy ≤3 khối (nhận định tổng + 1 điểm nổi + CTA "Xem chi tiết") — đúng L2.
  - AC6 — Given khách DISC C, When trình bày, Then *cách trình bày* chuyển sang dữ liệu chi tiết/đối chiếu chuẩn; **không** in chữ "DISC = C" ra UI (L4).
  - AC7 — Given bản phân tích, When HLV bấm "Vì sao?" tại điểm khuyến nghị, Then mở lời giải thích gắn bằng chứng (chỉ ở điểm quyết định — L7).
  - AC8 — Given mọi trường hợp, Then disclaimer "không thần dược…" hiển thị (liên kết US-E02-09).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-04_phan_tich.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-04_phan_tich.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §5.
- **Open question:** Bảng tiêu chuẩn WHO/Tanita theo tuổi & giới cần chốt đầy đủ trong foundation.

---

### US-E02-05 — Xem lộ trình (giải pháp + lộ trình 3 tháng)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem lộ trình đầy đủ (lợi ích + kết quả + lộ trình 3 tháng + gói dịch vụ + cam kết) để giải thích cho KH & chốt tham gia.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bản phân tích + tick mục tiêu (US-E02-04), When vào "Xem lộ trình" (T1), Then hiện tên chương trình đề xuất theo các lựa chọn: Cơ bản, Nâng cao, Tối ưu.
  - AC2 — Given chương trình, When xem, Then hiện **lợi ích** (gạch đầu dòng) + **kết quả đạt được** (dự kiến). Nội dung lợi ích như sau:
    - Tăng cơ, tăng sức khỏe, điều chỉnh các thói quen
    - Tối ưu vóc dáng, trẻ hóa, xây thói quen bền vững
  - AC3 — Given lộ trình, When xem, Then hiện **lộ trình 3 tháng cố định** (không cho chọn 1 tháng/trọn đời), mô tả từng tháng:
    - **Tháng 1:** điều chỉnh cân nặng, trang bị kiến thức cơ bản thay đổi tư duy dinh dưỡng & thể chất.
    - **Tháng 2:** tăng cơ, tăng cường sức khỏe, điều chỉnh thói quen không lành mạnh.
    - **Tháng 3:** tối ưu vóc dáng, trẻ hóa, duy trì năng lượng, xây dựng thói quen lành mạnh bền vững.
  - AC4 — Given cam kết, When xem, Then hiện disclaimer inline (US-E02-09).
  - AC5 — Given KH đồng ý + thanh toán xong (ngoài app), When HLV bấm "Tạo tài khoản", Then mở pop-up Tạo TK (US-E02-08); Given KH chưa đồng ý, When bấm "Đóng", Then về DS KH.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-05_giai_phap.html` ✅
  - Prototype: `docs/04-prototypes/coach/CONS-05_giai_phap.html` ✅
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §6 (logic chương trình); `packaged-service-advice-v1.0.md` (gói SP).
- **Open question:** ✅ D08 chốt logic 3 chương trình; D09 (% khả thi) không còn áp dụng (lộ trình cố định 3 tháng).

---

### US-E02-06 — Chốt gói (đơn giản — Q34)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chốt gói với KH sau khi xem lộ trình; nếu KH chưa đồng ý thì **Đóng về DS KH** (xử lý từ chối làm man-to-man ngoài app), để luồng app gọn & tập trung vào quyết định.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã xem lộ trình (US-E02-05), When KH đồng ý, Then HLV bấm "Tạo tài khoản" → chuyển sang US-E02-08.
  - AC2 — Given KH chưa đồng ý, When HLV bấm "Đóng", Then quay về DS KH (luồng E01); KH giữ trạng thái "tiềm năng/chưa chốt".
  - AC3 — Given xử lý từ chối, Then **không có Objection Handler trong app ở P0** (Q34 — man-to-man, hạn chế HLV nhìn màn hình); Objection Handler FAB 5 nhánh (D07) đặt **P1+ sau** khi có đủ kịch bản.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-06_chot_goi.png` *(đổi tên từ S-CONS-06_xu_ly_tu_choi)*
  - Prototype: `docs/04-prototypes/coach/CONS-06_chot_goi.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Q34 (decisions-log); `Objection-Handler-Framework-v1.0.md` (P1+, placeholder).
- **Open question:** Khi nào đủ kịch bản để bật Objection Handler (D07)? — P1+.

---

### US-E02-07 — Gợi ý bữa ăn 10 ngày đầu
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống tự sinh thực đơn 10 ngày đầu theo mục tiêu + persona-fit, để giao cho KH ngay sau chốt gói mà không tự lên menu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (catalog món) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã chốt gói + mục tiêu, When vào "Gợi ý bữa ăn" (T1), Then hệ thống sinh thực đơn 10 ngày theo cấu trúc 3 nhóm (Đạm/Béo/Đường-bột) + persona-fit (diet_type, budget, liked/disliked).
  - AC2 — Given thực đơn, When xem, Then hiện gợi ý bữa ăn theo 5 bữa/ngày (Sáng/Phụ sáng/Trưa/Phụ chiều/Tối).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-07_bua_an.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-07_bua_an.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (calo + 3 nhóm + Persona-fit + Feasibility).

---

### US-E02-08 — Tạo tài khoản KH
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn tạo tài khoản KH nhanh sau khi chốt gói, để KH có thể đăng nhập app & bắt đầu lộ trình ngay trong buổi tư vấn.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã chốt gói, When vào "Tạo tài khoản KH" (T1), Then hệ thống điền sẵn từ dữ liệu lead (Họ tên, SĐT); HLV chỉ xác nhận.
  - AC2 — Given tạo xong, When gửi, Then KH nhận link kích hoạt (Zalo/SMS); tài khoản gắn HLV hiện tại.
  - AC3 — Given KH kích hoạt, When đăng nhập lần đầu, Then thấy onboarding ngắn + lộ trình đã có sẵn (mục tiêu + bữa ăn).
  - AC4 — Given lead, When tạo tài khoản, Then lead chuyển trạng thái "đã thành KH" — không còn trong DS KHTN.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-08_tao_tk.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-08_tao_tk.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Mô hình tài khoản liên kết HLV–KH (xem `customer-persona-data-model_v1.0.md` trong archive).
- **Open question:** Onboarding KH ngắn gồm những bước gì?

---

### US-E02-09 — Disclaimer "không thần dược"
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn disclaimer "không thần dược" hiển thị rõ trong bản phân tích & khi chốt gói, để đảm bảo minh bạch & tuân thủ nguyên tắc đạo đức.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✗ (bắt buộc) · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bản phân tích (US-E02-04), When hiển thị, Then disclaimer hiện: *"Không có gì là thần dược; để có kết quả cần kiến thức dinh dưỡng, kỷ luật bản thân, hiểu nguyên lý để không phụ thuộc vào HLV hoặc sản phẩm."*
  - AC2 — Given chốt gói (US-E02-06), When xác nhận, Then KH phải xác nhận đã đọc disclaimer trước khi đồng ý gói.
  - AC3 — Given tài khoản KH (US-E02-08), When KH đăng nhập lần đầu, Then disclaimer hiển thị trong onboarding.
- **Truy vết:**
  - Mockup: *(thành phần trong S-CONS-04, S-CONS-06, S-CONS-08)*
  - Prototype: —
  - Khuôn màn: — (component bắt buộc)
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §7; nguyên tắc đạo đức — `docs/00-foundation/vision-and-values.md` §Định hướng 6.
- **Open question:** Vị trí & dạng disclaimer (inline / modal) cần chốt.

---

## Open questions epic — đã chốt (xem `docs/00-foundation/decisions-log.md`)
- ✅ **D01** 1 shell chung HLV/KH → **1 app chung role-based** (mockup 1 bộ 2 nhánh).
- ✅ **D02** Mục tiêu KH & KD → **tách 2 model riêng** (health_goal + business_goal).
- ⏳ **D05** Bảng tiêu chuẩn WHO/Tanita → AI tìm/đề xuất (TODO fetch).
- ⏳ **D06** Bộ câu hỏi khảo sát → 7 nhóm sample, DISC/Stage HLV tự đánh giá ngoài form.
- ⏳ **D07** Objection Handler 5×4 → **chuyển P1+** (Q34: P0 chỉ "Đóng về DS KH", man-to-man); placeholder `Objection-Handler-Framework-v1.0.md`.
- ✅ **D08** 3 chương trình theo mục tiêu → đã đưa vào `Consultation-15min-Process-v1.0.md` §6.
- ✅ **D09** Công thức % khả thi → tốc độ an toàn × thời gian.
- ~~**D10** Danh sách đội ngũ (US-E02-01)~~ → **KHÔNG còn** (Q33: US-E02-01 Phá băng xóa, nội dung chuyển E05 đào tạo).
- ✅ **D11** Disclaimer → inline.
- ✅ **D13** Catalog DMO → PO cung cấp sau (placeholder).
- ✅ **D14** Copilot làm ấm/mời → P1 rule-based.
- ✅ **D15** Chống trùng lead → theo SĐT.
- ✅ **D16** Import lead → P0 chỉ nhập tay.
- ✅ **D17** Chọn talking point → hybrid (tuần mặc định, HLV đổi theo Stage).
- ⏳ **D18** 21 talking point → PO cung cấp sau (placeholder).
- ✅ **D19** Nhắc 72h → tự động gửi nhắc đến HLV.
- ✅ **D20** Metric báo cáo → talking point (tinh thần) + tỷ lệ check-in (thói quen) + số người chia sẻ (lan tỏa).
- ⏳ **D21** Ánh xạ 12 bước → PO cung cấp sau (placeholder).
- ✅ **D22** Phân quyền tuyến dưới → cấp 1 + cấp 2.
- ✅ **D23** Vòng tròn thành công → synonym 12 bước (glossary).
- ✅ **D24** Gamification → gộp 1 hệ thống credit chung.
- ✅ **D25** Sơ đồ trả thưởng → tĩnh (P0).
- ⏳ **D26** Catalog micro-course → PO cung cấp sau (placeholder).
- ✅ **D27** Streak/credit → P0 chỉ điểm check-in (3/2/1/0).
- ✅ **D28** Đồng hồ sinh học → tô màu trạng thái + gợi ý nhiệm vụ (không quản gia ảo phức tạp ở P0).
- ✅ **D29** AI companion chat → proactively gợi ý nhẹ, không phán xét.
- ⏳ **D30** 3 persona lõi → PO định nghĩa lại (placeholder).
- ✅ **Q31** RFM → đã chốt (`Customer-RFM-Scoring-v1.0.md`); ⏳ Q31a/Q31b chờ PO.
- ✅ **Q32** Attribution người mời → mặc định HLV, cho đổi (chống trùng SĐT).
- ✅ **Q33** Phá băng → **BỎ khỏi luồng app**; nội dung chuyển E05 đào tạo. US-E02-01 xóa.
- ✅ **Q34** Objection → P0 chỉ "Đóng về DS KH"; Objection Handler FAB P1+.
- ✅ **Q35** "Khảo sát mục tiêu" → **gộp vào Card Chân dung KH** (US-E02-02).

> **Chú thích:** ✅ đã chốt hoàn toàn · ⏳ đã chốt hướng nhưng chờ PO cung cấp nội dung chi tiết.
