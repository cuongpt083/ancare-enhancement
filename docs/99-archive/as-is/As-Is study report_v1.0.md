# **TÀI LIỆU KHẢO SÁT VÀ CHUẨN HÓA THIẾT KẾ HỆ THỐNG ỨNG DỤNG AN-CARE**

**Phiên bản:** v1.2 — *(SỬA QUAN TRỌNG: app khách hàng và CRM/onboarding của HLV ĐÃ TỒN TẠI — đính chính giả định sai ở v1.1 rằng "app chưa có giao diện khách hàng". Hợp nhất 2 tài liệu khảo sát chuyên sâu: `As-Is-study-report-appendix-v1.0.md` (CRM & onboarding cho HLV) và `As-Is-study-report-Customer-module-v1.0.md` (app Khách hàng 4 tab)).*
> **Lưu ý đọc:** Mục 4bis, và cập nhật ở các mục 5–8, phản ánh hiện trạng đã xác minh từ màn hình thực tế. Hai file phụ lục nói trên là một phần không tách rời của báo cáo As-Is này.
**Đối tượng sử dụng tài liệu:** Business Analyst (BA), Đội ngũ Phát triển Phần mềm.  
**Mục tiêu:** Chuẩn hóa hiện trạng cấu trúc thông tin, kiến trúc chức năng và hành trình người dùng (User Journey) của ứng dụng AN-Care phục vụ vai trò Huấn luyện viên dinh dưỡng (Health Coach) và Nhà vận hành nhóm dinh dưỡng.

**Bối cảnh & giai đoạn sản phẩm:** App đang ở giai đoạn **production có người dùng thử nghiệm**. Mục tiêu của đợt khảo sát là đánh giá và cải tiến trải nghiệm người dùng (UX), đồng thời rà soát xem tập chức năng hiện tại đã thuận tiện/tối ưu cho từng nhóm người dùng hay chưa, làm cơ sở cho báo cáo To-be và phân tích GAP.

**Mục tiêu kinh doanh của đợt enhancement (Aim):**
- Giảm tải thao tác cho Huấn luyện viên / Nhà vận hành.
- Tăng giữ chân khách hàng và nâng trải nghiệm xuyên suốt hệ sinh thái.
- Bổ sung năng lực vận hành cho Nutrition Club: quản lý kho, bán lẻ cho khách vãng lai (chưa đăng ký gói trải nghiệm), và quản lý kinh doanh (doanh thu, lời/lỗ).

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

## **4bis. HIỆN TRẠNG ĐÃ XÁC MINH — CRM/HLV & APP KHÁCH HÀNG (BỔ SUNG v1.2)**

Khảo sát chuyên sâu cho thấy nhiều năng lực **đã tồn tại trong app**, không phải "chưa có" như v1.1 từng giả định. Tóm tắt (chi tiết xem 2 file phụ lục):

**A. CRM & Onboarding phía HLV (file appendix):**
- Thu thập dữ liệu đầu vào: hồ sơ định danh + nhập chỉ số Tanita **hỗ trợ nhập tay hoặc quét ảnh/OCR**.
- Phân tích & khuyến nghị tự động: khớp dữ liệu Tanita với chuẩn WHO/Asian-Pacific, sinh bản tư vấn đánh giá từng chỉ số (xanh/đỏ) + khối lượng mỡ/cơ cần điều chỉnh.
- **Cấp tài khoản khách hàng:** HLV chủ động tạo tài khoản KH qua **Email + mật khẩu mặc định**, gắn gói dịch vụ.
- Journey builder: tham số hóa lộ trình 30 ngày (cân nặng mục tiêu, delta calo, số bữa) + auto-generate thực đơn.
- Action menu: chỉnh sửa, đặt lại mật khẩu, xóa tài khoản, **xuất báo cáo theo dải ngày tùy chỉnh**.

**B. App Khách hàng — đã tồn tại, 4 tab (file customer-module):**
- **Trang chủ:** dashboard mục tiêu, % hoàn thành, **streak**, đồng bộ chỉ số Tanita, **checklist thực đơn hôm nay (tick + chụp ảnh)**, nhật ký nước/ngủ/vận động, báo cáo "hôm nay nổi bật" + gợi ý tự động của Coach.
- **Lộ trình:** tiến độ ngày/tuần, KPI ngày, phân tích dữ liệu hôm trước.
- **Chat:** cộng đồng + **DM 1-1 với HLV phụ trách** (text, ảnh).
- **Hồ sơ:** thông tin định danh, trạng thái gói dịch vụ, truy cập báo cáo & lịch sử lộ trình.
- **Business rule:** gói dịch vụ hết hạn → **chặn check-in/log dữ liệu** cho tới khi gia hạn.

> **Hệ quả:** các điểm đau C1 (tự theo dõi tại nhà), một phần C2 (nhắc/checklist), và P4 (kênh giao tiếp HLV–khách) **phần lớn đã được app hiện tại đáp ứng**. Mục 5–8 dưới đây được hiệu chỉnh theo hiện trạng đã xác minh.

## **5\. STAKEHOLDER & PERSONA (cập nhật v1.2)**

Khảo sát hiện trạng xác định **3 nhóm người dùng (persona) riêng biệt** trong hệ sinh thái Nutrition Club, thay vì một persona "Huấn luyện viên" duy nhất như mô hình v1.0:

| Persona | Vai trò & nhu cầu cốt lõi | Hiện trạng tiếp cận hệ thống |
| :---- | :---- | :---- |
| **Nhà Sáng lập (Founder)** | Người kinh doanh sở hữu club. Cần nắm tình hình kinh doanh (doanh thu, lợi nhuận), chân dung khách hàng, hiệu quả chăm sóc, sức khỏe tồn kho, và kênh kết nối/chăm sóc khách hàng mọi lúc (sinh nhật, ngày lễ). | App hiện **chưa có** phân hệ Quản lý kinh doanh / Kho / CRM marketing chuyên biệt cho góc nhìn này. |
| **Nhà vận hành / Huấn luyện viên (Health Coach)** | Trực tiếp vận hành club, tư vấn, theo dõi và đồng hành cùng khách hàng. | **Đã xác nhận:** sử dụng app HLV (5 tab) + CRM/onboarding đầy đủ (tạo tài khoản KH, OCR Tanita, journey builder, báo cáo tùy chỉnh — xem 4bis.A). |
| **Khách hàng (Member / Khách vãng lai)** | Thành viên trải nghiệm lộ trình, hoặc khách vãng lai được thành viên mời đến. | **Đã xác nhận (đính chính):** app khách hàng **ĐÃ TỒN TẠI** (4 tab — xem 4bis.B). Khách đăng nhập bằng tài khoản do HLV cấp; tự log bữa ăn/nước/ngủ, xem tiến độ, chat với HLV. *Khách vãng lai (chưa có gói) hiện chưa có luồng riêng trong app.* |

## **6\. PAIN POINT REGISTER (HIỆN TRẠNG NGHIỆP VỤ — BỔ SUNG v1.1)**

Tổng hợp các điểm đau hiện hữu, phân theo persona. Phần lớn đang được xử lý **thủ công (sổ sách, trí nhớ, công cụ ngoài app)** — đây là ranh giới As-Is để đối chiếu khi phân tích GAP.

> **Lưu ý hiệu chỉnh v1.2:** nhãn trạng thái mỗi pain point: **[CÒN]** = vẫn đúng/chưa giải; **[ĐÃ GIẢI]** = app hiện tại đã đáp ứng; **[GIẢI MỘT PHẦN]** = có nhưng chưa đủ.

**A. Nhà vận hành / Huấn luyện viên**
- P1 — **[CÒN]** *Bán lẻ khách vãng lai:* khi đông khách, không nhớ đã bán cho ai, bao nhiêu → khó cân đối thu/chi cuối ngày. *(App chưa có POS.)*
- P2 — **[CÒN]** *Kiểm kho cuối ngày:* không nắm lượng đã xuất kho của bản thân và đồng vận hành. *(App chưa có quản lý kho.)*
- P3 — **[ĐÃ GIẢI]** *Theo dõi hành trình dài hạn:* nay đã có hồ sơ số, lộ trình 30 ngày, lịch sử log và báo cáo tùy chỉnh thay cho sổ giấy.
- P4 — **[GIẢI MỘT PHẦN]** *Đồng hành khi khách ở nhà:* đã có chat 1-1, checklist thực đơn, gợi ý của Coach trong app; **còn thiếu nhắc nhở chủ động (push reminder theo khung giờ)**.
- P5 — **[GIẢI MỘT PHẦN]** *Chia sẻ kết quả của khách:* app đã có đồ thị/insight tiến độ; **còn thiếu khả năng xuất bản chia sẻ giàu cảm xúc ra mạng xã hội**.

**B. Khách hàng**
- C1 — **[ĐÃ GIẢI]** *Tự theo dõi tại nhà:* app khách hàng đã cho phép tự log bữa ăn/nước/ngủ/ảnh, xem chỉ số & tiến độ — dữ liệu không còn kẹt trong sổ giấy.
- C2 — **[GIẢI MỘT PHẦN]** *Lời dặn & nhắc nhở:* đã có checklist thực đơn và nhật ký; **còn thiếu nhắc nhở/báo thức tự động theo khung giờ** (khách vẫn phải tự nhớ mở app).
- C3 — **[CÒN]** *Chia sẻ MXH:* chưa có cách thuận tiện để biên soạn & chia sẻ hành trình ra mạng xã hội.
- C4 — **[CÒN]** *Gián đoạn khi hết gói:* business rule chặn check-in/log khi gói hết hạn → trải nghiệm bị ngắt, có thể gây bỏ cuộc nếu gia hạn chậm.

**C. Nhà Sáng lập**
- F1 — *Thiếu bức tranh kinh doanh:* doanh thu, lợi nhuận, lời/lỗ chưa được hệ thống hóa.
- F2 — *Thiếu chân dung & chiến lược chăm sóc khách hàng hiệu quả.*
- F3 — *Thiếu giám sát tồn kho.*
- F4 — *Thiếu kênh kết nối/chăm sóc khách hàng từ xa* (dịp sinh nhật, lễ…).

## **7\. RANH GIỚI PHẠM VI HIỆN TẠI (NHỮNG GÌ APP CHƯA HỖ TRỢ — cập nhật v1.2)**

Sau khi xác minh, các năng lực **thực sự chưa nằm trong app** (đây mới là khoảng trống GAP đáng tin):
- **Bán lẻ POS** cho khách vãng lai và đối soát thu/chi cuối ngày.
- **Quản lý kho** và phân tách xuất kho theo từng người vận hành.
- **Phân hệ quản lý kinh doanh & báo cáo lời/lỗ** cho Nhà sáng lập (dashboard quản trị, đa club).
- **CRM marketing chủ động** (nhắc sinh nhật, ngày lễ, chiến dịch chăm sóc).
- **Nhắc nhở chủ động (push reminder theo khung giờ)** cho khách hàng.
- **Xuất bản & chia sẻ hành trình ra mạng xã hội** (infographic giàu cảm xúc).
- **Luồng riêng cho khách vãng lai** (chưa có gói) trong app.

> **Đính chính:** "Giao diện khách hàng" và "tự theo dõi tại nhà" **KHÔNG còn** là khoảng trống — đã tồn tại (xem 4bis.B).

## **8\. CÁC ĐIỂM ĐÃ XÁC NHẬN & HẠN CHẾ DỮ LIỆU (cập nhật v1.2)**

**Đã xác nhận (chốt As-Is):**
1. **Giao diện khách hàng:** App khách hàng **ĐÃ TỒN TẠI** (4 tab; tự log, tiến độ, chat với HLV). *Đính chính giả định sai ở v1.1.* Khách đăng nhập bằng tài khoản Email/mật khẩu do HLV cấp.
2. **CRM/HLV:** HLV đã có đầy đủ onboarding (cấp tài khoản, OCR Tanita, journey builder, báo cáo tùy chỉnh).
3. **Mapping vai trò:** "Nhà vận hành" **chính là** persona HLV.
4. **Khách vãng lai:** chưa có luồng riêng trong app (gắn với khoảng trống POS).

**Hạn chế dữ liệu (lưu ý cho GAP & đo lường To-be):**
5. **Chưa có số liệu baseline định lượng** (tỷ lệ check-in, chuyển đổi lead→KH, At-risk, thời gian xử lý/ca, quy mô HLV/khách). GAP & đánh giá To-be giai đoạn này dựa trên **đánh giá định tính**; khuyến nghị thiết lập đo lường khi triển khai.