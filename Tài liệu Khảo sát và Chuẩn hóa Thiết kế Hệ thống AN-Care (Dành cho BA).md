# **TÀI LIỆU KHẢO SÁT VÀ CHUẨN HÓA THIẾT KẾ HỆ THỐNG ỨNG DỤNG AN-CARE**

**Đối tượng sử dụng tài liệu:** Business Analyst (BA), Đội ngũ Phát triển Phần mềm.  
**Mục tiêu:** Chuẩn hóa hiện trạng cấu trúc thông tin, kiến trúc chức năng và hành trình người dùng (User Journey) của ứng dụng AN-Care phục vụ vai trò Huấn luyện viên dinh dưỡng (Health Coach) và Nhà vận hành nhóm dinh dưỡng.

## **1\. TỔNG QUAN HỆ THỐNG**

Ứng dụng AN-Care hoạt động như một hệ thống quản lý quan hệ khách hàng (CRM) kết hợp theo dõi sức khỏe chuyên biệt. Hệ thống xoay quanh việc tối ưu hóa quy trình chăm sóc sức khỏe chủ động, kết hợp giữa sản phẩm bổ sung Herbalife và các mô hình vận hành như Nhóm dinh dưỡng (Nutrition Club) hoặc Nhóm dinh dưỡng vận động (Fit Nutrition Club).

## **2\. KIẾN TRÚC THÔNG TIN & CẤU TRÚC PHÂN HỆ (SYSTEM DESIGN)**

Hệ thống được tổ chức thành 5 phân hệ chính tương ứng với cấu trúc thanh điều hướng điều hướng (Tab Navigation):

| Phân hệ (Tab) | Chức năng thành phần | Dữ liệu & Chỉ số quản lý |
| :---- | :---- | :---- |
| **Trang Chủ (Dashboard)** | Hiển thị tổng quan hoạt động trong ngày, danh sách công việc cần làm (To-do) và cảnh báo hệ thống. | Số lượng khách hàng, số lượng nhà phân phối (NPP), doanh thu (0đ), danh sách task hôm nay (KH cần follow up, KH chưa check-in), log hoạt động gần đây. |
| **Team (Quản lý KH hiện tại)** | Giám sát, theo dõi tiến độ và quản lý chỉ số chi tiết của nhóm khách hàng đang tham gia lộ trình. | Trạng thái KH (Tất cả, Đang hoạt động, Có nguy cơ/At risk), Chuỗi ngày tham gia, chỉ số BMI, mục tiêu Calo, chỉ số cơ thể từ cân Tanita, lộ trình thực đơn 30 ngày. |
| **Chat (Giao tiếp)** | Kênh tương tác trực tiếp, giao tiếp nhóm cộng đồng và hỗ trợ thông minh từ AI. | Kênh Cộng đồng (nhận thông báo tự động), Trợ lý AI (tư vấn dinh dưỡng), Danh sách hội thoại cá nhân với khách hàng (Chưa có cuộc trò chuyện nào). |
| **HLV (Quản lý KH tiềm năng)** | Phân phễu khách hàng tiềm năng, thực hiện khảo sát đầu vào và tự động tạo bài tư vấn cá nhân hóa. | Phân loại (KH tiềm năng, KH của tôi), Form tạo lead mới (Họ tên, SĐT, Ngày sinh, Giới tính, Chiều cao), Bảng câu hỏi khảo sát (nhóm tính cách DISC, thói quen), Bài tư vấn cá nhân hóa (Phân tích trọng điểm, Gợi ý dinh dưỡng & vận động). |
| **Hồ Sơ (Profile & Settings)** | Quản lý thông tin định danh của Huấn luyện viên, cấu hình ứng dụng và các gói dịch vụ cung cấp. | Họ tên HLV, SĐT, Email, Mã NPP, Mã giới thiệu, Gói chăm sóc cá nhân (Đang hoàn thiện), cấu hình quyền riêng tư (Chia sẻ dữ liệu cho AI Coach), tùy chỉnh cỡ chữ. |

## **3\. CHI TIẾT CÁC THỰC THỂ DỮ LIỆU CỐT LÕI (DATA ENTITIES)**

### **3.1. Chỉ số cơ thể từ cân Tanita (Body Composition Metrics)**

Dữ liệu trắc lượng sinh học cốt lõi dùng để theo dõi tiến độ của khách hàng bao gồm:

* Cân nặng (C.Nặng \- kg)  
* Tỷ lệ mỡ (%) (Mỡ \- %)  
* Khối lượng cơ (Cơ \- kg)  
* Tỷ lệ nước trong cơ thể (Nước \- %)  
* Chỉ số mỡ nội tạng (Mỡ NT)  
* Khối lượng xương (Xương)  
* Tuổi sinh học (Tuổi SH)  
* Tỷ lệ trao đổi chất cơ bản (BMR)

### **3.2. Cấu trúc lộ trình 30 ngày (30-Day Program Metrics)**

* **Chỉ số mục tiêu tiêu chuẩn:** Calo mục tiêu tiêu thụ (CSKD \- kcal/ngày), Delta áp dụng (kcal), Lượng nước tiêu thụ mục tiêu (ml/ngày), Thời gian giấc ngủ (h), Nhóm tính cách DISC.  
* **Biểu đồ tiến trình cân nặng:** Theo dõi biến thiên từ Cân nặng bắt đầu đến Cân nặng kết thúc, tính toán mức chênh lệch mục tiêu.  
* **Thực đơn hàng ngày chuẩn hóa (Meal Plan):** Chia nhỏ thành 5 bữa (Bữa sáng, Phụ sáng, Bữa trưa, Phụ 16h, Bữa tối) kèm định lượng Calo chi tiết và tích hợp công thức sử dụng sản phẩm bổ sung Herbalife (Ví dụ: Shake F1, bột Protein PPP, Niteworks, Lô hội...).  
* **Hướng dẫn hành vi:** Danh mục thực phẩm "Nên ăn" (Rau xanh luộc, ức gà, cá tươi...), "Hạn chế" (Đồ chiên rán, nước ngọt, bia rượu...) và các lưu ý thay thế thực phẩm (Thịt đỏ, trứng, nước & thải độc...).

## **4\. MÔ HÌNH HÀNH TRÌNH NGƯỜI DÙNG (USER JOURNEYS)**

BA cần lưu ý 3 luồng hành trình cốt lõi của Huấn luyện viên khi tương tác với hệ thống:

### **Luồng 1: Vận hành & Giám sát hàng ngày (Daily Operation Loop)**

1. Huấn luyện viên đăng nhập, truy cập **Trang Chủ** để tiếp nhận bức tranh tổng thể về hiệu suất kinh doanh (Khách hàng, NPP, Doanh thu).  
2. Kiểm tra phân hệ **Hệ thống Alert** để nhận biết các thông báo tự động (Ví dụ: Báo cáo hàng ngày đã sẵn sàng).  
3. Kiểm tra danh sách tác vụ tại phân hệ **Hôm nay** để lên kế hoạch tương tác cá nhân (Follow up khách hàng mục tiêu, xử lý trường hợp chưa check-in).  
4. Rà soát lịch sử cập nhật tại mục **Hoạt động gần đây** để nắm bắt biến động chỉ số của toàn team.

### **Luồng 2: Phát triển Khách hàng tiềm năng & Thuyết phục giải pháp (Lead Generation & Conversion)**

1. Huấn luyện viên truy cập tab **HLV**, chọn tính năng Thêm mới (nút \+) tại danh sách "KH tiềm năng".  
2. Nhập các trường dữ liệu định danh và trắc lượng cơ bản (Họ tên, SĐT, Ngày sinh, Giới tính, Chiều cao).  
3. Phối hợp cùng khách hàng hoàn thành **Bảng câu hỏi khảo sát** nhằm thu thập thói quen sinh hoạt và xác định nhóm tính cách DISC đầu vào.  
4. Hệ thống xử lý dữ liệu khảo sát, tự động xuất ra **Bài tư vấn cá nhân hóa** bao gồm Phân tích trọng điểm (so sánh chỉ số thực tế với tiêu chuẩn WHO) và Gợi ý lộ trình dinh dưỡng. HLV sử dụng giao diện này làm tài liệu thuyết phục khách hàng chuyển đổi sang gói chính thức.

### **Luồng 3: Quản lý lộ trình Chăm sóc chủ động (Customer Retention & Tracking)**

1. Huấn luyện viên truy cập tab **Team** để quản lý tập trung danh sách khách hàng chính thức.  
2. Sử dụng bộ lọc trạng thái để định vị nhanh nhóm khách hàng **Có nguy cơ (At risk)** – những người có số ngày bỏ lỡ cập nhật cao (Ví dụ: missed 40 days) – để tiến hành kích hoạt lại.  
3. Chọn một hồ sơ khách hàng cụ thể để xem chi tiết tiến độ. Rà soát bảng chỉ số cơ thể Tanita cập nhật mới nhất để đánh giá hiệu quả chuyển hóa sinh học.  
4. Truy cập mục **Lộ trình 30 ngày chi tiết** để kiểm soát việc tuân thủ thực đơn (Meal Plan), hướng dẫn khách hàng cách sử dụng đúng các sản phẩm Herbalife đi kèm theo từng khung giờ và theo dõi biểu đồ xu hướng cân nặng để điều chỉnh kịp thời.