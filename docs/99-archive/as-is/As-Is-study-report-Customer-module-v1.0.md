# **TÀI LIỆU CHUẨN HÓA THIẾT KẾ HỆ THỐNG AN-CARE**

## **(PHÂN HỆ KHÁCH HÀNG \- CUSTOMER APP)**

**Đối tượng sử dụng:** Business Analyst (BA), PO/PM, Đội ngũ Phát triển Phần mềm.  
**Mục tiêu:** Sơ đồ hóa kiến trúc thông tin và phân tích các luồng hành trình trải nghiệm của Khách hàng (End-user) trên ứng dụng AN-Care dựa trên phương pháp Reverse Engineering từ màn hình thực tế.

## ---

**1\. KIẾN TRÚC THÔNG TIN (INFORMATION ARCHITECTURE)**

Ứng dụng Khách hàng được thiết kế với thanh điều hướng 4 Tab chính, tập trung vào việc hiển thị lộ trình cá nhân hóa và các tác vụ check-in hàng ngày.

| Phân hệ (Tab) | Thành phần UI & Chức năng chính |
| :---- | :---- |
| **Trang Chủ (Home)** | **Header:** Lời chào cá nhân hóa, Chuông thông báo, Nhãn hạng thành viên (Cơ bản), Trạng thái gói dịch vụ (Cảnh báo hết hạn). **Dashboard Mục tiêu:** Tiến độ giảm/tăng cân (Cân nặng hiện tại \-\> Mục tiêu), % hoàn thành, số kg đã giảm/còn lại, chỉ số mỡ/cơ thay đổi, chuỗi ngày liên tiếp (streak). **Chỉ số cơ thể:** Hiển thị đồng bộ dữ liệu trắc lượng (Cân nặng, Mỡ, Cơ, Nước, Mỡ nội tạng, Xương, Tuổi SH, BMR). **Thực đơn hôm nay (Checklist):** Lộ trình bữa ăn chi tiết (Sáng, Trưa, Phụ, Tối) kèm mức Calo định mức. Có tính năng tick hoàn thành và chụp ảnh bữa ăn. **Nhật ký sinh hoạt:** Nút thao tác nhanh cập nhật Nước uống, Giấc ngủ, Hoạt động thể chất. Thư viện ảnh cá nhân. **Báo cáo & Gợi ý:** Tóm tắt "Hôm nay nổi bật" (Điểm tốt / Cần cải thiện), Lời khuyên tự động (Coach gợi ý), Lịch sử cập nhật hệ thống. |
| **Lộ Trình (Journey)** | **Tiến độ tổng quan:** Ngày hiện tại trên tổng ngày (VD: Ngày 1/30), Tiến độ tuần (Tuần 1/5), Thanh progress bar %. **Chỉ tiêu trong ngày:** Tổng hợp nhanh KPI ngày (Mức Calo ăn, Lượng nước uống, Giờ ngủ, Số bài tập). **Phân tích:** Nhận xét dữ liệu ngày hôm trước (tự động phân tích). |
| **Chat (Giao tiếp)** | **Cộng đồng:** Kênh nhận thông báo chung hoặc sinh hoạt nhóm. **Direct Message:** Kênh chat 1-1 trực tiếp với Huấn luyện viên phụ trách (VD: Phạm Mi). Hỗ trợ gửi tin nhắn text, hình ảnh. |
| **Hồ Sơ (Profile)** | **Thông tin định danh:** Ảnh đại diện, Họ tên, Tuổi, Giới tính, Email, Số điện thoại. **Quản lý dịch vụ:** Trạng thái Gói chăm sóc (Active / Hết hạn). **Công cụ phụ trợ:** Nút truy cập nhanh "Báo cáo" và "Lịch sử lộ trình". Nút Đăng xuất. |

## **2\. CÁC LUỒNG HÀNH TRÌNH NGƯỜI DÙNG (USER JOURNEYS)**

### **Luồng 1: Tracking & Báo cáo sinh hoạt hàng ngày (Daily Check-in)**

*Mục đích: Khách hàng ghi nhận các hoạt động ăn uống, sinh hoạt để HLV và hệ thống theo dõi.*

1. **Tracking Thực đơn:** Khách hàng mở **Trang Chủ** \-\> Cuộn đến mục **Thực đơn hôm nay** \-\> Xem định lượng bữa ăn (VD: Bữa trưa cần 600 kcal) \-\> Thực hiện bữa ăn \-\> Bấm vào icon **Camera** để chụp ảnh minh chứng hoặc bấm icon **Tick (Hoàn thành)**.  
2. **Tracking Sinh hoạt:** Tại mục **Hoạt động** \-\> Khách hàng thao tác tăng/giảm số **cốc nước** đã uống \-\> Bấm vào icon Edit ở **Giấc ngủ** \-\> Nhập số giờ ngủ (VD: 7 giờ 00 phút) \-\> Đánh giá chất lượng giấc ngủ (1-5 sao) \-\> Bấm **Lưu**.

**Business Rule (Ràng buộc hệ thống):** Nếu Khách hàng không có "Gói chăm sóc" hợp lệ (đã hết hạn), hệ thống sẽ chặn hành động ghi nhận dữ liệu (VD: Hiển thị lỗi "Không thể lưu giấc ngủ. Vui lòng thử lại" hoặc yêu cầu liên hệ HLV để gia hạn trước khi tiếp tục check-in/log bữa ăn).

### **Luồng 2: Xem tiến độ & Báo cáo sức khỏe (Progress Review)**

*Mục đích: Khách hàng tự theo dõi hiệu quả của quá trình thay đổi vóc dáng.*

1. **Dashboard nhanh:** Khách hàng xem biểu đồ tuyến tính tại thẻ **Mục tiêu giảm cân** ngay trên đầu Trang Chủ để biết khoảng cách tới đích.  
2. **Phân tích sâu:** Cuộn đến mục **Hôm nay nổi bật** \-\> Chọn **Xem chi tiết** \-\> Đọc "Báo cáo chi tiết".  
3. Hệ thống hiển thị báo cáo dưới dạng văn bản (text logic) bao gồm: Lời chào phân tích tổng quan \-\> Bóc tách **Điểm mạnh** (VD: Mỡ nội tạng tốt, lượng cơ bắp cao) \-\> Chỉ điểm **Cần cải thiện** (VD: Cân nặng dư thừa, tỷ lệ mỡ cao) \-\> Đưa ra **Đề xuất từ HLV** (Lượng nước cần uống, mức Calo tối đa, thực phẩm bổ sung cần thiết).

### **Luồng 3: Tương tác hỗ trợ (Support & Communication)**

*Mục đích: Kết nối khi có thắc mắc hoặc cần động lực.*

1. Khách hàng chuyển sang tab **Chat**.  
2. Chọn kênh **Huấn luyện viên cá nhân** (Hệ thống tự động liên kết tài khoản KH với HLV phụ trách).  
3. Gửi tin nhắn văn bản trao đổi thắc mắc về thực đơn, cách sử dụng sản phẩm hoặc yêu cầu gia hạn gói dịch vụ.