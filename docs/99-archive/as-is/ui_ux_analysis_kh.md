# Báo cáo Phân tích UI/UX hiện tại của ứng dụng AnCare (Phân hệ Khách hàng)

Tài liệu này phân tích hiện trạng thiết kế UI/UX của phân hệ dành cho **Khách hàng** trên ứng dụng AnCare, dựa trên 9 ảnh chụp màn hình được thực hiện tự động dưới chế độ responsive giả lập **iPhone 14 Pro Max** (430 x 932 px), đăng nhập bằng tài khoản thử nghiệm của khách hàng (username: `0989111112`, password: `1`).

---

## Danh sách 9 màn hình tính năng đã capture

Dưới đây là chuỗi ảnh chụp màn hình phân hệ khách hàng theo trình tự thao tác. Mỗi màn hình đều đi kèm hình ảnh thực tế và các nhận xét chuyên môn về UI/UX.

### 1. Màn hình Chào mừng (Welcome)
- **Tên file:** [01_welcome.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/01_welcome.png)
- **Hình ảnh:**
  ![Màn hình Chào mừng](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/01_welcome.png)
- **Nhận xét UI/UX:**
  - Đồng nhất với phân hệ HLV. Sử dụng tông màu xanh lá đậm `#1E3322` làm chủ đạo, logo nằm giữa và nút "Bắt đầu ngay" nổi bật phía dưới chân trang.

---

### 2. Màn hình Đăng nhập (Login)
- **Tên file:** [02_login.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/02_login.png)
- **Hình ảnh:**
  ![Màn hình Đăng nhập](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/02_login.png)
- **Nhận xét UI/UX:**
  - Ô nhập liệu số điện thoại/email và mật khẩu sử dụng placeholder màu xám nhạt rõ ràng.
  - Hạn chế: Nút "Đăng nhập" thiết kế dưới dạng thẻ `div` thay vì thẻ `<button>` chuẩn, không có thuộc tính hỗ trợ tiếp cận (accessibility).

---

### 3. Màn hình Trang Chủ Khách hàng (Client Dashboard)
- **Tên file:** [03_dashboard.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/03_dashboard.png)
- **Hình ảnh:**
  ![Màn hình Trang Chủ Khách hàng](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/03_dashboard.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Chứa thông tin tổng quan về sức khỏe của khách hàng hôm nay. Bao gồm các thẻ (cards): "Chỉ số cơ thể (16/06)" với các chỉ số đo từ máy Tanita (Cân nặng, Mỡ, Cơ, Nước, Mỡ nội tạng, Xương, Tuổi sinh học, BMR); các thẻ cập nhật sức khỏe như "Giấc ngủ", "Thêm ảnh vóc dáng".
  - **Hạn chế:** 
    - Thẻ "Chỉ số cơ thể" cố gắng nhồi nhét quá nhiều số liệu viết tắt và số liệu khô khan (ví dụ: `C.Nặng 60.0`, `Mỡ (%) 14.0`, `Cơ (kg) 52.0`, `Mỡ NT 6.0`...) vào một không gian nhỏ hẹp, gây rối mắt cho người dùng phổ thông.
    - Icon trong các thẻ (như hình trái tim, hình mặt trăng ngủ) là các ký tự đặc biệt, không đồng bộ về mặt đồ họa.
    - Phần "Hôm nay nổi bật" phân loại "Điểm tốt" và "Cần cải thiện" hiển thị dưới dạng văn bản thô sơ, chưa có biểu tượng hay màu sắc trực quan (như màu xanh cho điểm tốt, màu cam/đỏ cho điểm cần cải thiện) để người dùng dễ nhận diện nhanh.

---

### 4. Chi tiết Chỉ số cơ thể (Body Metrics Detail)
- **Tên file:** [04_chi_so_co_the.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/04_chi_so_co_the.png)
- **Hình ảnh:**
  ![Chi tiết Chỉ số cơ thể](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/04_chi_so_co_the.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Hiển thị chi tiết từng thông số cơ thể và biểu đồ tiến trình.
  - **Hạn chế:** Các biểu đồ hiển thị đơn điệu hoặc thiếu tính tương tác cao. Các chữ số giải thích thông số sinh học khá nhỏ, khó đọc đối với đối tượng khách hàng trung niên hoặc lớn tuổi.

---

### 5. Cập nhật Nhật ký Giấc ngủ (Sleep Logger)
- **Tên file:** [05_giac_ngu.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/05_giac_ngu.png)
- **Hình ảnh:**
  ![Cập nhật Nhật ký Giấc ngủ](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/05_giac_ngu.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Màn hình/modal giúp khách hàng ghi nhận thời gian ngủ và chất lượng giấc ngủ hàng ngày.
  - **Hạn chế:** Giao diện nhập liệu thiếu tính gamification hoặc tương tác trực quan. Thay vì các thanh trượt (slider) mượt mà hay các icon cảm xúc sinh động, giao diện hiện tại khá cơ bản và khô khan, khó tạo thói quen log dữ liệu hàng ngày cho khách hàng.

---

### 6. Thêm Ảnh Vóc Dáng (Progress Photo Upload)
- **Tên file:** [06_them_anh.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/06_them_anh.png)
- **Hình ảnh:**
  ![Thêm Ảnh Vóc Dáng](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/06_them_anh.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Nơi khách hàng tải lên hình ảnh so sánh vóc dáng (trước/sau) để theo dõi tiến trình giảm cân/tăng cơ.
  - **Hạn chế:** Giao diện tải ảnh thô sơ, chưa hỗ trợ các tính năng như hướng dẫn chụp ảnh đúng góc độ (overlay chụp ảnh) hoặc so sánh trực tiếp hai ảnh cạnh nhau (side-by-side comparison slider).

---

### 7. Màn hình Lộ Trình (Client Journey / Program Timeline)
- **Tên file:** [07_lo_trinh.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/07_lo_trinh.png)
- **Hình ảnh:**
  ![Màn hình Lộ Trình](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/07_lo_trinh.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Hiển thị chương trình dinh dưỡng khách hàng đang tham gia, tiến trình thực hiện và lịch sử cột mốc. Có nút "Liên hệ HLV" nổi bật ở phía trên.
  - **Hạn chế:** Trình bày lộ trình theo dạng văn bản tuần tự thô sơ, thiếu tính trực quan của một "hành trình cuộc sống" (timeline/gamified road map). Khách hàng khó nhìn thấy các mốc thành tựu (milestones) hoặc phần thưởng ảo (badges) để có động lực tiếp tục.

---

### 8. Màn hình Trò chuyện Q&A (Customer Q&A Chat)
- **Tên file:** [08_chat.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/08_chat.png)
- **Hình ảnh:**
  ![Màn hình Trò chuyện Q&A](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/08_chat.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Cho phép khách hàng nhắn tin trực tiếp với HLV cá nhân ("Phạm Thanh Cường") hoặc tham gia phòng chat "Cộng đồng" của câu lạc bộ.
  - **Hạn chế:** Tab chat của khách hàng dùng URL `/qna` nhưng nhãn tab vẫn ghi là "Chat", có thể gây nhầm lẫn trong kiến trúc thông tin nội bộ. Giao diện danh sách chat hiển thị khá đơn điệu, các avatar người dùng nhỏ và độ giãn cách dòng chưa tối ưu.

---

### 9. Màn hình Hồ Sơ cá nhân (Customer Profile)
- **Tên file:** [09_profile.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/09_profile.png)
- **Hình ảnh:**
  ![Màn hình Hồ Sơ cá nhân](/Users/cuongpt/Workspaces/ancare-enhancement/docs/as-is/screenshots-kh/09_profile.png)
- **Nhận xét UI/UX:**
  - **Nhận xét đặc biệt:** Khi chuyển sang tab Hồ Sơ (`/profile`), giao diện hiển thị lại các thẻ chỉ số cơ thể, giấc ngủ, thêm ảnh tương tự như Trang Chủ. Điều này cho thấy sự trùng lặp nghiêm trọng về mặt nội dung giữa tab Trang Chủ và tab Hồ Sơ.
  - **Hạn chế:** Tab Hồ Sơ cá nhân của khách hàng nên tập trung vào thông tin tài khoản, cài đặt thông báo, lịch sử giao dịch/gói dịch vụ, quản lý liên kết với HLV. Việc lặp lại toàn bộ các thẻ hoạt động sức khoẻ của trang chủ tại đây làm loãng trải nghiệm người dùng và gây rối rắm trong cấu trúc điều hướng.

---

## Tóm tắt Điểm Đau (Pain Points) và Gợi ý Cải tiến cho Phân hệ Khách hàng

1. **Sự trùng lặp Layout (Trang Chủ vs Hồ Sơ):**
   - *Điểm đau:* Trang chủ và trang Hồ Sơ cá nhân của khách hàng gần như lặp lại thông tin của nhau.
   - *Cải tiến:* Thiết kế lại trang Hồ Sơ tập trung vào thông tin hội viên, gói dịch vụ đã mua (số buổi còn lại, hạn sử dụng), lịch sử quét mã check-in tại câu lạc bộ và cài đặt tài khoản.

2. **Trực quan hoá Chỉ số sức khoẻ (Health Data Visualization):**
   - *Điểm đau:* Bảng chỉ số cơ thể hiển thị quá nhiều ký tự viết tắt chuyên môn khô khan khiến khách hàng khó hiểu ý nghĩa sức khoẻ thực tế của họ.
   - *Cải tiến:* Chuyển đổi các số liệu thành các vòng tròn tiến trình (như Apple Health/Google Fit) hoặc các thanh đo mức độ (Dưới trung bình / Bình thường / Cao) kèm màu sắc trực quan (Xanh, Vàng, Đỏ). Cung cấp giải thích ngắn gọn, dễ hiểu về các chỉ số khi khách hàng chạm vào (ví dụ: "Mỡ nội tạng của bạn ở mức 6 - là mức an toàn").

3. **Luồng Game hóa và Giữ chân (Gamification & Retention):**
   - *Điểm đau:* Các nhiệm vụ hàng ngày như cập nhật giấc ngủ, uống nước, thêm ảnh vóc dáng đang trình bày dưới dạng danh sách nút bấm thô sơ, chưa tạo được hứng thú.
   - *Cải tiến:* Xây dựng trải nghiệm dạng "Nhiệm vụ hàng ngày" sinh động. Thêm phần thưởng điểm tích lũy, huy hiệu thành tích (Ví dụ: "7 ngày uống đủ nước", "Giảm 1% mỡ cơ thể") để kích thích khách hàng sử dụng app mỗi ngày.

4. **Trực quan hóa Lộ trình (Client Timeline UX):**
   - *Điểm đau:* Lộ trình dinh dưỡng hiển thị dạng text thô, thiếu tính liên tục và hấp dẫn.
   - *Cải tiến:* Sử dụng thiết kế dạng bản đồ hành trình (journey map) tuyến tính với các điểm mốc (milestones) rõ ràng, giúp khách hàng thấy rõ mình đã đi được bao xa và mục tiêu tiếp theo là gì.
