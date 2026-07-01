# Tài liệu Thiết kế Hệ thống (System Design Document)
## Tính năng: Cỏ Ba Lá Sức Khỏe (Health Clover) - Ứng dụng Huawei Sức Khỏe

---

## 1. Tổng quan tính năng (Feature Overview)
Tính năng **"Cỏ ba lá sức khỏe"** là một trung tâm quản lý và theo dõi lối sống lành mạnh của người dùng dựa trên việc hoàn thành các nhiệm vụ cốt lõi hàng ngày (như Thức dậy, Uống nước, Vận động, Ngủ, Đo cân nặng, Hít thở, Tâm trạng). 

Mục tiêu UX cốt lõi là sử dụng đồ họa trực quan hình **Cỏ ba lá 3 cánh** (mỗi cánh đại diện cho một nhóm chỉ số chính: Ngủ/Thức dậy, Tập luyện/Vận động, Tâm trạng/Hành vi) kết hợp với các hiệu ứng chuyển cảnh mượt mà để khuyến khích người dùng duy trì thói quen tốt.

---

## 2. Thiết kế Giao diện Người dùng (UI Components)

### 2.1. Thanh điều hướng thời gian (Time Navigation Bar)
* **Vị trí:** Phía trên cùng của giao diện tính năng.
* **Thành phần:** * Dòng chữ hiển thị thứ và ngày tháng hiện tại (Ví dụ: *Thứ năm, 18 tháng 6, 2026*).
    * Hàng ngang chứa các biểu tượng Cỏ ba lá thu nhỏ đại diện cho các ngày trong tuần (CN, T2, T3, T4, T5, T6, T7).
* **Trạng thái hiển thị:**
    * Ngày hiện tại được highlight bằng màu nền đỏ/cam ở ký hiệu thứ (Ví dụ: **T5**).
    * Các biểu tượng cỏ ba lá thu nhỏ sẽ tự động lấp đầy màu sắc tương ứng với tiến độ hoàn thành của ngày đó trong quá khứ.

### 2.2. Khu vực Đồ họa Trung tâm: Cỏ Ba Lá Tiến Trình (Central Clover Widget)
* **Hình dáng:** Cấu trúc hình cỏ ba lá gồm 3 cánh lớn lồng vào nhau, tạo thành một vòng tròn đồng tâm ở giữa.
    * **Cánh phía trên:** Đại diện cho hoạt động thể chất / Tập luyện (Biểu tượng người chạy bộ). Màu sắc chủ đạo: Cam/Vàng.
    * **Cánh phía dưới bên trái:** Đại diện cho Giấc ngủ / Nghỉ ngơi (Biểu tượng mặt trăng). Màu sắc chủ đạo: Tím.
    * **Cánh phía dưới bên phải:** Đại diện cho Trạng thái tinh thần / Hít thở / Tâm trạng (Biểu tượng mặt cười). Màu sắc chủ đạo: Xanh lục/Xanh dương.
* **Bảng thông số nhanh (Quick Stats Panel):** Nằm bên phải cỏ ba lá trung tâm, hiển thị trạng thái tóm tắt:
    * *Thức dậy vào:* `--` hoặc giờ cụ thể (Ví dụ: *05:20 AM*).
    * *Số bước:* Hiển thị số bước hiện tại (Ví dụ: *0 bước*, *1496 bước*).
    * *Tâm trạng / Bài tập hít thở:* Lối tắt hoặc trạng thái.

### 2.3. Danh sách Nhiệm vụ Hàng ngày (Daily Task List)
Nằm phía dưới khu vực trung tâm, hiển thị dưới dạng các thẻ (Cards) danh sách có thể cuộn dọc (Scroll view). Mỗi thẻ bao gồm:
* **Biểu tượng (Icon):** Hình ảnh đại diện cho nhiệm vụ (Mặt trăng cho thức dậy, Ly nước cho uống nước, Cân cho đo cân nặng, v.v.).
* **Tiêu đề (Title):** Tên nhiệm vụ (*Thức dậy*, *Uống nước*, *Đo cân nặng*, *Hít thở*, *Hoạt động*, *Số bước*, *Ngủ*).
* **Tiến độ/Mục tiêu (Progress/Goal):** Hiển thị dưới dạng `Đã đạt được / Mục tiêu` (Ví dụ: *0,25/1,5 L*, *0/30 phút*, *0/10.000 bước*).
* **Nút Thao tác nhanh (Quick Action):** Nút tròn hoặc vùng chạm để ghi nhận nhanh kết quả (Ví dụ: Nút chấm tròn để bấm hoàn thành).
* **Rìa bên trái màn hình:** Một đuờng kẻ dọc nét đứt có điểm trên cùng là biểu tượng Măt trời mọc, điểm dứơi cùng là biểu tượng Mặt trăng nằm ngủ, hai biểu tượng này đại diện cho khoảng thời gian trong ngày từ lúc thức dậy tới lúc đi ngủ.

### 2.4. Các Bottom Sheet / Giao diện Nhập liệu (Input Sheets)
Khi người dùng tương tác với một thẻ nhiệm vụ, một cửa sổ dạng Bottom Sheet hoặc màn hình lớp phủ (Overlay) sẽ xuất hiện từ dưới lên.
* **Thẻ "Thức dậy":** Hiển thị hình ảnh minh họa cô gái thức dậy đón bình minh. Nút bấm nổi bật: "NHẬP THỦ CÔNG".
* **Trình chọn giờ (Time Picker):** Giao diện cuộn (Wheel picker) để chọn Giờ và Phút cho thời gian ngủ/thức dậy.
* **Thẻ "Uống nước":** Hiển thị hình ảnh minh họa người ngồi uống nước trên sa mạc. Hàng biểu tượng các ly nước đại diện cho lượng nước nạp vào. Nút bấm: "UỐNG NƯỚC" để cộng dồn (Mỗi lần bấm thêm +250ml).

---

## 3. Quy trình Tương tác & Trải nghiệm Người dùng (Interaction & UX)

### 3.1. Kịch bản 1: Cập nhật thời gian thức dậy thủ công
1.  **Chạm (Tap):** Người dùng ấn vào thẻ nhiệm vụ **"Thức dậy"**.
2.  **Phản hồi UI:** Một Bottom Sheet xuất hiện từ dưới lên hiển thị trạng thái "Đã hoàn thành 20 ngày".
3.  **Hành động:** Người dùng chọn **"Nhập thủ công"** -> Hệ thống chuyển hướng đến màn hình cấu hình **"Giờ ngủ"**.
4.  **Nhập liệu:** Người dùng cuộn bánh xe chọn thời gian thức dậy (Ví dụ: điều chỉnh từ mặc định sang *05:20*).
5.  **Xác nhận:** Người dùng bấm dấu tích xác nhận (hoặc quay lại).
6.  **Hiệu ứng UX (Visual Feedback):**
    * Hệ thống quay trở lại màn hình chính.
    * Thẻ "Thức dậy" được cập nhật thời gian từ `~/07:00 AM` thành `05:20 AM / 07:00 AM`.
    * **Đồng thời:** Cánh cỏ ba lá phía dưới bên trái (màu tím) ngay lập tức được lấp đầy một phần màu sắc sáng hơn để thể hiện tiến trình đã được ghi nhận.

### 3.2. Kịch bản 2: Ghi nhận lượng nước uống
1.  **Chạm (Tap):** Người dùng ấn vào thẻ nhiệm vụ **"Uống nước"**.
2.  **Phản hồi UI:** Màn hình lớp phủ "Uống nước" xuất hiện với thông tin "Đã hoàn thành 1 ngày" cùng thông điệp sức khỏe ngắn. Phía dưới có 6 biểu tượng ly nước rỗng.
3.  **Hành động:** Người dùng bấm vào nút lớn **"UỐNG NƯỚC"** ở dưới cùng.
4.  **Hiệu ứng UX (Visual Feedback):**
    * Ly nước đầu tiên trong hàng ly được lấp đầy bằng màu xanh nước biển.
    * Khi quay lại màn hình chính, chỉ số trên thẻ "Uống nước" thay đổi từ `0/1,5 L` thành `0,25/1,5 L`.

### 3.3. Kịch bản 3: Xem lịch sử các ngày cũ
1.  **Thao tác:** Người dùng vuốt (Swipe) ngang trên thanh điều hướng thời gian hoặc bấm chọn trực tiếp vào một thứ khác trong tuần (Ví dụ: Chọn **T2** hoặc **CN** trước đó).
2.  **Hiệu ứng UX:** * Toàn bộ dữ liệu của danh sách nhiệm vụ phía dưới thay đổi để khớp với ngày được chọn.
    * Cỏ ba lá trung tâm co giãn nhẹ (Animation scale) và thay đổi mức độ lấp đầy màu sắc theo đúng dữ liệu lịch sử của ngày đó (Ví dụ: Ngày T2 có 1496 bước -> Cánh cỏ ba lá màu vàng được lấp đầy một phần; Ngày CN có 4964 bước -> Cánh cỏ ba lá màu vàng được lấp đầy nhiều hơn).

---

## 4. Quy tắc Logic & Cập nhật Trạng thái Hệ thống

* **Logic Lập đầy Cỏ Ba Lá (Clover Filling Logic):**
    * Diện tích màu sáng (Active color) được lấp đầy trên mỗi cánh hoa tỷ lệ thuận với tỷ lệ phần trăm hoàn thành của nhóm nhiệm vụ đó.
    * $Tỷ\ lệ\ lấp\ đầy = \frac{Chỉ\ số\ thực\ tế}{Mục\ tiêu} \times 100\%$ (Tối đa 100%).
* **Trạng thái Cuộn dữ liệu (Scroll Behavior):** Khi người dùng cuộn danh sách nhiệm vụ xuống dưới, khu vực cỏ ba lá trung tâm có thể thu nhỏ lại hoặc ẩn dần để nhường diện tích hiển thị cho các thẻ nhiệm vụ phía dưới, tối ưu hóa không gian màn hình thiết bị di động.