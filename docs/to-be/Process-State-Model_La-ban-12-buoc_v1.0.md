# **ĐẶC TẢ: LA BÀN QUY TRÌNH 12 BƯỚC (PROCESS STATE MODEL)**

## *(Xương sống xuyên suốt 4 module — hỗ trợ thực thi Bước 1 → 12)*

**Phiên bản:** v1.0
**Thuộc:** To-be AnCare DXP v2.0 — năng lực nền tảng dùng chung.
**Cơ sở:** `docs/references/01.Quy-trinh-12-buoc-kinh-doanh.md`; README.md (4 module); As-Is v1.2; tiểu mô-đun Thu hút & Chuyển đổi (AC) v1.0.

---

## 1. Ý TƯỞNG CỐT LÕI

Quy trình 12 bước là một **đường ống chuyển đổi + nhân bản đào tạo theo trình tự**. Để AnCare thành công cụ đắc lực thực thi quy trình, cần **một mô hình tiến trình duy nhất (Process State Model — PSM)** làm xương sống, điều khiển cả 4 module thay vì để mỗi module rời rạc.

PSM số hóa chính **Sơ đồ dẫn (SĐD)** — công cụ "dẫn khách hàng/thành viên đi đúng lộ trình" mà tài liệu xem là 1 trong 3 công cụ KD cốt lõi. Đây là **viên gạch khóa** kết nối toàn hệ thống.

### 1.1. Hai nhánh trạng thái

- **Nhánh Khách hàng (Bước 1→6):** KHTN → đến 2/1 → trải nghiệm BMO → KH hạnh phúc → Đại sứ sức khỏe → (nếu muốn KD) Khai mở → Thành viên kinh doanh.
- **Nhánh Thành viên kinh doanh (Bước 6→12):** TV mới → HLCB1 → HLCB2 → Định hướng BMO → Cầm tay chỉ việc → Đồng vận hành → Giám sát viên vận hành độc lập.

Một người có thể chuyển từ nhánh 1 sang nhánh 2 tại Bước 5–6.

### 1.2. PSM điều khiển gì

Với mỗi người dùng, PSM xác định **bước hiện tại** và từ đó tự động:
1. **Hiển thị việc cần làm tiếp theo** (next action).
2. **Đề xuất nội dung/khóa học** phù hợp bước (Module 3/4).
3. **Kích hoạt hành động chăm sóc** cho HLV/bảo trợ (Module 2).
4. **Kiểm tra Definition of Done (DoD)** của bước = "tiêu chí hoàn thành xuất sắc" trong tài liệu.

### 1.3. Definition of Done theo bước

Mỗi bước có DoD lấy từ tài liệu, ví dụ: Bước 2 (kết quả SK trong 10 ngày + thuộc >70% 10 bài dinh dưỡng); Bước 4 (đưa ≥1 người đến 2/1 + thuộc >80% 21 bài); Bước 5 (>90% 21 bài + đưa ≥2 người + ra quyết định KD)…

> **Ranh giới:** các tiêu chí **điểm cá nhân (PPV), số đơn hàng** thuộc VNHUB — PSM **không** quản lý phần tài chính này; PSM bám phần **trải nghiệm – kiến thức – quan hệ – hành động** (đã trải nghiệm gì, học tới đâu, đưa mấy người đến 2/1, đã chia sẻ câu chuyện chưa). Có thể nhập tay mốc tài chính nếu cần, nhưng không tích hợp VNHUB.

---

## 2. THAY ĐỔI THEO TỪNG MODULE ĐỂ BÁM QUY TRÌNH

### 2.1. Module Hành trình khách hàng (Bước 3–4, nối tiếp AC ở Bước 1–2)

- **Talking points + quiz** gắn trong app khách; dùng ngưỡng 70/80/90% làm **cổng mở khóa** sang bước sau (hiện thực hóa "không nhảy cóc").
- Tự phát hiện **cột mốc "khách hạnh phúc"** (kết quả sức khỏe) → nhắc nâng cấp thành **Đại sứ sức khỏe**.
- Nối tiêu chí "đưa ≥1 / ≥2 người đến 2/1" vào **phễu referral (AC)** → khép vòng Bước 4/5 ↔ Bước 1.
- Lịch & đăng ký **HOM**.

### 2.2. Module Hành trình kinh doanh — HLV / Bảo trợ (Bước 3–12)

- **Pipeline 12 bước cấp quản lý:** xem toàn bộ khách & tuyến dưới đang ở bước nào, ai cần hành động gì hôm nay.
- **Số hóa 3 công cụ KD:** **GNV** (giấy nhắc việc — task & cadence hằng ngày), **DSKHTN** (đã có ở AC), **SĐD** (= chính PSM).
- **Coaching tuyến dưới (duplication):** khung **Tell–Show–Try–Do** + theo dõi tiến độ TV mới qua Bước 6–12 (phần phi tài chính).
- Chăm sóc theo dịp & động viên (gắn giữ chân Bước 3–4).

### 2.3. Module Đào tạo (trục xương sống Bước 2–12)

- **Ánh xạ micro-course 1:1 với giáo trình quy trình:** 21 talking points dinh dưỡng, Lớp Khai mở, HLCB1, HLCB2, Định hướng BMO, Cầm tay chỉ việc, kỹ năng riêng theo BMO.
- **Playlist "nên đọc/xem/nghe" theo từng bước** (tài liệu liệt kê sẵn) → lộ trình học có ngữ cảnh, gắn DoD.
- Nội dung chuyên sâu theo **nhóm KH đặc thù** (tiểu đường, thai sản, tim mạch…) phục vụ tư vấn Bước 3–4.
- **Gamification thi đua** + ngưỡng kiến thức làm điều kiện hoàn thành bước.
- Hỗ trợ **Tell–Show–Try–Do** (video + checklist thực hành) cho Bước 8–11.

### 2.4. Module Phát triển bản thân (Bước 5–12)

- **Lộ trình thăng tiến tới Giám sát viên** (và kế hoạch trả thưởng) trực quan, có điều kiện mở khóa từng mốc.
- **Gợi ý cá nhân hóa "việc/khóa tiếp theo"** đúng vị trí trên la bàn (cho cả khách & HLV).
- Khóa **kỹ năng lãnh đạo/bảo trợ** để dẫn tuyến dưới (Bước 7–12).

---

## 3. THƯỚC ĐO THÀNH CÔNG

- **Tỷ lệ tiến bước:** % người dùng chuyển từ bước n → n+1 trong khoảng thời gian (phễu 12 bước).
- **Thời gian trung bình mỗi bước** & điểm nghẽn (bước nào đọng nhiều người).
- **Tuân thủ tần suất:** mức độ hoàn thành GNV hằng ngày.
- **Hiệu quả nhân bản:** số TV tuyến dưới đạt từng mốc Bước 6–12.

---

## 4. RÀNG BUỘC & PHỤ THUỘC

- **Độc lập Herbalife apps:** không tích hợp kỹ thuật; điểm PPV/đơn hàng thuộc VNHUB.
- **Lớp live vẫn live:** PSM/Module 3 bổ trợ, ôn tập, đo tiến độ — không thay lớp Khai mở/HLCB.
- **Phụ thuộc nội dung:** Module 3/4 cần kho micro-course & tài liệu theo bước.
- **PSM là nền:** AC (Bước 1–2) và các thay đổi Module 2/3/4 (Bước 3–12) đều cắm vào PSM → nên ưu tiên dựng khung PSM sớm.
