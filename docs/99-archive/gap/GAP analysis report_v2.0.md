# **PHÂN TÍCH KHOẢNG CÁCH (GAP) — ANCARE DXP**

**Phiên bản:** v2.0 — *Đối chiếu theo định hướng DXP. Thay thế GAP v1.0.*
**Cơ sở:** As-Is v1.2 (`docs/as-is/`, gồm 2 phụ lục) ↔ To-be v2.0 (`docs/to-be/To-be study report_v2.1 (consolidated).md`).

> **Khác biệt cốt lõi với v1.0:** loại bỏ toàn bộ GAP về POS/kho/quản trị kinh doanh (chuyển cho VNHUB). Nhiều năng lực phía khách hàng đã được app hiện tại đáp ứng, nên khoảng trống thật co lại và **dịch trọng tâm sang nội dung, đào tạo, lan tỏa, cá nhân hóa, kết nối phễu**.

---

## 1. QUY ƯỚC

Loại GAP: **[MỚI]** chưa có, xây mới · **[NÂNG CẤP]** đã có một phần · **[ĐÃ CÓ]** không còn là gap · **[NỀN TẢNG]** hạ tầng dùng chung. Công sức: Thấp (S) · Trung bình (M) · Cao (L).

> Hạn chế: chưa có baseline định lượng → ưu tiên/công sức mang tính định tính.

---

## 2. BẢNG KHOẢNG CÁCH THEO MODULE

### 2.1. Module Hành trình khách hàng

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| CJ1 | Tự theo dõi sức khỏe/dinh dưỡng/thói quen | Đã có (log, tiến độ, streak) | Giữ & tinh chỉnh | [ĐÃ CÓ] | — | — |
| CJ2 | Chat 1-1 HLV + cộng đồng | Đã có | Giữ | [ĐÃ CÓ] | — | — |
| CJ3 | Nhắc nhở chủ động (push theo khung giờ) | Chưa có push chủ động | Nhắc bữa ăn/nước/thói quen | [MỚI] | M | 1 |
| CJ4 | Tạo & chia sẻ câu chuyện thành công ra MXH | Có đồ thị nội bộ; chưa chia sẻ | Sinh nội dung giàu cảm xúc, 1 chạm share (kênh thu hút của bánh đà CJ6) | [MỚI] | M | 1 |
| CJ5 | Kho nội dung kiến thức cho khách tiềm năng | Chưa có | Nội dung sinh động, cô đọng | [MỚI] | M | 2 |
| CJ6 | **Động cơ thu hút bằng nội dung + Content-Attribution Matching** (hợp nhất CJ4/CJ7) | Chưa có (HLV tự tạo lead) | HLV sáng tạo/chia sẻ nội dung kèm mã giới thiệu → khách tương tác tự gắn về HLV (matching chính); thuật toán chỉ fallback cho lead mồ côi | [MỚI] | L | 2-3 |
| CJ7 | Vòng lặp giới thiệu (referral) — *thuộc bánh đà CJ6* | Chưa có | Mã giới thiệu/deep-link, attribution, theo dõi nguồn; quyền chọn/đổi HLV; chống poaching & gian lận | [MỚI] | M | 2-3 |
| CJ8 | Buổi sinh hoạt HOM (thông tin & tham gia) | Chưa có trong app | Lịch HOM, chủ đề, đăng ký | [MỚI] | M | 3 |
| CJ9 | Gián đoạn khi hết gói (rủi ro bỏ cuộc - C4) | Chặn cứng check-in | Trải nghiệm gia hạn mềm hơn | [NÂNG CẤP] | S | 1 |

### 2.0. Nền tảng — La bàn Quy trình 12 bước (Process State Model)

> Đặc tả: `docs/to-be/To-be study report_v2.1 (consolidated).md (Phần II)`. Là xương sống nối 4 module; nên ưu tiên dựng sớm.

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| PS1 | Process State Model (số hóa SĐD, 2 nhánh, DoD theo bước) | Chưa có (sổ tay) | Mô hình tiến trình điều khiển 4 module | [NỀN TẢNG] | L | 1 |
| PS2 | GNV (giấy nhắc việc) số hóa + cadence | Chưa có | Task/nhắc việc hằng ngày gắn bước | [MỚI] | M | 1 |
| PS3 | Definition of Done theo bước (trừ PPV/đơn hàng) | Chưa có | Kiểm tra tiêu chí hoàn thành mỗi bước | [MỚI] | M | 2 |

### 2.1bis. Tiểu mô-đun Thu hút & Chuyển đổi (AI) — Bước 1 → đầu Bước 2

> Đặc tả: `docs/to-be/To-be study report_v2.1 (consolidated).md (Phần III)`. Toàn bộ nhóm này hiện **chưa có** trong app (As-Is chỉ có luồng HLV tự tạo lead thủ công).

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| AC1 | DSKHTN số hóa (phễu 3 bước, trạng thái lead) | Thủ công/sổ tay | Danh sách số, import, trạng thái phễu | [MỚI] | M | 1 |
| AC2 | Chấm điểm & ưu tiên lead | Chưa có | Phân khúc + pain point + ưu tiên (P1 rule-based → P4 uplift) | [MỚI] | L | 2→sau MVP-3 |
| AC3 | Engine cá nhân hóa làm ấm & mời | Chưa có | Phân tầng P1 thư viện kịch bản → P2 MI copilot → P3 chân dung động+RAG → P4 NBA/bandit | [MỚI] | L | 2→sau MVP-3 |

> **Engine cá nhân hóa AC2/AC3 bóc tầng theo độ trưởng thành dữ liệu (chi tiết ở To-do TD-AC5-P1..P4):** P1 thư viện kịch bản (DISC + Stage-of-Change + LLM viết lại, không cần ML) → P2 copilot theo Phỏng vấn tạo động lực (MI) → P3 chân dung động + RAG khớp nội dung (cần dữ liệu hành vi) → P4 uplift + Next-Best-Action bandit (cần lịch sử chuyển đổi). DISC chỉ là thẻ phụ. Bổ sung AC9: AI nhập vai luyện tập cho người mới (song song, MVP-2).
| AC4 | Phễu thị trường lạnh + chatbot sàng lọc | Chưa có | Landing/quiz + chatbot đặt lịch | [MỚI] | L | 3 |
| AC5 | Đặt lịch & chuẩn bị cuộc gặp 2/1 | Chưa có | Booking + nhắc 3 bên + hồ sơ lead cho TAB | [MỚI] | M | 1-2 |
| AC6 | Matching KHTN ↔ HLV/BMO (kể cả khách ở xa) | Chưa có | Gợi ý HLV/BMO phù hợp, plug-in nhà vận hành gần | [MỚI] | L | 3 |
| AC7 | Checklist buổi trải nghiệm đầu (10 vai trò BMO) | Một phần (CRM HLV) | Số hóa đón tiếp + hồ sơ liền mạch lead→trải nghiệm | [NÂNG CẤP] | M | 2 |
| AC8 | La bàn quy trình + nhắc tần suất + đo phễu | Chưa có | Vị trí trên Bước 1-2, việc tiếp theo, cadence, phễu metrics | [MỚI] | M | 1 |

### 2.2. Module Hành trình kinh doanh (HLV)

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| BJ1 | Quản lý KH, onboarding, journey, báo cáo | Đã có đầy đủ | Giữ | [ĐÃ CÓ] | — | — |
| BJ2 | Chăm sóc theo dịp đặc biệt + động viên | Chưa có | Nhắc sinh nhật/kỷ niệm/lễ, gợi ý lời động viên | [MỚI] | M | 1 |
| BJ3 | Chia sẻ nội dung sản phẩm/giải pháp/cơ hội KD (prospecting) | Chưa có | Bộ nội dung & công cụ chia sẻ | [MỚI] | M | 2 |
| BJ4 | Định hướng phát triển kỹ năng & lộ trình thăng tiến | Chưa có | Liên kết Module Đào tạo/PT bản thân | [MỚI] | M | 2-3 |
| BJ5 | Công cụ vận hành DMO đa mô hình | Một phần (app HLV cơ bản) | Mở rộng theo mô hình club (không làm POS/kho/quản trị) | [NÂNG CẤP] | M | 3 |
| BJ6 | Pipeline 12 bước cấp quản lý (khách + tuyến dưới) | Chưa có | Xem vị trí & hành động cần làm theo PSM | [MỚI] | M | 2 |
| BJ7 | Coaching tuyến dưới (Tell-Show-Try-Do, theo dõi Bước 6-12) | Chưa có | Khung huấn luyện & theo dõi nhân bản | [MỚI] | M | 3 |

### 2.3. Module Đào tạo

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| TR1 | Hạ tầng micro-course (tạo/quản lý/học) | Chưa có | LMS nhẹ: bài học ngắn, theo dõi tiến độ | [NỀN TẢNG] | L | 2 |
| TR2 | Nội dung chuyên sâu theo nhóm KH đặc thù | Chưa có | Khóa cho béo phì/tiểu đường/thai sản… | [MỚI] | M | 2 |
| TR3 | Thư viện KH: video tập, công thức, chuyên gia, câu chuyện | Chưa có | Thư viện nội dung đa dạng | [MỚI] | M | 2 |
| TR4 | Gamification học tập (thi đua, bảng xếp hạng) | Streak có sẵn ở tracking; chưa có cho học tập | Thi đua/tranh tài/điểm/huy hiệu | [MỚI] | M | 2 |
| TR5 | Ánh xạ micro-course 1:1 giáo trình quy trình + ngưỡng 70/80/90% làm cổng | Chưa có | Khai mở/HLCB1-2/BMO/Cầm tay chỉ việc/21 talking points; gate theo PSM | [MỚI] | M | 2 |
| TR6 | Playlist "đọc/xem/nghe" theo bước + hỗ trợ Tell-Show-Try-Do | Chưa có | Lộ trình học có ngữ cảnh + video/checklist Bước 8-11 | [MỚI] | M | 2-3 |

### 2.4. Module Phát triển bản thân

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| SD1 | Gợi ý thông minh cá nhân hóa nội dung/khóa học | Chưa có | Recommender theo dữ liệu & hành vi | [MỚI] | L | 3 |
| SD2 | Nội dung giới thiệu sản phẩm/cơ hội KD cho khách tiềm năng | Chưa có | Trang/luồng phễu cho tiềm năng | [MỚI] | M | 2 |
| SD3 | Lộ trình đào tạo có điều kiện cho HLV | Chưa có | Learning path + điều kiện + tài liệu | [MỚI] | M | 3 |
| SD4 | Lộ trình thăng tiến tới Giám sát viên (mở khóa theo mốc) | Chưa có | Trực quan hóa kế hoạch trả thưởng, gắn PSM Bước 6-12 | [MỚI] | M | 3 |
| SD5 | Khóa kỹ năng lãnh đạo/bảo trợ | Chưa có | Đào tạo dẫn tuyến dưới | [MỚI] | M | 3 |

### 2.5. Nền tảng & xuyên suốt

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| PF1 | Hệ thống thông báo đẩy (push) | Có chuông thông báo; chưa rõ push chủ động | Hạ tầng push cho nhắc nhở/chăm sóc | [NỀN TẢNG] | M | 1 |
| PF3 | Đo lường engagement/lan tỏa/học tập | Chưa có | Theo dõi share, hoàn thành khóa, giới thiệu | [DỮ LIỆU] | M | 1-2 |

> **Không tích hợp Herbalife:** AnCare là ứng dụng độc lập, KHÔNG đặt mục tiêu tích hợp kỹ thuật (SSO/đồng bộ dữ liệu) với VNHUB/Learning/SHOP/Pro2col. Quan hệ với các app này thuần túy là **bổ trợ về phạm vi** (AnCare không làm POS/kho/quản trị kinh doanh), không phải kết nối hệ thống.

---

### 2.6. Bổ sung từ review (2026-06-14) — test người dùng & định hướng PO

> Nguồn: `docs/reviews/20260614-01.md` (Đức, Mi), `20260614-02.md` (PO). *DMO = Daily Method of Operations (mô hình KD nhóm dinh dưỡng), không phải Digital Marketing Organization.*

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| RV1 | Kịch bản tư vấn nhanh 15 phút (+ gợi ý gói theo nhu cầu/tài chính) | Có nhập Tanita + bản tư vấn rời | Flow lõi: đo nhanh + DISC nhanh → tư vấn + gợi ý gói | [NÂNG CẤP] | M | 1 |
| RV2 | Cá nhân hóa theo thể trạng/bệnh lý nền | Gợi ý chung | AI khuyến nghị riêng (thận/phổi/tiểu đường…) | [MỚI] | L | 1-2 |
| RV3 | Thực đơn + nhật ký + AI nhận diện ảnh bữa ăn | Có tick + chụp ảnh (chưa AI) | AI nhận diện, chấm điểm, thiết kế thực đơn ngày sau | [MỚI] | L | 1-2 |
| RV4 | AnCare Health Score (tính năng "chữ ký") | Chưa có | Điểm 1–100 ngày/tuần/tháng, ngưỡng, khuyến khích chia sẻ | [MỚI] | M | 1 |
| RV5 | AI trả lời tức thì theo Skill Script → handoff HLV/bác sĩ | Chat có sẵn; AI chậm, không scripted | Phản hồi tức thì có kịch bản + điều hướng người thật | [MỚI] | L | 1 |
| RV6 | Kiểm duyệt/quản trị chất lượng câu trả lời AI | Chưa có | Giới hạn phạm vi + rà soát + log | [MỚI] | M | 1-2 |
| RV7 | Điểm danh/check-in tham gia | Chưa rõ | Ghi nhận điểm danh | [MỚI] | S | 2 |
| RV8 | Tích hợp wearable/health apps (Garmin/Coros/Apple Health) | Chưa có | Import dữ liệu sức khỏe | [MỚI] | M | 2-3 |
| RV9 | Tích hợp Google Calendar cho lịch 2/1 | Chưa có | Đồng bộ/nhắc/tránh trùng (bổ sung AC5) | [MỚI] | S | 2 |
| RV10 | UGC reward — khách làm KOL/KOC | Chưa có | Điểm thưởng theo nội dung & tương tác, đổi quà | [MỚI] | M | 3 |
| RV11 | "Chăm sóc chéo" cộng đồng (HLV cổ vũ khách của nhau) | Chưa có | Tương tác chúc mừng/thả tim chéo | [MỚI] | S | 2 |
| RV12 | Feedback Loop + SRS + tài liệu chuẩn hóa HLV | Chưa có | Kênh ghi nhận lỗi/góp ý real-time | [MỚI] | S | 1 |

## 3. KHOẢNG CÁCH TRỌNG TÂM (NHẬN ĐỊNH)

Khoảng cách lớn nhất **không** còn ở vận hành mà ở **năm trục trải nghiệm mới**: (1) **thu hút & chuyển đổi có AI hỗ trợ** (AC1–AC8 — trọng tâm cho Bước 1–2), (2) **lan tỏa/virality** (CJ4, CJ7), (3) **đào tạo/nội dung** (TR1–TR4, CJ5), (4) **phễu & kết nối** (CJ6, SD2), (5) **cá nhân hóa** (SD1). Các trục này chính là phần "lấp khoảng trống" mà tầm nhìn AnCare đặt ra so với app Herbalife hiện hữu.

Hai hạng mục công sức Cao (L) — hạ tầng micro-course (TR1), matching (CJ6) và recommender (SD1) — là các "viên gạch nền" cần PoC/đánh giá kỹ.

**Xương sống nối tất cả:** **Process State Model (PS1)** số hóa Sơ đồ dẫn (SĐD) là nền điều khiển cả 4 module — AC (Bước 1-2), Module 2/3/4 (Bước 3-12) đều cắm vào PSM. Cùng GNV (PS2) và DSKHTN (AC1) tạo đủ bộ 3 công cụ KD. Nên ưu tiên dựng khung PSM sớm (MVP-1).

---

## 4. PHÂN BỐ THEO MVP

> **Đã đảo ưu tiên theo PO (2026-06-14):** MVP-1 dồn vào **tư vấn & trải nghiệm sức khỏe (Lớp 1–2)**; phễu/đào tạo lùi về MVP-2. PSM giữ vai trò nền mỏng từ MVP-1.

- **MVP-1 (Tư vấn & Trải nghiệm sức khỏe — lõi PO):** **RV1** (tư vấn 15p), **RV3** (thực đơn + AI ảnh bữa ăn), **RV4** (Health Score), **RV5** (AI scripted + handoff), **RV2** (cá nhân hóa bệnh nền — phần an toàn), **RV12** (feedback loop) + CJ3 (nhắc nhở), CJ9, PF1, PF3 + **PS1, PS2** (nền mỏng) + AC8 (la bàn) + đo lường. *(RV6 kiểm duyệt AI đi kèm RV5.)*
- **MVP-2 (Học tập, Nội dung & Thu hút):** **PS3** + TR1–TR6 (micro-course 21 Talk + Quiz), CJ5, BJ3, BJ6, SD2 + AC1, AC2, AC3, AC5, AC7 + CJ4/CJ6/CJ7 (Content-Attribution) + BJ2 (chăm sóc dịp) + RV7 (điểm danh), RV9 (Calendar), RV11 (chăm sóc chéo), RV8 (wearable).
- **MVP-3 (Phễu lạnh, Matching fallback, Cá nhân hóa, Nhân bản & Sự nghiệp):** CJ8, BJ4, BJ5, BJ7, SD1, SD3, SD4, SD5 + AC4, AC8c + **RV10** (UGC reward) — phức tạp nhất.

---

## 5. RỦI RO & PHỤ THUỘC

- **Phụ thuộc nội dung:** Module Đào tạo (TR1–TR4) chỉ có giá trị khi có nội dung chất lượng — cần nguồn sản xuất & kiểm duyệt (chuyên gia).
- **Tuân thủ thương hiệu/quy định:** chia sẻ MXH (CJ4) về sức khỏe phải tuân thủ quy định Herbalife & pháp luật quảng cáo.
- **Cá nhân hóa (SD1):** chất lượng recommender phụ thuộc dữ liệu hành vi đủ lớn — rủi ro "cold start" giai đoạn đầu.

---

## 6. BƯỚC TIẾP THEO

Chuyển GAP v2.0 thành **To-do recommendations v2.0** theo module, kèm DoD & phụ thuộc.
