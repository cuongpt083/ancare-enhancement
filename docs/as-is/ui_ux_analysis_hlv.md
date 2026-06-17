# Báo cáo Phân tích UI/UX hiện tại của ứng dụng AnCare (HLV)

Báo cáo này tổng hợp thiết kế UI/UX hiện tại của AnCare (dành cho Huấn luyện viên - HLV) được duyệt và chụp ảnh tự động dưới chế độ responsive iPhone 14 Pro Max (430 x 932 px). Báo cáo cung cấp đánh giá nhanh về hiện trạng thiết kế và đưa ra các điểm gợi ý cải tiến nhằm phục vụ quá trình brainstorm thiết kế UI/UX mới.

---

## Danh sách 13 màn hình tính năng đã capture

Dưới đây là chuỗi ảnh chụp màn hình theo trình tự thao tác của người dùng. Mỗi màn hình đều đi kèm hình ảnh thực tế và các nhận xét chuyên môn về UI/UX.

### 1. Màn hình Chào mừng (Welcome)
- **Tên file:** [01_welcome.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/01_welcome.png)
- **Hình ảnh:**
  ![Màn hình Chào mừng](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/01_welcome.png)
- **Nhận xét UI/UX:**
  - **Aesthetics:** Sử dụng tông màu xanh lá đậm `#1E3322` mang cảm giác thiên nhiên, sức khỏe. Layout tối giản, có hiệu ứng gradient mờ ở nền khá hiện đại.
  - **Bố cục:** Logo nằm giữa, tiêu đề lớn màu trắng và nút "Bắt đầu ngay" bo góc tròn đầy (pill-shaped) nằm nổi bật ở chân trang.
  - **Hạn chế:** Khoảng trống phía dưới khá nhiều, chữ giới thiệu ("Hành trình chăm sóc...") có độ tương phản hơi thấp do dùng màu trắng mờ trên nền xanh lá sáng dần.

---

### 2. Màn hình Đăng nhập (Login)
- **Tên file:** [02_login.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/02_login.png)
- **Hình ảnh:**
  ![Màn hình Đăng nhập](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/02_login.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Sử dụng lại tông nền của màn chào mừng nhưng thu nhỏ logo lên góc trên để chừa không gian cho form.
  - **Form:** 2 ô nhập liệu "Số điện thoại/Email" và "Mật khẩu" với placeholder xám nhạt rõ ràng.
  - **Hạn chế:** Nút "Đăng nhập" là phần tử `div` không có thuộc tính `role="button"` hay tag `<button>` chuẩn, có thể ảnh hưởng đến khả năng truy cập (accessibility). Các link như "Quên mật khẩu?" và "Đăng ký" xếp cạnh nhau nhưng phân bổ lề chưa tối ưu.

---

### 3. Màn hình Trang Chủ (Dashboard)
- **Tên file:** [03_dashboard.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/03_dashboard.png)
- **Hình ảnh:**
  ![Màn hình Trang Chủ](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/03_dashboard.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Hiển thị 3 chỉ số chính ở phần trên: Khách hàng, NPP, Doanh thu. Phía dưới là danh sách công việc cần làm hôm nay (ví dụ: "KH 02: Cập nhật chỉ số Tanita").
  - **Hạn chế:** Các thẻ số liệu (KPIs) hiển thị văn bản lồng ghép hơi dày đặc ("0 Khách hàng — NPP 0đ Doanh thu" chung một dòng lớn). Menu điều hướng dưới cùng (Bottom Tab bar) có các nhãn văn bản "Trang Chủ", "Team", "Chat", "HLV", "Hồ Sơ" kết hợp icon dạng ký tự đặc biệt (có thể bị lỗi font hoặc hiển thị không đồng nhất trên các thiết bị).

---

### 4. Chi tiết cập nhật chỉ số Tanita
- **Tên file:** [04_tanita_update.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/04_tanita_update.png)
- **Hình ảnh:**
  ![Chi tiết cập nhật chỉ số Tanita](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/04_tanita_update.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Hiển thị chi tiết hành trình/chỉ số sinh học của Khách hàng 02 (cân nặng, mỡ cơ thể, cơ xương, mỡ nội tạng...). Đây là màn hình thao tác lõi của HLV khi khách hàng đo máy Tanita tại Club.
  - **Hạn chế:** Thông tin xếp chồng theo hàng dọc khá dài, người dùng phải cuộn trang nhiều để xem hết. Giao diện form nhập số liệu Tanita cần được chia nhóm trực quan hơn thay vì một danh sách dài các ô số đơn điệu.

---

### 5. Màn hình Danh sách Nhóm (Team)
- **Tên file:** [05_team.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/05_team.png)
- **Hình ảnh:**
  ![Màn hình Danh sách Nhóm](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/05_team.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Quản lý danh sách hội viên do HLV này phụ trách. Có ô tìm kiếm nhanh và nút nổi bật "Mời KH mới" (màu xanh lá đậm).
  - **Hạn chế:** Giao diện danh sách khách hàng hiển thị thông tin ở dạng thẻ thô (tên, số điện thoại, ngày cập nhật, trạng thái tư vấn). Phông chữ hiển thị nhỏ và độ giãn cách chưa tối ưu.

---

### 6. Mời khách hàng mới (Invite Client)
- **Tên file:** [06_moi_kh_moi.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/06_moi_kh_moi.png)
- **Hình ảnh:**
  ![Mời khách hàng mới](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/06_moi_kh_moi.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Biểu mẫu điền thông tin để mời khách hàng mới tham gia hệ sinh thái AnCare (qua email hoặc số điện thoại).
  - **Hạn chế:** Form nhập liệu đơn giản nhưng các trường thông tin không có validation trực quan ngay khi gõ. Màu sắc của các nút nhấn ("Lưu", "Hủy") thiếu sự phân cấp chính phụ rõ rệt.

---

### 7. Màn hình Trò chuyện (Chat list)
- **Tên file:** [07_chat.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/07_chat.png)
- **Hình ảnh:**
  ![Màn hình Trò chuyện](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/07_chat.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Chia làm 2 phần chính phía trên: "Cộng đồng" (Group chat) và "Trợ lý AI" (AI chatbot). Bên dưới là danh sách khách hàng để chat trực tiếp.
  - **Hạn chế:** Các thẻ "Cộng đồng" và "Trợ lý AI" chiếm dụng diện tích khá lớn ở nửa trên màn hình, khiến phần danh sách chat cá nhân bị đẩy xuống sâu. Icon và văn bản hiển thị trong thẻ hơi rời rạc.

---

### 8. Chat với Trợ lý AI (AI Assistant Chat)
- **Tên file:** [08_chat_tro_ly_ai.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/08_chat_tro_ly_ai.png)
- **Hình ảnh:**
  ![Chat với Trợ lý AI](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/08_chat_tro_ly_ai.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Hộp thoại hỏi đáp thông tin dinh dưỡng, gợi ý thực đơn từ trợ lý AI của AnCare.
  - **Hạn chế:** Giao diện bong bóng chat (chat bubbles) có màu sắc tương đối đơn điệu. Thanh nhập liệu tin nhắn sát viền dưới, chưa tối ưu khoảng đệm (padding) cho bàn phím ảo trên iOS.

---

### 9. Chat Cộng đồng (Community Chat Room)
- **Tên file:** [09_chat_cong_dong.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/09_chat_cong_dong.png)
- **Hình ảnh:**
  ![Chat Cộng đồng](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/09_chat_cong_dong.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Phòng chat chung của Club dành cho tất cả hội viên và HLV.
  - **Hạn chế:** Không gian trò chuyện đơn giản, thiếu các tính năng tương tác nhanh (react tin nhắn, gửi hình ảnh/file đính kèm mượt mà).

---

### 10. Màn hình HLV (Consultant Hub)
- **Tên file:** [10_hlv.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/10_hlv.png)
- **Hình ảnh:**
  ![Màn hình HLV](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/10_hlv.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Tab chuyên sâu dành cho HLV để theo dõi trạng thái tư vấn của hội viên (Đã tư vấn / Chưa tư vấn).
  - **Hạn chế:** Giao diện rất giống màn hình Team dẫn đến sự trùng lặp trải nghiệm (HLV dễ nhầm lẫn giữa 2 tab HLV và Team vì cả hai đều hiển thị danh sách khách hàng). Cần tái thiết kế để phân biệt rõ vai trò quản lý thành viên (Team) và hoạt động nghiệp vụ tư vấn (HLV).

---

### 11. Chi tiết Khách hàng (Client Detail / Timeline)
- **Tên file:** [11_chi_tiet_khach_hang.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/11_chi_tiet_khach_hang.png)
- **Hình ảnh:**
  ![Chi tiết Khách hàng](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/11_chi_tiet_khach_hang.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Hồ sơ sức khỏe của khách hàng cụ thể (ở đây là KH 02), hiển thị lịch sử đo chỉ số, nhật ký ăn uống và lộ trình tư vấn.
  - **Hạn chế:** Thiết kế bảng số liệu thô sơ. Chưa có các biểu đồ trực quan (line chart, bar chart) biểu diễn xu hướng tăng/giảm cân nặng hoặc mỡ thừa của khách hàng theo thời gian, khiến HLV khó thuyết phục khách hàng về hiệu quả.

---

### 12. Màn hình Hồ Sơ cá nhân (Profile)
- **Tên file:** [12_profile.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/12_profile.png)
- **Hình ảnh:**
  ![Màn hình Hồ Sơ cá nhân](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/12_profile.png)
- **Nhận xét UI/UX:**
  - **Bố cục:** Thông tin cá nhân HLV, câu lạc bộ đang quản lý, các tuỳ chọn quản trị, nút "Tạo gói" và nút "Đăng xuất" (màu đỏ `#C44040` nổi bật ở cuối).
  - **Hạn chế:** Nút "Tạo gói" (Create package) đặt ở đây chưa thực sự hợp lý về mặt luồng tác vụ (user flow). Thông thường, tạo gói dinh dưỡng nên nằm trong phần quản lý bán hàng/POS hoặc trong hồ sơ khách hàng thay vì nằm trong Profile cá nhân của HLV.

---

### 13. Màn hình Tạo gói dinh dưỡng (Create Package)
- **Tên file:** [13_tao_goi.png](file:///Users/cuongpt/Workspaces/ancare-enhancement/screenshots/13_tao_goi.png)
- **Hình ảnh:**
  ![Màn hình Tạo gói dinh dưỡng](/Users/cuongpt/Workspaces/ancare-enhancement/screenshots/13_tao_goi.png)
- **Nhận xét UI/UX:**
  - **Tính năng:** Thiết lập gói dịch vụ mới cho Club (tên gói, giá tiền, số buổi, các sản phẩm đi kèm như F1, Trà...).
  - **Hạn chế:** Các trường nhập thông số và chọn sản phẩm đính kèm hiển thị dạng danh sách cuộn dọc đơn thuần. Trải nghiệm chọn sản phẩm từ kho hoặc danh mục chưa mượt mà, thiếu hình ảnh sản phẩm minh họa trực quan.

---

## Định hướng Brainstorm Thiết kế Mới (To-Be UX/UI)

Dựa trên các phân tích trên và định hướng dự án "AnCare Enhancement", dưới đây là một số gợi ý cốt lõi để nâng cấp thiết kế UI/UX:

1. **Đồng bộ Hệ thống Thiết kế (Design System):**
   - Thay thế các biểu tượng font ký tự đặc biệt lỗi thời ở Bottom Tab Bar bằng bộ icon SVG hiện đại (ví dụ dùng Lucide Icons hoặc Heroicons).
   - Tối ưu bảng màu: Giữ lại màu xanh lá đặc trưng nhưng phối hợp với các gam màu trung tính tinh tế hơn để tăng độ tương phản và cảm giác premium.
   - Thống nhất phông chữ hiển thị, tối ưu cỡ chữ lớn hơn trên màn hình di động nhằm giúp các HLV lớn tuổi dễ dàng đọc chỉ số.

2. **Cải tiến Trực quan hóa Dữ liệu (Data Visualization):**
   - *Màn hình Chi tiết Khách hàng:* Thay thế bảng số liệu Tanita khô khan bằng biểu đồ tương tác biểu diễn tiến trình sức khỏe (Cân nặng/Mỡ giảm đi, cơ bắp tăng lên). Đây là tính năng then chốt giúp tăng động lực cho Khách hàng và hỗ trợ HLV tư vấn hiệu quả hơn.

3. **Tái cấu trúc Luồng Người dùng (Information Architecture):**
   - *Phân biệt rõ tab Team và tab HLV:* Tab Team nên tập trung vào thông tin nhân khẩu học, quản lý gói dịch vụ và POS bán hàng. Tab HLV nên tập trung vào hoạt động tư vấn, chấm điểm lộ trình, nhắc nhở nhiệm vụ hàng ngày.
   - *Di chuyển tính năng "Tạo gói":* Nên đưa tính năng này vào phần cấu hình danh mục sản phẩm hoặc POS thay vì để trong tab Hồ Sơ cá nhân.

4. **Trải nghiệm Nhập liệu Thao tác nhanh:**
   - Hỗ trợ quét mã vạch sản phẩm bằng camera điện thoại khi xuất kho hoặc thanh toán POS.
   - Thiết kế lại biểu mẫu nhập chỉ số Tanita dạng bàn phím số lớn (Numpad) hỗ trợ nhập nhanh liên tiếp, giảm thiểu số lần nhấn và cuộn trang.
