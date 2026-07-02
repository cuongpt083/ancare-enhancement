# Mô tả wireframe và các màn hình

## Yêu cầu chung

Người dùng sau khi đăng nhập với vai trò KH sẽ đi qua các màn hình sau để xem thông tin và quản lý tài khoản của mình. Danh sách các màn hình bao gồm:
- Màn hình trang chủ: hiển thị tổng quát các thông tin của KH. 
- Màn hình Báo cáo: hiển thị số liệu thống kê kết quả trải nghiệm của KH và cho phép xuất infographic để KH có thể tải về, chia sẻ cho bạn bè trên Mạng Xã hội.
- Màn hình Đào tạo: hiển thị danh sách các bài học của KH theo từng nhóm. (Cần làm rõ thêm về cấu trúc và nội dung các bài học)

### 1. Màn hình trang chủ

Các thông tin chính bao gồm:
    - Thông tin cơ bản của KH: ảnh đại diện (avatar) của KH, lời chào mừng, chuông thông báo (tùy chọn để bật/tắt nhận thông báo), gói giải pháp KH đã mua (nếu KH có mua gói giải pháp), icon ảnh
    - Các nút check-in hôm nay 1/5 mục đã ghi Ăn- Uống- Ngủ- Vận động- Học TKP. Khi bấm vào nút check in, ứng dụng sẽ hiển thị màn hình "Check-in" để KH thực hiện các nhiệm vụ trong ngày. 
    - Dashboard tóm tắt sức khỏe toàn diện (theo dạng đồng hồ sinh học, đã mô tả ): chấm điểm các nhiệm vụ hàng ngày. gồm có dinh dưỡng, vận động, TKP
    - Mục tiêu của bạn, số buổi/tổng số buổi trải nghiệm.
    - Chỉ số cơ thể: hiển thị kết quả phân tích dạng bảng, bao gồm các thông tin sau:
        - Các cột thông tin: Tiêu chuẩn, Mục tiêu,ngày hiện tại, Đánh giá (thừa, thiếu bao nhiêu kg, %)
        - Mỗi dòng thông tin hiển thị các giá trị tương ứng với các cột thông tin trên, sắp xếp theo thứ tự: Cân nặng, Khối lượng cơ, Khối lượng xương, Tỷ lệ nước, Tỷ lệ mỡ, Tỷ lệ mỡ nội tạng, Vóc dáng, Tuổi sinh học, Năng lượng nghỉ ngơi. Màu sắc của mỗi dòng sẽ thay đổi theo mức độ nguy hiểm (tốt, trung bình, nguy hiểm), trong đó:
            - Màu xanh lá: Tốt - ở mức bình thường
            - Màu vàng: Trung bình - cần cải thiện
            - Màu đỏ: Nguy hiểm - cần cải thiện gấp
    - Báo cáo tổng quát về tiến trình trải nghiệm gói Giải pháp của khách hàng theo dạng biểu đồ line-chart nhằm thể hiện xu hướng cải thiện sức khỏe, thể chất của cá nhân KH.các giá trị tương ứng với các cột thông tin trên, sắp xếp theo thứ tự: Cân nặng, Khối lượng cơ, Khối lượng xương, Tỷ lệ nước, Tỷ lệ mỡ, Tỷ lệ mỡ nội tạng, Vóc dáng, Tuổi sinh học, Năng lượng nghỉ ngơi trong 3 ngày gần nhất.
    -Phân tích chuyên sâu và lời khuyên, gồm các mục sau:
        - Đánh giá tiền trình chuyển hóa: (Phân tích vấn đề chỉ số, ăn uống, ngủ, vận động. đưa ra các vấn đề 1 ngày của khách hàng đồng thời kèm theo nguyên nhân
        - Giải pháp: đưa ra chiến lược tăng cư (tăng đạm), tối ưu hóa dung môi chuyển hóa (nước), giáp pháp bệnh lý đang gặp phải.

### 2. Màn hình check-in

Màn hình này hiển thị danh sách các nhiệm vụ check-in mà KH cần thực hiện trong ngày, được chia thành các Card thông tin sau:

- Thông tin chỉ số cơ thể. Card này hiển thị các thông tin sau: Cân nặng (kg), Mỡ cơ thể (%), Mỡ nội tạng (%), Cơ bắp (kg), Xương (kg), Nước (%), Tuổi sinh học, Trao đổi chất cơ bản (kcal). Các thông tin này tổ chức dưới dạng một bảng thông tin với 3 cột. Phía dưới bảng này là một nút bấm dạng link cho phép bấm vào để nhập lại các thông số này (Chạm để cập nhật chỉ số), khi nhập lại thì dữ liệu sẽ được ghi đè dữ liệu đã có, nếu chưa có thì được thêm mới. 
- Con số kỳ diệu: Lấy thông tin con số kỳ diệu kcal.
- Gợi ý bữa ăn. Card này bao gồm các mục nhỏ sau (kèm theo icon minh họa tương ứng, danh sách các mục này tùy theo số bữa KH đã đăng ký trong gói giải pháp đang sử dụng, ví dụ có gói 3 bữa/ngày, có gói 5 bữa/ngày)
    - Bữa sáng
    - Ăn nhẹ buổi sáng
    - Bữa trưa
    - Ăn nhẹ buổi chiều
    - Bữa tối
    - Ăn nhẹ buổi tối
    Mỗi mục này sẽ bao gồm các thành phần sau:
    - Tổng số calo mục tiêu trong bữa ăn
    - Cấu trúc bữa ăn: tính theo Calo và gam Đạm đối với 3 nhóm: Đạm - Tinh bột - Chất béo.
    - Nút chụp ảnh (icon máy ảnh): cho phép chụp ảnh món ăn để AI đánh giá. Khi bấm vào nút này ứng dụng mở màn hình "Ghi nhận bữa ăn" để lưu thông tin về bữa ăn đó.
    - Icon check hoàn thành bên cạnh nút chụp ảnh, icon này sẽ sáng màu xanh lá cây nếu như KH đã chụp ảnh và bấm nút “Lưu”, nếu chưa hoàn thành thì hiển thị màu xám.
- Hoạt động dinh dưỡng và thể chất khác như Uống nước, Giấc ngủ, Thể thao:
    - Uống nước: hiển thị theo số cốc nước đã uống (mặc định là 200ml/cốc), KH có thể tăng số cốc (bấm + hoặc - để tăng hoặc giảm số cốc)
    - Giấc ngủ: có nút nhập để nhập thời gian đi ngủ, thời gian thức dậy (format giờ: phút), ứng dụng sẽ tự động tính toán số giờ ngủ.
    - Thể thao/vận động: có nút bấm để KH nhập các hoạt động thể thao/vận động đã thực hiện trong ngày. Màn hình thêm hoạt động này sẽ bao gồm các chức năng:
        - tìm kiếm: nhập tên hoạt động, hệ thống hiển thị gợi ý các hoạt động (nếu có trong database)
        - danh sách hoạt động thể thao: hiển thị dưới dạng list, bên cạnh tên hoạt động sẽ có ước lượng Calo tương ứng cho 30 phút (tùy theo mức độ).
        - ô input bên dưới, cho phép nhập thời gian vận động theo phút.
        - KH bấm vào tên hoạt động, nhập thời gian vận động, hệ thống sẽ cho phép KH bấm nút Thêm để ghi nhận hoạt động. Sau khi KH bấm nút Thêm, hệ thống lưu hoạt động, thực hiện tính calo, tính điểm cho hoạt động
- Kiến thức TKP. Card này bao gồm các mục nhỏ sau:
    - Tên bài học cần thực hiện: hiển thị tên bài học, có biểu tượng video bên cạnh. Khi bấm vào tên bài học, ứng dụng sẽ chuyển sang màn hình Đào tạo, mở video và KH xem hết bài học sẽ được tính là đã hoàn thành bài học, tính điểm.
    - Trước khi mở màn hình Đào tạo, hệ thống sẽ hiển thị lưu ý, KH cần xem hết video để được tính điểm. Sau khi KH bấm nút "Xem bài học", hệ thống sẽ mở video. Sau khi KH xem hết video, hệ thống sẽ hiển thị màn hình survey để khách hàng trả lời 3 câu hỏi khảo sát:
        - Bạn ấn tượng gì về bài học hôm nay?
        - Bạn sẽ áp dụng kiến thức này như thế nào vào cuộc sống?
        - Bạn sẽ giới thiệu, chia sẻ bài học này với ai không?
        - Nút "Gửi khảo sát" sẽ sáng đèn khi KH trả lời xong 3 câu hỏi.
    
### 3. Màn hình ghi nhận bữa ăn 

Màn hình này dùng để KH chụp ảnh món ăn (có thể chụp ảnh hoặc upload ảnh từ thư viện ảnh có sẵn). Sau khi chụp ảnh xong, ứng dụng hiển thị ảnh và AI sẽ đánh giá cấu trúc bữa ăn (tỷ lệ % của Đạm, Tinh bột, Chất béo) và hiển thị dưới dạng Calo và gam Đạm đối với 3 nhóm: Năng lượng- Đường bột - Đạm - Chất béo tốt. Hiển thị so sánh với thiêu chuẩn được bổ sung thiếu/thừa. Có 1 câu nhận xét. Đây là các giá trị ước tính,KH có thể chỉnh sửa lại để phù hợp với thực tế. Sau khi chỉnh xong KH bấm nút “Lưu” để lưu lại thông tin. Nếu KH có sử dụng các sản phẩm hỗ trợ, ứng dụng sẽ hiển thị thêm mục bổ sung thông tin sử dụng các sản phẩm hỗ trợ này (ví dụ: số viên, số ml...)

### 2. Màn hình báo cáo

Màn hình này có nhiệm vụ hiển thị:
+ Biểu đồ tổng kết thông tin trong ngày (thực hiện vào buổi tối khoảng 21h00 - 22h00): hiển thị các thông tin tóm tắt về tình hình sức khỏe, thể chất của cá nhân KH, kèm theo các Phân tích và Đề xuất bao gồm:
        + Phân tích chuyên sâu về các chỉ số đo được trong ngày.
        + Lý do ảnh hưởng đến chỉ số
        + Lời khuyên, góp ý cho ngày hôm sau.
        + Nâng cấp gói sản phẩm, mua bổ sung sản phẩm (nếu cần)
    + Bảng tổng hợp tiến trình (periodic report) theo gói trải nghiệm: hiển thị tiến trình KH đang sử dụng, bao gồm các chỉ số, mục tiêu, ngày đầu, ngày gần nhất và thay đổi.
    + Nội dung Đề xuất: Tab này hiển thị các sản phẩm/gói giải pháp mà KH có thể quan tâm.
    + Nút tạo Infographic về nhật ký: cho phép KH tạo infographic về các nội dung trong ngày: Nội dung kiến thức (tóm lược từ các nội dung đã học trong ngày), Hành trình trải nghiệm (bữa ăn, thể chất), Ảnh bản thân, ảnh giao lưu trong ngày. Đây là infographic dạng dọc để chia sẻ qua mạng xã hội (Zalo, Facebook, ...)

### 3. Màn hình đào tạo

* **Sẽ mô tả chi tiết sau**