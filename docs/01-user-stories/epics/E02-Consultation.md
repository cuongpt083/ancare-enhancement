# E02 — Consultation 15 phút

- **Vai trò:** HLV (với khách ngồi cạnh)
- **Mục tiêu:** Số hóa buổi tư vấn 15 phút theo công thức 1-7-2-3-2 — từ cân quét chỉ số → khảo sát chân dung → bản tư vấn đồng cảm → xác định mục tiêu → xử lý từ chối/chốt gói → gợi ý bữa ăn 10 ngày → tạo tài khoản KH → disclaimer.
- **Nguồn:** feature-tree §2.2; tham chiếu `docs/99-archive/to-be/Empathy-Consultation_v1.0.md`, `Objection-Handler_v1.0.md`.

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E02-01 | Cân quét / nhập chỉ số Tanita (OCR ảnh) | Must |
| US-E02-02 | Khảo sát chân dung (bệnh lý, ăn, uống, vận động, DISC, mong muốn) | Must |
| US-E02-03 | Bản tư vấn đối chiếu chuẩn (5 lớp đồng cảm) | Must |
| US-E02-04 | Xác định mục tiêu + tính % khả thi | Must |
| US-E02-05 | Xử lý từ chối / chốt gói (3–6 tháng) | Must |
| US-E02-06 | Gợi ý bữa ăn 10 ngày đầu | Must |
| US-E02-07 | Tạo tài khoản KH | Must |
| US-E02-08 | Hiển thị disclaimer "không thần dược" | Must |

---

### US-E02-01 — Cân quét / nhập chỉ số Tanita (OCR ảnh)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chụp ảnh màn hình cân Tanita & hệ thống tự nhận diện (OCR) các chỉ số, để nhập dữ liệu trong ≤1 phút thay vì gõ tay từng chỉ số.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (OCR) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV vào bước "Cân quét", When chụp ảnh cân Tanita, Then OCR nhận diện: cân nặng, mỡ %, cơ kg, nước %, mỡ nội tạng, xương, tuổi sinh học, BMR.
  - AC2 — Given OCR xong, When HLV kiểm tra, Then các giá trị điền sẵn vào form (T1); HLV có thể sửa nếu nhận sai.
  - AC3 — Given không chụp được ảnh, When HLV chọn "Nhập tay", Then mở form nhập tay với cùng trường.
  - AC4 — Given đã lưu chỉ số, When chuyển bước, Then dữ liệu gắn vào phiên tư vấn hiện tại.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-01_tanita.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-01_tanita.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** OCR Tanita cần PoC (xem Feasibility — đồng bộ dữ liệu lai Tanita). Độ chính xác tối thiểu? Có API Tanita?

---

### US-E02-02 — Khảo sát chân dung
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chạy bộ khảo sát chân dung ngắn (bệnh lý, ăn, uống, vận động, DISC, mong muốn) với KH trả lời ngắn gọn, để thu thập đủ dữ liệu sinh bản tư vấn & xác định DISC.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã nhập Tanita, When vào bước khảo sát, Then hiện câu hỏi từng nhóm (bệnh lý → ăn → uống → vận động → mong muốn), mỗi câu 1 màn (T1), KH trả lời ngắn gọn.
  - AC2 — Given câu hỏi DISC, When KH trả lời, Then hệ thống đề xuất `disc_primary` (D/I/S/C) — HLV xác nhận.
  - AC3 — Given câu hỏi bệnh lý, When KH nêu vấn đề (vd "mất ngủ"), Then ghi vào `pain_points[]`.
  - AC4 — Given hoàn thành khảo sát, When chuyển bước, Then dữ liệu gắn vào phiên & sẵn sàng sinh bản tư vấn.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-02_khao_sat.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-02_khao_sat.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Persona framework — `docs/00-foundation/personas.md`.
- **Open question:** Bộ câu hỏi khảo sát rút gọn cần chốt (DISC + Stage + pain points) — đặc tả business-rule.

---

### US-E02-03 — Bản tư vấn đối chiếu chuẩn (5 lớp đồng cảm)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn một bản tư vấn tự động đối chiếu chỉ số Tanita với chuẩn WHO/Tanita, chỉ ra điểm cần cải thiện & nguy cơ theo cấu trúc đồng cảm (5 lớp), để thuyết phục khách trong khi vẫn đang ngồi cạnh họ mà không phải tự tra cứu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (5 lớp cần chốt mẫu) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã nhập đủ Tanita + khảo sát, When HLV bấm "Tạo bản tư vấn", Then hiển thị bản tư vấn (khuôn T1) đối chiếu chuẩn & danh sách điểm cần cải thiện; thời gian thao tác mục tiêu ≤ ~7 phút/KH.
  - AC2 — Given bản tư vấn, When xem lớp đầu (above-the-fold), Then thấy ≤3 khối (nhận định tổng + 1 điểm nổi + CTA "Xem chi tiết") — đúng L2.
  - AC3 — Given khách thuộc DISC C, When trình bày, Then *cách trình bày* chuyển sang dữ liệu chi tiết/đối chiếu chuẩn; **không** in chữ "DISC = C" ra UI (L4).
  - AC4 — Given bản tư vấn, When HLV bấm "Vì sao?" tại điểm khuyến nghị gói, Then mở lời giải thích gắn bằng chứng (chỉ ở điểm quyết tiền — L7).
  - AC5 — Given mọi trường hợp, Then disclaimer "không thần dược…" hiển thị (liên kết US-E02-08).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-03_ban_tu_van.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-03_ban_tu_van.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/packaged-service-advice-v1.0.md` (chốt gói); empathy 5 lớp — chưng cất tiếp từ archive.
- **Open question:** Cấu trúc 5 lớp đồng cảm cụ thể cần chốt mẫu câu (xem `Empathy-Consultation_v1.0.md` trong archive — đưa rule tóm lược vào foundation khi chốt).

---

### US-E02-04 — Xác định mục tiêu + tính % khả thi
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chọn gói + thời gian cho KH và thấy ngay % khả thi đạt mục tiêu, để đề xuất gói khả thi nhất & tinh chỉnh mục tiêu mà không tính tay.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bản tư vấn, When vào "Thiết lập mục tiêu" (T1), Then hệ thống chọn sẵn gói đề xuất + thời gian dựa chỉ số & persona (L3 mặc định thông minh).
  - AC2 — Given gói đề xuất, When xem, Then hiện nhãn ngôn ngữ khả thi ("Khả thi" / "Tham vọng") thay vì % số — L4.
  - AC3 — Given muốn tinh chỉnh, When HLV bấm "Chỉnh", Then mở tùy chỉnh mục tiêu/thời gian; % cập nhật theo thời gian thực.
  - AC4 — Given "Vì sao?" tại % khả thi, When bấm, Then giải thích yếu tố ảnh hưởng (tốc độ an toàn, baseline, thời gian) — L7.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-04_muc_tieu.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-04_muc_tieu.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/packaged-service-advice-v1.0.md` (quy tắc gói); `Calorie-Meal-Business-Rules-v1.1.md` (tốc độ an toàn).
- **Open question:** Công thức % khả thi cần chốt (dựa tốc độ an toàn + adherence dự kiến).

---

### US-E02-05 — Xử lý từ chối / chốt gói (3–6 tháng)
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn trợ lý xử lý từ chối (Objection Handler) gợi ý cách phản hồi khi khách băn khoăn, để chốt gói cao nhất 3–6 tháng mà vẫn tôn trọng quyết định khách.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (nhánh phản đối) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bước chốt gói, When khách nêu băn khoăn, Then HLV bấm FAB "Khách đang băn khoăn" → mở nhánh phản đối (đắt/rẻ · phụ thuộc SP · tái béo · đa cấp/TPCN/BĐ gen · đói).
  - AC2 — Given chọn nhánh, When xem gợi ý, Then hiện mẫu câu phản hồi phù hợp DISC + Stage (gợi ý chỉnh sửa được, **không auto-gửi** — L5).
  - AC3 — Given khách vẫn từ chối, When HLV đánh dấu "để sau", Then cập nhật Stage & gợi ý DMO tiếp theo (không tạo áp lực).
  - AC4 — Given chốt thành công, When HLV chọn gói + thời gian, Then chuyển sang tạo tài khoản (US-E02-07).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-05_xu_ly_tu_choi.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-05_xu_ly_tu_choi.html` *(chưa tạo)*
  - Khuôn màn: T1 + component ObjectionHandler
  - Nghiệp vụ: `docs/99-archive/srs/Objection-Handler_v1.0.md` (chưng cất tiếp vào foundation).
- **Open question:** Nhánh phản đối & mẫu câu cần chốt đầy đủ 4 DISC × 5 phản đối.

---

### US-E02-06 — Gợi ý bữa ăn 10 ngày đầu
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống tự sinh thực đơn 10 ngày đầu theo mục tiêu + persona-fit, để giao cho KH ngay sau chốt gói mà không tự lên菜单.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (catalog món) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã chốt gói + mục tiêu, When vào "Gợi ý bữa ăn" (T1), Then hệ thống sinh thực đơn 10 ngày theo cấu trúc 3 nhóm (Đạm/Xơ/Đường-bột) + persona-fit (diet_type, budget, liked/disliked).
  - AC2 — Given thực đơn, When xem, Then hiện nhãn khả thi ("Dễ áp dụng" / "Hơi khó" / "Khó") — L4, không hiện Feasibility Score số.
  - AC3 — Given muốn chỉnh, When HLV bấm "Chỉnh", Then đổi món trong ngày; hệ thống gợi ý món thay thế cùng nhóm.
  - AC4 — Given "Vì sao?" tại khả thi, When bấm, Then giải thích (ngân sách, khẩu vị, độ phức tạp nấu) — L7.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-06_bua_an.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-06_bua_an.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (calo + 3 nhóm + Persona-fit + Feasibility).
- **Open question:** Catalog món ăn & hệ số đơn vị (tham khảo anh Hoàng — `[TBD]`).

---

### US-E02-07 — Tạo tài khoản KH
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
  - Mockup: `docs/03-mockups/coach/S-CONS-07_tao_tk.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-07_tao_tk.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Mô hình tài khoản liên kết HLV–KH (xem `customer-persona-data-model_v1.0.md` trong archive).
- **Open question:** Onboarding KH ngắn gồm những bước gì?

---

### US-E02-08 — Hiển thị disclaimer "không thần dược"
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn disclaimer "không thần dược" hiển thị rõ trong bản tư vấn & khi chốt gói, để đảm bảo minh bạch & tuân thủ nguyên tắc đạo đức.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✗ (bắt buộc) · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given bản tư vấn (US-E02-03), When hiển thị, Then disclaimer hiện: *"Không có gì là thần dược; để có kết quả cần kiến thức dinh dưỡng, kỷ luật bản thân, hiểu nguyên lý để không phụ thuộc vào HLV hoặc sản phẩm."*
  - AC2 — Given chốt gói (US-E02-05), When xác nhận, Then KH phải xác nhận đã đọc disclaimer trước khi đồng ý gói.
  - AC3 — Given tài khoản KH (US-E02-07), When KH đăng nhập lần đầu, Then disclaimer hiển thị trong onboarding.
- **Truy vết:**
  - Mockup: *(thành phần trong S-CONS-03, S-CONS-05, S-CONS-07)*
  - Prototype: —
  - Khuôn màn: — (component bắt buộc)
  - Nghiệp vụ: Nguyên tắc đạo đức — `docs/00-foundation/vision-and-values.md` §Định hướng 6.
- **Open question:** Vị trí & dạng disclaimer (inline / modal) cần chốt.

---

## Open questions epic
- 5 lớp đồng cảm: chốt mẫu câu + catalog chỉ số cho Lớp 2.
- Objection Handler: chốt nhánh 5 phản đối × 4 DISC.
- Catalog món ăn & hệ số đơn vị cho US-E02-06 (tham khảo anh Hoàng — `[TBD]`).
- Công thức % khả thi cho US-E02-04.
