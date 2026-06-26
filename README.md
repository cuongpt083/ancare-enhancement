# ancare-enhancement

Phân tích & thiết kế nâng cấp **AnCare DXP** — nền tảng trải nghiệm số chăm sóc sức khỏe chủ động, đồng hành với quy trình kinh doanh 12 bước của Nutrition Club (Herbalife). Tài liệu chi tiết nằm trong `docs/` (xem [Cấu trúc tài liệu](#cấu-trúc-tài-liệu) ở cuối).

# Tầm nhìn

AnCare Digital User Experience Platform định vị là một nền tảng trải nghiệm người dùng số về chăm sóc sức khỏe chủ động cho hàng triệu người Việt Nam. AnCare DXP sẽ trở thành một nền tảng chăm sóc khách hàng xuất sắc phục vụ cho các khách hàng quan tâm đến sức khỏe, có mong muốn phát triển bản thân, tìm kiếm cơ hội kinh doanh trong lĩnh vực chăm sóc sức khỏe chủ động.

# Sứ mệnh

AnCare DXP là một cầu nối giữa khách hàng tiềm năng, khách hàng hiện tại với hệ sinh thái chăm sóc sức khỏe chủ động của AnCare. Tại AnCare DXP, khách hàng được cung cấp kiến thức về sức khỏe, được trải nghiệm dịch vụ chăm sóc sức khỏe chủ động cá nhân hóa, được tư vấn thay đổi thói quen, lối sống và được phát triển bản thân cũng như định hướng cơ hội kinh doanh hấp dẫn, nhân văn

AnCare lấp đầy khoảng trống giữa các Ứng dụng phục vụ Huấn luyện viên dinh dưỡng, đối tác kinh doanh của Herbalife (ví dụ VNHUB, Herbalife Learning, Herbalife SHOP) và các ứng dụng phục vụ khách hàng sau này như Herbalife Pro2col. Các app hiện tại chưa bám sát vào các trải nghiệm thực tế tại Nhóm dinh dưỡng, chưa thực sự hiểu văn hóa, tâm lý của nhiều phân khúc khách hàng tại Việt Nam.

# Giá trị cốt lõi

AnCare DXP mang lại 4 giá trị cốt lõi cho người dùng:
1. **Ứng dụng chăm sóc sức khỏe chủ động:**
   - Là nền tảng giúp người dùng có thể truy cập các nội dung hữu ích để chăm sóc sức khỏe của chính mình, giúp họ thay đổi thói quen ăn uống lành mạnh, tăng cường vận động, quản lý cân nặng và xây dựng một lối sống tích cực hơn.
   - Hơn cả một ứng dụng theo dõi sức khỏe, AnCare DXP là một không gian để khách hàng tìm thấy cảm hứng và động lực để bắt đầu một hành trình chăm sóc sức khỏe chủ động cho chính bản thân và chia sẻ, truyền cảm hứng và động lực tới những người xung quanh thông qua câu chuyện, kết quả đạt được trên mạng xã hội.

2. **Ứng dụng phát triển bản thân và cơ hội kinh doanh:**
   - Là nền tảng giúp người dùng có thể phát triển kỹ năng mềm, kỹ năng bán hàng, kỹ năng lãnh đạo và có cơ hội kinh doanh hấp dẫn, nhân văn
   - Là một phễu thu hút khách hàng, khơi gợi sự quan tâm đến giải pháp chăm sóc sức khỏe chủ động, bền vững, cũng như cơ hội kinh doanh khởi nghiệp nhân văn, chi phí thấp, an toàn, rủi ro thấp, linh hoạt thời gian với chính sách trả thưởng hấp dẫn từ Herbalife.

3. **Nền tảng giao tiếp và kết nối với nhau:**
   - Là nền tảng giao tiếp, kết nối giữa khách hàng với Huấn luyện viên dinh dưỡng và các thành viên trong Nhóm dinh dưỡng, giúp họ có thể dễ dàng giao tiếp, học hỏi và phát triển bản thân

# Các nhóm tính năng chính trên AnCare DXP
1. **Module Hành trình khách hàng:**
   Là một Khách hàng tiềm năng, tôi quan tâm tới các kiến thức sinh động, cô đọng, dễ hiểu về sức khỏe, về sản phẩm, về những thói quen tốt để cải thiện vóc dáng, sức khỏe. Khi tôi có sự quan tâm, AnCare sẽ kết nối tôi với Huấn luyện viên dinh dưỡng phù hợp để tư vấn, chia sẻ, đồng hành cùng tôi. Khi tôi bắt đầu thay đổi, tôi quan tâm tới việc theo dõi sức khỏe, dinh dưỡng, thói quen của mình. AnCare cung cấp cho tôi các công cụ để tôi có thể theo dõi sức khỏe, dinh dưỡng, thói quen của mình. Khi tôi cảm thấy hài lòng, tôi có thể giới thiệu cho bạn bè, người thân cùng sử dụng AnCare, từ đó tạo ra một vòng tròn liên tục với những người quan tâm tới sức khỏe, vóc dáng, dinh dưỡng.
   
   Là một Khách hàng đã mua gói sản phẩm và tham gia trải nghiệm tại Nhóm dinh dưỡng (nutrition club), tôi quan tâm tới các thay đổi tích cực của mình và những người bạn đồng hành, tôi quan tâm tới các nội dung chia sẻ, hướng dẫn để có thể tăng cường vận động, thay đổi thói quen ăn uống, lối sống lành mạnh. Tôi quan tâm tới việc cập nhật các thông tin, kết quả tập luyện, chỉ số cơ thể, tôi cũng quan tâm tới các nội dung chia sẻ, động viên từ Huấn luyện viên dinh dưỡng của tôi và các thành viên trong nhóm dinh dưỡng, tôi có thể chia sẻ, lan tỏa những trải nghiệm tích cực này cho bạn bè, người thân thông qua mạng xã hội hoặc trực tiếp. Để làm được điều đó, tôi quan tâm tới việc có thể dễ dàng chia sẻ các nội dung này với bạn bè, người thân, tạo nên những câu chuyện thành công cho chính tôi, cho bạn bè, người thân, truyền cảm hứng cho họ. Tôi cũng quan tâm tới các buổi sinh hoạt (HOM) của Nhóm dinh dưỡng mà tôi tham gia về các chủ đề chuyên sâu về dinh dưỡng cũng như lối sống, kinh doanh.
2. **Module Hành trình kinh doanh (dành cho Huấn luyện viên dinh dưỡng):**
   Là một Huấn luyện viên dinh dưỡng, tôi quan tâm tới việc phát triển kỹ năng mềm, kỹ năng bán hàng, kỹ năng lãnh đạo, con đường thăng tiến trong kế hoạch trả thưởng của Herbalife. Tôi cũng quan tâm tới việc có thể dễ dàng quản lý khách hàng của tôi, theo dõi, hỗ trợ họ đạt được mục tiêu sức khỏe, vóc dáng của họ, thể hiện sự quan tâm tới họ qua các thăm hỏi động viên vào các thời điểm đặc biệt như sinh nhật, kỷ niệm, ngày lễ, hoặc đơn giản chỉ là những lời động viên khi họ cảm thấy xuống tinh thần, từ đó giúp họ gia tăng sự hài lòng, gắn bó và gia tăng cơ hội để họ giới thiệu bạn bè, người thân sử dụng các sản phẩm của Herbalife. Tôi cũng quan tâm tới việc có thể dễ dàng chia sẻ các nội dung, thông tin về sản phẩm, về giải pháp sức khỏe, vóc dáng cũng như cơ hội kinh doanh của Herbalife cho khách hàng tiềm năng, cho bạn bè, người thân của tôi, giúp họ quan tâm, sử dụng sản phẩm cũng như tham gia các cơ hội kinh doanh mà Herbalife mang lại. 
   
   Là một Huấn luyện viên dinh dưỡng, tôi quan tâm tới việc học hỏi kiến thức về dinh dưỡng, sản phẩm, huấn luyện, tư vấn, chăm sóc sức khỏe, vóc dáng cho khách hàng, các nội dung đào tạo chuyên sâu dành cho các nhóm khách hàng có nhu cầu khác nhau (thừa cân, thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, bà mẹ mang thai và sau sinh..).

   Là một Huấn luyện viên dinh dưỡng, tôi có nhiệm vụ vận hành Nhóm dinh dưỡng (có thể là các DMO như nhóm dinh dưỡng chuyên sâu, nhóm dinh dưỡng vận động, nhóm dinh dưỡng Spa, ...), là các mô hình kinh doanh khác nhau, tôi quan tâm tới các tính năng công cụ để có thể dễ dàng vận hành, quản lý nhóm dinh dưỡng của tôi, bổ trợ cho các tính năng đã có trên các ứng dụng như VNHUB của Herbalife.

   3. **Module đào tạo**

   Là một Huấn luyện viên, tôi quan tâm tới các kiến thức về dinh dưỡng, sản phẩm, huấn luyện, tư vấn, chăm sóc sức khỏe, vóc dáng cho khách hàng, các nội dung đào tạo chuyên sâu dành cho các nhóm khách hàng có nhu cầu khác nhau (thừa cân, thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, bà mẹ mang thai và sau sinh..).

   Là một Khách hàng, tôi quan tâm tới việc có thể dễ dàng tìm kiếm, truy cập các kiến thức hữu ích về dinh dưỡng, sản phẩm, về các chủ đề liên quan tới sức khỏe, vóc dáng, các câu chuyện thành công, các video hướng dẫn tập luyện, các công thức nấu ăn lành mạnh, các lời khuyên từ các chuyên gia hàng đầu trong lĩnh vực dinh dưỡng, chăm sóc sức khỏe để qua đó tôi có thể cải thiện sức khỏe, vóc dáng, lối sống của tôi. Tôi cũng quan tâm tới các khóa học, chương trình huấn luyện do các chuyên gia xây dựng nhằm giúp tôi hiểu sâu hơn về dinh dưỡng, sản phẩm, về các thói quen lành mạnh, về cách sử dụng sản phẩm, về cách theo dõi sức khỏe, dinh dưỡng, thói quen, về cách xây dựng một lối sống lành mạnh để từ đó tôi có thể cải thiện sức khỏe, vóc dáng, lối sống của tôi.

   Quá trình đào tạo, học tập kiến thức cần tổ chức theo dạng **micro-course** (các khóa học ngắn gọn, tập trung vào một kỹ năng cụ thể, dễ dàng tiếp thu và áp dụng), với nội dung đa dạng về dinh dưỡng, sản phẩm, huấn luyện, tư vấn, chăm sóc sức khỏe, vóc dáng cho khách hàng, các nội dung đào tạo chuyên sâu dành cho các nhóm khách hàng có nhu cầu khác nhau (thừa cân, thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, bà mẹ mang thai và sau sinh..), và có hình thức thi đua, tranh tài nhằm tạo sự hứng thú cho người học theo trải nghiệm Gamification.

   4. **Module Phát triển bản thân cho Khách hàng và Huấn luyện viên** 

   Là một Khách hàng, tôi quan tâm tới việc có thể dễ dàng tìm kiếm và được gợi ý các kiến thức, nội dung, khóa học, chương trình huấn luyện phù hợp với nhu cầu của tôi thông qua tính năng gợi ý thông minh, cá nhân hóa, được xây dựng dựa trên các thông tin về sức khỏe, dinh dưỡng, thói quen, mục tiêu, sở thích, hành vi sử dụng của tôi trên ứng dụng. 

   Là một Khách hàng tiềm năng, tôi quan tâm tới việc có thể dễ dàng tìm kiếm, truy cập các nội dung giới thiệu về sản phẩm của Herbalife, về giải pháp sức khỏe, vóc dáng của Herbalife, về cơ hội kinh doanh của Herbalife, về các câu chuyện thành công của các Khách hàng và Huấn luyện viên của Herbalife. 

   Là một Huấn luyện viên, tôi quan tâm tới việc có thể dễ dàng tìm kiếm các chủ đề đào tạo cơ bản, đào tạo chuyên sâu trong lĩnh vực kinh doanh bán hàng trực tiếp và chăm sóc sức khỏe chủ động, kèm theo điều kiện, lộ trình đào tạo, tài liệu tham khảo để tôi có mục tiêu phát triển bản thân phù hợp.

# Định hướng thiết kế chính (cập nhật từ quá trình phân tích)

Từ tầm nhìn trên, quá trình phân tích As-Is → To-be → GAP → To-do đã chốt các định hướng thiết kế sau:

1. **Bám sát Quy trình 12 bước kinh doanh.** AnCare được thiết kế như **công cụ đắc lực thực thi quy trình 12 bước** (tài liệu gốc: `docs/references/01.Quy-trinh-12-buoc-kinh-doanh.md`) — từ thu hút khách tiềm năng (Bước 1–2) đến nhân bản thành Giám sát viên vận hành club (Bước 6–12).

2. **La bàn Quy trình (Process State Model) — xương sống.** Số hóa "Sơ đồ dẫn (SĐD)", xác định mỗi người đang ở bước nào và điều khiển cả 4 module: việc cần làm tiếp theo, nội dung/khóa học đề xuất, hành động chăm sóc, và tiêu chí hoàn thành mỗi bước. Cùng GNV (giấy nhắc việc) và DSKHTN tạo đủ bộ **3 công cụ KD số hóa**.

3. **Trọng tâm Bước 1–2: Trợ lý phát triển khách hàng (AI-assisted).** Gỡ nút thắt khi quy mô tăng và rào cản người mới — DSKHTN số, chấm điểm lead, copilot làm ấm/mời, phễu + chatbot, đặt lịch 2/1, số hóa buổi trải nghiệm đầu. Engine cá nhân hóa triển khai **phân tầng theo độ trưởng thành dữ liệu** (P1 thư viện kịch bản + Stage-of-Change → P2 Phỏng vấn tạo động lực → P3 chân dung động + RAG → P4 uplift/Next-Best-Action). AI **hỗ trợ, không thay** vai trò con người.

4. **Kết nối khách ↔ HLV theo công sức (Content-Attribution Matching).** HLV sáng tạo/chia sẻ nội dung kèm mã giới thiệu → khách tương tác **tự gắn về HLV** (cơ chế chính, tạo động lực); thuật toán chỉ phân phối lead "mồ côi". Hợp nhất chia sẻ câu chuyện thành công + vòng lặp giới thiệu + matching thành một bánh đà; khách luôn được quyền chọn/đổi HLV.

5. **Độc lập, không trùng lặp Herbalife apps.** AnCare **không tích hợp kỹ thuật** với VNHUB/Learning/SHOP/Pro2col, và **không làm** POS bán lẻ, quản lý kho, dashboard quản trị kinh doanh (thuộc VNHUB) — chỉ bổ trợ về phạm vi.

6. **Số hóa MLM tập trung có rủi ro đặc thù.** Đã rà soát 15 rủi ro (quyền sở hữu lead, tranh chấp tuyến, "cắt cầu", pháp lý đa cấp & quảng cáo sức khỏe, riêng tư dữ liệu, tự động hóa xói mòn quan hệ, adoption…). Nguyên tắc giảm thiểu: **trao quyền không thâu tóm; AI hỗ trợ không thay người & không thao túng; tuân thủ là ràng buộc thiết kế; minh bạch & quyền người dùng; cấu hình được; thắng nhỏ tạo niềm tin trước khi mở rộng**.

# Năng lực & trải nghiệm sản phẩm (đã thiết kế chi tiết)

Từ định hướng trên, các luồng trọng tâm đã được đặc tả nghiệp vụ + UI-UX + prototype tương tác. Đây là phần phản ánh rõ nhất "phần mềm này mang lại trải nghiệm gì".

## A. Trải nghiệm phía Khách hàng — sống khỏe theo Thân · Tâm · Trí

Toàn bộ trải nghiệm KH xoay quanh triết lý **Thân – Tâm – Trí**: Thân (sức khỏe thể chất & tinh thần), Tâm (lối sống lành mạnh, biết ơn, quản trị cảm xúc), Trí (kiến thức tài chính, đầu tư, kinh doanh — Phát triển bản thân).

- **Trang chủ cá nhân hóa:** % hoàn thành ngày/tuần, đánh giá sức khỏe toàn diện theo 3 trụ cột, lịch biểu (học tập/quiz/sự kiện), tổng kết cuối ngày (đủ đạm/calo/nước/ngủ, điểm, lưu ý cải thiện).
- **"Sức khỏe tổng thể" — Đồng hồ sinh học:** vòng tròn 24h chia múi theo hoạt động, tô màu trạng thái; check-in từng nhiệm vụ với **chấm điểm theo độ đúng giờ** (3/2/1/0 → nền tảng streak & credit thưởng), **uống nước ghi nhận nhiều lần (cốc ~250ml)**, hai vùng "đã/chờ thực hiện" tạo động lực.
- **Cá nhân hóa thời gian biểu:** KH tự chọn **số bữa ăn (3/4/5)** và giờ từng hoạt động; hệ thống hiển thị **mức tối ưu đồng hồ sinh học** và điểm tối đa (lệch nhịp sinh học → giảm điểm) để cân bằng giữa tối ưu và khả thi.
- **Gợi ý bữa ăn cá nhân hóa:** thực đơn theo mục tiêu cân nặng + số bữa, cấu trúc **3 nhóm (Đạm/Xơ/Đường-bột)**; ghi nhận bữa ăn bằng **chụp ảnh → AI bóc tách món + ước lượng đơn vị (bát/lạng)** hoặc nhập tay form → **API tính calo**.
- **Kết nối & truyền cảm hứng:** chat trực tiếp với HLV (hỏi đáp thực đơn, được động viên), chia sẻ tiến bộ.

## B. Trải nghiệm phía HLV — đồng hành & chuyển đổi bằng dữ liệu

- **Tổng quan (Dashboard):** KPI KH/lead, "hôm nay nên tiếp cận", cảnh báo gợi ý bữa ăn cần làm mới.
- **Quản lý KH tiềm năng theo chân dung:** danh sách lead gắn **chân dung khách hàng + tính cách DISC + giai đoạn sẵn sàng (Stage-of-Change) + lead score + việc cần làm tiếp**; bộ câu hỏi khảo sát sinh chân dung, AI gợi ý cách tiếp cận (có nêu bằng chứng, tôn trọng consent).
- **Luồng tư vấn chuẩn hóa:** Tạo KH tiềm năng → **Nhập chỉ số Tanita (OCR ảnh)** → **Bản tư vấn** (đối chiếu chuẩn WHO/Tanita, chỉ ra điểm cần cải thiện & nguy cơ) → **Thiết lập mục tiêu** (chọn gói + thời gian, **tính % khả thi**, tinh chỉnh mục tiêu) → **Tạo tài khoản & đặt gói** → **Gợi ý bữa ăn**.
- **Gợi ý bữa ăn đa phiên bản:** mỗi thực đơn hiệu lực **10 ngày** → đo lại → điều chỉnh mục tiêu → tạo phiên bản mới (lưu lịch sử).
- **Chi tiết KH & chăm sóc:** xem Tanita, mục tiêu, ảnh check-in, lịch sử thực đơn; **HLV làm gương** — tự thực hiện lộ trình và chia sẻ ảnh/kết quả qua chat tới KH/cộng đồng.

## C. Nền tảng dữ liệu & quy tắc nghiệp vụ

- **Chân dung khách hàng (mô hình 2 bảng):** `users` (cơ bản) + `customer_personas` (JSONB linh hoạt: DISC, Stage, pain points, **lưu cả câu hỏi–câu trả lời khảo sát** làm bằng chứng cho AI suy luận).
- **Quy tắc Calo & bữa ăn:** tính "con số kỳ diệu" (RMR+AMR+EX=TMR), cấu trúc bữa 3 nhóm thực phẩm, ràng buộc tốc độ an toàn, nước ≥ 0,4 L/10 kg/ngày.
- **Quy tắc đề xuất gói:** chọn gói theo mục tiêu × thời gian × chân dung (DISC/Stage/ngân sách), tính % đạt được.
- **Đạo đức & tuân thủ:** AI hỗ trợ không thay người, không thao túng; mọi xử lý dữ liệu cá nhân tuân thủ consent.

> Các luồng trên đã có **prototype HTML tương tác** trong `prototypes/kh/` (Khách hàng) và `prototypes/hlv/` (HLV), nối điều hướng đầy đủ.

## Lộ trình MVP (tóm tắt)

- **MVP-1 — Nền tảng PSM + Lan tỏa & Gắn kết:** dựng La bàn quy trình/GNV; chia sẻ câu chuyện thành công, nhắc nhở chủ động, chăm sóc theo dịp; nền tảng phễu (DSKHTN số, đặt lịch 2/1).
- **MVP-2 — Học tập, Nội dung & AI hỗ trợ chuyển đổi:** Module Đào tạo micro-course + gamification; copilot làm ấm/mời (P1–P2); attribution nội dung; pipeline 12 bước.
- **MVP-3 — Phễu lạnh, Matching fallback, Cá nhân hóa, Nhân bản & Sự nghiệp:** chatbot, recommender, HOM, coaching tuyến dưới, lộ trình thăng tiến.
- **Sau MVP-3:** lớp tối ưu AI (uplift + Next-Best-Action) khi đủ dữ liệu.

## Cấu trúc tài liệu

| Thư mục | Nội dung |
| :-- | :-- |
| `docs/as-is/` | Khảo sát hiện trạng (As-Is v1.2) + 2 phụ lục (CRM/HLV, app Khách hàng). |
| `docs/to-be/` | **`To-be study report_v2.1 (consolidated).md`** — bản hợp nhất: Phần I tổng thể · Phần II La bàn 12 bước (PSM) · Phần III Thu hút & Chuyển đổi (AI) · Phần IV Rà soát rủi ro. |
| `docs/gap/` | Phân tích khoảng cách (GAP v2.0). |
| `docs/to-do/` | Khuyến nghị hành động theo MVP (To-do v2.0). |
| `docs/to-be/` (workflow & UI-UX) | `Workflow-HLV.md`, `Workflow-KH.md` (luồng nghiệp vụ); `Objection-Handler_v1.0.md` (trợ lý xử lý băn khoăn/từ chối, ghép vào Workflow-HLV §1.3–1.5); `Empathy-Consultation_v1.0.md` (bản tư vấn theo hướng đồng cảm 5 lớp, ghép vào §1.3); `Conversational-Explainable-UX_v1.0.md` (nguyên lý xuyên suốt: tách lớp quyết định/diễn đạt, lớp "Vì sao?", companion chat — đưa "chất hội thoại" vào UI cố định); `UI-UX-HLV_v1.1.md`, `UI-UX-Lo-trinh-Dong-ho-sinh-hoc_v1.0.md` (đặc tả UI-UX); `customer-persona-disc-framework_v1.0.md`; case study `Huawei-Health-Clover-case-study.md`. |
| `docs/technical/` | Thiết kế kỹ thuật: `customer-persona-data-model_v1.0.md` (mô hình 2 bảng + ERD). |
| `docs/business-rules/` | `Calorie-Meal-Business-Rules-v1.1.md` (calo & bữa ăn 3 nhóm; **v1.1**: tầng Persona-fit — chế độ ăn/ngân sách/sở thích/quyền chủ động + Feasibility Score); `packaged-service-advice-v1.0.md` (đề xuất gói). |
| `docs/as-is/` (bổ sung) | `high-level-design.md` — HLD hệ thống hiện trạng. |
| `prototypes/` | Prototype HTML tương tác: `kh/` (màn Khách hàng), `hlv/` (màn HLV), `tabler-icons.min.css`. |
| `docs/references/` | Tài liệu gốc Quy trình 12 bước kinh doanh. |

> *Các bản v1.0 (To-be/GAP/To-do) và nghiên cứu khả thi v1.0 theo định hướng cũ (vận hành club) được giữ để tham khảo, đã lỗi thời so với định hướng DXP hiện tại.*

