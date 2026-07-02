# Mô tả wireframe và các màn hình

## Yêu cầu chung

Người dùng sau khi đăng nhập với vai trò HLV.

### 1. Màn hình trang chủ

- Sau khi đăng nhập thành công, người dùng sẽ được chuyển đến màn hình trang chủ.
- Màn hình trang chủ hiển thị Dashboard (3 phần:KPI, Action center, Task list).
- Menu điều hướng gồm:
    - Trang chủ
    - Team: Quản lý danh sách KH (tiềm năng, khách hàng ...)
    - Chat: các màn hình chat nhóm với cộng đồng (Khách hàng, nhóm khách hàng), chat với Trợ lý AI để hỏi đáp
    - Hồ sơ: quản lý tài khoản, cài đặt ứng dụng, gói chăm sóc của tôi
- Nút Floating button: cho phép HLV tùy biến hành vi thường xuyên làm của mình. Ví dụ: thêm mới KH, thêm mới KH tiềm năng, tạo bản tư vấn... Khi bấm vào nút này, ứng dụng hiển thị menu dạng radial với các hành vi mà HLV đã tùy biến.

### 2. Nhóm màn hình quản lý KH (Team)

Flow màn hình thao tác phục vụ tư vấn 15 phút để chuyển đổi KH tiềm năng thành KH (có mua gói giải pháp):

1. Bấm nút "Team" trên thanh điều hướng
2. Màn hình hiển thị danh sách KH tiềm năng (mặc định là hiển thị tab KH tiềm năng). Trên cùng có tabs để chuyển đổi giữa "KH tiềm năng" và "Khách hàng của tôi".
3. Màn hình "KH của tôi" được thiết kế bao gồm 2 Card:
    3.1. Card Thông tin tóm lược (Summary): có nhiệm vụ hiển thị báo cáo tổng quát về tình hình sử dụng các gói giải pháp của cá nhân KH. Card này bao gồm:
     - một bộ lọc theo "Tên KH", "Trạng thái KH" (trạng thái được tính theo Recency, Frequency, Monetary bao gồm: tích cực - hoạt động thường xuyên, có nguy cơ - sắp hết hạn hoặc lâu không hoạt động, kém quan tâm - ít tương tác)
     - thống kê số lượng KH theo từng trạng thái. Mỗi loại trạng thái được tô màu tương ứng với rủi ro, ví dụ: tích cực (tốt) - màu xanh lá, có nguy cơ (trung bình) - màu vàng, kém quan tâm (nguy hiểm) - màu đỏ
    3.2. Card Danh sách KH: card này có nhiệm vụ hiển thị thông tin cơ bản về các KH, bao gồm:
     - Tên KH
     - Gói dịch vụ: tên gói, tiến độ hoàn thành mục tiêu, thời gian sử dụng còn lại
     - Nhóm KH: nhóm KH (màu sắc tùy theo nhóm)
     - Bấm vào tên KH hoặc thẻ thông tin chi tiết sẽ chuyển sang màn hình chi tiết thông tin KH

    Màn hình "KH của tôi" sẽ có nút "Thêm mới" để nhập thông tin KH mới. Khi bấm vào nút này sẽ chuyển sang màn hình "Thêm mới KH".
4. Màn hình "Thêm mới KH" có nhiệm vụ nhận thông tin đầu vào của 1 KH mới hoặc một KH tiềm năng mới. Màn hình này gồm các card thông tin sau:
    4.1. Card Thông tin cơ bản: bao gồm các trường thông tin sau:
        - Tên người mời: (là một HLV hoặc một KH đóng vai trò đại sứ hoặc bảo trợ). Mặc định: Tên của HLV đang đăng nhập. HLV có thể nhập tên HLV hoặc KH khác để chỉ định người giới thiệu.
        - Số điện thoại người mời (là một HLV hoặc một KH đóng vai trò đại sứ hoặc bảo trợ). Mặc định: bỏ trống.
        - Họ và tên KH: là một trường bắt buộc
        - Số điện thoại: là một trường không bắt buộc
        - Email: là một trường không bắt buộc
        - Ngày sinh: là một trường không bắt buộc (theo format dd/mm/yyyy)
        - Giới tính: là một trường không bắt buộc (nam, nữ, khác), mặc định: nam
        - Chiều cao (cm): là một trường không bắt buộc
        - Cân nặng (kg): là một trường không bắt buộc
        - Địa chỉ: là một trường không bắt buộc
        Sau khi bấm nút "Lưu", nếu người dùng nhập đầy đủ các trường bắt buộc, ứng dụng sẽ chuyển sang màn hình "Khảo sát mục tiêu"
    4.2. Card Chân dung Khách hàng: Card này có nhiệm vụ thu thập thông tin về mục tiêu hiện tại, tình hình sức khỏe, hoạt động thường ngày, mối quan tâm về sức khỏe, phong cách sống của KH. Card này được chia thành 2 nhóm thông tin khi khảo sát:
        - Danh sách các câu hỏi cơ bản, các câu hỏi này chỉ hiển thị dưới dạng một paragraph lớn, không cần nút bấm hay tương tác, HLV chỉ cần đọc và hỏi KH. Danh sách câu hỏi gồm có:
            - Mệt mỏi/dễ cảm?
            - Đau đầu, đau lưng, đau mỏi?
            - Có tiểu đường, huyết áp, tim mạch, khớp?
            - Công việc/gia đình có áp lực?
            - Giấc ngủ tốt không?
            - Hay đói hoặc thèm ăn?
            - Thường ăn đồ chế biến sẵn?
            - Có nghĩ thức ăn ảnh hưởng sức khỏe?
            - Có thường bỏ bữa sáng?
            - Mỗi ngày uống khoảng bao nhiêu cốc nước?
            - Có tập thể dục không?
            - Bác sĩ có khuyên giảm cân hoặc giảm cholesterol?
            - Muốn giảm cân hoặc giảm vòng bụng?
            - Muốn tăng cân?
            - Có hút thuốc hoặc tiếp xúc khói thuốc?
            - Có thường uống rượu, bia hoặc cà phê?
            - Mục tiêu chính khi kiểm tra sức khỏe là gì?
        - Trả lời (cho HLV): là một ô nhập liệu cho phép HLV nhập câu trả lời cho tất cả các câu hỏi trên (độ dài không giới hạn). HLV có thể trả lời một cách ngắn gọn và tập trung vào kết quả KH mong muốn (ví dụ: tôi chỉ bị mất ngủ, còn lại Không có gì đáng ngại). 
        Sau khi ghi nhận thông tin, hệ thống tự động phân tích câu trả lời và lưu "Chân dung Khách hàng" vào KH đã tạo. Sau khi lưu xong, ứng dụng sẽ chuyển sang màn hình "Khảo sát Tanita".
5. Màn hình "Khảo sát Tanita": có nhiệm vụ thu thập kết quả cân, đo bằng thiết bị Tanita. Màn hình này bao gồm các thông tin: 
  - Nút thao tác nhanh: cho phép HLV nhập nhanh bằng cách bấm nút "Chụp ảnh" hoặc "Chọn ảnh" để upload ảnh chụp phiếu ghi chỉ số Tanita từ máy ảnh trên điện thoại. Sau khi upload ảnh, hệ thống sẽ tự động trích xuất thông tin từ ảnh và hiển thị lên màn hình. HLV có thể chọn "Sử dụng kết quả này" hoặc "Chỉnh sửa" để chỉnh sửa lại thông tin trước khi lưu. 
  - Form nhập liệu thủ công bao gồm các thông tin theo thứ tự sau (thứ tự hiển thị trên cân điện tử Tanita):
    - Cân nặng
    - Tỷ lệ mỡ cơ thể (%)
    - Khối lượng xương (kg)
    - Tỷ lệ nước (%)
    - Khối lượng cơ (kg)
    - Vóc dáng
    - Tuổi sinh học (tuổi)
    - Năng lượng nghỉ ngơi (kcal)
    - Tỷ lệ mỡ nội tạng (1-50)
  - Sau khi nhập xong kết quả, HLV bấm nút "Tạo bản tư vấn", ứng dụng sẽ tính toán, tạo bản tư vấn và chuyển sang màn hình "Phân tích kết quả".
6. Màn hình "Phân tích kết quả": có nhiệm vụ hiển thị kết quả phân tích cho KH và đưa ra lời khuyên cho HLV, bao gồm:
    - Kết quả phân tích: hiển thị kết quả phân tích dạng bảng, bao gồm các thông tin sau:
        - Các cột thông tin: Hiện tại, Cần tăng giảm (không hiển thị tên cột), Tiêu chuẩn, Đánh giá (thừa, thiếu bao nhiêu kg, %)
        - Mỗi dòng thông tin hiển thị các giá trị tương ứng với các cột thông tin trên, sắp xếp theo thứ tự: Cân nặng, Khối lượng cơ, Khối lượng xương, Tỷ lệ nước, Tỷ lệ mỡ, Tỷ lệ mỡ nội tạng, Vóc dáng, Tuổi sinh học, Năng lượng nghỉ ngơi. Màu sắc của mỗi dòng sẽ thay đổi theo mức độ nguy hiểm (tốt, trung bình, nguy hiểm), trong đó:
            - Màu xanh lá: Tốt - ở mức bình thường
            - Màu vàng: Trung bình - cần cải thiện
            - Màu đỏ: Nguy hiểm - cần cải thiện gấp
        - Mỗi dòng thông tin có thể bấm vào để xem chi tiết. Khi bấm vào, ứng dụng sẽ mở rộng dưới dạng drop-down ra một bảng nhỏ với các thông tin chi tiết hơn về kết quả phân tích, được trình bày theo 2 cột:
            - Ý nghĩa của thông tin: giải thích ý nghĩa của chỉ số phân tích
            - Rủi ro bệnh lý liên quan
    - Sau khi HLV trao đổi và tư vấn cho KH để chốt mục tiêu (tăng cân, giảm cân-giảm mỡ, hoặc giữ cân), HLV sẽ tick vào ô tròn bên cạnh mục tiêu đó. Ứng dụng sẽ tính toán và hiển thị Tên chương trình đề xuất. Cụ thể:
        - Nếu là Tăng cân: Chương trình Dinh dưỡng tế bào.
        - Nếu là Giảm cân: Chương trình Cơ Nước Mỡ.
        - Nếu là Giữ cân: Chương trình Bữa sáng lành mạnh.
    - HLV sẽ giải thích cho KH về các Chương trình này. Sau đó nếu KH đồng ý tham gia thì bấm nút "Xem lộ trình", nếu KH chưa đồng ý thì bấm nút "Đóng" để quay lại màn hình "Danh sách KH".
7. Màn hình "Xem lộ trình": Dựa trên mục tiêu và chương trình đã chọn, ứng dụng có nhiệm vụ hiển thị lộ trình cho KH và đưa ra lời khuyên cho HLV, bao gồm:
    - Lợi ích của chương trình: hiển thị lợi ích của chương trình dưới dạng các gạch đầu dòng
    - Kết quả đạt được
    - Lộ trình: chọn theo các lựa chọn 1 tháng, 3 tháng, trọn đời. Trong đó, mặc định là 3 tháng.
    - Gói chương trình: hiển thị các gói sản phẩm đi kèm với chương trình. Không hiển thị giá, HLV sẽ giải thích chi tiết bên ngoài app.
    - Các cam kết, disclaimer.

    Sau khi KH đồng ý tham gia chương trình và thanh toán xong (bên ngoài app), HLV bấm vào "Tạo tài khoản", ứng dụng sẽ hiển thị màn hình pop-up "Tạo Tài khoản KH" để HLV nhập thông tin tài khoản KH.
8. Màn hình pop-up "Tạo Tài khoản KH": có nhiệm vụ hiển thị thông tin tài khoản KH và cho phép HLV nhập thông tin tài khoản KH.
    - Tài khoản: số điện thoại hoặc email (lấy từ thông tin KH ở màn hình trước, hoặc HLV có thể chỉnh sửa)
    - Mật khẩu: được tạo ngẫu nhiên, HLV có thể chỉnh sửa
    - Xác nhận mật khẩu: được tạo ngẫu nhiên, HLV có thể chỉnh sửa
    - Sau khi HLV bấm "Tạo tài khoản", ứng dụng sẽ gửi email chứa thông tin tài khoản (bao gồm tài khoản và mật khẩu) cho KH và chuyển sang màn hình "Xây dựng gợi ý bữa ăn".
9. Màn hình "Xây dựng gợi ý bữa ăn": có nhiệm vụ hiển thị gợi ý bữa ăn cho KH dựa trên mục tiêu và chương trình đã chọn, và cho phép HLV chỉnh sửa gợi ý bữa ăn cho KH. Màn hình này gồm các phần sau:
    - Card Mục tiêu: chứa các thông tin về mục tiêu calo trong ngày, số bữa ăn trong ngày mà khách hàng có thể thực hiện, trong đó các thông tin này hiển thị dưới dạng số kèm theo nút +/- để HLV điều chỉnh. Mặc định Calo trong ngày hiển thị theo số Calo kỳ diệu đã tính ở màn hình trước. Số bữa ăn mặc định hiển thị 4 bữa. Bên dưới là nút "Tạo gợi ý bữa ăn", khi bấm nút này thì ứng dụng sẽ tính toán và hiển thị gợi ý bữa ăn.
    - Card Gợi ý bữa ăn: chứa các thông tin về gợi ý bữa ăn, bao gồm:
        - Cấu trúc bữa ăn: là thành phần dĩnh dưỡng theo các thông tin: Con số calo kỳ diệu, Tỷ lệ Calo từ Đạm (protein) 30%, Tỷ lệ Calo từ Bột đường (carbohydrate) 40%, Tỷ lệ Calo từ Chất béo tốt (fat) 30%. Lượng nước khuyến nghị (tính theo công thức dựa trên cân nặng và tình trạng bệnh lý nếu có).
        - Gợi ý bữa ăn chi tiết: bao gồm các bữa ăn theo thứ tự Bữa sáng, Bữa trưa, Bữa phụ, Bữa tối. Mỗi bữa ăn hiển thị các thông tin sau:
            - Tên bữa ăn
            - Danh sách các món ăn trong bữa ăn:
                - Món đạm (protein): bao gồm tên nhóm thực phẩm (gà/cá/nấm/trứng): Số lượng (tính theo bát, lạng), Calo tương ứng.
                - Món bột đường: bao gồm tên nhóm thực phẩm (cơm, khoai): Số lượng (tính theo bát, củ), Calo tương ứng.
                - Món rau: bao gồm tên nhóm thực phẩm (rau lá xanh, rau củ): Số lượng (tính theo bát, lạng), Calo tương ứng.
            - Các món ăn kèm: là các món ăn bổ sung (nếu có), ví dụ sữa chua, trái cây, vừng, lạc, ...
            - Thực phẩm bổ sung: là các sản phẩm trong gói chương trình đã mua, ví dụ: Bữa ăn lành mạnh, Bột Protein, Omega3, ...
            - Các lưu ý, lời khuyên của HLV trong bữa ăn này: ví dụ Ăn ngược (ăn đạm trước, rau trước, bột đường cuối), Ăn chậm, nhai kỹ...
        - Lượng nước uống trong ngày: tính theo lít và ghi chú theo cốc, ví dụ: 2.5L (8 cốc)
        - Khuyến nghị về thời gian và thói quen sinh hoạt: ví dụ 7:00 AM - 7:30 AM Ăn sáng, 11:30 PM - 1:00 PM Ăn trưa, 4:00 PM - 5:00 PM Ăn bữa phụ, 6:00 PM - 7:00 PM Ăn tối. Giờ đi ngủ, chế độ vận động.
        
    - Sau khi HLV đã chỉnh sửa gợi ý bữa ăn cho KH, HLV bấm "Hoàn thành", ứng dụng sẽ quay về màn hình danh sách KH.


    
  
     
     





    