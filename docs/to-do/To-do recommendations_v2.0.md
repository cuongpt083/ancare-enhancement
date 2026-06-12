# **KHUYẾN NGHỊ HÀNH ĐỘNG (TO-DO) — ANCARE DXP**

**Phiên bản:** v2.0 — *Theo định hướng DXP. Thay thế To-do v1.0.*
**Cơ sở:** GAP v2.0 (`docs/gap/GAP analysis report_v2.0.md`), To-be v2.0, As-Is v1.2.

> Mỗi hạng mục tham chiếu mã GAP gốc (CJ/BJ/TR/SD/PF). **DoD** = tiêu chí nghiệm thu tối thiểu. Đã loại bỏ mọi hạng mục POS/kho/quản trị kinh doanh (thuộc VNHUB).

---

## 0a. NỀN TẢNG — LA BÀN QUY TRÌNH 12 BƯỚC (PROCESS STATE MODEL)

> Đặc tả: `docs/to-be/To-be study report_v2.1 (consolidated).md (Phần II)`. Xương sống nối 4 module; ưu tiên dựng sớm.

### TD-PS1 — Process State Model (số hóa SĐD) *(PS1, MVP-1, nền tảng)*
- **Hành động:** Mô hình tiến trình 2 nhánh (Khách hàng 1→6, TV kinh doanh 6→12); mỗi người dùng có bước hiện tại + việc kế tiếp; API cho các module truy vấn/điều khiển.
- **DoD:** Xác định đúng bước của người dùng; trả về next action; các module đọc được trạng thái.
- **Phụ thuộc:** — (làm sớm).

### TD-PS2 — GNV (giấy nhắc việc) số hóa + cadence *(PS2, MVP-1)*
- **Hành động:** Danh sách việc/nhắc hằng ngày gắn bước hiện tại; theo dõi mức hoàn thành; thúc tần suất.
- **DoD:** Người dùng nhận GNV hằng ngày theo bước; có thống kê hoàn thành.
- **Phụ thuộc:** TD-PS1.

### TD-PS3 — Definition of Done theo bước *(PS3, MVP-2)*
- **Hành động:** Mã hóa tiêu chí hoàn thành mỗi bước (kiến thức %, đưa người đến 2/1, trải nghiệm…), trừ PPV/đơn hàng (VNHUB); kiểm tra & mở khóa bước sau.
- **DoD:** Bước chỉ "hoàn thành" khi đạt DoD; mở khóa bước kế tiếp theo đúng trình tự.
- **Phụ thuộc:** TD-PS1, (Module Đào tạo TD-2.1 cho ngưỡng kiến thức).

---

## 0. TRỌNG TÂM — TIỂU MÔ-ĐUN THU HÚT & CHUYỂN ĐỔI (AI), HỖ TRỢ BƯỚC 1 → ĐẦU BƯỚC 2

> Đặc tả: `docs/to-be/To-be study report_v2.1 (consolidated).md (Phần III)`. Đây là nhóm nhiệm vụ giúp AnCare thành công cụ đắc lực thực thi quy trình ở Bước 1–2. Các hạng mục được rải vào MVP theo độ ưu tiên/phụ thuộc.

### TD-AC1 — DSKHTN số hóa *(AC1, MVP-1)*
- **Hành động:** Danh sách KH tiềm năng số; import danh bạ/MXH; chống trùng; trạng thái phễu (Mới→Làm ấm→Đã mời→Nhận lời→Đến 2/1→Trải nghiệm).
- **DoD:** Tạo/nhập lead, chuyển trạng thái; không mất/không trùng lead; lọc theo nguồn nóng/ấm/lạnh.
- **Phụ thuộc:** —.

### TD-AC2 — La bàn quy trình + nhắc tần suất + đo phễu *(AC8, MVP-1)*
- **Hành động:** Hiển thị lead/khách đang ở chặng nào của Bước 1–2, việc cần làm tiếp; nhắc nhịp hành động; đo phễu kết nối→mời→nhận lời→đến 2/1→trải nghiệm.
- **DoD:** Mỗi lead có "vị trí + việc tiếp theo"; có nhắc cadence; dashboard phễu cập nhật.
- **Phụ thuộc:** TD-AC1.

### TD-AC3 — Đặt lịch & chuẩn bị cuộc gặp 2/1 *(AC5, MVP-1/2)*
- **Hành động:** Booking 2/1 (offline/Zoom); nhắc 3 bên (khách/TV/TAB); tự tổng hợp hồ sơ lead gửi TAB trước buổi gặp; ghi nhận kết quả.
- **DoD:** Đặt & nhắc được lịch; TAB nhận hồ sơ lead trước gặp; kết quả cập nhật vào phễu.
- **Phụ thuộc:** TD-AC1.

### TD-AC4 — Chấm điểm & ưu tiên lead (rule-based) *(AC2 — P1)*
- **Hành động:** Gắn thẻ phân khúc + pain point (chọn tay/quy tắc đơn giản); lead score = phù hợp × ấm theo quy tắc; danh sách "hôm nay nên tiếp cận ai".
- **DoD:** Mỗi lead có thẻ + điểm ưu tiên; danh sách ưu tiên hằng ngày. *(Chưa cần ML.)*
- **Phụ thuộc:** TD-AC1.

### TD-AC5 — Engine cá nhân hóa làm ấm & mời (phân tầng P1→P4)

> Bóc tách theo độ trưởng thành dữ liệu: P1–P2 chạy ngay (không cần ML); P3–P4 bật khi tích lũy đủ dữ liệu hành vi/chuyển đổi. DISC là *một thẻ phụ*, không phải trung tâm.

**TD-AC5-P1 — Thư viện kịch bản thông minh** *(AC3 — P1, MVP-2)*
- **Hành động:** Thư viện tin làm ấm/khơi gợi/lời mời, gắn thẻ theo DISC + **giai đoạn sẵn sàng thay đổi (Stage-of-Change)**; LLM chỉ *viết lại cho mượt/đúng tông*; HLV chọn & sửa; giữ "lập trường" kết nối (không pitch).
- **DoD:** HLV chọn được kịch bản theo thẻ; LLM cá nhân hóa tông giọng; tuân thủ quy tắc nội dung.
- **Phụ thuộc:** TD-AC1, (kho nội dung TD-2.4).

**TD-AC5-P2 — Copilot theo Phỏng vấn tạo động lực (MI)** *(AC3 — P2, MVP-2)*
- **Hành động:** LLM sinh gợi ý hội thoại theo tinh thần MI (hỏi mở, khẳng định, phản chiếu, gợi "lời nói thay đổi"), điều kiện theo giai đoạn sẵn sàng (set tay hoặc suy luận đơn giản).
- **DoD:** Gợi ý bám MI & đúng giai đoạn; được HLV đánh giá hữu ích; không mang tính thao túng.
- **Phụ thuộc:** TD-AC5-P1.

**TD-AC5-P3 — Chân dung động + khớp nội dung ngữ nghĩa** *(AC2/AC3 nâng cao — P3, MVP-3)*
- **Hành động:** Suy luận phong cách/giai đoạn từ hành vi (tự cập nhật); **RAG/embedding** lấy "câu chuyện/nội dung giống bạn"; look-alike từ khách đã chuyển đổi.
- **DoD:** Chân dung tự cập nhật theo hành vi; nội dung gợi ý khớp ngữ nghĩa pain point.
- **Phụ thuộc:** TD-AC5-P2, dữ liệu hành vi tích lũy (TD-AC2 đo phễu), kho nội dung TD-2.4.

**TD-AC5-P4 — Lớp tối ưu hóa (uplift + Next-Best-Action)** *(AC2 nâng cao — P4, sau MVP-3)*
- **Hành động:** Nâng lead scoring → **uplift/persuadable**; **Next-Best-Action bằng contextual bandit** tự tối ưu nội dung–thời điểm–kênh theo kết quả.
- **DoD:** Hệ thống ưu tiên nhóm "lay chuyển được"; bandit cải thiện tỷ lệ theo thời gian (A/B đo được).
- **Phụ thuộc:** TD-AC5-P3, **lịch sử chuyển đổi đủ lớn**.

### TD-AC9 — AI nhập vai luyện tập cho người mới *(song song, MVP-2)*
- **Hành động:** "Khách ảo" do AI đóng theo từng chân dung/giai đoạn để người mới tập làm ấm/mời; phản hồi & chấm điểm theo MI; ghép vào Module Đào tạo.
- **DoD:** Người mới tập được hội thoại với ≥3 kiểu khách ảo; nhận phản hồi cải thiện.
- **Phụ thuộc:** TD-AC5-P1 (thư viện kịch bản), (Module Đào tạo TD-2.1).

### TD-AC6 — Số hóa buổi trải nghiệm đầu (đầu Bước 2) *(AC7, MVP-2)*
- **Hành động:** Hồ sơ liền mạch lead→trải nghiệm (không nhập lại); checklist đón tiếp theo 10 vai trò BMO; OCR Tanita + AI gợi ý chế độ cá nhân hóa (nâng cấp).
- **DoD:** Khách mới được tạo từ lead không nhập lại; hoàn tất checklist buổi đầu; có gợi ý chế độ.
- **Phụ thuộc:** TD-AC1.

### TD-AC7 — Phễu thị trường lạnh + chatbot *(AC4, MVP-3)*
- **Hành động:** Landing/quiz sức khỏe thu lead + tự lập chân dung; chatbot AI sàng lọc, trả lời cơ bản, đặt lịch; luôn chuyển tư vấn sâu sang HLV/2/1.
- **DoD:** Quiz tạo lead có chân dung; chatbot sàng lọc & đặt được lịch; tuân thủ quy định nội dung sức khỏe.
- **Phụ thuộc:** TD-AC2, TD-AC4.

### TD-AC8 — Content-Attribution Matching (mô hình lai) *(AC6 + hợp nhất CJ4/CJ7)*

> Matching CHÍNH = gắn lead theo công sức thu hút bằng nội dung; thuật toán chỉ là fallback. Triển khai theo 2 lớp.

**TD-AC8a — Mã giới thiệu & attribution theo nội dung** *(MVP-2)*
- **Hành động:** Mỗi HLV có mã giới thiệu/deep-link; gắn vào nội dung HLV sáng tạo/chỉnh sửa & chia sẻ; khách tương tác/đăng ký qua nội dung → tự gắn (attribution) về HLV. Quy tắc: hành động ý nghĩa đầu tiên; khách có quyền chọn/đổi HLV; chống "poaching" khách đã có HLV; chống gian lận tương tác ảo.
- **DoD:** Lead vào qua nội dung của HLV được gắn đúng HLV; khách đổi được HLV; có log lý do gắn (minh bạch); phát hiện bất thường cơ bản.
- **Phụ thuộc:** TD-AC1, TD-1.3 (chia sẻ nội dung), TD-2.4 (kho nội dung).

**TD-AC8b — Phân tích hiệu quả nội dung cho HLV** *(MVP-2/3)*
- **Hành động:** Dashboard "nội dung nào của tôi đang hút khách" (lượt xem/tương tác/lead/chuyển đổi theo từng nội dung); AI gợi ý nên làm nội dung gì cho phân khúc nào.
- **DoD:** HLV xem được hiệu quả từng nội dung; nhận gợi ý nội dung tiếp theo.
- **Phụ thuộc:** TD-AC8a.

**TD-AC8c — Matching thuật toán fallback (lead mồ côi)** *(MVP-3)*
- **Hành động:** Lead inbound không có người giới thiệu → pool chung → phân phối công bằng theo khu vực/chuyên môn DMO/tải khách; khách ở xa tìm nhà vận hành gần (plug-in).
- **DoD:** Lead mồ côi được phân phối công bằng; có luồng plug-in cho khách ở xa.
- **Phụ thuộc:** TD-AC8a, TD-AC4.

---

## 1. MVP-1 — LAN TỎA & GẮN KẾT (+ NỀN TẢNG PHỄU)

> Mục tiêu: tạo giá trị engagement nhanh trên nền dữ liệu/tính năng đã có; dựng xương sống thu hút/chuyển đổi (TD-AC1, TD-AC2, TD-AC3).

### TD-1.1 — Hạ tầng thông báo đẩy *(PF1, nền tảng)*
- **Hành động:** Tích hợp push (FCM/APNs); cấu hình loại thông báo, lịch gửi, opt-in/out.
- **DoD:** Gửi được push theo lịch/sự kiện tới đúng thiết bị; người dùng bật/tắt được.
- **Phụ thuộc:** — (làm đầu tiên).

### TD-1.2 — Nhắc nhở chủ động cho khách hàng *(CJ3)*
- **Hành động:** Nhắc bữa ăn/nước/thói quen theo khung giờ lộ trình; khách tinh chỉnh giờ.
- **DoD:** Khách nhận nhắc đúng khung; chỉnh giờ được; có thống kê tỷ lệ phản hồi.
- **Phụ thuộc:** TD-1.1.

### TD-1.3 — Tạo & chia sẻ câu chuyện thành công ra MXH *(CJ4)*
- **Hành động:** Tự sinh ảnh/infographic hành trình (đồ thị tiến độ + cột mốc + thông điệp) giàu cảm xúc; 1 chạm chia sẻ; tuân thủ quy định thương hiệu/sức khỏe.
- **DoD:** Sinh được bản chia sẻ từ dữ liệu thật; chia sẻ thành công ra ít nhất 1 nền tảng MXH; có kiểm duyệt nội dung nhạy cảm.
- **Phụ thuộc:** —.

### TD-1.4 — Chăm sóc khách theo dịp đặc biệt (HLV) *(BJ2)*
- **Hành động:** Nhắc HLV dịp sinh nhật/kỷ niệm/lễ; gợi ý lời động viên khi khách xuống tinh thần (dựa tín hiệu giảm tương tác); mẫu tin nhanh.
- **DoD:** Danh sách nhắc sinh đúng đối tượng/đúng ngày; HLV gửi được lời chăm sóc từ mẫu.
- **Phụ thuộc:** TD-1.1.

### TD-1.5 — Trải nghiệm gia hạn gói mềm hơn *(CJ9)*
- **Hành động:** Thay chặn cứng bằng thông báo gia hạn + cho phép xem dữ liệu/đọc nội dung khi hết hạn (giới hạn ghi); kênh gia hạn rõ ràng.
- **DoD:** Khi hết gói, khách vẫn xem được tiến độ & nhận hướng dẫn gia hạn thay vì bị chặn hoàn toàn.
- **Phụ thuộc:** —.

### TD-1.6 — Đo lường engagement & lan tỏa *(PF3)*
- **Hành động:** Theo dõi lượt chia sẻ, tỷ lệ phản hồi nhắc nhở, tần suất mở app.
- **DoD:** Chỉ số hiển thị nội bộ, cập nhật định kỳ — làm baseline cho MVP sau.
- **Phụ thuộc:** TD-1.2, TD-1.3.

---

## 2. MVP-2 — HỌC TẬP & NỘI DUNG

> Mục tiêu: dựng Module Đào tạo và kho nội dung — phần "lấp khoảng trống" cốt lõi.

### TD-2.1 — Hạ tầng micro-course (LMS nhẹ) *(TR1, nền tảng)*
- **Hành động:** Tạo/quản lý khóa ngắn (bài học, media, quiz), theo dõi tiến độ học, chứng nhận hoàn thành.
- **DoD:** Tạo được một micro-course nhiều bài; học viên hoàn thành và hệ thống ghi nhận tiến độ.
- **Phụ thuộc:** —.

### TD-2.2 — Gamification học tập *(TR4)*
- **Hành động:** Điểm/huy hiệu, thi đua, bảng xếp hạng cho hoạt động học.
- **DoD:** Hoàn thành khóa sinh điểm/huy hiệu; bảng xếp hạng hoạt động.
- **Phụ thuộc:** TD-2.1.

### TD-2.3 — Nội dung chuyên sâu theo nhóm KH đặc thù *(TR2)*
- **Hành động:** Biên soạn/đưa lên khóa cho nhóm thừa-thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, thai sản…
- **DoD:** Có ít nhất một bộ khóa cho 3+ nhóm; gắn nhãn theo nhu cầu.
- **Phụ thuộc:** TD-2.1.

### TD-2.4 — Thư viện nội dung cho khách hàng *(TR3, CJ5)*
- **Hành động:** Bài viết kiến thức, video tập luyện, công thức nấu ăn, lời khuyên chuyên gia, câu chuyện thành công; tìm kiếm & phân loại.
- **DoD:** Khách tìm và xem được nội dung theo chủ đề; nội dung cho khách tiềm năng truy cập được.
- **Phụ thuộc:** TD-2.1 (tái dùng hạ tầng nội dung).

### TD-2.5 — Bộ nội dung & công cụ chia sẻ cho HLV (prospecting) *(BJ3)*
- **Hành động:** Thư viện nội dung sản phẩm/giải pháp/cơ hội KD để HLV chia sẻ cho khách tiềm năng/người thân.
- **DoD:** HLV chọn và chia sẻ được nội dung qua kênh phổ biến; theo dõi lượt mở.
- **Phụ thuộc:** TD-2.4.

### TD-2.6 — Luồng nội dung phễu cho khách tiềm năng *(SD2)*
- **Hành động:** Trang/luồng giới thiệu sản phẩm/giải pháp/cơ hội KD + câu chuyện thành công cho người chưa mua gói.
- **DoD:** Khách tiềm năng truy cập được luồng phễu mà không cần tài khoản đầy đủ.
- **Phụ thuộc:** TD-2.4.

### TD-2.8b — Pipeline 12 bước cấp quản lý *(BJ6)*
- **Hành động:** Cho HLV/bảo trợ xem toàn bộ khách & tuyến dưới đang ở bước nào (gắn PSM), ai cần hành động gì hôm nay.
- **DoD:** Danh sách khách/tuyến dưới theo bước; gợi ý hành động ưu tiên.
- **Phụ thuộc:** TD-PS1.

### TD-2.9 — Ánh xạ micro-course với giáo trình quy trình + cổng kiến thức *(TR5, TR6)*
- **Hành động:** Tạo các khóa khớp giáo trình (21 talking points, Khai mở, HLCB1/2, BMO, Cầm tay chỉ việc); playlist "đọc/xem/nghe" theo bước; ngưỡng 70/80/90% làm cổng (gắn DoD TD-PS3).
- **DoD:** Hoàn thành khóa + đạt ngưỡng → mở khóa bước kế; playlist hiển thị đúng bước.
- **Phụ thuộc:** TD-2.1, TD-PS3.

> **Lưu ý phạm vi:** AnCare KHÔNG tích hợp kỹ thuật với VNHUB/các app Herbalife (không SSO, không đồng bộ dữ liệu). AnCare là ứng dụng độc lập, chỉ bổ trợ về phạm vi (không làm POS/kho/quản trị kinh doanh).

---

## 3. MVP-3 — PHỄU & CÁ NHÂN HÓA

> Mục tiêu: hoàn thiện vòng tròn thu hút–kết nối–cá nhân hóa. Phức tạp nhất.

### TD-3.1 — Kết nối khách tiềm năng ↔ HLV (matching) *(CJ6)*
- **Hành động:** Cơ chế gợi ý/ghép HLV theo khu vực, chuyên môn DMO, tải khách; luồng tiếp nhận quan tâm.
- **DoD:** Khách tiềm năng bày tỏ quan tâm → được ghép & kết nối với HLV phù hợp.
- **Phụ thuộc:** TD-2.6.

### TD-3.2 — Vòng lặp giới thiệu (referral) *(CJ7)*
- **Hành động:** Mời bạn bè/người thân, theo dõi trạng thái giới thiệu, ghi nhận nguồn.
- **DoD:** Tạo & chia sẻ lời mời; hệ thống quy được khách mới về người giới thiệu.
- **Phụ thuộc:** TD-1.3 (chia sẻ), TD-3.1.

### TD-3.3 — Buổi sinh hoạt HOM *(CJ8)*
- **Hành động:** Lịch HOM, chủ đề, đăng ký tham gia, nhắc nhở.
- **DoD:** Khách xem lịch & đăng ký HOM; nhận nhắc trước buổi.
- **Phụ thuộc:** TD-1.1.

### TD-3.4 — Gợi ý thông minh cá nhân hóa *(SD1)*
- **Hành động:** Recommender nội dung/khóa học theo dữ liệu sức khỏe, thói quen, mục tiêu, hành vi; xử lý cold-start.
- **DoD:** Mỗi người dùng nhận gợi ý cá nhân hóa có liên quan; có cơ chế khởi đầu khi thiếu dữ liệu.
- **Phụ thuộc:** TD-2.1, TD-2.4 (cần kho nội dung), TD-1.6 (dữ liệu hành vi).

### TD-3.5 — Lộ trình phát triển & thăng tiến cho HLV *(BJ4, SD3)*
- **Hành động:** Learning path có điều kiện + tài liệu; liên kết kế hoạch trả thưởng Herbalife.
- **DoD:** HLV thấy lộ trình theo mục tiêu, điều kiện mở khóa, tài liệu tham khảo.
- **Phụ thuộc:** TD-2.1.

### TD-3.6 — Công cụ vận hành DMO (đặc thù trải nghiệm club) *(BJ5)*
- **Hành động:** Công cụ vận hành theo mô hình club (chuyên sâu/vận động/Spa) tập trung vào trải nghiệm tại Nhóm dinh dưỡng — không làm POS/kho/quản trị kinh doanh (thuộc VNHUB).
- **DoD:** HLV vận hành được đặc thù trải nghiệm club; không lấn sang nghiệp vụ kinh doanh của VNHUB.
- **Phụ thuộc:** —.

### TD-3.7 — Coaching tuyến dưới (duplication) *(BJ7)*
- **Hành động:** Khung Tell–Show–Try–Do; theo dõi tiến độ TV mới qua Bước 6–12 (phần phi tài chính); nhắc bảo trợ đồng hành.
- **DoD:** Bảo trợ xem & hỗ trợ được tiến độ từng TV tuyến dưới theo bước.
- **Phụ thuộc:** TD-PS1.

### TD-3.8 — Lộ trình thăng tiến tới GSV + kỹ năng lãnh đạo *(SD4, SD5)*
- **Hành động:** Trực quan hóa lộ trình tới Giám sát viên (mở khóa theo mốc, gắn PSM nhánh 6–12); khóa kỹ năng lãnh đạo/bảo trợ.
- **DoD:** HLV thấy lộ trình thăng tiến & điều kiện; truy cập khóa lãnh đạo phù hợp vị trí.
- **Phụ thuộc:** TD-PS1, TD-2.1.

---

## 4. SƠ ĐỒ THỨ TỰ (TÓM TẮT)

```
Nền tảng (PSM):  TD-PS1 → TD-PS2 ; {TD-PS1, TD-2.1} → TD-PS3
Thu hút & Chuyển đổi (AC):
        TD-AC1 → {TD-AC2, TD-AC3, TD-AC4, TD-AC6}
        TD-AC4 → {TD-AC8} ; {TD-AC2,TD-AC4} → TD-AC7
        Engine cá nhân hóa (theo độ trưởng thành dữ liệu):
          TD-AC5-P1 → TD-AC5-P2 → TD-AC5-P3 → TD-AC5-P4
          (P1 cần kho nội dung TD-2.4 ; P3 cần dữ liệu hành vi ; P4 cần lịch sử chuyển đổi)
          TD-AC5-P1 → TD-AC9 (nhập vai luyện tập)

MVP-1:  TD-PS1 → TD-PS2
        TD-1.1 → {TD-1.2, TD-1.4} ; TD-1.3 ; TD-1.5 ; {TD-1.2,TD-1.3} → TD-1.6
        TD-AC1 → {TD-AC2, TD-AC3, TD-AC4}
MVP-2:  TD-2.1 → {TD-2.2, TD-2.3, TD-2.4} → {TD-2.5, TD-2.6}
        {TD-PS1,TD-2.1} → TD-PS3 → TD-2.9 ; TD-PS1 → TD-2.8b
        TD-AC5-P1 → TD-AC5-P2 ; TD-AC9 ; TD-AC6
MVP-3:  TD-2.6 → TD-3.1 → TD-3.2 ; TD-1.1 → TD-3.3 ;
        {TD-2.1,TD-2.4,TD-1.6} → TD-3.4 ; TD-2.1 → TD-3.5 ; TD-3.6 (độc lập)
        TD-PS1 → {TD-3.7, TD-3.8} ; TD-AC7 ; TD-AC5-P3
        {TD-AC1,TD-1.3,TD-2.4} → TD-AC8a → {TD-AC8b, TD-AC8c}  (TD-AC8a/b ở MVP-2; TD-AC8c ở MVP-3)
Sau MVP-3:  TD-AC5-P4 (cần lịch sử chuyển đổi đủ lớn)
```

---

## 5. KHUYẾN NGHỊ TRIỂN KHAI

1. **Dựng nền tảng PSM (TD-PS1) sớm nhất:** đây là xương sống mọi module cắm vào; làm cùng nhóm MVP-1 lan tỏa/gắn kết để tận dụng dữ liệu/tính năng đã có (tracking, chat, đồ thị).
2. **AnCare độc lập, không tích hợp Herbalife:** không đầu tư SSO/đồng bộ dữ liệu; tự quản lý tài khoản & dữ liệu người dùng.
3. **Đảm bảo nguồn nội dung trước khi xây LMS:** Module Đào tạo vô nghĩa nếu thiếu nội dung chất lượng — chuẩn bị quy trình sản xuất & kiểm duyệt song song TD-2.1.
4. **PoC cho hạng mục công sức cao:** micro-course (TD-2.1), matching (TD-3.1), recommender (TD-3.4).
5. **Tuân thủ quy định chia sẻ sức khỏe (TD-1.3):** rà soát pháp lý & thương hiệu trước khi mở chia sẻ MXH.
6. **Cài đo lường engagement (TD-1.6) ngay từ MVP-1** để có baseline.

---

## 6. KẾT THÚC QUY TRÌNH

Chuỗi tài liệu phiên bản DXP: README (tầm nhìn) → As-Is v1.2 → To-be v2.0 → GAP v2.0 → To-do v2.0. Bước tiếp theo khả dĩ: nghiên cứu khả thi v2.0 cho lộ trình DXP, hoặc thiết kế chi tiết từng module.
