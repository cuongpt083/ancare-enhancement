# **KHUYẾN NGHỊ HÀNH ĐỘNG (TO-DO) — ANCARE DXP**

**Phiên bản:** v2.0 — *Theo định hướng DXP. Thay thế To-do v1.0.*
**Cơ sở:** GAP v2.0 (`docs/gap/GAP analysis report_v2.0.md`), To-be v2.0, As-Is v1.2.

> Mỗi hạng mục tham chiếu mã GAP gốc (CJ/BJ/TR/SD/PF). **DoD** = tiêu chí nghiệm thu tối thiểu. Đã loại bỏ mọi hạng mục POS/kho/quản trị kinh doanh (thuộc VNHUB).

---

## 1. MVP-1 — LAN TỎA & GẮN KẾT

> Mục tiêu: tạo giá trị engagement nhanh trên nền dữ liệu/tính năng đã có.

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

---

## 4. SƠ ĐỒ THỨ TỰ (TÓM TẮT)

```
MVP-1:  TD-1.1 → {TD-1.2, TD-1.4} ; TD-1.3 ; TD-1.5 ; {TD-1.2,TD-1.3} → TD-1.6
MVP-2:  TD-2.1 → {TD-2.2, TD-2.3, TD-2.4} → {TD-2.5, TD-2.6}
MVP-3:  TD-2.6 → TD-3.1 → TD-3.2 ; TD-1.1 → TD-3.3 ;
        {TD-2.1,TD-2.4,TD-1.6} → TD-3.4 ; TD-2.1 → TD-3.5 ; TD-3.6 (độc lập)
```

---

## 5. KHUYẾN NGHỊ TRIỂN KHAI

1. **Khởi động MVP-1 trước:** tận dụng dữ liệu/tính năng đã có (tracking, chat, đồ thị) để tạo giá trị lan tỏa & chăm sóc nhanh, chi phí thấp.
2. **AnCare độc lập, không tích hợp Herbalife:** không đầu tư SSO/đồng bộ dữ liệu; tự quản lý tài khoản & dữ liệu người dùng.
3. **Đảm bảo nguồn nội dung trước khi xây LMS:** Module Đào tạo vô nghĩa nếu thiếu nội dung chất lượng — chuẩn bị quy trình sản xuất & kiểm duyệt song song TD-2.1.
4. **PoC cho hạng mục công sức cao:** micro-course (TD-2.1), matching (TD-3.1), recommender (TD-3.4).
5. **Tuân thủ quy định chia sẻ sức khỏe (TD-1.3):** rà soát pháp lý & thương hiệu trước khi mở chia sẻ MXH.
6. **Cài đo lường engagement (TD-1.6) ngay từ MVP-1** để có baseline.

---

## 6. KẾT THÚC QUY TRÌNH

Chuỗi tài liệu phiên bản DXP: README (tầm nhìn) → As-Is v1.2 → To-be v2.0 → GAP v2.0 → To-do v2.0. Bước tiếp theo khả dĩ: nghiên cứu khả thi v2.0 cho lộ trình DXP, hoặc thiết kế chi tiết từng module.
