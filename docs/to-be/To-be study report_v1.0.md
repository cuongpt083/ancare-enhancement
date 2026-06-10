# **BÁO CÁO THIẾT KẾ TRẠNG THÁI MỤC TIÊU (TO-BE) — ỨNG DỤNG AN-CARE**

**Phiên bản:** v1.0
**Đối tượng sử dụng tài liệu:** Business Analyst (BA), Đội ngũ Phát triển Phần mềm, Nhà sáng lập / Chủ Nutrition Club.
**Cơ sở xây dựng:** As-Is study report v1.1 (`docs/as-is/`) và buổi brainstorm theo phương pháp SMART POLE (`docs/to-be/To-be brainstorm notes.md`).
**Mục tiêu tài liệu:** Mô tả trạng thái mục tiêu (To-be) của hệ sinh thái An-Care — định hướng trải nghiệm, kiến trúc chức năng và lộ trình triển khai theo lớp MVP — làm đầu vào cho phân tích GAP và khuyến nghị To-do.

---

## 1. BỐI CẢNH & TẦM NHÌN

### 1.1. Vấn đề cốt lõi của hiện trạng

Hiện trạng (As-Is) cho thấy An-Care mới phục vụ **một persona duy nhất** là Huấn luyện viên (HLV) qua app 5 tab, trong khi thực tế hệ sinh thái Nutrition Club có **ba nhóm người dùng** với nhu cầu khác biệt. Hệ quả: phần lớn nghiệp vụ quan trọng — bán lẻ, quản lý kho, theo dõi hành trình khách hàng, đồng hành từ xa, và quản trị kinh doanh — đang được xử lý **thủ công bằng sổ sách và trí nhớ**, gây thất thoát, mất dữ liệu và giảm khả năng giữ chân khách hàng.

### 1.2. Tầm nhìn To-be

An-Care chuyển từ **một app công cụ cho HLV** thành **một hệ sinh thái đa vai trò** kết nối liền mạch ba persona: Nhà sáng lập điều hành bằng dữ liệu, Nhà vận hành/HLV vận hành club không thất thoát và đồng hành khách hàng xuyên suốt, Khách hàng tự theo dõi và lan tỏa hành trình sức khỏe của mình.

### 1.3. Mục tiêu kinh doanh (Aim)

Hệ thống To-be hướng tới ba mục tiêu: **giảm tải thao tác** cho HLV/Nhà vận hành; **tăng giữ chân khách hàng** và nâng trải nghiệm xuyên suốt; **bổ sung năng lực vận hành & kinh doanh** cho Nutrition Club (bán lẻ, quản lý kho, quản trị lời/lỗ). Thước đo ưu tiên của đợt triển khai đầu là **hiệu quả vận hành** (giảm thời gian và sai sót thao tác hằng ngày của HLV).

---

## 2. CÁC PERSONA MỤC TIÊU

| Persona | Vai trò | Giá trị họ coi trọng | Giao diện To-be |
| :---- | :---- | :---- | :---- |
| **Nhà sáng lập (Founder)** | Chủ club, người kinh doanh. | Minh bạch tài chính, hiểu khách hàng, kiểm soát tồn kho, chăm sóc từ xa. | Dashboard quản trị riêng (1 hoặc nhiều club). |
| **Nhà vận hành / HLV** | Vận hành club, tư vấn, đồng hành khách hàng. | Thao tác nhanh, không thất thoát, theo dõi được hành trình. | App HLV nâng cấp (POS, kho, hồ sơ hành trình, cầu nối khách). |
| **Khách hàng (Member / Vãng lai)** | Người trải nghiệm lộ trình. | Tự chủ dữ liệu, được nhắc nhở/đồng hành, được ghi nhận & chia sẻ. | App khách hàng (mới). |

---

## 3. NĂNG LỰC MỤC TIÊU THEO PERSONA

### 3.1. Nhà vận hành / Huấn luyện viên (HLV)

**Vận hành tại club**

- **Bán lẻ POS quét mã vạch:** màn hình bán hàng quét barcode sản phẩm Herbalife, tự cộng tiền và chốt đơn trong vài giây, kể cả lúc đông khách. Giải quyết tình trạng không nhớ "đã bán cho ai, bao nhiêu" và khó cân đối thu/chi cuối ngày.
- **Quản lý kho gắn danh tính người vận hành:** mỗi giao dịch xuất kho được gắn với người thực hiện, cho phép đối soát chính xác cuối ngày ("ai đã xuất bao nhiêu") trong môi trường nhiều người đồng vận hành.
- **Hồ sơ hành trình số hóa:** thay thế sổ giấy bằng một timeline check-in chi tiết (chỉ số cơ thể Tanita + ghi chú HLV), kết hợp tự động đánh dấu các cột mốc của lộ trình 30 ngày để tra cứu nhanh tiến độ dài hạn của từng khách.

**Đồng hành từ xa (kết nối sang app khách)**

- **Cầu nối nhắc nhở hai chiều HLV ↔ Khách:** HLV gán khung nhắc nhở theo lộ trình; hệ thống tự nhắc khách (bữa ăn, nước, sản phẩm) khi họ ở nhà, giảm phụ thuộc vào sự tự giác.
- **Chia sẻ kết quả tự động:** hệ thống tự sinh ảnh/infographic hành trình (đồ thị + insight) để khách một chạm chia sẻ lên mạng xã hội — thay cho ảnh chụp sổ kém cảm xúc.

**Cải tiến trải nghiệm**

- **Tối ưu luồng tạo lead & khảo sát DISC:** rút gọn thao tác nhập liệu và bảng khảo sát đầu vào hiện đang rườm rà.

### 3.2. Khách hàng

- **Sổ sức khỏe số (mang về nhà):** khách tự ghi nhật ký hằng ngày tại nhà (cân nặng, bữa ăn, nước, giấc ngủ, việc dùng sản phẩm); **chỉ số Tanita được đồng bộ từ buổi đo tại club** (mô hình dữ liệu lai). Dữ liệu không còn "kẹt" trong sổ giấy để lại club.
- **Nhắc nhở kết hợp:** HLV đặt khung mặc định theo lộ trình, khách tinh chỉnh giờ cho hợp sinh hoạt; app tự động nhắc.
- **Chia sẻ hành trình tự động:** nhận bản tóm tắt trực quan (đồ thị tiến bộ, cột mốc) để chia sẻ MXH dễ dàng.
- **Onboarding qua lời mời của HLV:** HLV tạo hồ sơ và mời, khách kích hoạt bằng số điện thoại — liên kết chặt HLV–Khách, khớp với luồng khách vãng lai từ POS.
- **Động lực giữ chân (3 trụ):** đồ thị tiến bộ giàu cảm xúc, chuỗi ngày/huy hiệu (gamification), và chia sẻ & cộng đồng (kết nối tab Cộng đồng sẵn có).

### 3.3. Nhà sáng lập

- **Dashboard quản trị riêng:** xem số liệu cho một club cụ thể hoặc gộp nhiều club thuộc sở hữu.
- **Báo cáo tài chính 3 tầng:** thu/chi cơ bản → lời/lỗ đầy đủ (giá vốn, hoa hồng, chi phí vận hành) → xu hướng/dự báo doanh thu và cảnh báo bất thường.
- **Chân dung khách hàng (3 chiều):** phân nhóm theo giá trị/chi tiêu, mức độ gắn bó, và kênh/nguồn giới thiệu — làm cơ sở chăm sóc hiệu quả.
- **Sức khỏe tồn kho:** tổng hợp từ dữ liệu kho của HLV, cảnh báo sắp hết để nhập kịp thời.
- **CRM chăm sóc kết hợp:** tự động gửi tin nhắn dịp phổ biến (sinh nhật, lễ) theo mẫu, đồng thời nhắc người phụ trách chủ động liên hệ cho các trường hợp cần cá nhân hóa.

---

## 4. KIẾN TRÚC & NỀN TẢNG DÙNG CHUNG

Hai nền tảng bắt buộc phải xây trước vì nhiều năng lực phụ thuộc vào chúng:

1. **Catalog sản phẩm Herbalife có mã vạch** — nền tảng cho POS bán lẻ và quản lý kho.
2. **App/giao diện Khách hàng và mô hình tài khoản liên kết HLV–Khách** — nền tảng cho toàn bộ persona Khách hàng và cụm đồng hành từ xa.

**Quan hệ phụ thuộc dữ liệu:** Dữ liệu giao dịch từ POS và kho (do HLV tạo) chảy lên thành báo cáo tài chính và tồn kho cho Nhà sáng lập. Do đó báo cáo kinh doanh không thể có số liệu thật nếu chưa có POS/kho. Tương tự, cụm đồng hành từ xa (nhắc nhở, chia sẻ) không hoạt động nếu chưa có app khách.

---

## 5. LỘ TRÌNH TRIỂN KHAI THEO LỚP MVP

Cắt lớp theo nguyên tắc: ưu tiên điểm đau gây thất thoát trực tiếp, tôn trọng thứ tự phụ thuộc nền tảng, và để khoản đầu tư lớn nhất (app khách) ở lớp sau.

### MVP-1 — "Vận hành không thất thoát" (đường găng, ra trước)

Tập trung giải điểm đau chảy máu nhất (thất thoát bán lẻ/kho) và phục vụ trực tiếp thước đo hiệu quả vận hành.

- Nền tảng A: catalog sản phẩm có mã vạch.
- POS quét mã vạch (bán lẻ) và quản lý kho gắn danh tính người xuất, đối soát cuối ngày.
- Báo cáo thu/chi/lãi gộp cơ bản cho Nhà sáng lập (tận dụng dữ liệu POS sẵn có).
- *Phạm vi cắt:* dự báo tài chính, gộp đa club, chân dung khách hàng nâng cao.

### MVP-2 — "Số hóa hồ sơ & quản trị"

- Hồ sơ hành trình số hóa (timeline + cột mốc) thay thế sổ giấy.
- Tối ưu trải nghiệm: rút gọn khảo sát DISC, tăng tốc nhập liệu Tanita.
- Dashboard Nhà sáng lập đầy đủ: chân dung khách hàng, tồn kho nâng cao + cảnh báo, CRM chăm sóc, báo cáo lời/lỗ đầy đủ + dự báo, gộp đa club.
- *Phạm vi cắt:* gamification phía khách.

### MVP-3 — "Hệ sinh thái khách hàng" (đầu tư lớn, làm sau)

- Nền tảng B: app khách hàng + tài khoản liên kết HLV–Khách.
- Sổ sức khỏe số, nhắc nhở kết hợp, chia sẻ hành trình tự động, ba trụ giữ chân.

---

## 6. THƯỚC ĐO THÀNH CÔNG

Do hiện trạng **chưa có số liệu baseline**, To-be áp dụng cách tiếp cận: thiết lập đo lường ngay từ MVP-1 và đặt mục tiêu cải thiện tương đối.

| Nhóm | Chỉ số cần đo (cài đặt từ MVP) | Kỳ vọng To-be |
| :---- | :---- | :---- |
| **Hiệu quả vận hành (ưu tiên)** | Thời gian & sai sót thao tác hằng ngày của HLV; thời gian chốt đối soát cuối ngày. | Giảm rõ rệt so với quy trình sổ sách. |
| **Giữ chân khách hàng** | Tỷ lệ check-in, tỷ lệ At-risk, thời gian gắn bó. | Tăng giữ chân, giảm At-risk. |
| **Kinh doanh** | Độ chính xác báo cáo lời/lỗ và tồn kho; tỷ lệ thất thoát bán lẻ. | Minh bạch và giảm thất thoát. |
| **Tăng trưởng** | Tỷ lệ chuyển đổi lead→KH; lượt chia sẻ MXH/giới thiệu. | Tăng dần ở MVP-2/3. |

---

## 7. GIẢ ĐỊNH & ĐIỂM CẦN LÀM RÕ TIẾP

- **Baseline đo lường:** cần thu thập số liệu vận hành thực tế khi triển khai MVP-1 để định lượng GAP và đánh giá hiệu quả.
- **Quy mô:** số HLV/club, số khách hàng và tần suất sử dụng thực tế còn để mở.
- **MVP-3 (app khách)** là khoản đầu tư mở rộng phạm vi lớn nhất — cần đánh giá nguồn lực/chi phí kỹ ở giai đoạn lập kế hoạch chi tiết.

---

## 8. BƯỚC TIẾP THEO

To-be report này là đầu vào cho **phân tích GAP** (đối chiếu As-Is v1.1 ↔ To-be v1.0 để xác định khoảng cách chức năng, dữ liệu, trải nghiệm) và **khuyến nghị To-do** (danh sách hạng mục hành động theo lớp MVP).
