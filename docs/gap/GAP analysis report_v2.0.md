# **PHÂN TÍCH KHOẢNG CÁCH (GAP) — ANCARE DXP**

**Phiên bản:** v2.0 — *Đối chiếu theo định hướng DXP. Thay thế GAP v1.0.*
**Cơ sở:** As-Is v1.2 (`docs/as-is/`, gồm 2 phụ lục) ↔ To-be v2.0 (`docs/to-be/To-be study report_v2.0.md`).

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
| CJ4 | Tạo & chia sẻ câu chuyện thành công ra MXH | Có đồ thị nội bộ; chưa chia sẻ | Sinh nội dung giàu cảm xúc, 1 chạm share | [MỚI] | M | 1 |
| CJ5 | Kho nội dung kiến thức cho khách tiềm năng | Chưa có | Nội dung sinh động, cô đọng | [MỚI] | M | 2 |
| CJ6 | Kết nối khách tiềm năng ↔ HLV phù hợp (matching) | Chưa có (HLV tự tạo lead) | Cơ chế gợi ý/ghép HLV | [MỚI] | L | 3 |
| CJ7 | Vòng lặp giới thiệu (referral) | Chưa có | Mời bạn bè/người thân, theo dõi giới thiệu | [MỚI] | M | 3 |
| CJ8 | Buổi sinh hoạt HOM (thông tin & tham gia) | Chưa có trong app | Lịch HOM, chủ đề, đăng ký | [MỚI] | M | 3 |
| CJ9 | Gián đoạn khi hết gói (rủi ro bỏ cuộc - C4) | Chặn cứng check-in | Trải nghiệm gia hạn mềm hơn | [NÂNG CẤP] | S | 1 |

### 2.2. Module Hành trình kinh doanh (HLV)

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| BJ1 | Quản lý KH, onboarding, journey, báo cáo | Đã có đầy đủ | Giữ | [ĐÃ CÓ] | — | — |
| BJ2 | Chăm sóc theo dịp đặc biệt + động viên | Chưa có | Nhắc sinh nhật/kỷ niệm/lễ, gợi ý lời động viên | [MỚI] | M | 1 |
| BJ3 | Chia sẻ nội dung sản phẩm/giải pháp/cơ hội KD (prospecting) | Chưa có | Bộ nội dung & công cụ chia sẻ | [MỚI] | M | 2 |
| BJ4 | Định hướng phát triển kỹ năng & lộ trình thăng tiến | Chưa có | Liên kết Module Đào tạo/PT bản thân | [MỚI] | M | 2-3 |
| BJ5 | Công cụ vận hành DMO đa mô hình (bổ trợ VNHUB) | Một phần (app HLV cơ bản) | Mở rộng theo mô hình club | [NÂNG CẤP] | M | 3 |

### 2.3. Module Đào tạo

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| TR1 | Hạ tầng micro-course (tạo/quản lý/học) | Chưa có | LMS nhẹ: bài học ngắn, theo dõi tiến độ | [NỀN TẢNG] | L | 2 |
| TR2 | Nội dung chuyên sâu theo nhóm KH đặc thù | Chưa có | Khóa cho béo phì/tiểu đường/thai sản… | [MỚI] | M | 2 |
| TR3 | Thư viện KH: video tập, công thức, chuyên gia, câu chuyện | Chưa có | Thư viện nội dung đa dạng | [MỚI] | M | 2 |
| TR4 | Gamification học tập (thi đua, bảng xếp hạng) | Streak có sẵn ở tracking; chưa có cho học tập | Thi đua/tranh tài/điểm/huy hiệu | [MỚI] | M | 2 |

### 2.4. Module Phát triển bản thân

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| SD1 | Gợi ý thông minh cá nhân hóa nội dung/khóa học | Chưa có | Recommender theo dữ liệu & hành vi | [MỚI] | L | 3 |
| SD2 | Nội dung giới thiệu sản phẩm/cơ hội KD cho khách tiềm năng | Chưa có | Trang/luồng phễu cho tiềm năng | [MỚI] | M | 2 |
| SD3 | Lộ trình đào tạo có điều kiện cho HLV | Chưa có | Learning path + điều kiện + tài liệu | [MỚI] | M | 3 |

### 2.5. Nền tảng & xuyên suốt

| # | Hạng mục | As-Is | To-be | Loại | CS | MVP |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: |
| PF1 | Hệ thống thông báo đẩy (push) | Có chuông thông báo; chưa rõ push chủ động | Hạ tầng push cho nhắc nhở/chăm sóc | [NỀN TẢNG] | M | 1 |
| PF3 | Đo lường engagement/lan tỏa/học tập | Chưa có | Theo dõi share, hoàn thành khóa, giới thiệu | [DỮ LIỆU] | M | 1-2 |

> **Không tích hợp Herbalife:** AnCare là ứng dụng độc lập, KHÔNG đặt mục tiêu tích hợp kỹ thuật (SSO/đồng bộ dữ liệu) với VNHUB/Learning/SHOP/Pro2col. Quan hệ với các app này thuần túy là **bổ trợ về phạm vi** (AnCare không làm POS/kho/quản trị kinh doanh), không phải kết nối hệ thống.

---

## 3. KHOẢNG CÁCH TRỌNG TÂM (NHẬN ĐỊNH)

Khoảng cách lớn nhất **không** còn ở vận hành mà ở **bốn trục trải nghiệm mới**: (1) **lan tỏa/virality** (CJ4, CJ7), (2) **đào tạo/nội dung** (TR1–TR4, CJ5, TR3), (3) **phễu & kết nối** (CJ6, SD2), (4) **cá nhân hóa** (SD1). Các trục này chính là phần "lấp khoảng trống" mà tầm nhìn AnCare đặt ra so với app Herbalife hiện hữu.

Hai hạng mục công sức Cao (L) — hạ tầng micro-course (TR1), matching (CJ6) và recommender (SD1) — là các "viên gạch nền" cần PoC/đánh giá kỹ.

---

## 4. PHÂN BỐ THEO MVP

- **MVP-1 (Lan tỏa & Gắn kết):** CJ3, CJ4, CJ9, BJ2, PF1, PF3 — tận dụng dữ liệu sẵn có, tạo giá trị engagement nhanh.
- **MVP-2 (Học tập & Nội dung):** TR1–TR4, CJ5, BJ3, SD2 — nặng về nền tảng đào tạo.
- **MVP-3 (Phễu & Cá nhân hóa):** CJ6, CJ7, CJ8, BJ4, BJ5, SD1, SD3 — phức tạp nhất (matching, recommender).

---

## 5. RỦI RO & PHỤ THUỘC

- **Phụ thuộc nội dung:** Module Đào tạo (TR1–TR4) chỉ có giá trị khi có nội dung chất lượng — cần nguồn sản xuất & kiểm duyệt (chuyên gia).
- **Tuân thủ thương hiệu/quy định:** chia sẻ MXH (CJ4) về sức khỏe phải tuân thủ quy định Herbalife & pháp luật quảng cáo.
- **Cá nhân hóa (SD1):** chất lượng recommender phụ thuộc dữ liệu hành vi đủ lớn — rủi ro "cold start" giai đoạn đầu.

---

## 6. BƯỚC TIẾP THEO

Chuyển GAP v2.0 thành **To-do recommendations v2.0** theo module, kèm DoD & phụ thuộc.
