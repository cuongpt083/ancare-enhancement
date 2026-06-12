# **ĐẶC TẢ TIỂU MÔ-ĐUN: THU HÚT & CHUYỂN ĐỔI KHÁCH HÀNG (AI-ASSISTED)**

## *(Hỗ trợ Bước 1 → Giai đoạn đầu Bước 2 của Quy trình 12 bước kinh doanh)*

**Phiên bản:** v1.0
**Thuộc:** Module Hành trình khách hàng (Module 1) — To-be AnCare DXP v2.0.
**Đối tượng đọc:** BA, PO/PM, Đội phát triển.
**Cơ sở:** README.md (tầm nhìn 4 module), `docs/references/01.Quy-trinh-12-buoc-kinh-doanh.md` (Bước 1–2), As-Is v1.2.

---

## 1. BỐI CẢNH & VẤN ĐỀ

Bước 1 (đưa KHTN/TVTN đến cuộc gặp 2/1) và giai đoạn đầu Bước 2 (dẫn đến mô hình BMO phù hợp để trải nghiệm) là **nút thắt khi quy mô tăng** và **rào cản lớn nhất với người mới kinh doanh**. Khi ít khách, mọi việc làm tay được; khi nhiều lên, các việc *tìm kiếm – lập chân dung – làm ấm – mời – chuyển đổi* trở nên quá tải, dễ bỏ sót, và người mới thường "không biết tìm ai, nói gì, mời thế nào".

**Mục tiêu tiểu mô-đun:** biến AnCare thành **trợ lý phát triển khách hàng** số hóa và có AI hỗ trợ, giúp thực hiện đúng quy trình ở Bước 1–2 với năng suất cao và rào cản thấp — đồng thời **giữ đúng vai trò con người** và **tuân thủ** quy tắc nghiệp vụ.

### 1.1. Nguyên tắc nền (bám quy trình)

- **Người mới chỉ đóng vai KẾT NỐI**, không tư vấn/bán sản phẩm — việc thuyết phục sâu do TAB thực hiện ở cuộc gặp 2/1 (Business Rule của Bước 1). AI hỗ trợ kết nối/làm ấm/mời, **không thay người mới đi pitch**.
- **Tần suất & tuân thủ là yếu tố quyết định** — công cụ phải thúc đẩy hành động đều đặn theo trình tự, không nhảy cóc.
- **Bám sát 3 công cụ KD cốt lõi:** DSKHTN (danh sách KH tiềm năng), GNV (giấy nhắc việc), SĐD (sơ đồ dẫn).
- **Tôn trọng văn hóa Việt:** quan hệ ấm, cá nhân hóa, không spam đại trà.

---

## 2. CÁC NĂNG LỰC (CAPABILITIES)

### 2.1. DSKHTN số hóa (Digital Prospect List)
- Số hóa danh sách KH tiềm năng theo quy trình 3 bước (lập danh sách → làm ấm → trao lời mời).
- Nhập nhanh từ danh bạ/MXH; chống trùng; gắn thẻ nguồn (nóng/ấm/lạnh).
- Trạng thái từng lead theo phễu: *Mới → Đang làm ấm → Đã mời → Nhận lời → Đã đến 2/1 → Đang trải nghiệm (Bước 2)*.

### 2.2. Lập chân dung & chấm điểm lead (AI Profiling & Lead Scoring)
- Từ thông tin tối thiểu, AI gợi ý **phân khúc** (thừa/thiếu cân, tiểu đường, tim mạch, mẹ bỉm, dân văn phòng bận rộn, người cao tuổi…) và **"nỗi đau"** tiềm năng.
- **Lead score = độ phù hợp × độ ấm** → xếp thứ tự ưu tiên tiếp cận. *(Giải bài toán scale: làm việc với đúng người trước.)*
- Gợi ý "hôm nay nên chăm sóc/mời ai".

### 2.3. Engine cá nhân hóa làm ấm & mời (Nurture & Invite — phân tầng P1→P4)
> Bóc tách theo độ trưởng thành dữ liệu (chi tiết & DoD ở To-do TD-AC5-P1..P4). DISC chỉ là *một thẻ phụ*, không phải trung tâm.
- **P1 — Thư viện kịch bản thông minh:** tin làm ấm/khơi gợi/lời mời gắn thẻ DISC + **giai đoạn sẵn sàng thay đổi (Stage-of-Change)**; LLM viết lại cho mượt/đúng tông; HLV chọn & sửa. **Bảo toàn "lập trường" kết nối** ("tôi chưa giúp được bạn, hãy đi cùng tôi gặp người đã giúp tôi") — không lộ nội dung pitch. *(Không cần ML — chạy ngay.)*
- **P2 — Copilot theo Phỏng vấn tạo động lực (MI):** hỏi mở, khẳng định, phản chiếu, gợi "lời nói thay đổi", điều kiện theo giai đoạn sẵn sàng — nhân văn, không thao túng.
- **P3 — Chân dung động + khớp nội dung ngữ nghĩa:** suy luận phong cách/giai đoạn từ hành vi (tự cập nhật); RAG/embedding lấy "câu chuyện giống bạn"; look-alike. *(Cần dữ liệu hành vi.)*
- **P4 — Lớp tối ưu hóa:** uplift/persuadable + Next-Best-Action (contextual bandit) tự tối ưu nội dung–thời điểm–kênh. *(Cần lịch sử chuyển đổi đủ lớn.)*
- Xuyên suốt: theo dõi tín hiệu quan tâm (đã xem gì, mở mấy lần) để chọn thời điểm mời.

### 2.3b. AI nhập vai luyện tập cho người mới (Role-play)
- "Khách ảo" do AI đóng theo từng chân dung/giai đoạn để người mới tập làm ấm/mời; phản hồi theo MI. Ghép Module Đào tạo (To-do TD-AC9). Triển khai song song, không phụ thuộc dữ liệu.

### 2.4. Phễu thị trường lạnh + Chatbot (Cold-Market Funnel)
- Trang phễu/landing với **quiz sức khỏe** ("đánh giá nguy cơ", mini-test BMI/thói quen): vừa thu lead vừa **tự lập chân dung** đầu vào.
- **Chatbot AI** trả lời câu hỏi sức khỏe cơ bản, sàng lọc quan tâm, đặt lịch — và **luôn chuyển phần tư vấn sâu sang HLV/2/1** (tôn trọng quy tắc).
- Gắn với vòng lặp referral: câu chuyện thành công của khách hiện tại → thu hút người lạ → quy về người giới thiệu.

### 2.5. Đặt lịch & chuẩn bị cuộc gặp 2/1 (2/1 Orchestration)
- Đặt lịch cuộc gặp 2/1 (offline/Zoom), nhắc đồng thời **khách + TV giới thiệu + TAB**.
- Tự tổng hợp **hồ sơ lead** (chân dung, pain point, nội dung đã tương tác) gửi TAB trước buổi gặp để tăng tỉ lệ chốt.
- Ghi nhận kết quả buổi gặp → cập nhật trạng thái phễu.

### 2.6. Matching KHTN ↔ HLV / BMO phù hợp
- Gợi ý **HLV phù hợp** theo khu vực, chuyên môn DMO, tải khách hiện tại.
- Gợi ý **mô hình BMO** (NDD/Fit/Yoga/online) hợp đặc điểm khách (tuổi, mục tiêu, thời gian, sở thích).
- **Khách ở xa:** tự tìm nhà vận hành gần nhất để "gửi khách" (plug-in) — đúng lưu ý trong tài liệu quy trình.

### 2.7. Giai đoạn đầu Bước 2 — Buổi trải nghiệm đầu tiên
- Hồ sơ chảy **liền mạch** từ lead → khách trải nghiệm (không nhập lại).
- **Checklist đón tiếp** số hóa theo 10 vai trò BMO (chào đón, hỏi mong muốn, giới thiệu mô hình, cam kết giá trị, nội quy, hướng dẫn sản phẩm…).
- Thu thập mong muốn + thói quen; OCR chỉ số Tanita (đã có) → **AI gợi ý chế độ ăn/vận động cá nhân hóa** (nâng cấp năng lực sẵn có).

### 2.8. La bàn quy trình & nhắc tần suất (Process Compass)
- Hiển thị mỗi lead/khách **đang ở chặng nào** của Bước 1–2 và **việc cần làm tiếp theo**.
- **Nhắc nhịp hành động** (cadence) cho người mới: số lời mời/ngày, lead cần làm ấm, follow-up đến hạn.
- Đo **phễu chuyển đổi**: số kết nối → lời mời → nhận lời → đến 2/1 → vào trải nghiệm. *(Tạo baseline số liệu đang thiếu.)*

---

## 3. VAI TRÒ AI — TÓM TẮT

| Năng lực AI | Giải quyết |
| :-- | :-- |
| Lead scoring & ưu tiên | Quá tải khi scale — tập trung đúng người |
| Copilot soạn nội dung/tin nhắn | Rào cản người mới — "không biết nói gì" |
| Phân khúc & gợi ý nội dung | Cá nhân hóa làm ấm theo pain point |
| Chatbot sàng lọc + đặt lịch | Tự động hóa đầu phễu thị trường lạnh |
| Nhắc tần suất theo quy trình | Kỷ luật & tuân thủ trình tự |

---

## 4. RÀNG BUỘC & TUÂN THỦ (GUARDRAILS)

1. **Không thay vai con người:** AI hỗ trợ kết nối/làm ấm/mời/sàng lọc; KHÔNG thay người mới tư vấn sản phẩm, KHÔNG thay cuộc gặp 2/1.
2. **Tuân thủ quy định sức khỏe/quảng cáo:** nội dung phễu & chatbot về sức khỏe phải tuân thủ quy định Herbalife và pháp luật Việt Nam; tránh tuyên bố công dụng quá mức.
3. **Riêng tư dữ liệu:** chân dung & chấm điểm lead dựa trên dữ liệu được phép thu thập; minh bạch & cho phép opt-out.
4. **Chống spam:** giữ tính cá nhân, có giới hạn tần suất gửi; tôn trọng văn hóa quan hệ ấm của người Việt.
5. **Độc lập với Herbalife apps:** không tích hợp kỹ thuật VNHUB/Learning/SHOP; dữ liệu điểm/đơn hàng không thuộc phạm vi.

---

## 5. THƯỚC ĐO THÀNH CÔNG

- **Năng suất:** số lead một HLV/người mới xử lý được, tỷ lệ lead không bị "bỏ rơi".
- **Phễu chuyển đổi:** tỷ lệ kết nối→mời→nhận lời→đến 2/1→vào trải nghiệm.
- **Rào cản người mới:** thời gian từ lúc bắt đầu đến lời mời đầu tiên / khách đầu tiên đến 2/1.
- **Chất lượng matching:** tỷ lệ khách được ghép tiếp tục trải nghiệm tại BMO.

---

## 6. PHỤ THUỘC & LƯU Ý TRIỂN KHAI

- Cần **kho nội dung** (bài viết/video/câu chuyện thành công) để AI làm ấm & phễu hoạt động → liên kết Module Đào tạo.
- Cold-start cho lead scoring: giai đoạn đầu dùng quy tắc (rule-based) trước, học dần khi đủ dữ liệu.
- PoC khuyến nghị: chatbot sàng lọc + lead scoring + copilot soạn lời mời.
