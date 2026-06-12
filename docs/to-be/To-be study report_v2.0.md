# **BÁO CÁO THIẾT KẾ TRẠNG THÁI MỤC TIÊU (TO-BE) — ANCARE DXP**

**Phiên bản:** v2.0 — *Tái định hướng theo tầm nhìn AnCare Digital Experience Platform (README.md). Thay thế To-be v1.0 (vốn xoay quanh vận hành club & quản trị kinh doanh).*
**Đối tượng đọc:** BA, PO/PM, Đội phát triển, Ban lãnh đạo sản phẩm.
**Cơ sở:** README.md (tầm nhìn/sứ mệnh/giá trị/4 module), As-Is v1.2 (app khách + CRM HLV đã có), 2 phụ lục As-Is.

> **Thay đổi định hướng cốt lõi so với v1.0:** AnCare KHÔNG còn định vị là công cụ vận hành Nutrition Club. AnCare là **nền tảng trải nghiệm số (DXP)** về chăm sóc sức khỏe chủ động. **Loại khỏi phạm vi:** POS bán lẻ, quản lý kho, dashboard quản trị kinh doanh cho Nhà sáng lập — các năng lực này đã có ở **VNHUB** của Herbalife. AnCare **bổ trợ**, không trùng lặp.

---

## 1. ĐỊNH VỊ & MỤC TIÊU TÁI HÌNH DUNG

### 1.1. Định vị "lấp khoảng trống"

AnCare DXP nằm giữa hai cụm ứng dụng của Herbalife: nhóm phục vụ HLV/đối tác kinh doanh (VNHUB, Herbalife Learning, Herbalife SHOP) và nhóm phục vụ khách hàng tương lai (Pro2col). Khoảng trống mà AnCare lấp đầy: **bám sát trải nghiệm thực tế tại Nhóm dinh dưỡng và thấu hiểu văn hóa, tâm lý của nhiều phân khúc khách hàng Việt Nam** — điều các app hiện tại chưa làm tốt.

### 1.2. Mục tiêu hướng đến

AnCare DXP là **cầu nối** đưa khách hàng tiềm năng và khách hàng hiện tại vào hệ sinh thái chăm sóc sức khỏe chủ động, qua bốn vai trò giá trị: (a) công cụ chăm sóc sức khỏe chủ động & nguồn cảm hứng; (b) phễu thu hút và bệ phóng phát triển bản thân/cơ hội kinh doanh nhân văn; (c) nền tảng giao tiếp & kết nối HLV–khách–cộng đồng; (d) không gian học tập (đào tạo micro-course, gamification).

Trọng tâm trải nghiệm chuyển từ "quản lý vận hành" sang **gắn kết (engagement), lan tỏa (virality), cá nhân hóa (personalization) và học tập (learning)**.

---

## 2. PERSONA MỤC TIÊU (cập nhật theo DXP)

| Persona | Vai trò trong DXP | Trọng tâm trải nghiệm |
| :-- | :-- | :-- |
| **Khách hàng tiềm năng** | Người quan tâm sức khỏe, chưa mua gói | Kiến thức sinh động dễ hiểu, câu chuyện thành công, kết nối với HLV phù hợp |
| **Khách hàng (thành viên club)** | Đang trải nghiệm lộ trình | Theo dõi sức khỏe, nội dung đồng hành, cộng đồng/HOM, chia sẻ & lan tỏa |
| **Huấn luyện viên dinh dưỡng (HLV)** | Vận hành club, tư vấn, kinh doanh | Phát triển kỹ năng/sự nghiệp, chăm sóc khách hàng, chia sẻ nội dung thu hút, công cụ vận hành bổ trợ VNHUB |

> *Persona "Nhà sáng lập với góc nhìn quản trị kinh doanh" rời khỏi phạm vi AnCare (thuộc VNHUB).*

---

## 3. NĂNG LỰC MỤC TIÊU THEO 4 MODULE

Ký hiệu: **[ĐÃ CÓ]** tái sử dụng từ app hiện tại · **[NÂNG CẤP]** mở rộng cái đã có · **[MỚI]** xây mới.

### 3.0. Năng lực nền tảng — La bàn Quy trình 12 bước (Process State Model)

> **Xương sống xuyên suốt 4 module.** Đặc tả: `docs/to-be/Process-State-Model_La-ban-12-buoc_v1.0.md`. PSM số hóa **Sơ đồ dẫn (SĐD)** — một trong 3 công cụ KD cốt lõi — và là viên gạch khóa kết nối toàn hệ thống. Với mỗi người dùng, PSM xác định **bước hiện tại** (nhánh Khách hàng 1→6, nhánh Thành viên KD 6→12) rồi điều khiển: việc cần làm tiếp theo, nội dung/khóa học đề xuất (Module 3/4), hành động chăm sóc của HLV (Module 2), và kiểm tra Definition of Done của bước (= "tiêu chí hoàn thành xuất sắc" trong tài liệu, trừ điểm PPV/đơn hàng thuộc VNHUB). Cùng với PSM là số hóa **GNV (giấy nhắc việc)** và **DSKHTN** (đã có ở tiểu mô-đun AC) → đủ bộ 3 công cụ KD.

### 3.1. Module Hành trình khách hàng (Customer Journey)

> **Tiểu mô-đun trọng tâm — Thu hút & Chuyển đổi (AI-assisted), hỗ trợ Bước 1 → đầu Bước 2 của Quy trình 12 bước.** Đặc tả chi tiết: `docs/to-be/Module_Thu-hut-Chuyen-doi_AI-assisted_v1.0.md`. Gồm: DSKHTN số hóa, AI lập chân dung & chấm điểm lead, AI Copilot làm ấm & mời, phễu thị trường lạnh + chatbot, đặt lịch & chuẩn bị cuộc gặp 2/1, matching KH↔HLV/BMO, checklist buổi trải nghiệm đầu, và La bàn quy trình + nhắc tần suất. Mục tiêu: gỡ nút thắt khi scale và rào cản người mới, giữ đúng vai trò con người (người mới chỉ kết nối) và tuân thủ quy định.

Bao trọn phễu tiềm năng → thành viên → người lan tỏa:

- **[MỚI]** Kho nội dung kiến thức sức khỏe/sản phẩm/thói quen tốt — sinh động, cô đọng, dễ hiểu, dành cho khách tiềm năng.
- **[MỚI]** **Động cơ thu hút bằng nội dung + gắn lead theo công sức (Content-Attribution Matching).** Hợp nhất "matching", "chia sẻ câu chuyện thành công" và "vòng lặp giới thiệu" thành một bánh đà:
  - HLV **chủ động sáng tạo/chỉnh sửa nội dung** (câu chuyện thành công, kiến thức) và chia sẻ kèm **mã giới thiệu/deep-link** riêng.
  - Khách tiềm năng tương tác/đăng ký qua nội dung đó → **tự gắn (attribution) về HLV** — lead là thứ *kiếm được bằng công sức*, không bị nền tảng phân phối tùy ý. Đây là cơ chế matching **chính**, tạo động lực.
  - **Matching thuật toán chỉ là fallback** cho lead "mồ côi" (inbound lạnh, không qua ai): phân phối công bằng theo khu vực/chuyên môn DMO/tải khách.
  - Khách **luôn có quyền chọn/đổi HLV**; có quy tắc xử lý tranh chấp (hành động ý nghĩa đầu tiên), chống "poaching" khách đã có HLV, và chống gian lận tương tác ảo.
  - AI chuyển vai: **giúp HLV thắng công bằng** — gợi ý nên làm nội dung gì cho phân khúc nào, copilot chỉnh sửa, và phân tích "nội dung nào của tôi đang hút khách".
- **[ĐÃ CÓ]** Công cụ tự theo dõi sức khỏe/dinh dưỡng/thói quen (log bữa ăn, nước, ngủ, chỉ số, tiến độ, streak).
- **[ĐÃ CÓ]** Nội dung động viên/gợi ý từ HLV; chat 1-1; cộng đồng.
- **[MỚI]** Thông tin & tham gia **buổi sinh hoạt HOM** của Nhóm dinh dưỡng (chủ đề dinh dưỡng/lối sống/kinh doanh).

### 3.2. Module Hành trình kinh doanh — dành cho HLV

- **[ĐÃ CÓ]** Quản lý khách hàng, theo dõi & hỗ trợ đạt mục tiêu (CRM/onboarding/journey builder/báo cáo).
- **[MỚI]** **Chăm sóc khách hàng theo thời điểm đặc biệt** (sinh nhật, kỷ niệm, ngày lễ) + động viên khi khách xuống tinh thần → tăng hài lòng, gắn bó, giới thiệu.
- **[MỚI]** **Chia sẻ nội dung sản phẩm/giải pháp/cơ hội kinh doanh** cho khách tiềm năng & người thân (công cụ prospecting).
- **[MỚI]** Định hướng **phát triển kỹ năng & lộ trình thăng tiến** trong kế hoạch trả thưởng Herbalife (liên kết Module Đào tạo & Phát triển bản thân).
- **[NÂNG CẤP]** Công cụ **vận hành Nhóm dinh dưỡng theo nhiều mô hình DMO** (chuyên sâu, vận động, Spa…) — tập trung trải nghiệm tại club, không làm nghiệp vụ kinh doanh (POS/kho/quản trị) vốn thuộc VNHUB.
- **[MỚI]** **Pipeline 12 bước cấp quản lý:** xem toàn bộ khách & tuyến dưới đang ở bước nào, ai cần hành động gì hôm nay (gắn PSM).
- **[MỚI]** **Số hóa GNV (giấy nhắc việc)** + **SĐD** (= PSM) → đủ bộ 3 công cụ KD dùng hằng ngày.
- **[MỚI]** **Coaching tuyến dưới (duplication):** khung Tell–Show–Try–Do + theo dõi tiến độ TV mới qua Bước 6–12 (phần phi tài chính).

### 3.3. Module Đào tạo (Training)

- **[MỚI]** **Micro-course** (khóa ngắn, tập trung một kỹ năng) về dinh dưỡng, sản phẩm, huấn luyện, tư vấn.
- **[MỚI]** Nội dung chuyên sâu theo **nhóm khách hàng đặc thù** (thừa/thiếu cân, thể thao, béo phì, tiểu đường, tim mạch, người cao tuổi, bà mẹ mang thai & sau sinh…).
- **[MỚI]** Thư viện cho khách hàng: bài viết, **video hướng dẫn tập luyện, công thức nấu ăn lành mạnh**, lời khuyên chuyên gia, câu chuyện thành công.
- **[MỚI]** **Gamification học tập:** thi đua, tranh tài, bảng xếp hạng để tạo hứng thú.
- **[MỚI]** **Ánh xạ micro-course 1:1 với giáo trình quy trình:** 21 talking points, Lớp Khai mở, HLCB1, HLCB2, Định hướng BMO, Cầm tay chỉ việc, kỹ năng riêng theo BMO; ngưỡng kiến thức 70/80/90% làm điều kiện hoàn thành bước (gắn PSM).
- **[MỚI]** **Playlist "nên đọc/xem/nghe" theo từng bước** + hỗ trợ Tell–Show–Try–Do (video + checklist) cho Bước 8–11.

### 3.4. Module Phát triển bản thân (Self-development)

- **[MỚI]** **Gợi ý thông minh cá nhân hóa** nội dung/khóa học/chương trình theo dữ liệu sức khỏe, thói quen, mục tiêu, sở thích, hành vi sử dụng.
- **[MỚI]** Nội dung giới thiệu sản phẩm/giải pháp/cơ hội kinh doanh Herbalife cho **khách tiềm năng** (phễu).
- **[MỚI]** Với HLV: **lộ trình đào tạo có điều kiện/tài liệu tham khảo** cho mục tiêu phát triển bản thân trong bán hàng trực tiếp & chăm sóc sức khỏe chủ động.
- **[MỚI]** **Lộ trình thăng tiến tới Giám sát viên** (kế hoạch trả thưởng) trực quan, có điều kiện mở khóa từng mốc (gắn PSM nhánh Bước 6–12).
- **[MỚI]** Khóa **kỹ năng lãnh đạo/bảo trợ** để dẫn tuyến dưới; gợi ý "việc/khóa tiếp theo" theo vị trí trên la bàn.

---

## 4. NGUYÊN TẮC THIẾT KẾ (DESIGN PRINCIPLES)

1. **Bám sát thực tế Nhóm dinh dưỡng & văn hóa Việt Nam** — khác biệt cốt lõi so với app hiện hữu.
2. **Engagement & cảm hứng trước, công cụ sau** — AnCare là không gian tạo động lực, không chỉ là sổ theo dõi.
3. **Virality gắn vào hành trình** — mọi cột mốc tích cực đều dễ biến thành nội dung chia sẻ.
4. **Cá nhân hóa xuyên suốt** — gợi ý theo dữ liệu & hành vi.
5. **Độc lập & không trùng lặp Herbalife apps** — AnCare KHÔNG tích hợp kỹ thuật với VNHUB và không làm POS/kho/quản trị kinh doanh (đó là phạm vi VNHUB); AnCare tập trung trải nghiệm, nội dung, đào tạo, kết nối.

---

## 5. NĂNG LỰC NGOÀI PHẠM VI (OUT OF SCOPE)

- POS bán lẻ & đối soát thu/chi — *thuộc VNHUB.*
- Quản lý kho — *thuộc VNHUB.*
- Dashboard quản trị kinh doanh/lời-lỗ cho Nhà sáng lập — *thuộc VNHUB.*

> Các điểm đau P1/P2 (bán lẻ/kho) và F1–F4 (quản trị kinh doanh) trong As-Is **được chuyển giao cho VNHUB**, không nằm trong To-be AnCare.

---

## 6. LỘ TRÌNH MVP (đề xuất theo định hướng DXP)

- **MVP-1 — Lan tỏa & Gắn kết:** Tạo & chia sẻ câu chuyện thành công ra MXH (3.1), nhắc nhở chủ động (push), chăm sóc khách theo dịp đặc biệt (3.2). *Tận dụng tối đa dữ liệu/tính năng đã có; ROI engagement nhanh.*
- **MVP-2 — Học tập & Nội dung:** Kho nội dung kiến thức + Module Đào tạo micro-course có gamification (3.3), thư viện video/công thức.
- **MVP-3 — Phễu & Cá nhân hóa:** Kết nối khách tiềm năng ↔ HLV (matching), referral loop, gợi ý thông minh cá nhân hóa (3.4), HOM.

> Thứ tự có thể điều chỉnh sau khi xác nhận ưu tiên với stakeholder; đây là đề xuất khởi điểm cho bước GAP & To-do.

---

## 7. ĐIỂM CẦN LÀM RÕ TIẾP

> **Đã chốt:** AnCare là ứng dụng **độc lập**, KHÔNG tích hợp kỹ thuật (SSO/đồng bộ dữ liệu) với VNHUB/Learning/SHOP/Pro2col. Quan hệ với các app Herbalife thuần túy là bổ trợ về phạm vi.

- Nguồn & quy trình kiểm duyệt nội dung đào tạo (ai sản xuất micro-course, chuyên gia nào).
- Cơ chế matching khách tiềm năng ↔ HLV (theo khu vực, chuyên môn DMO, tải khách).
- Chính sách chia sẻ MXH (thương hiệu, tuân thủ quy định Herbalife về quảng cáo/khẳng định sức khỏe).
