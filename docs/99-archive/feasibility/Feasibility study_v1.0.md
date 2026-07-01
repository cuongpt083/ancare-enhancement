# **NGHIÊN CỨU KHẢ THI KỸ THUẬT & ƯỚC LƯỢNG — HỆ SINH THÁI AN-CARE**

**Phiên bản:** v1.0
**Đối tượng đọc:** Nhà sáng lập / Ban quản lý (phi kỹ thuật), Product Owner, BA.
**Phạm vi ước lượng:** Toàn bộ lộ trình MVP-1, MVP-2, MVP-3 theo To-do recommendations v1.0.
**Mô hình triển khai:** Cloud. **Bàn giao:** phần mềm + đào tạo + 3 tháng hypercare. **Phần cứng:** ngoài phạm vi (dùng dịch vụ cloud).
**Cơ sở yêu cầu:** As-Is v1.1, To-be v1.0, GAP v1.0, To-do v1.0 (`docs/`).

> Báo cáo trả lời ba câu hỏi: (1) Có xây được không? (2) Bao nhiêu tháng? (3) Bao nhiêu tiền? Đây **không** phải business case hay phân tích ROI.

---

## I. TÓM TẮT ĐIỀU HÀNH

An-Care To-be là một **hệ sinh thái đa vai trò** gồm app cho Huấn luyện viên (HLV), app cho Khách hàng, và dashboard quản trị cho Nhà sáng lập, đặt trên một nền dữ liệu giao dịch (bán lẻ/kho) và đồng bộ HLV ↔ Khách.

| Chỉ số phạm vi | Giá trị |
| :-- | :-- |
| Tổng số yêu cầu (ước tính) | ~192 |
| Số phân hệ | 17 |
| Số nhóm người dùng (actor) | 6 |
| Số tích hợp ngoài | 5 |
| Kênh phân phối | 3 (app HLV, app Khách, web Founder) |

**Kết luận khả thi (tóm tắt):** Dự án **KHẢ THI** về kỹ thuật — toàn bộ yêu cầu ánh xạ được sang công nghệ đã chứng minh trong sản xuất, không có hạng mục cần R&D không lối ra. Có 2-3 hạng mục "Rất cao" (đồng bộ dữ liệu lai, sinh infographic, dự báo tài chính) nên làm **PoC** trước khi cam kết toàn bộ ngân sách lớp tương ứng.

| Chỉ số then chốt | Giá trị |
| :-- | :-- |
| Tổng chi phí (dải ước tính) | **~3,8 – 5,7 tỷ VND** (điểm ~4,75 tỷ) |
| Thời gian | **~11 tháng** (10–12, có track song song) |
| Quy mô đội đỉnh điểm | ~10–11 người |
| Rủi ro hàng đầu | Mở rộng phạm vi đa app & đồng bộ dữ liệu lai Tanita |

---

## II. PHẠM VI & QUY MÔ

### II.1. Danh mục phân hệ

| STT | Phân hệ | Mô tả | Số YC | MVP |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Catalog sản phẩm | Danh mục Herbalife: mã vạch, giá, nhóm | 8 | 1 |
| 2 | POS bán lẻ | Quét mã vạch, giỏ hàng, chốt đơn, khách vãng lai, lịch sử | 12 | 1 |
| 3 | Quản lý kho | Xuất/nhập gắn người, tự trừ kho, đối soát cuối ngày | 12 | 1 |
| 4 | Hồ sơ hành trình số hóa | Timeline check-in, chỉ số Tanita, cột mốc, ghi chú | 10 | 2 |
| 5 | Lead & Khảo sát DISC | Tối ưu form lead, khảo sát, bài tư vấn cá nhân hóa | 10 | 2 |
| 6 | Báo cáo tài chính | Thu/chi, lời/lỗ (COGS, hoa hồng), dự báo, cảnh báo | 14 | 1-2 |
| 7 | Chân dung khách hàng | Phân nhóm theo giá trị/gắn bó/kênh | 8 | 2 |
| 8 | Tồn kho nâng cao | Tổng hợp tồn, ngưỡng cảnh báo, gợi ý nhập | 6 | 2 |
| 9 | CRM chăm sóc | Tự động dịp lễ, mẫu tin, nhắc thủ công | 10 | 2 |
| 10 | Dashboard & phân quyền đa club | Vai trò Founder, gộp đa club, dashboard | 12 | 2 |
| 11 | Đo lường & Analytics | Chỉ số vận hành, giữ chân, tăng trưởng | 8 | 1-2 |
| 12 | Nền tảng app khách + tài khoản | App khách, mô hình account, onboard mời, xác thực | 16 | 3 |
| 13 | Sổ sức khỏe số (dữ liệu lai) | Khách tự log + đồng bộ Tanita, hợp nhất | 14 | 3 |
| 14 | Nhắc nhở kết hợp | Khung nhắc, push, lịch, theo dõi tuân thủ | 12 | 3 |
| 15 | Chia sẻ tự động | Sinh infographic hành trình, chia sẻ MXH | 10 | 3 |
| 16 | Giữ chân & gamification | Đồ thị tiến bộ, streak/huy hiệu, cộng đồng | 12 | 3 |
| 17 | Tích hợp & nâng cấp app HLV hiện có | Refactor, nối các tab sẵn có (Team/Chat/Profile) | 8 | 1-3 |
| | **TỔNG** | | **~192** | |

### II.2. Nhóm người dùng (Actor)

| Actor | Vai trò |
| :-- | :-- |
| Nhà sáng lập | Quản trị kinh doanh, đa club |
| Nhà vận hành / HLV | Vận hành club, tư vấn, đồng hành |
| Đồng vận hành | Cùng xuất kho/bán lẻ trong club |
| Khách hàng (thành viên) | Trải nghiệm lộ trình, dùng app khách |
| Khách vãng lai | Mua lẻ, chưa là thành viên |
| Quản trị hệ thống / Trợ lý AI | Cấu hình hệ thống; AI tư vấn (đã có) |

### II.3. Quy trình nghiệp vụ chính

Bán lẻ & đối soát cuối ngày; quản lý xuất/nhập kho đa người; lập lead → khảo sát → tư vấn → chuyển đổi; theo dõi hành trình 30 ngày; đồng hành/nhắc nhở từ xa; chia sẻ kết quả; báo cáo kinh doanh & CRM chăm sóc.

---

## III. ĐÁNH GIÁ KHẢ THI KỸ THUẬT

### III.1. Phân bố độ phức tạp

| Mức | Phân hệ tiêu biểu | Tỷ trọng |
| :-- | :-- | :-- |
| **Rất cao** | Sổ sức khỏe số (đồng bộ dữ liệu lai), Sinh infographic tự động, Dự báo tài chính | ~18% |
| **Cao** | POS+Kho đồng bộ realtime, Nền tảng app khách + phân quyền đa vai trò, Nhắc nhở push, Gộp đa club | ~30% |
| **Trung bình** | Hồ sơ hành trình, Chân dung KH, CRM, Gamification | ~30% |
| **Thấp** | Catalog, Tồn kho cảnh báo, Đo lường, Tối ưu khảo sát | ~22% |

> ~48% yêu cầu ở mức Cao/Rất cao → áp **dự phòng 15%** (không phải 10%).

### III.2. Ngăn xếp công nghệ đề xuất

| Lớp | Công nghệ | Lý do chọn |
| :-- | :-- | :-- |
| Backend | Node.js (NestJS) hoặc Java Spring Boot | Phù hợp thị trường VN, chứng minh ở quy mô tương tự |
| CSDL giao dịch | PostgreSQL | Row-level security, không phí license; đủ cho quy mô |
| Object storage | S3/GCS (cloud) | Lưu ảnh infographic, tài liệu |
| Frontend (web Founder) | React + TypeScript | Chuẩn ngành, nhân lực dồi dào |
| App Khách (mới) | React Native | Một codebase iOS + Android, tiết kiệm |
| App HLV (hiện có) | Nâng cấp trên nền tảng sẵn có | Tránh viết lại; bổ sung POS/kho/hành trình |
| Push notification | FCM + APNs | Tiêu chuẩn nhắc nhở di động |
| Xác thực/OTP | Zalo/SMS provider | Onboarding khách bằng SĐT |
| Sinh infographic | Render server-side (chart lib) | Tạo ảnh hành trình từ dữ liệu thật |
| Phân tích/báo cáo | PostgreSQL + Metabase | Đủ cho quy mô; không cần OLAP nặng |
| Hạ tầng | Cloud managed K8s hoặc container service | Co giãn, giảm gánh DevOps |

Không có thành phần nào cần R&D không lối ra. **Cờ PoC** cho: đồng bộ dữ liệu lai Tanita (phân hệ 13) và sinh infographic (phân hệ 15).

### III.3. Hạ tầng (cloud)

Môi trường dev/staging/prod tách biệt; container hóa; CDN cho ảnh chia sẻ; sao lưu CSDL định kỳ; giám sát & log tập trung. Chi phí vận hành cloud là **chi phí định kỳ**, tách khỏi chi phí xây dựng (ước tính riêng ở phần ghi chú).

---

## IV. KIẾN TRÚC HỆ THỐNG

### IV.1. Kiến trúc phân lớp

| Lớp | Thành phần |
| :-- | :-- |
| Trải nghiệm | App HLV (nâng cấp), App Khách (RN), Web Founder (React) |
| API / Dịch vụ | API backend (POS, kho, hồ sơ, CRM, báo cáo, nhắc nhở, chia sẻ) |
| Nghiệp vụ | Engine bán lẻ/kho, engine hành trình & cột mốc, engine phân nhóm KH, engine nhắc nhở |
| Dữ liệu | PostgreSQL (giao dịch), Object storage (ảnh/tài liệu), lớp phân tích |
| Tích hợp | Push (FCM/APNs), OTP (Zalo/SMS), chia sẻ MXH, nhập dữ liệu Tanita |
| Hạ tầng & vận hành | Container/K8s cloud, CI/CD, giám sát, sao lưu |

### IV.2. Quyết định kiến trúc then chốt

| Quyết định | Lựa chọn | Phương án thay thế | Chi phí nếu đảo ngược |
| :-- | :-- | :-- | :-- |
| App khách đa nền tảng | React Native | Native iOS + Android riêng | Cao (gấp đôi công mobile) |
| CSDL phân tích | PostgreSQL + Metabase | ClickHouse (OLAP) | Trung bình (chỉ khi dữ liệu >100M dòng) |
| Đồng bộ Tanita | Nhập/đồng bộ từ buổi đo tại club | Tích hợp trực tiếp thiết bị cân | Cao (phụ thuộc API thiết bị) |
| Backend | Một service module hóa | Microservices | Trung bình–Cao |

---

## V. KẾ HOẠCH TRIỂN KHAI

### V.1. Các giai đoạn

| GĐ | Tên | Thời gian | Nội dung chính |
| :-- | :-- | :-- | :-- |
| GĐ0 | Khởi động & PoC | Tháng 1 | Thiết lập hạ tầng, PoC đồng bộ Tanita & infographic, chuẩn hóa yêu cầu |
| GĐ1 | MVP-1 Vận hành | Tháng 1–4 | Catalog, POS, kho, thu/chi cơ bản, đo lường |
| GĐ2 | MVP-2 Hồ sơ & quản trị | Tháng 4–7 | Hồ sơ hành trình, tối ưu DISC, dashboard Founder, lời/lỗ + dự báo, CRM |
| GĐ3 | MVP-3 App khách | Tháng 7–11 | Nền tảng app khách, sổ sức khỏe số, nhắc nhở, chia sẻ, gamification |
| GĐ4 | Hypercare | 3 tháng sau go-live từng lớp | Hỗ trợ vận hành, sửa lỗi, tinh chỉnh |

### V.2. Gantt tổng quát (1 ô = 1 tháng)

| Hạng mục | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Khởi động & PoC | ██ | | | | | | | | | | |
| MVP-1 | ██ | ██ | ██ | ██ | | | | | | | |
| MVP-2 | | | | ██ | ██ | ██ | ██ | | | | |
| MVP-3 | | | | | | | ██ | ██ | ██ | ██ | ██ |
| Đo lường (xuyên suốt) | | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ |

### V.3. Thành phần đội

| Vai trò | Số lượng | Số tháng tham gia |
| :-- | :-: | :-: |
| Project Manager | 1 | 11 |
| Business Analyst | 1 | 8 |
| Technical Architect / Lead | 1 | 11 |
| Backend Developer | 2 | 11 / 9 |
| Frontend Developer (web) | 1 | 7 |
| Mobile Developer (RN khách) | 1 | 8 |
| Mobile Developer (app HLV) | 1 | 6 |
| UI/UX Designer | 1 | 5 |
| QA Engineer | 1 | 9 |
| DevOps | 1 | 6 |

Đỉnh điểm ~10–11 người (GĐ giao thoa MVP-2/MVP-3).

---

## VI. ƯỚC TÍNH CHI PHÍ

> Đơn vị: triệu VND. Đơn giá tham chiếu thị trường VN 2025–2026 (gross).

### VI.1. Chi phí nhân sự

| Vai trò | SL | Tháng | Đơn giá | Thành tiền |
| :-- | :-: | :-: | :-: | --: |
| Project Manager | 1 | 11 | 45 | 495 |
| Business Analyst | 1 | 8 | 35 | 280 |
| Technical Architect/Lead | 1 | 11 | 52 | 572 |
| Backend Developer #1 | 1 | 11 | 35 | 385 |
| Backend Developer #2 | 1 | 9 | 35 | 315 |
| Frontend Developer (web) | 1 | 7 | 30 | 210 |
| Mobile Developer (RN khách) | 1 | 8 | 32 | 256 |
| Mobile Developer (app HLV) | 1 | 6 | 32 | 192 |
| UI/UX Designer | 1 | 5 | 30 | 150 |
| QA Engineer | 1 | 9 | 28 | 252 |
| DevOps | 1 | 6 | 42 | 252 |
| **Cộng nhân sự** | | | | **3.359** |

### VI.2. Chi phí ngoài nhân sự

| Hạng mục | Cơ sở | Thành tiền |
| :-- | :-- | --: |
| Công cụ & license | ~2,5% nhân sự | 84 |
| Đào tạo & tài liệu | ~3,5% nhân sự | 118 |
| Thiết lập go-live | ~3% nhân sự | 101 |
| Hypercare 3 tháng | 1 kỹ sư × 32 × 3 | 96 |
| **Cộng ngoài nhân sự** | | **399** |

### VI.3. Tổng hợp

| Khoản | Thành tiền (triệu VND) |
| :-- | --: |
| Trực tiếp (nhân sự + ngoài nhân sự) | 3.758 |
| Overhead (10%) | 376 |
| Dự phòng (15%) | 620 |
| **Tổng (điểm ước tính)** | **~4.754** |
| **Dải ước tính (±20%)** | **~3.800 – 5.700** |

> **Ghi chú chi phí cloud (định kỳ, ngoài chi phí xây dựng):** ước tính ~15–40 triệu VND/tháng tùy lượng người dùng và dung lượng ảnh/dữ liệu — cần tinh chỉnh khi rõ quy mô.

---

## VII. ĐÁNH GIÁ RỦI RO

| Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu |
| :-- | :-- | :-- | :-- |
| Mở rộng phạm vi đa app vượt nguồn lực | Cao | Cao | Cổng quyết định sau MVP-2: chỉ cam kết ngân sách MVP-3 khi MVP-1/2 đạt nghiệm thu; có thể tách thầu MVP-3 |
| Đồng bộ dữ liệu lai Tanita xung đột/trùng | Cao | Cao | PoC trong Tháng 1; chốt nguồn ưu tiên (club vs khách tự nhập) và quy tắc hợp nhất trước khi build phân hệ 13 |
| Thiếu baseline → khó chứng minh hiệu quả | Cao | Trung bình | Cài đo lường (D1) ngay từ MVP-1, thu thập ≥2 tuần làm mốc |
| Sinh infographic không đạt kỳ vọng cảm xúc | Trung bình | Trung bình | PoC mẫu chia sẻ sớm; lấy phản hồi HLV/khách trước khi hoàn thiện |
| Phụ thuộc nhà cung cấp OTP/MXH | Trung bình | Trung bình | Dùng sandbox + mock; thiết kế để onboarding/chia sẻ có phương án dự phòng |
| Giữ nhân sự hiếm (mobile RN, DevOps) suốt 11 tháng | Trung bình | Trung bình | Chính sách chuyển giao tri thức; không để một người là điểm chết của một phân hệ |
| Người dùng quen sổ giấy chậm thích nghi | Trung bình | Trung bình | Đào tạo tại club, thiết kế UX tối giản, chạy song song sổ giấy giai đoạn đầu |

---

## VIII. KẾT LUẬN & KHUYẾN NGHỊ

### VIII.1. Phán quyết 4 chiều

| Tiêu chí | Kết quả | Cơ sở đánh giá |
| :-- | :-- | :-- |
| Kỹ thuật | ✓ Khả thi (có điều kiện) | Mọi YC ánh xạ công nghệ đã chứng minh; 2 hạng mục Rất cao cần PoC |
| Nhân lực | ~ Có điều kiện | Đội tuyển được tại VN; cần giữ chân RN/DevOps suốt 11 tháng |
| Thời gian | ✓ Khả thi | Đường găng có track song song; ~11 tháng hợp lý |
| Ngân sách | ~ Có điều kiện | Dải ~3,8–5,7 tỷ; PoC giúp thu hẹp dải trước cam kết MVP-3 |

### VIII.2. Khuyến nghị ưu tiên

1. **Bắt đầu bằng GĐ0 (PoC + hạ tầng)** trước khi cam kết toàn bộ ngân sách — đặc biệt PoC đồng bộ Tanita và infographic.
2. **Đặt cổng quyết định sau MVP-2:** đánh giá kết quả & baseline thực tế rồi mới giải ngân MVP-3 (khoản đầu tư lớn nhất).
3. **Cài đo lường ngay từ MVP-1** để có dữ liệu chứng minh hiệu quả vận hành.
4. **Chốt sớm hợp đồng nhân sự hiếm** (mobile RN, DevOps) cho trọn vòng đời dự án.
5. **Tách bạch chi phí cloud định kỳ** trong kế hoạch tài chính vận hành.

### VIII.3. Điều kiện tiên quyết để khởi động

Chuẩn hóa danh mục sản phẩm Herbalife (mã vạch, giá); xác nhận nguồn dữ liệu Tanita và quy tắc đồng bộ; quyết định nhà cung cấp OTP/MXH; chốt nguồn lực đội và mô hình hợp tác (in-house vs thuê ngoài).

> **Lưu ý ước lượng:** các con số trên mang tính định tính do hiện trạng chưa có baseline; cần tinh chỉnh sau GĐ0 và sau khi có dữ liệu thực tế từ MVP-1.
