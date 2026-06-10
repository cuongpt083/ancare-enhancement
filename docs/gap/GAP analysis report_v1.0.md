# **BÁO CÁO PHÂN TÍCH KHOẢNG CÁCH (GAP ANALYSIS) — ỨNG DỤNG AN-CARE**

**Phiên bản:** v1.0
**Đối tượng sử dụng tài liệu:** Business Analyst (BA), Đội ngũ Phát triển Phần mềm, Nhà sáng lập.
**Cơ sở đối chiếu:** As-Is study report v1.1 (`docs/as-is/`) ↔ To-be study report v1.0 (`docs/to-be/`).
**Mục tiêu:** Xác định khoảng cách giữa hiện trạng và trạng thái mục tiêu (chức năng, dữ liệu, trải nghiệm), phân loại bản chất khoảng cách và mức công sức, làm đầu vào trực tiếp cho khuyến nghị To-do.

---

## 1. PHƯƠNG PHÁP & QUY ƯỚC

Mỗi khoảng cách được đối chiếu theo: **Hiện trạng (As-Is)** → **Mục tiêu (To-be)** → **Loại GAP** → **Công sức** → **Lớp MVP**.

**Phân loại GAP:**

- **[MỚI]** — Năng lực hoàn toàn chưa tồn tại, phải xây mới.
- **[NỀN TẢNG]** — Hạ tầng dùng chung mà nhiều năng lực khác phụ thuộc.
- **[NÂNG CẤP]** — Năng lực đã có một phần trong app, cần mở rộng/cải tiến.
- **[UX]** — Chức năng đã có nhưng trải nghiệm chưa tối ưu.
- **[DỮ LIỆU]** — Khoảng cách về thu thập/đồng bộ/đo lường dữ liệu.

**Mức công sức (định tính):** Thấp (S) · Trung bình (M) · Cao (L).

> *Lưu ý:* Do hiện trạng **chưa có số liệu baseline**, đánh giá công sức và độ ưu tiên ở đây mang tính định tính, cần tinh chỉnh ở bước nghiên cứu khả thi/lập kế hoạch chi tiết.

---

## 2. BẢNG TỔNG HỢP KHOẢNG CÁCH

### 2.1. Nền tảng dùng chung

| # | Hạng mục | Hiện trạng (As-Is) | Mục tiêu (To-be) | Loại GAP | Công sức | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| N1 | Catalog sản phẩm có mã vạch | Chưa có; sản phẩm Herbalife chỉ xuất hiện trong công thức meal plan | Danh mục sản phẩm chuẩn hóa, có mã vạch, giá | [NỀN TẢNG] | M | 1 |
| N2 | App khách hàng + tài khoản liên kết HLV–Khách | Không có giao diện khách; khách dùng sổ giấy | App khách + mô hình tài khoản, onboarding qua lời mời HLV | [NỀN TẢNG] | L | 3 |

### 2.2. Persona: Nhà vận hành / HLV

| # | Hạng mục | Hiện trạng (As-Is) | Mục tiêu (To-be) | Loại GAP | Công sức | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| H1 | Bán lẻ POS (P1) | Ghi tay/nhớ; thất thoát, khó cân đối thu/chi | POS quét mã vạch, tự cộng tiền, chốt đơn nhanh | [MỚI] | M | 1 |
| H2 | Quản lý kho (P2) | Kiểm kho thủ công cuối ngày; không tách theo người | Kho gắn danh tính người xuất, đối soát cuối ngày | [MỚI] | M | 1 |
| H3 | Hồ sơ hành trình (P3) | Ghi chép thủ công vào sổ; app có chỉ số Tanita & lộ trình 30 ngày rời rạc | Timeline check-in + tự đánh dấu cột mốc, thay sổ giấy | [NÂNG CẤP] | M | 2 |
| H4 | Cầu nối nhắc nhở 2 chiều (P4) | Phụ thuộc tự giác của khách; không có kênh trong app | HLV gán khung, app tự nhắc khách qua app khách | [MỚI] | M | 3 |
| H5 | Chia sẻ kết quả tự động (P5) | Chụp ảnh sổ, kém cảm xúc | Tự sinh ảnh/infographic hành trình | [MỚI] | M | 3 |
| H6 | Luồng tạo lead & khảo sát DISC | Đã có nhưng rườm rà | Rút gọn thao tác, tối ưu nhập liệu | [UX] | S | 2 |

### 2.3. Persona: Khách hàng

| # | Hạng mục | Hiện trạng (As-Is) | Mục tiêu (To-be) | Loại GAP | Công sức | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| K1 | Sổ sức khỏe số (C1) | Dữ liệu kẹt trong sổ giấy để lại club | Khách tự log tại nhà + Tanita đồng bộ từ club (dữ liệu lai) | [MỚI] | L | 3 |
| K2 | Tự quản lý nhắc nhở (C2) | Khách tự ghi/đặt báo thức thủ công | Nhắc nhở kết hợp HLV đặt khung + khách tinh chỉnh | [MỚI] | M | 3 |
| K3 | Chia sẻ MXH (C3) | Không có cách thuận tiện | Bản tóm tắt trực quan, một chạm chia sẻ | [MỚI] | M | 3 |
| K4 | Động lực giữ chân | Không có | Đồ thị cảm xúc + gamification + cộng đồng | [MỚI] | M | 3 |

### 2.4. Persona: Nhà sáng lập

| # | Hạng mục | Hiện trạng (As-Is) | Mục tiêu (To-be) | Loại GAP | Công sức | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| F1a | Báo cáo thu/chi cơ bản | Doanh thu hiển thị 0đ; không hệ thống hóa | Thu/chi/lãi gộp cơ bản từ dữ liệu POS | [MỚI] | S | 1 |
| F1b | Lời/lỗ đầy đủ + dự báo | Không có | COGS, hoa hồng, chi phí vận hành → lợi nhuận ròng + dự báo | [MỚI] | L | 2 |
| F2 | Chân dung khách hàng | Không có phân nhóm | Phân nhóm theo giá trị/gắn bó/kênh | [MỚI] | M | 2 |
| F3 | Sức khỏe tồn kho | Không có | Tổng hợp tồn kho từ HLV + cảnh báo sắp hết | [NÂNG CẤP] | M | 2 |
| F4 | CRM chăm sóc từ xa | Không có | Tự động dịp phổ biến + nhắc thủ công ca cá nhân hóa | [MỚI] | M | 2 |
| F5 | Dashboard đa club | Không có; app đơn vai trò HLV | Dashboard quản trị riêng, gộp nhiều club | [MỚI] | M | 2 |

### 2.5. Dữ liệu & Đo lường (xuyên suốt)

| # | Hạng mục | Hiện trạng (As-Is) | Mục tiêu (To-be) | Loại GAP | Công sức | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| D1 | Số liệu baseline vận hành | Hoàn toàn trống | Cài đặt đo thời gian/sai sót thao tác HLV từ MVP-1 | [DỮ LIỆU] | S | 1 |
| D2 | Chỉ số giữ chân & tăng trưởng | Có trạng thái At-risk nhưng chưa đo hệ thống | Đo tỷ lệ check-in, At-risk, chuyển đổi lead→KH, lượt chia sẻ | [DỮ LIỆU] | M | 2-3 |

---

## 3. KHOẢNG CÁCH KIẾN TRÚC TỔNG THỂ

Khoảng cách lớn nhất không nằm ở từng tính năng riêng lẻ mà ở **mô hình hệ thống**: As-Is là **app đơn vai trò (HLV)**, To-be là **hệ sinh thái đa vai trò (Founder + HLV + Khách hàng)** với dữ liệu chảy xuyên suốt. Điều này kéo theo các khoảng cách nền tảng:

- **Mô hình vai trò & phân quyền:** hiện chỉ có HLV; cần bổ sung vai trò Nhà sáng lập (quyền xem quản trị) và Khách hàng (app riêng).
- **Luồng dữ liệu giao dịch:** hiện chưa có lớp giao dịch (bán lẻ/xuất kho); đây là nguồn dữ liệu cho cả báo cáo kinh doanh và đối soát.
- **Đồng bộ hai chiều HLV ↔ Khách:** hiện chưa tồn tại; là điều kiện cho đồng hành từ xa, sổ sức khỏe số và chia sẻ.

---

## 4. PHÂN BỐ KHOẢNG CÁCH THEO LỚP MVP

- **MVP-1 (đường găng):** N1, H1, H2, F1a, D1 — chủ yếu [MỚI]/[NỀN TẢNG] mức S–M, đánh trúng điểm thất thoát bán lẻ/kho và thước đo hiệu quả vận hành.
- **MVP-2:** H3, H6, F1b, F2, F3, F4, F5, D2 — số hóa hồ sơ và hoàn thiện lớp quản trị cho Nhà sáng lập; xuất hiện hạng mục công sức cao (F1b).
- **MVP-3 (đầu tư lớn):** N2, H4, H5, K1–K4 — toàn bộ hệ sinh thái khách hàng, phụ thuộc nền tảng N2 (app khách, mức L).

**Nhận định:** Phần lớn công sức Cao (L) tập trung ở nền tảng app khách (N2) và các năng lực khách hàng (K1) ở MVP-3 — phù hợp với quyết định để khoản đầu tư lớn nhất ở lớp sau.

---

## 5. RỦI RO & PHỤ THUỘC THEN CHỐT

- **Phụ thuộc nền tảng:** H1/H2/F1a phụ thuộc N1; toàn bộ MVP-3 phụ thuộc N2. Chậm nền tảng sẽ chặn cả lớp.
- **Thiếu baseline:** không có số liệu gốc khiến việc chứng minh hiệu quả khó định lượng nếu không cài đo lường (D1) ngay từ đầu.
- **Phạm vi mở rộng:** việc thêm app khách biến dự án thành hệ đa app, tăng đáng kể chi phí và độ phức tạp tích hợp/phân quyền.
- **Chất lượng dữ liệu Tanita:** mô hình dữ liệu lai (khách tự nhập + Tanita từ club) cần quy tắc đồng bộ rõ ràng để tránh xung đột/trùng lặp.

---

## 6. BƯỚC TIẾP THEO

Báo cáo GAP này là đầu vào trực tiếp cho **To-do recommendations**: chuyển từng khoảng cách thành hạng mục hành động cụ thể, sắp xếp theo lớp MVP và quan hệ phụ thuộc, kèm đề xuất tiêu chí nghiệm thu (Definition of Done) cho mỗi hạng mục.
