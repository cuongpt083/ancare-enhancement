# E02 — Consultation 15 phút

- **Vai trò:** HLV (với khách ngồi cạnh)
- **Mục tiêu:** Số hóa buổi tư vấn 15 phút theo **quy trình tiêu chuẩn 5 giai đoạn** (Phá băng → Khảo sát → Đo lường → Phân tích & Cảnh báo → Tư vấn giải pháp & Chốt chương trình) → Gợi ý bữa ăn → Tạo tài khoản KH → Disclaimer.
- **Nguồn:** feature-tree §2.2; **quy trình chuẩn:** `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` (chưng cất từ `docs/00-foundation/consultation-sample-15-minutes.md`); tham chiếu `docs/99-archive/srs/Objection-Handler_v1.0.md`.

## Danh sách stories
| ID | Bước | Tên ngắn | Ưu tiên |
|---|---|---|---|
| US-E02-01 | Giai đoạn 1 | Phá băng & Xây dựng thiện cảm | Must |
| US-E02-02 | Giai đoạn 2 | Khảo sát & Khai thác thông tin | Must |
| US-E02-03 | Giai đoạn 3 | Hướng dẫn đo lường Tanita (OCR + tư thế) | Must |
| US-E02-04 | Giai đoạn 4 | Phân tích chỉ số & Cảnh báo sức khỏe (5 bước) | Must |
| US-E02-05 | Giai đoạn 5 | Tư vấn giải pháp + Xác định mục tiêu | Must |
| US-E02-06 | Giai đoạn 5 | Xử lý từ chối / Chốt gói (3–6 tháng) | Must |
| US-E02-07 | Sau chốt | Gợi ý bữa ăn 10 ngày đầu | Must |
| US-E02-08 | Sau chốt | Tạo tài khoản KH | Must |
| US-E02-09 | Xuyên suốt | Disclaimer "không thần dược" | Must |

---

### US-E02-01 — Phá băng & Xây dựng thiện cảm
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn một checklist phá băng & xây dựng thiện cảm (hỏi thăm cá nhân, đồng cảm/khen ngợi, giới thiệu bản thân & đội ngũ kèm kết quả tiêu biểu), để tạo niềm tin ngay trong 1–2 phút đầu trước khi đi vào khảo sát.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào buổi tư vấn, When HLV mở bước "Phá băng", Then hiện checklist (khuôn T1): (1) hỏi thăm cá nhân (vd năm sinh), (2) đồng cảm & khen ngợi đặc điểm tích cực, (3) giới thiệu bản thân & vai trò, (4) giới thiệu đội ngũ kèm kết quả tiêu biểu.
  - AC2 — Given giới thiệu đội ngũ, When HLV xem, Then hiện danh sách thành viên + kết quả đã đạt được (vd: cải thiện trào ngược dạ dày, giảm 5 cân, giúp người thân cải thiện sức khỏe) → tạo niềm tin bằng bằng chứng người thật; HLV có thể tùy chỉnh danh sách.
  - AC3 — Given hoàn thành phá băng, When HLV bấm "Bắt đầu khảo sát", Then chuyển sang US-E02-02.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-01_pha_bang.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-01_pha_bang.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §2.
- **Open question:** Danh sách đội ngũ & kết quả tiêu biểu: HLV tự nhập hay có template chung cho club?

---

### US-E02-02 — Khảo sát & Khai thác thông tin
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chạy bộ khảo sát theo trình tự 7 nhóm chuẩn (mục tiêu → tiền sử bệnh lý → giấc ngủ → ăn sáng → uống nước → vận động/sinh hoạt → tạo động lực), để thu thập đủ dữ liệu sinh bản tư vấn & tạo động lực trước khi đo lường.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given hoàn thành phá băng (US-E02-01), When vào khảo sát, Then hiện câu hỏi theo trình tự 7 nhóm: (1) mục tiêu mong muốn, (2) tiền sử bệnh lý (tim mạch/huyết áp/đại tràng/dạ dày), (3) giấc ngủ (giờ ngủ/giờ thức/độ sâu), (4) ăn sáng, (5) uống nước, (6) vận động & sinh hoạt (tập thể dục/hút thuốc/rượu bia), (7) tạo động lực.
  - AC2 — Given KH trả lời, When nhập ngắn gọn (text/gõ, vd "tôi chỉ bị mất ngủ, còn lại bình thường"), Then hệ thống phân tích & ghi vào `primary_goal`, `pain_points[]`, `lifestyle` (sleep, diet, water, exercise, habits).
  - AC3 — Given khảo sát xong, When đến nhóm 7 (tạo động lực), Then hiện gợi ý câu chuyện thành công của HLV + hàng nghìn người đã giúp để truyền tự tin cho KH trước khi đo.
  - AC4 — Given hoàn thành khảo sát, When HLV bấm "Tiếp theo", Then chuyển sang đo lường Tanita (US-E02-03).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-02_khao_sat.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-02_khao_sat.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §3; Persona framework — `docs/00-foundation/personas.md`.
- **Open question:** Bộ câu hỏi khảo sát rút gọn cần chốt đầy đủ (DISC + Stage + pain points) — đặc tả business-rule.

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

### US-E02-05 — Tư vấn giải pháp + Xác định mục tiêu
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống tự đề xuất giải pháp theo mục tiêu (giảm→Cơ-Nước-Mỡ, tăng→Dinh dưỡng tế bào, giữ→Bữa ăn lành mạnh) & tính % khả thi, để đề xuất gói phù hợp & tinh chỉnh mà không tính tay.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bản phân tích + kết luận nhu cầu (Bước 5, US-E02-04), When vào "Tư vấn giải pháp" (T1), Then hệ thống đề xuất chương trình theo logic:
    - **giảm cân** → **"Cân bằng Cơ — Nước — Mỡ"**
    - **tăng cân** → **"Dinh dưỡng tế bào"**
    - **giữ cân** → **"Bữa ăn lành mạnh"**
  - AC2 — Given giải pháp đề xuất (vd "Cơ — Nước — Mỡ"), When xem, Then hiện cơ chế giải pháp (giảm **đúng mỡ thừa**, giữ/tăng cơ + nước) + phân tích sai lầm khi tự giảm cân (nhịn ăn/tập quá sức → mất cơ+nước, mỡ giữ nguyên/tăng).
  - AC3 — Given gói + thời gian, When xem, Then hiện nhãn ngôn ngữ khả thi ("Khả thi" / "Tham vọng") thay vì % số — L4.
  - AC4 — Given muốn tinh chỉnh, When HLV bấm "Chỉnh", Then mở tùy chỉnh mục tiêu/thời gian; khả thi cập nhật theo thời gian thực.
  - AC5 — Given "Vì sao?" tại khả thi, When bấm, Then giải thích yếu tố ảnh hưởng (tốc độ an toàn, baseline, thời gian) — L7.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-05_giai_phap.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-05_giai_phap.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Consultation-15min-Process-v1.0.md` §6; `packaged-service-advice-v1.0.md` (quy tắc gói); `Calorie-Meal-Business-Rules-v1.1.md` (tốc độ an toàn).
- **Open question:** Công thức % khả thi cần chốt (dựa tốc độ an toàn + adherence dự kiến).

---

### US-E02-06 — Xử lý từ chối / Chốt gói (3–6 tháng)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn trợ lý xử lý từ chối (Objection Handler) gợi ý cách phản hồi khi khách băn khoăn, để chốt gói cao nhất 3–6 tháng mà vẫn tôn trọng quyết định khách.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (nhánh phản đối) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bước chốt gói, When khách nêu băn khoăn, Then HLV bấm FAB "Khách đang băn khoăn" → mở nhánh phản đối (đắt/rẻ · phụ thuộc SP · tái béo · đa cấp/TPCN/BĐ gen · đói).
  - AC2 — Given chọn nhánh, When xem gợi ý, Then hiện mẫu câu phản hồi phù hợp DISC + Stage (gợi ý chỉnh sửa được, **không auto-gửi** — L5).
  - AC3 — Given khách vẫn từ chối, When HLV đánh dấu "để sau", Then cập nhật Stage & gợi ý DMO tiếp theo (không tạo áp lực).
  - AC4 — Given chốt thành công, When HLV chọn gói + thời gian, Then chuyển sang tạo tài khoản (US-E02-08).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-06_xu_ly_tu_choi.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-06_xu_ly_tu_choi.html` *(chưa tạo)*
  - Khuôn màn: T1 + component ObjectionHandler
  - Nghiệp vụ: `docs/99-archive/srs/Objection-Handler_v1.0.md` (chưng cất tiếp vào foundation).
- **Open question:** Nhánh phản đối & mẫu câu cần chốt đầy đủ 4 DISC × 5 phản đối.

---

### US-E02-07 — Gợi ý bữa ăn 10 ngày đầu
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống tự sinh thực đơn 10 ngày đầu theo mục tiêu + persona-fit, để giao cho KH ngay sau chốt gói mà không tự lên menu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (catalog món) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã chốt gói + mục tiêu, When vào "Gợi ý bữa ăn" (T1), Then hệ thống sinh thực đơn 10 ngày theo cấu trúc 3 nhóm (Đạm/Xơ/Đường-bột) + persona-fit (diet_type, budget, liked/disliked).
  - AC2 — Given thực đơn, When xem, Then hiện nhãn khả thi ("Dễ áp dụng" / "Hơi khó" / "Khó") — L4, không hiện Feasibility Score số.
  - AC3 — Given muốn chỉnh, When HLV bấm "Chỉnh", Then đổi món trong ngày; hệ thống gợi ý món thay thế cùng nhóm.
  - AC4 — Given "Vì sao?" tại khả thi, When bấm, Then giải thích (ngân sách, khẩu vị, độ phức tạp nấu) — L7.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-07_bua_an.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-07_bua_an.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (calo + 3 nhóm + Persona-fit + Feasibility).
- **Open question:** Catalog món ăn & hệ số đơn vị (tham khảo anh Hoàng — `[TBD]`).

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

## Open questions epic
- Bảng tiêu chuẩn WHO/Tanita theo tuổi & giới cho US-E02-04.
- Objection Handler: chốt nhánh 5 phản đối × 4 DISC cho US-E02-06.
- Catalog món ăn & hệ số đơn vị cho US-E02-07 (tham khảo anh Hoàng — `[TBD]`).
- Công thức % khả thi cho US-E02-05.
- Bộ câu hỏi khảo sát rút gọn (DISC + Stage + pain points) cho US-E02-02.
