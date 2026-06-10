# GHI CHÚ BRAINSTORM TO-BE — ỨNG DỤNG AN-CARE

> **Trạng thái:** Ghi chú làm việc (chưa phải To-be report chính thức). Kết tinh từ buổi brainstorm theo phương pháp SMART POLE, dựa trên As-Is study report v1.1.
> **Phạm vi (Outline):** Phân tích chuyên sâu toàn bộ mục tiêu, tính năng và trải nghiệm phù hợp cho 3 persona.
> **Mục tiêu kinh doanh (Aim):** Giảm tải thao tác HLV · Tăng giữ chân khách hàng · Bổ sung năng lực vận hành & kinh doanh cho Nutrition Club.

---

## 1. PERSONA: NHÀ VẬN HÀNH / HUẤN LUYỆN VIÊN (HLV)

**Cụm vận hành tại club**
- **P1 — POS quét mã vạch:** màn hình bán lẻ quét barcode, tự cộng tiền, chốt đơn nhanh khi đông khách. *(Điều kiện nền: dựng catalog sản phẩm Herbalife có mã vạch.)*
- **P2 — Kho gắn danh tính người vận hành:** mọi giao dịch xuất kho gắn người thực hiện → đối soát "ai xuất bao nhiêu" cuối ngày; cân đối thu/chi.
- **P3 — Hồ sơ hành trình kết hợp:** timeline check-in chi tiết (chỉ số Tanita + ghi chú HLV) *cộng* tự động đánh dấu cột mốc lộ trình → thay thế sổ giấy.

**Cụm đồng hành từ xa (kéo theo app khách hàng)**
- **P4 — Cầu nối nhắc nhở 2 chiều HLV ↔ Khách.**
- **P5 — Chia sẻ tự động:** hệ thống tự sinh ảnh/infographic hành trình (đồ thị + insight) cho khách một chạm chia sẻ MXH.

**UX cải tiến thêm**
- Rút gọn/tối ưu luồng **tạo lead + khảo sát DISC** (hiện rườm rà).

---

## 2. PERSONA: KHÁCH HÀNG (Member / Khách vãng lai)

- **C1 — Sổ sức khỏe số:** khách tự log hằng ngày tại nhà (cân nặng cân thường, bữa ăn, nước, ngủ, dùng sản phẩm); **chỉ số Tanita đồng bộ từ buổi đo tại club** (dữ liệu lai). Dữ liệu không còn kẹt trong sổ giấy để lại club.
- **C2 / P4 — Nhắc nhở kết hợp:** HLV gán khung mặc định theo lộ trình; khách tinh chỉnh giờ hợp sinh hoạt; app tự nhắc bữa ăn/nước/sản phẩm.
- **C3 / P5 — Chia sẻ tự động:** sinh ảnh/infographic hành trình (đồ thị + insight), khách một chạm chia sẻ MXH.
- **Onboarding:** HLV mời/tạo tài khoản, khách kích hoạt bằng SĐT → liên kết chặt HLV–khách (khớp luồng khách vãng lai từ POS).
- **Động lực giữ chân (3 trụ):** (a) đồ thị tiến bộ cảm xúc; (b) chuỗi ngày/huy hiệu (gamification); (c) chia sẻ & cộng đồng (nối với tab Chat/Cộng đồng đã có).

---

## 3. PERSONA: NHÀ SÁNG LẬP (Founder)

- **Vai trò & truy cập:** Dashboard quản trị riêng, xem **một club cụ thể hoặc gộp nhiều club** mà họ sở hữu.
- **F1 — Tài chính 3 tầng:** thu/chi cơ bản → lời/lỗ đầy đủ (COGS, hoa hồng, chi phí vận hành) → xu hướng/dự báo & cảnh báo bất thường.
- **F2 — Chân dung KH 3 chiều:** theo giá trị/chi tiêu · mức độ gắn bó · kênh/nguồn giới thiệu.
- **F3 — Sức khỏe tồn kho:** tổng hợp từ kho HLV (P2), cảnh báo sắp hết để nhập kịp.
- **F4 — CRM chăm sóc kết hợp:** tự động gửi dịp phổ biến (sinh nhật/lễ) + nhắc thủ công cho ca cần cá nhân hóa.

---

## 4. HAI NỀN TẢNG CHUNG (FOUNDATIONS) — phải làm trước

1. **Catalog sản phẩm Herbalife có mã vạch:** nền cho POS (P1) và quản lý kho (P2).
2. **App/giao diện Khách hàng + mô hình tài khoản & liên kết HLV–Khách:** nền cho P4, P5, C1, C2, C3.

## 5. QUAN HỆ PHỤ THUỘC & THỨ TỰ (đề xuất)

- Dữ liệu chảy: **POS/Kho (HLV)** → **báo cáo kinh doanh & tồn kho (Nhà sáng lập)**. ⇒ Không có P1/P2 thì F1/F3 không có dữ liệu thật.
- **App khách** là điều kiện của cụm đồng hành từ xa (P4/P5) và toàn bộ persona Khách hàng.
- Đề xuất lớp: (1) Foundations → (2) Vận hành club HLV (P1–P3) + Dashboard Nhà sáng lập (F1–F4) → (3) App khách & cầu nối đồng hành (P4/P5/C1–C3).

## 6. HỆ QUẢ PHẠM VI ĐÃ THỐNG NHẤT

- Đợt này **mở rộng từ "cải tiến app HLV" thành hệ sinh thái đa app** (HLV + Khách + Dashboard Nhà sáng lập) → tăng đáng kể phạm vi/chi phí, cần ý thức khi lập kế hoạch.

## 7. LỘ TRÌNH MVP CẮT LỚP (đã chốt)

**Bối cảnh quyết định:** điểm đau "chảy máu" nhất = thất thoát bán lẻ/kho (P1/P2); ràng buộc nguồn lực = vừa phải (2-3 lớp); thước đo thành công chính = **hiệu quả vận hành** (giảm thời gian/sai sót thao tác HLV).

**MVP-1 — "Vận hành không thất thoát" (đường găng, ra trước)**
- Nền tảng A: catalog sản phẩm Herbalife có mã vạch.
- POS quét mã vạch (P1) + Kho gắn danh tính người xuất, đối soát cuối ngày (P2).
- Báo cáo thu/chi/lãi gộp cơ bản cho Nhà sáng lập (F1 tầng 1 — gần như miễn phí từ dữ liệu POS).
- *Cắt:* dự báo tài chính, gộp đa club, chân dung KH nâng cao.

**MVP-2 — "Số hóa hồ sơ & quản trị"**
- Hồ sơ hành trình timeline + cột mốc (P3) thay sổ giấy.
- UX: rút gọn khảo sát DISC / nhập Tanita nhanh.
- Nhà sáng lập: chân dung KH (F2), tồn kho nâng cao + cảnh báo (F3), CRM chăm sóc (F4), lời/lỗ đầy đủ + dự báo (F1 tầng 2-3), gộp đa club.
- *Cắt:* gamification phía khách.

**MVP-3 — "Hệ sinh thái khách hàng" (đầu tư lớn, làm sau)**
- Nền tảng B: app khách + tài khoản liên kết HLV–Khách.
- Sổ sức khỏe số (C1), nhắc nhở kết hợp (C2/P4), chia sẻ tự động (C3/P5), 3 trụ giữ chân.

## 8. MỤC CÒN MỞ (mang sang To-be report / GAP)

- Chưa có **số liệu baseline** → To-be đặt mục tiêu định tính + **cài đặt đo lường ngay từ MVP-1**: thời gian/sai sót thao tác mỗi ngày của HLV; mở rộng dần sang tỷ lệ check-in, chuyển đổi lead→KH, At-risk.
