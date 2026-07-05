# Mô tả wireframe và các màn hình

## Yêu cầu chung

Người dùng sau khi đăng nhập với vai trò KH sẽ đi qua các màn hình sau để xem thông tin và quản lý tài khoản của mình. Danh sách các màn hình bao gồm:
- Màn hình trang chủ: hiển thị tổng quát các thông tin của KH. 
- Màn hình Báo cáo: hiển thị số liệu thống kê kết quả trải nghiệm của KH và cho phép xuất infographic để KH có thể tải về, chia sẻ cho bạn bè trên Mạng Xã hội.
- Màn hình Đào tạo: hiển thị danh sách các bài học của KH theo từng nhóm. (Cần làm rõ thêm về cấu trúc và nội dung các bài học)

### 1. Màn hình trang chủ

Các thông tin chính bao gồm:
    - Thông tin cơ bản của KH: ảnh đại diện (avatar) của KH, lời chào mừng, chuông thông báo (tùy chọn để bật/tắt nhận thông báo), gói giải pháp KH đã mua (nếu KH có mua gói giải pháp), có 1 ảnh (kích vào sẽ hiển thị kho ảnh bữa ăn)
    - card 1: Tổng quan gồm: 
        - Dashboard tóm tắt sức khỏe toàn diện (theo dạng biểu đồng sinh học hình tròn có màu sắc, đã mô tả ): chấm điểm các nhiệm vụ hàng ngày. gồm có dinh dưỡng, vận động, TKP. Cạnh điểm cho biểu tượng bó đuốc.
        - Mục tiêu của bạn, số buổi/tổng số buổi trải nghiệm. mục tiêu về vận động, cân nặng, thời gian hoàn thành mục tiêu 
        - Biểu đồ tiến trình:dạng biểu đồ line-chart màu sắc, thống kê 2 ngày gần nhất Chỉ số nào thay đổi nhiều nhất thì đưa lên,  tối đa 4 chỉ số thay đổi nhiều nhất, so sánh hiện tại với chỉ số liền trước
        -Phân tích chuyên sâu và lời khuyên, gồm các mục sau:
        - Đánh giá tiền trình chuyển hóa: (Phân tích vấn đề chỉ số, ăn uống, ngủ, vận động. đưa ra các vấn đề 1 ngày của khách hàng đồng thời kèm theo nguyên nhân
        - Giải pháp: đưa ra chỉ số đứng yên, xấu. Báo liên hệ với HLV để tư vấn giải pháp
    - Card 2: Nhiệm vụ 1 ngày
        - Con số kỳ diệu: Lấy thông tin con số kỳ diệu kcal.
        -  Chỉ số cơ thể: hiển thị kết quả phân tích dạng bảng, bao gồm các thông tin sau:
        - Kích vào để cập nhật chỉ số: Hiển màn hình cập nhật chỉ số 
        - Các cột thông tin:  Mục tiêu,ngày hiện tại, Đánh giá (thừa, thiếu bao nhiêu kg, %)
        - Mỗi dòng thông tin hiển thị các giá trị tương ứng với các cột thông tin trên, sắp xếp theo thứ tự: Cân nặng,Tỷ lệ nước, Tỷ lệ mỡ, Tỷ lệ mỡ nội tạng, Khối lượng cơ, Năng lượng nghỉ ngơi Khối lượng xương,  Vóc dáng, Tuổi sinh học. Màu sắc của mỗi dòng sẽ thay đổi theo mức độ nguy hiểm (tốt, trung bình, nguy hiểm), trong đó:
            - Màu xanh lá: Tốt - ở mức bình thường
            - Màu vàng: Trung bình - cần cải thiện
            - Màu đỏ: Nguy hiểm - cần cải thiện gấp
- Gợi ý bữa ăn. Card này bao gồm các mục nhỏ sau (kèm theo icon minh họa tương ứng, danh sách các mục này tùy theo số bữa KH đã đăng ký trong gói giải pháp đang sử dụng, ví dụ có gói 5 bữa/ngày)
-   Cấu trúc bữa ăn: là thành phần dĩnh dưỡng theo các thông tin: Con số calo kỳ diệu, Tỷ lệ Calo từ Đạm (protein) 30%, Tỷ lệ Calo từ Đường bột (carbohydrate) 40%, Tỷ lệ Calo từ Chất béo tốt (fat) 30%. Nước khuyến nghị (tối thiểu=  0,4x kg  cơ thể) (tính theo công thức dựa trên cân nặng và tình trạng bệnh lý nếu có).
    - Gợi ý bữa ăn chi tiết: bao gồm các bữa ăn theo thứ tự: Con số kỳ diệu: 1200 Cal/ Ngày, RMR, AMR, EX, TMR, Gợi ý bữa ăn, Sáng, 9h, Trưa, 16h, tối. Mỗi bữa ăn hiển thị các thông tin sau:
            - Sáng
                - Bữa ăn lành mạnh: 130 CAL
                - 3 lòng trắng trứng: 60 CAL
            - 9h
                - Hoa quả: 100 CAL
            - Trưa:
                - Thức ăn: 300 CAL
                - 1 bát rau: 100 CAL
                - 1/2 bát cơm: 100 CAL
            - 16h:
                - Bữa ăn lành mạnh: 90 CAL
            - Tối:
                - Thức ăn: 150 CAL
                - 1 bát rau: 100 CAL
                - 1/2 bát cơm 100 CAL
            - Các lưu ý:
                - 1. Hạn chế ăn thịt đỏ, đồ chiên, xào, nướng
                - 2. Uống tối thiểu 0,4 lít nước/10kg trọng lượng/ ngày
                - 3. Chương trình này cho 10 ngày vàng -> Đo lại -> Điều chỉnh 
        - Lượng nước uống trong ngày: tính theo lít và ghi chú theo cốc, ví dụ: 2.5L (8 cốc)
        - Khuyến nghị về thời gian và thói quen sinh hoạt: ví dụ 7:00 AM - 7:30 AM Ăn sáng, 11:30 PM - 1:00 PM Ăn trưa, 4:00 PM - 5:00 PM Ăn bữa phụ, 6:00 PM - 7:00 PM Ăn tối. Giờ đi ngủ, chế độ vận động.
        - có chức năng xuất gợi ý bữa ăn dạng pdf
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
Màn hình này hiển thị sau khi KH bấm nút "chụp ảnh" bữa ăn ở màn hình check-in KH. Màn hình này dùng để KH chụp ảnh món ăn (có thể chụp ảnh hoặc upload ảnh từ thư viện ảnh có sẵn). Sau khi chụp ảnh xong, ứng dụng hiển thị ảnh và AI sẽ đánh giá cấu trúc bữa ăn (tỷ lệ % của Đạm, Tinh bột, Chất béo) và hiển thị dưới dạng Calo và gam Đạm đối với 3 nhóm: Năng lượng- Đường bột - Đạm - Chất béo tốt. Hiển thị so sánh với thiêu chuẩn được bổ sung thiếu/thừa. Có 1 câu nhận xét. Đây là các giá trị ước tính,KH có thể chỉnh sửa lại để phù hợp với thực tế. Sau khi chỉnh xong KH bấm nút “Lưu” để lưu lại thông tin. Nếu KH có sử dụng các sản phẩm hỗ trợ, ứng dụng sẽ hiển thị thêm mục bổ sung thông tin sử dụng các sản phẩm hỗ trợ này (ví dụ: số viên, số ml...)

### 3. Màn hình đào tạo

* **Sẽ mô tả chi tiết sau**