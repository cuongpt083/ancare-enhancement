# **BÁO CÁO THIẾT KẾ TRẠNG THÁI MỤC TIÊU (TO-BE) — ANCARE DXP**
## *(Bản hợp nhất v2.1 — gộp To-be v2.0 + 3 đặc tả/phụ lục liên quan)*

**Phiên bản:** v2.1 (hợp nhất). Gộp: To-be study report v2.0, đặc tả tiểu mô-đun Thu hút & Chuyển đổi (AI), đặc tả Process State Model (La bàn 12 bước), và Rà soát rủi ro số hóa MLM sang DXP tập trung.
**Đối tượng đọc:** BA, PO/PM, Đội phát triển, Ban lãnh đạo sản phẩm.
**Cơ sở:** README.md (tầm nhìn/sứ mệnh/giá trị/4 module), As-Is v1.2, `docs/references/01.Quy-trinh-12-buoc-kinh-doanh.md`.

### MỤC LỤC
- **Phần I — Báo cáo To-be tổng thể** (định vị, persona, 4 module, lộ trình MVP)
- **Phần II — Đặc tả: La bàn Quy trình 12 bước (Process State Model)** — xương sống nền tảng
- **Phần III — Đặc tả: Tiểu mô-đun Thu hút & Chuyển đổi khách hàng (AI-assisted)** — Bước 1→2
- **Phần IV — Rà soát rủi ro số hóa MLM sang DXP tập trung** (R1–R15 + nguyên tắc giảm thiểu)

---
---

# PHẦN I — BÁO CÁO TO-BE TỔNG THỂ

> **Thay đổi định hướng cốt lõi so với v1.0:** AnCare KHÔNG còn định vị là công cụ vận hành Nutrition Club. AnCare là **nền tảng trải nghiệm số (DXP)** về chăm sóc sức khỏe chủ động. **Loại khỏi phạm vi:** POS bán lẻ, quản lý kho, dashboard quản trị kinh doanh cho Nhà sáng lập — các năng lực này đã có ở **VNHUB** của Herbalife. AnCare **bổ trợ**, không trùng lặp, và **không tích hợp kỹ thuật** với hệ sinh thái Herbalife.

## I.1. ĐỊNH VỊ & MỤC TIÊU TÁI HÌNH DUNG

### Định vị "lấp khoảng trống"
AnCare DXP nằm giữa hai cụm ứng dụng của Herbalife: nhóm phục vụ HLV/đối tác kinh doanh (VNHUB, Herbalife Learning, Herbalife SHOP) và nhóm phục vụ khách hàng tương lai (Pro2col). Khoảng trống mà AnCare lấp đầy: **bám sát trải nghiệm thực tế tại Nhóm dinh dưỡng và thấu hiểu văn hóa, tâm lý của nhiều phân khúc khách hàng Việt Nam** — điều các app hiện tại chưa làm tốt.

### Mục tiêu hướng đến
AnCare DXP là **cầu nối** đưa khách hàng tiềm năng và khách hàng hiện tại vào hệ sinh thái chăm sóc sức khỏe chủ động, qua bốn vai trò giá trị: (a) công cụ chăm sóc sức khỏe chủ động & nguồn cảm hứng; (b) phễu thu hút và bệ phóng phát triển bản thân/cơ hội kinh doanh nhân văn; (c) nền tảng giao tiếp & kết nối HLV–khách–cộng đồng; (d) không gian học tập (đào tạo micro-course, gamification).

Trọng tâm trải nghiệm chuyển từ "quản lý vận hành" sang **gắn kết (engagement), lan tỏa (virality), cá nhân hóa (personalization) và học tập (learning)**.

## I.2. PERSONA MỤC TIÊU

| Persona | Vai trò trong DXP | Trọng tâm trải nghiệm |
| :-- | :-- | :-- |
| **Khách hàng tiềm năng** | Người quan tâm sức khỏe, chưa mua gói | Kiến thức sinh động dễ hiểu, câu chuyện thành công, kết nối với HLV phù hợp |
| **Khách hàng (thành viên club)** | Đang trải nghiệm lộ trình | Theo dõi sức khỏe, nội dung đồng hành, cộng đồng/HOM, chia sẻ & lan tỏa |
| **Huấn luyện viên dinh dưỡng (HLV)** | Vận hành club, tư vấn, kinh doanh | Phát triển kỹ năng/sự nghiệp, chăm sóc khách hàng, chia sẻ nội dung thu hút, công cụ vận hành bổ trợ VNHUB |

> *Persona "Nhà sáng lập với góc nhìn quản trị kinh doanh" rời khỏi phạm vi AnCare (thuộc VNHUB).*

## I.3. NĂNG LỰC MỤC TIÊU THEO 4 MODULE

Ký hiệu: **[ĐÃ CÓ]** tái sử dụng từ app hiện tại · **[NÂNG CẤP]** mở rộng cái đã có · **[MỚI]** xây mới.

### Năng lực nền tảng — La bàn Quy trình 12 bước (Process State Model)
> **Xương sống xuyên suốt 4 module.** Chi tiết ở **Phần II**. PSM số hóa **Sơ đồ dẫn (SĐD)** — một trong 3 công cụ KD cốt lõi. Với mỗi người dùng, PSM xác định **bước hiện tại** (nhánh Khách hàng 1→6, nhánh Thành viên KD 6→12) rồi điều khiển: việc cần làm tiếp theo, nội dung/khóa học đề xuất (Module 3/4), hành động chăm sóc của HLV (Module 2), và kiểm tra Definition of Done của bước. Cùng PSM là số hóa **GNV (giấy nhắc việc)** và **DSKHTN** → đủ bộ 3 công cụ KD.

### Module 1 — Hành trình khách hàng (Customer Journey)
> **Tiểu mô-đun trọng tâm — Thu hút & Chuyển đổi (AI-assisted), hỗ trợ Bước 1 → đầu Bước 2.** Chi tiết ở **Phần III**.

- **[MỚI]** Kho nội dung kiến thức sức khỏe/sản phẩm/thói quen tốt — sinh động, cô đọng, dễ hiểu, dành cho khách tiềm năng.
- **[MỚI]** **Động cơ thu hút bằng nội dung + gắn lead theo công sức (Content-Attribution Matching).** Hợp nhất "matching", "chia sẻ câu chuyện thành công" và "vòng lặp giới thiệu" thành một bánh đà:
  - HLV **chủ động sáng tạo/chỉnh sửa nội dung** và chia sẻ kèm **mã giới thiệu/deep-link** riêng.
  - Khách tương tác/đăng ký qua nội dung đó → **tự gắn (attribution) về HLV** — lead *kiếm được bằng công sức*, không bị nền tảng phân phối tùy ý. Đây là cơ chế matching **chính**.
  - **Matching thuật toán chỉ là fallback** cho lead "mồ côi" (inbound lạnh): phân phối công bằng theo khu vực/chuyên môn DMO/tải khách.
  - Khách **luôn có quyền chọn/đổi HLV**; quy tắc xử lý tranh chấp (hành động ý nghĩa đầu tiên), chống "poaching", chống gian lận.
  - AI **giúp HLV thắng công bằng** — gợi ý nội dung cho phân khúc, copilot chỉnh sửa, phân tích "nội dung nào của tôi đang hút khách".
- **[ĐÃ CÓ]** Công cụ tự theo dõi sức khỏe/dinh dưỡng/thói quen (log bữa ăn, nước, ngủ, chỉ số, tiến độ, streak).
- **[ĐÃ CÓ]** Nội dung động viên/gợi ý từ HLV; chat 1-1; cộng đồng.
- **[MỚI]** Thông tin & tham gia **buổi sinh hoạt HOM** (chủ đề dinh dưỡng/lối sống/kinh doanh).

### Module 2 — Hành trình kinh doanh (dành cho HLV)
- **[ĐÃ CÓ]** Quản lý khách hàng, theo dõi & hỗ trợ đạt mục tiêu (CRM/onboarding/journey builder/báo cáo).
- **[MỚI]** **Chăm sóc khách hàng theo thời điểm đặc biệt** (sinh nhật, kỷ niệm, lễ) + động viên khi khách xuống tinh thần.
- **[MỚI]** **Chia sẻ nội dung sản phẩm/giải pháp/cơ hội kinh doanh** cho khách tiềm năng & người thân (prospecting).
- **[MỚI]** Định hướng **phát triển kỹ năng & lộ trình thăng tiến** trong kế hoạch trả thưởng Herbalife.
- **[NÂNG CẤP]** Công cụ **vận hành Nhóm dinh dưỡng theo nhiều mô hình DMO** — tập trung trải nghiệm tại club, không làm POS/kho/quản trị (VNHUB).
- **[MỚI]** **Pipeline 12 bước cấp quản lý:** khách & tuyến dưới đang ở bước nào, ai cần hành động gì hôm nay (gắn PSM).
- **[MỚI]** **Số hóa GNV + SĐD** (= PSM) → đủ bộ 3 công cụ KD dùng hằng ngày.
- **[MỚI]** **Coaching tuyến dưới (duplication):** Tell–Show–Try–Do + theo dõi tiến độ TV mới qua Bước 6–12 (phi tài chính).

### Module 3 — Đào tạo (Training)
- **[MỚI]** **Micro-course** về dinh dưỡng, sản phẩm, huấn luyện, tư vấn.
- **[MỚI]** Nội dung chuyên sâu theo **nhóm KH đặc thù** (thừa/thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, thai sản…).
- **[MỚI]** Thư viện cho khách: bài viết, **video tập luyện, công thức nấu ăn lành mạnh**, lời khuyên chuyên gia, câu chuyện thành công.
- **[MỚI]** **Gamification học tập:** thi đua, tranh tài, bảng xếp hạng.
- **[MỚI]** **Ánh xạ micro-course 1:1 với giáo trình quy trình:** 21 talking points, Khai mở, HLCB1, HLCB2, Định hướng BMO, Cầm tay chỉ việc; ngưỡng 70/80/90% làm điều kiện hoàn thành bước (gắn PSM).
- **[MỚI]** **Playlist "đọc/xem/nghe" theo từng bước** + hỗ trợ Tell–Show–Try–Do cho Bước 8–11.

### Module 4 — Phát triển bản thân (Self-development)
- **[MỚI]** **Gợi ý thông minh cá nhân hóa** nội dung/khóa học theo dữ liệu sức khỏe, thói quen, mục tiêu, hành vi.
- **[MỚI]** Nội dung giới thiệu sản phẩm/giải pháp/cơ hội kinh doanh cho **khách tiềm năng** (phễu).
- **[MỚI]** Với HLV: **lộ trình đào tạo có điều kiện/tài liệu tham khảo**.
- **[MỚI]** **Lộ trình thăng tiến tới Giám sát viên** (kế hoạch trả thưởng) trực quan, mở khóa từng mốc (gắn PSM nhánh 6–12).
- **[MỚI]** Khóa **kỹ năng lãnh đạo/bảo trợ**; gợi ý "việc/khóa tiếp theo" theo vị trí trên la bàn.

## I.4. NGUYÊN TẮC THIẾT KẾ
1. **Bám sát thực tế Nhóm dinh dưỡng & văn hóa Việt Nam.**
2. **Engagement & cảm hứng trước, công cụ sau.**
3. **Virality gắn vào hành trình** — mọi cột mốc tích cực đều dễ biến thành nội dung chia sẻ.
4. **Cá nhân hóa xuyên suốt.**
5. **Độc lập & không trùng lặp Herbalife apps** — không tích hợp kỹ thuật với VNHUB; không làm POS/kho/quản trị kinh doanh.

## I.5. NĂNG LỰC NGOÀI PHẠM VI (OUT OF SCOPE)
- POS bán lẻ & đối soát thu/chi — *thuộc VNHUB.*
- Quản lý kho — *thuộc VNHUB.*
- Dashboard quản trị kinh doanh/lời-lỗ cho Nhà sáng lập — *thuộc VNHUB.*

> Các điểm đau P1/P2 (bán lẻ/kho) và F1–F4 (quản trị kinh doanh) trong As-Is **chuyển giao cho VNHUB**, không nằm trong To-be AnCare.

## I.6. LỘ TRÌNH MVP (đề xuất)
- **MVP-1 — Nền tảng PSM + Lan tỏa & Gắn kết:** dựng PSM/GNV; chia sẻ câu chuyện thành công ra MXH, nhắc nhở chủ động (push), chăm sóc khách theo dịp; nền tảng phễu (DSKHTN số, đặt lịch 2/1, la bàn quy trình). *Tận dụng dữ liệu/tính năng đã có.*
- **MVP-2 — Học tập, Nội dung & AI hỗ trợ chuyển đổi:** Module Đào tạo micro-course + gamification, kho nội dung; AI lập chân dung/copilot làm ấm & mời (P1-P2), số hóa buổi trải nghiệm đầu, pipeline 12 bước, attribution nội dung.
- **MVP-3 — Phễu lạnh, Matching fallback, Cá nhân hóa, Nhân bản & Sự nghiệp:** chatbot phễu lạnh, matching fallback lead mồ côi, recommender, HOM, coaching tuyến dưới, lộ trình thăng tiến.
- **Sau MVP-3:** lớp tối ưu hóa AI (uplift + Next-Best-Action) khi đủ dữ liệu chuyển đổi.

## I.7. ĐIỂM CẦN LÀM RÕ TIẾP
> **Đã chốt:** AnCare **độc lập**, KHÔNG tích hợp kỹ thuật (SSO/đồng bộ dữ liệu) với VNHUB/Learning/SHOP/Pro2col.

- Nguồn & quy trình kiểm duyệt nội dung đào tạo (ai sản xuất micro-course, chuyên gia nào).
- Chính sách chia sẻ MXH (thương hiệu, tuân thủ quy định quảng cáo/khẳng định sức khỏe).

---
---

# PHẦN II — ĐẶC TẢ: LA BÀN QUY TRÌNH 12 BƯỚC (PROCESS STATE MODEL)
## *(Xương sống xuyên suốt 4 module — hỗ trợ thực thi Bước 1 → 12)*

## II.1. Ý TƯỞNG CỐT LÕI
Quy trình 12 bước là một **đường ống chuyển đổi + nhân bản đào tạo theo trình tự**. Để AnCare thành công cụ đắc lực thực thi quy trình, cần **một mô hình tiến trình duy nhất (PSM)** làm xương sống, điều khiển cả 4 module thay vì để mỗi module rời rạc. PSM số hóa chính **Sơ đồ dẫn (SĐD)** — viên gạch khóa kết nối toàn hệ thống.

### Hai nhánh trạng thái
- **Nhánh Khách hàng (Bước 1→6):** KHTN → đến 2/1 → trải nghiệm BMO → KH hạnh phúc → Đại sứ sức khỏe → (nếu muốn KD) Khai mở → Thành viên kinh doanh.
- **Nhánh Thành viên kinh doanh (Bước 6→12):** TV mới → HLCB1 → HLCB2 → Định hướng BMO → Cầm tay chỉ việc → Đồng vận hành → Giám sát viên vận hành độc lập.

Một người có thể chuyển từ nhánh 1 sang nhánh 2 tại Bước 5–6.

### PSM điều khiển gì
Với mỗi người dùng, PSM xác định **bước hiện tại** và tự động: (1) hiển thị việc cần làm tiếp theo; (2) đề xuất nội dung/khóa học phù hợp bước (Module 3/4); (3) kích hoạt hành động chăm sóc cho HLV/bảo trợ (Module 2); (4) kiểm tra Definition of Done (DoD) của bước.

### Definition of Done theo bước
Mỗi bước có DoD lấy từ tài liệu, ví dụ: Bước 2 (kết quả SK trong 10 ngày + thuộc >70% 10 bài dinh dưỡng); Bước 4 (đưa ≥1 người đến 2/1 + >80% 21 bài); Bước 5 (>90% 21 bài + đưa ≥2 người + ra quyết định KD)…

> **Ranh giới:** tiêu chí **điểm cá nhân (PPV), số đơn hàng** thuộc VNHUB — PSM **không** quản lý phần tài chính này; PSM bám phần **trải nghiệm – kiến thức – quan hệ – hành động**. Có thể nhập tay mốc tài chính nếu cần, nhưng không tích hợp VNHUB.

## II.2. THAY ĐỔI THEO TỪNG MODULE ĐỂ BÁM QUY TRÌNH

**Module 1 (Bước 3–4, nối tiếp AC ở Bước 1–2):** Talking points + quiz gắn trong app khách, ngưỡng 70/80/90% làm cổng mở khóa; tự phát hiện cột mốc "khách hạnh phúc" → nhắc nâng cấp Đại sứ sức khỏe; nối tiêu chí "đưa ≥1/≥2 người đến 2/1" vào phễu referral; lịch & đăng ký HOM.

**Module 2 (Bước 3–12):** Pipeline 12 bước cấp quản lý; số hóa 3 công cụ KD (GNV, DSKHTN, SĐD=PSM); coaching tuyến dưới Tell–Show–Try–Do; chăm sóc theo dịp.

**Module 3 (trục xương sống Bước 2–12):** Ánh xạ micro-course 1:1 giáo trình; playlist "đọc/xem/nghe" theo bước gắn DoD; nội dung chuyên sâu theo nhóm KH đặc thù; gamification + ngưỡng kiến thức; hỗ trợ Tell–Show–Try–Do (Bước 8–11).

**Module 4 (Bước 5–12):** Lộ trình thăng tiến tới GSV (mở khóa từng mốc); gợi ý cá nhân hóa "việc/khóa tiếp theo"; khóa kỹ năng lãnh đạo/bảo trợ.

## II.3. THƯỚC ĐO THÀNH CÔNG
- **Tỷ lệ tiến bước:** % người dùng chuyển từ bước n → n+1 (phễu 12 bước).
- **Thời gian trung bình mỗi bước** & điểm nghẽn.
- **Tuân thủ tần suất:** mức hoàn thành GNV hằng ngày.
- **Hiệu quả nhân bản:** số TV tuyến dưới đạt từng mốc Bước 6–12.

## II.4. RÀNG BUỘC & PHỤ THUỘC
- Độc lập Herbalife apps; điểm PPV/đơn hàng thuộc VNHUB.
- Lớp live vẫn live; PSM/Module 3 bổ trợ, không thay.
- Phụ thuộc nội dung: Module 3/4 cần kho micro-course & tài liệu theo bước.
- **PSM là nền:** AC (Bước 1–2) và thay đổi Module 2/3/4 (Bước 3–12) đều cắm vào PSM → ưu tiên dựng khung PSM sớm.

---
---

# PHẦN III — ĐẶC TẢ: TIỂU MÔ-ĐUN THU HÚT & CHUYỂN ĐỔI KHÁCH HÀNG (AI-ASSISTED)
## *(Hỗ trợ Bước 1 → Giai đoạn đầu Bước 2)*

## III.1. BỐI CẢNH & VẤN ĐỀ
Bước 1 (đưa KHTN/TVTN đến cuộc gặp 2/1) và đầu Bước 2 là **nút thắt khi quy mô tăng** và **rào cản lớn nhất với người mới** ("không biết tìm ai, nói gì, mời thế nào"). Mục tiêu: biến AnCare thành **trợ lý phát triển khách hàng** số hóa & có AI hỗ trợ, năng suất cao, rào cản thấp — giữ đúng vai trò con người và tuân thủ.

### Nguyên tắc nền (bám quy trình)
- **Người mới chỉ KẾT NỐI**, không tư vấn/bán sản phẩm — thuyết phục sâu do TAB ở cuộc gặp 2/1. AI không thay người mới đi pitch.
- **Tần suất & tuân thủ là yếu tố quyết định.**
- **Bám 3 công cụ KD:** DSKHTN, GNV, SĐD.
- **Tôn trọng văn hóa Việt:** quan hệ ấm, cá nhân hóa, không spam.

## III.2. CÁC NĂNG LỰC

**DSKHTN số hóa:** danh sách KH tiềm năng theo quy trình 3 bước; nhập từ danh bạ/MXH; chống trùng; thẻ nguồn (nóng/ấm/lạnh); trạng thái phễu (Mới → Làm ấm → Đã mời → Nhận lời → Đến 2/1 → Trải nghiệm).

**Lập chân dung & chấm điểm lead:** AI gợi ý phân khúc + "nỗi đau"; lead score = phù hợp × ấm; gợi ý "hôm nay nên tiếp cận ai".

**Engine cá nhân hóa làm ấm & mời (phân tầng P1→P4, theo độ trưởng thành dữ liệu; DISC chỉ là thẻ phụ):**
- **P1 — Thư viện kịch bản thông minh:** tin làm ấm/mời gắn thẻ DISC + **giai đoạn sẵn sàng thay đổi (Stage-of-Change)**; LLM viết lại; HLV chọn & sửa; giữ "lập trường" kết nối. *(Không cần ML.)*
- **P2 — Copilot theo Phỏng vấn tạo động lực (MI):** hỏi mở, khẳng định, phản chiếu, gợi "lời nói thay đổi" theo giai đoạn sẵn sàng — nhân văn, không thao túng.
- **P3 — Chân dung động + khớp nội dung ngữ nghĩa:** suy luận từ hành vi (tự cập nhật); RAG/embedding "câu chuyện giống bạn"; look-alike. *(Cần dữ liệu hành vi.)*
- **P4 — Lớp tối ưu hóa:** uplift/persuadable + Next-Best-Action (contextual bandit). *(Cần lịch sử chuyển đổi đủ lớn.)*

**AI nhập vai luyện tập cho người mới:** "khách ảo" theo từng chân dung/giai đoạn để tập làm ấm/mời; phản hồi theo MI; ghép Module Đào tạo. Triển khai song song, không phụ thuộc dữ liệu.

**Phễu thị trường lạnh + Chatbot:** landing/quiz sức khỏe thu lead + tự lập chân dung; chatbot AI sàng lọc/đặt lịch, luôn chuyển tư vấn sâu sang HLV/2/1; gắn vòng lặp referral.

**Đặt lịch & chuẩn bị cuộc gặp 2/1:** booking (offline/Zoom), nhắc 3 bên (khách/TV/TAB); tự tổng hợp hồ sơ lead gửi TAB trước gặp; ghi nhận kết quả.

**Content-Attribution Matching (mô hình lai — gắn lead theo công sức):**
- **Lớp chính (earned):** HLV sáng tạo/chỉnh sửa nội dung + mã giới thiệu/deep-link; khách tương tác/đăng ký → tự gắn về HLV.
- **Lớp fallback:** lead mồ côi → pool chung → matching thuật toán công bằng (khu vực/chuyên môn DMO/tải khách); khách ở xa → plug-in nhà vận hành gần.
- **Phân tích nội dung cho HLV:** dashboard "nội dung nào của tôi đang hút khách" + AI gợi ý nội dung tiếp theo.
- **Quy tắc & bảo vệ:** hành động ý nghĩa đầu tiên để gắn; khách luôn được chọn/đổi HLV; chống poaching & gian lận; minh bạch lý do gắn lead.

**Giai đoạn đầu Bước 2 — buổi trải nghiệm đầu:** hồ sơ liền mạch lead → trải nghiệm (không nhập lại); checklist đón tiếp theo 10 vai trò BMO; OCR Tanita + AI gợi ý chế độ cá nhân hóa.

**La bàn quy trình & nhắc tần suất:** vị trí trên Bước 1–2 + việc tiếp theo; nhắc nhịp hành động; đo phễu chuyển đổi (tạo baseline đang thiếu).

## III.3. RÀNG BUỘC & TUÂN THỦ (GUARDRAILS)
1. **Không thay vai con người** (kết nối/làm ấm/mời/sàng lọc; không thay tư vấn sản phẩm/cuộc gặp 2/1).
2. **Tuân thủ quy định sức khỏe/quảng cáo** (Herbalife + pháp luật VN; tránh tuyên bố công dụng quá mức).
3. **Riêng tư dữ liệu** (chỉ dữ liệu được phép; minh bạch & opt-out).
4. **Chống spam** (cá nhân hóa, giới hạn tần suất).
5. **Độc lập với Herbalife apps.**

## III.4. THƯỚC ĐO & LƯU Ý TRIỂN KHAI
- Năng suất (số lead xử lý/không bỏ rơi); phễu chuyển đổi; rào cản người mới (thời gian tới lời mời đầu); chất lượng matching.
- Cần kho nội dung để AI làm ấm & phễu hoạt động (liên kết Module Đào tạo).
- PoC khuyến nghị: chatbot sàng lọc + lead scoring + copilot soạn lời mời.

---
---

# PHẦN IV — RÀ SOÁT RỦI RO: SỐ HÓA QUY TRÌNH BÁN HÀNG TRỰC TIẾP NHIỀU CẤP SANG DXP TẬP TRUNG

> **Nguyên lý xuyên suốt:** mâu thuẫn gốc là **"tập trung hóa dữ liệu/trải nghiệm" vs "quyền sở hữu & quan hệ phân tán của phân phối viên"**. Vấn đề matching (đã xử lý bằng Content-Attribution) chỉ là một biểu hiện. Phần lớn rủi ro dưới đây đều quy về đó.

## A. Quyền lợi & động lực của phân phối viên (HLV)
- **R1 — Quyền sở hữu khách/lead** *(đã có hướng giải)*: nền tảng dễ bị xem là "gom rồi chia tùy ý". → **Content-Attribution Matching**; minh bạch lý do gắn; thuật toán chỉ phân phối lead mồ côi.
- **R2 — Tranh chấp tuyến/chéo tuyến & poaching:** genealogy nhiều cấp → tranh chấp khi khách tương tác nhiều HLV. → Quy tắc attribution rõ (hành động ý nghĩa đầu tiên); tôn trọng quan hệ hiện hữu; cơ chế khiếu nại; khách được chọn/đổi HLV.
- **R3 — Nỗi sợ bị "cắt cầu" (disintermediation):** lo nền tảng bán thẳng tới khách. → Định vị trao quyền cho HLV; mọi điểm chạm gắn HLV; truyền thông cam kết.
- **R4 — Áp lực thành tích lệch hướng từ gamification:** spam/ép khách/gaming chỉ số. → Chỉ số quanh chất lượng & hành vi lành mạnh; chống gian lận; không phơi bày thu nhập/áp lực thái quá.

## B. Pháp lý & tuân thủ
- **R5 — Tuân thủ pháp luật bán hàng đa cấp** (vd Nghị định 40/2018): nền tảng tập trung khuếch đại rủi ro thông điệp sai về thu nhập. → **Không hứa thu nhập**; kiểm duyệt nội dung; rà soát pháp lý; tách "trải nghiệm sức khỏe" khỏi "cơ hội kinh doanh".
- **R6 — Tuyên bố sức khỏe & quảng cáo:** UGC + chia sẻ MXH dễ vi phạm. → Thư viện được chuyên gia duyệt; kiểm duyệt tự động + thủ công; chống "before/after" gây hiểu lầm.

## C. Dữ liệu & quyền riêng tư
- **R7 — Tập trung dữ liệu sức khỏe nhạy cảm** (vd Nghị định 13/2023): → consent minh bạch, tối thiểu hóa dữ liệu, mã hóa, chính sách lưu trữ/xóa.
- **R8 — Phân quyền theo cấp bậc (ai thấy dữ liệu của ai):** → RBAC theo vai trò & tuyến; khách kiểm soát mức chia sẻ; tuyến trên chỉ thấy dữ liệu tổng hợp/được phép.

## D. Quan hệ con người & đạo đức
- **R9 — Tự động hóa xói mòn quan hệ cá nhân:** → AI hỗ trợ không thay người; tinh thần MI; giới hạn tần suất; người mới chỉ kết nối.
- **R10 — Chuẩn hóa cứng nhắc vs đa dạng thực tế:** → PSM/quy trình cấu hình được theo BMO/tuyến.
- **R11 — Sức khỏe tinh thần & wellbeing:** → thiết kế quan tâm wellbeing; tránh so sánh tiêu cực; ngôn ngữ động viên.

## E. Vận hành & kỹ thuật
- **R12 — Ranh giới & trùng lặp với Herbalife (không tích hợp):** rủi ro trùng/lệch dữ liệu. → Khoanh rõ ranh giới chức năng; nhập tay tối thiểu thay vì tích hợp.
- **R13 — Khoảng cách số & đa dạng người dùng:** → UX tối giản, tiếng Việt đời thường, hỗ trợ giọng nói/hình ảnh; đào tạo; giữ kênh offline song song.
- **R14 — Phụ thuộc nền tảng & điểm chết đơn:** → độ sẵn sàng cao, sao lưu, chế độ offline cho tác vụ cốt lõi.
- **R15 — Áp lực niềm tin & chấp nhận (adoption) — rủi ro lớn nhất:** → đồng thiết kế cùng HLV; minh bạch mục tiêu trao quyền; thắng nhanh ở MVP-1.

## Nguyên tắc thiết kế để giảm thiểu
1. **Trao quyền, không thâu tóm** (Content-Attribution).
2. **AI hỗ trợ, không thay người & không thao túng.**
3. **Tuân thủ là ràng buộc thiết kế** (không thu nhập/health claim; kiểm duyệt; bảo vệ dữ liệu).
4. **Minh bạch & quyền của người dùng** (khách chọn/đổi HLV; biết dữ liệu dùng thế nào).
5. **Cấu hình được, tôn trọng đa dạng thực tế.**
6. **Thắng nhỏ tạo niềm tin trước khi mở rộng** (bám lộ trình MVP).

> Các rủi ro trên nên được phản ánh thành **ràng buộc (guardrails) & hạng mục To-do** trong các module liên quan, không chỉ là cảnh báo.
