# **TÀI LIỆU CẬP NHẬT THIẾT KẾ HỆ THỐNG AN-CARE**

## **(BỔ SUNG QUY TRÌNH CHUYỂN ĐỔI & QUẢN LÝ KHÁCH HÀNG CHO HLV)**

**Đối tượng sử dụng:** Business Analyst (BA), PO/PM, Đội ngũ Phát triển Phần mềm.  
**Mục tiêu:** Bổ sung và làm rõ kiến trúc luồng dữ liệu liên quan đến việc tạo mới khách hàng tiềm năng, phân tích chỉ số, thiết lập tài khoản, và khởi tạo lộ trình 30 ngày dành cho Huấn luyện viên (Health Coach) dựa trên hiện trạng ứng dụng.

## ---

**1\. MỞ RỘNG KIẾN TRÚC CHỨC NĂNG (CRM & ONBOARDING)**

Dựa trên phân tích bổ sung, phân hệ Quản lý Khách hàng của HLV sở hữu một hệ thống CRM thu nhỏ với các chức năng chi tiết như sau:

| Nhóm Chức năng | Chi tiết tính năng (Features) |
| :---- | :---- |
| **1\. Thu thập dữ liệu đầu vào (Data Intake)** | Tạo hồ sơ định danh: Họ tên, SĐT, Ngày sinh, Giới tính, Chiều cao. Nhập liệu Trắc lượng sinh học (Tanita): Hỗ trợ nhập tay hoặc quét ảnh/OCR (Tính năng Chụp ảnh/Chọn ảnh) các chỉ số: Cân nặng, Tỷ lệ mỡ, Xương, Nước, Cơ, Vóc dáng, Tuổi sinh học, BMR, Mỡ nội tạng. |
| **2\. Phân tích & Khuyến nghị tự động** | Hệ thống xử lý (Processing): Khớp nối dữ liệu Tanita với Bảng tiêu chuẩn WHO và Asian-Pacific action points. Bản tư vấn (Consultation Report): Đánh giá từng chỉ số (Màu xanh: Tốt, Màu đỏ/cam: Xấu/Cảnh báo) kèm khối lượng mỡ/cơ cần giảm/tăng. |
| **3\. Quản lý Tài khoản Khách hàng (Provisioning)** | Cấp quyền truy cập (App Access): HLV chủ động tạo tài khoản cho KH qua Email và Mật khẩu mặc định (có thể đổi sau). Gắn Gói dịch vụ (Package Assignment): Liên kết tài khoản KH với một Gói chăm sóc cụ thể. |
| **4\. Thiết lập Lộ trình (Journey Builder)** | Tham số hóa lộ trình 30 ngày: Thiết lập cân nặng mục tiêu, hệ số thâm hụt Calo (Delta áp dụng, VD: \-400 kcal), số lượng bữa ăn trong ngày (4, 5, 6 bữa). Auto-generation: Hệ thống tự động tính toán tổng Calo mục tiêu/ngày, lượng nước, giờ ngủ và cấu trúc lại Thực đơn chi tiết. |
| **5\. Tác vụ Quản trị nâng cao (Action Menu)** | Quản lý vòng đời (Life-cycle): Chỉnh sửa thông tin, đặt lại mật khẩu, xóa tài khoản. Truy xuất báo cáo: Xuất lịch sử báo cáo AI, tạo báo cáo theo dải ngày tùy chỉnh (3 ngày, 5 ngày... hoặc custom range). |

## **2\. CHUẨN HÓA CÁC LUỒNG HÀNH TRÌNH BỔ SUNG (UPDATED USER JOURNEYS)**

### **Luồng 4: Onboarding & Cấp tài khoản cho Khách hàng mới (Lead to Active Conversion)**

*Mục đích: Chuyển đổi một người quan tâm thành khách hàng chính thức trên hệ thống.*

1. **Khởi tạo hồ sơ:** HLV vào tab **HLV** \-\> Thêm mới Khách hàng tiềm năng \-\> Nhập thông tin cơ bản.  
2. **Đo lường cơ thể:** HLV đưa khách hàng lên cân Tanita \-\> Chọn **Nhập chỉ số Tanita** \-\> Điền các thông số tương ứng \-\> Bấm **Tạo bản tư vấn**.  
3. **Tư vấn thuyết phục:** Hệ thống hiển thị trạng thái "Đang phân tích" \-\> Xuất ra **Bảng phân tích chỉ số** chi tiết. HLV dùng bảng này để giải thích tình trạng sức khỏe cho khách hàng.  
4. **Cấp tài khoản & Chuyển đổi:** Khách hàng đồng ý tham gia \-\> HLV bấm **Tạo tài khoản cho KH** \-\> Nhập Email, set Mật khẩu, chọn Gói dịch vụ \-\> Bấm **Xác nhận**.  
5. **Hoàn tất:** Khách hàng lúc này được chuyển sang danh sách **KH của tôi (Team)** với trạng thái *"Ready to convert" (Sẵn sàng kích hoạt)*.

### **Luồng 5: Khởi tạo và Cá nhân hóa Lộ trình 30 ngày (Journey Personalization)**

*Mục đích: Lên kế hoạch chi tiết về dinh dưỡng và sinh hoạt cho khách hàng trong 1 tháng tiếp theo.*

1. **Truy cập hồ sơ:** HLV mở danh sách **Team** \-\> Chọn khách hàng vừa cấp tài khoản.  
2. **Kích hoạt lộ trình:** Cuộn xuống phần Lộ trình 30 ngày \-\> Chọn **Tạo lộ trình 30 ngày**.  
3. **Cấu hình thông số:**  
   * Hệ thống gợi ý Cân nặng mục tiêu dựa trên thể trạng.  
   * HLV tinh chỉnh **Delta Calo** (mức thâm hụt/dư thừa mỗi ngày, VD: Giảm 400 kcal) bằng nút (+)/(-).  
   * HLV chọn thói quen ăn uống của khách: **Số bữa ăn mỗi ngày** (4, 5, hoặc 6 bữa).  
4. **Sinh dữ liệu:** Bấm **Tạo lộ trình**. Hệ thống chạy thuật toán (Phân tích sức khỏe \-\> Tính toán CSKD \+ Nước \+ Ngủ \-\> Xây dựng thực đơn 30 ngày).  
5. **Kiểm duyệt (Review):** Lộ trình hoàn tất. HLV xem lại chi tiết Thực đơn hàng ngày đã được sinh ra để đảm bảo phù hợp trước khi khách hàng bắt đầu thực hiện trên app của họ.

### **Luồng 6: Trích xuất Báo cáo tiến trình tùy chỉnh (Custom Progress Reporting)**

*Mục đích: Đánh giá hiệu quả sau một chu kỳ nhỏ (VD: 3 ngày, 1 tuần) thay vì đợi hết 30 ngày.*

1. Trong hồ sơ khách hàng, HLV bấm vào icon **Menu (3 dấu chấm)** ở góc trên bên phải.  
2. Chọn **Tạo báo cáo**.  
3. Pop-up xuất hiện cho phép chọn nhanh khoảng thời gian (3 ngày, 5 ngày, 2 tuần, 1 tháng) hoặc nhập **Từ ngày \- Đến ngày (Tùy chỉnh)**.  
4. Hệ thống tổng hợp dữ liệu log bữa ăn, cân nặng, sinh hoạt trong khoảng thời gian đó để HLV có cơ sở feedback cho khách hàng.