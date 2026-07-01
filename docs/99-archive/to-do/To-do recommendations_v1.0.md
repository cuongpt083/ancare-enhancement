# **KHUYẾN NGHỊ HÀNH ĐỘNG (TO-DO RECOMMENDATIONS) — ỨNG DỤNG AN-CARE**

**Phiên bản:** v1.0
**Đối tượng sử dụng tài liệu:** Product Owner, BA, Đội ngũ Phát triển, Nhà sáng lập.
**Cơ sở:** GAP analysis report v1.0 (`docs/gap/`), To-be study report v1.0, As-Is study report v1.1.
**Mục tiêu:** Chuyển từng khoảng cách (GAP) thành hạng mục hành động cụ thể, sắp xếp theo lớp MVP và quan hệ phụ thuộc, kèm sản phẩm bàn giao và tiêu chí nghiệm thu (Definition of Done – DoD).

---

## 1. CÁCH ĐỌC TÀI LIỆU

- Mỗi hạng mục To-do tham chiếu mã GAP gốc (vd: `H1`, `N1`) để truy vết.
- **DoD** = tiêu chí nghiệm thu tối thiểu để coi hạng mục là "xong".
- **Phụ thuộc** = hạng mục phải hoàn thành trước.
- Thứ tự thực hiện đề xuất tuân theo lớp MVP; trong cùng một lớp, làm nền tảng trước.

---

## 2. MVP-1 — "VẬN HÀNH KHÔNG THẤT THOÁT"

> Mục tiêu lớp: chặn thất thoát bán lẻ/kho và cài đặt đo lường hiệu quả vận hành.

### TD-1.1 — Xây catalog sản phẩm có mã vạch *(GAP N1, nền tảng)*
- **Hành động:** Tạo danh mục sản phẩm Herbalife chuẩn hóa: tên, mã vạch, đơn giá, đơn vị, nhóm sản phẩm; cho phép cập nhật giá.
- **Sản phẩm bàn giao:** Module quản lý catalog + dữ liệu sản phẩm thực tế đã nhập.
- **DoD:** Quét được mã vạch ra đúng sản phẩm & giá; sửa giá phản ánh ngay vào POS.
- **Phụ thuộc:** — (làm đầu tiên).

### TD-1.2 — Màn hình bán lẻ POS quét mã vạch *(GAP H1)*
- **Hành động:** Bán lẻ bằng quét barcode, tự cộng tiền, chốt đơn; ghi nhận người bán và thời điểm; hỗ trợ khách vãng lai (chưa là thành viên).
- **Sản phẩm bàn giao:** Luồng POS + lịch sử đơn bán lẻ.
- **DoD:** Chốt một đơn nhiều sản phẩm dưới ~15 giây; mỗi đơn truy ra được "ai bán, bán gì, bao nhiêu".
- **Phụ thuộc:** TD-1.1.

### TD-1.3 — Quản lý kho gắn danh tính người xuất *(GAP H2)*
- **Hành động:** Ghi nhận xuất/nhập kho gắn người thực hiện; tự trừ kho khi bán qua POS; bảng đối soát cuối ngày theo người.
- **Sản phẩm bàn giao:** Module kho + báo cáo đối soát cuối ngày.
- **DoD:** Tồn kho cuối ngày khớp với (tồn đầu − xuất + nhập); xem được "ai đã xuất bao nhiêu".
- **Phụ thuộc:** TD-1.1, TD-1.2.

### TD-1.4 — Báo cáo thu/chi cơ bản cho Nhà sáng lập *(GAP F1a)*
- **Hành động:** Tổng hợp doanh thu, chi phí nhập hàng, lãi gộp theo ngày/tuần/tháng từ dữ liệu POS & kho.
- **Sản phẩm bàn giao:** Trang báo cáo thu/chi cơ bản.
- **DoD:** Số liệu khớp với lịch sử POS/kho; lọc được theo khoảng thời gian.
- **Phụ thuộc:** TD-1.2, TD-1.3.

### TD-1.5 — Cài đặt đo lường hiệu quả vận hành *(GAP D1)*
- **Hành động:** Ghi nhận chỉ số vận hành: thời gian chốt một đơn, thời gian đối soát cuối ngày, số lần thao tác lỗi/hủy.
- **Sản phẩm bàn giao:** Lớp thu thập số liệu + bảng theo dõi cơ bản.
- **DoD:** Có dữ liệu vận hành trong ≥2 tuần đầu để làm baseline cho các đợt sau.
- **Phụ thuộc:** TD-1.2, TD-1.3.

---

## 3. MVP-2 — "SỐ HÓA HỒ SƠ & QUẢN TRỊ"

> Mục tiêu lớp: thay sổ giấy bằng hồ sơ số và hoàn thiện lớp quản trị cho Nhà sáng lập.

### TD-2.1 — Hồ sơ hành trình số hóa *(GAP H3)*
- **Hành động:** Timeline check-in (chỉ số Tanita + ghi chú HLV) + tự động đánh dấu cột mốc lộ trình 30 ngày.
- **DoD:** Mỗi khách có timeline tra cứu được theo thời gian; cột mốc hiển thị tự động; thay thế hoàn toàn nhu cầu ghi sổ giấy.
- **Phụ thuộc:** — (dùng dữ liệu Tanita & lộ trình sẵn có).

### TD-2.2 — Tối ưu luồng tạo lead & khảo sát DISC *(GAP H6, UX)*
- **Hành động:** Rút gọn số bước, gom trường nhập liệu, hỗ trợ điền nhanh; tăng tốc nhập chỉ số Tanita.
- **DoD:** Giảm rõ số thao tác/thời gian hoàn tất một lead so với hiện trạng (đo bằng D1).
- **Phụ thuộc:** —.

### TD-2.3 — Báo cáo lời/lỗ đầy đủ + dự báo *(GAP F1b)*
- **Hành động:** Bổ sung giá vốn (COGS), hoa hồng, chi phí vận hành → lợi nhuận ròng; thêm xu hướng và dự báo doanh thu, cảnh báo bất thường.
- **DoD:** Báo cáo lợi nhuận ròng theo kỳ; có biểu đồ xu hướng + ít nhất một cảnh báo bất thường hoạt động.
- **Phụ thuộc:** TD-1.4.

### TD-2.4 — Chân dung khách hàng *(GAP F2)*
- **Hành động:** Phân nhóm khách theo giá trị/chi tiêu, mức độ gắn bó, kênh/nguồn giới thiệu.
- **DoD:** Lọc/nhóm được khách theo cả ba chiều; mỗi khách quy được về kênh nguồn.
- **Phụ thuộc:** TD-1.2 (dữ liệu chi tiêu).

### TD-2.5 — Tồn kho nâng cao + cảnh báo *(GAP F3)*
- **Hành động:** Tổng hợp tồn kho, ngưỡng cảnh báo sắp hết, gợi ý nhập.
- **DoD:** Cảnh báo kích hoạt đúng khi tồn dưới ngưỡng cấu hình.
- **Phụ thuộc:** TD-1.3.

### TD-2.6 — CRM chăm sóc kết hợp *(GAP F4)*
- **Hành động:** Tự động gửi tin dịp phổ biến (sinh nhật/lễ) theo mẫu + nhắc người phụ trách liên hệ ca cá nhân hóa.
- **DoD:** Tin tự động gửi đúng dịp; danh sách nhắc thủ công sinh đúng đối tượng.
- **Phụ thuộc:** TD-2.4 (chân dung để chọn đối tượng).

### TD-2.7 — Dashboard quản trị đa club *(GAP F5)*
- **Hành động:** Vai trò Nhà sáng lập với dashboard riêng; xem một club hoặc gộp nhiều club.
- **DoD:** Chuyển đổi xem theo từng club và xem gộp; phân quyền tách khỏi giao diện vận hành HLV.
- **Phụ thuộc:** TD-1.4, TD-2.3.

### TD-2.8 — Mở rộng đo lường giữ chân & tăng trưởng *(GAP D2)*
- **Hành động:** Đo tỷ lệ check-in, At-risk, chuyển đổi lead→KH.
- **DoD:** Các chỉ số hiển thị trên dashboard và cập nhật định kỳ.
- **Phụ thuộc:** TD-2.1, TD-2.7.

---

## 4. MVP-3 — "HỆ SINH THÁI KHÁCH HÀNG"

> Mục tiêu lớp: mở app khách hàng và cụm đồng hành từ xa. Đây là khoản đầu tư lớn nhất.

### TD-3.1 — Nền tảng app khách + tài khoản liên kết *(GAP N2, nền tảng)*
- **Hành động:** Xây app/giao diện khách hàng; mô hình tài khoản; onboarding qua lời mời HLV, kích hoạt bằng SĐT; liên kết hồ sơ khách ↔ HLV (nối tiếp khách vãng lai từ POS).
- **DoD:** Khách nhận lời mời, kích hoạt và đăng nhập; hồ sơ khách liên kết đúng HLV/club.
- **Phụ thuộc:** TD-1.2 (hồ sơ khách vãng lai), TD-2.1 (hồ sơ hành trình).

### TD-3.2 — Sổ sức khỏe số (dữ liệu lai) *(GAP K1)*
- **Hành động:** Khách tự log tại nhà (cân nặng, bữa ăn, nước, ngủ, dùng sản phẩm); đồng bộ chỉ số Tanita từ buổi đo tại club; quy tắc hợp nhất tránh xung đột.
- **DoD:** Dữ liệu khách nhập và dữ liệu Tanita hiển thị trên cùng timeline, không trùng/không xung đột.
- **Phụ thuộc:** TD-3.1, TD-2.1.

### TD-3.3 — Nhắc nhở kết hợp HLV ↔ Khách *(GAP H4, K2)*
- **Hành động:** HLV gán khung nhắc theo lộ trình; khách tinh chỉnh giờ; app tự nhắc bữa ăn/nước/sản phẩm.
- **DoD:** Khách nhận nhắc đúng khung; chỉnh giờ được; HLV thấy trạng thái tuân thủ.
- **Phụ thuộc:** TD-3.1, TD-3.2.

### TD-3.4 — Chia sẻ hành trình tự động *(GAP H5, K3)*
- **Hành động:** Tự sinh ảnh/infographic hành trình (đồ thị + insight); khách một chạm chia sẻ MXH.
- **DoD:** Sinh được bản chia sẻ trực quan từ dữ liệu thật; chia sẻ ra MXH thành công.
- **Phụ thuộc:** TD-3.2.

### TD-3.5 — Ba trụ giữ chân *(GAP K4)*
- **Hành động:** Đồ thị tiến bộ giàu cảm xúc; chuỗi ngày/huy hiệu (gamification); kết nối chia sẻ & cộng đồng (tab Cộng đồng).
- **DoD:** Khách thấy đồ thị tiến bộ, nhận huy hiệu/streak, và tham gia cộng đồng trong app.
- **Phụ thuộc:** TD-3.2, TD-3.4.

---

## 5. SƠ ĐỒ THỨ TỰ THỰC HIỆN (TÓM TẮT)

```
MVP-1:  TD-1.1 → TD-1.2 → TD-1.3 → TD-1.4
                         └→ TD-1.5
MVP-2:  TD-2.1 ; TD-2.2 (độc lập)
        TD-1.4 → TD-2.3 → TD-2.7
        TD-1.2 → TD-2.4 → TD-2.6
        TD-1.3 → TD-2.5
        TD-2.1 + TD-2.7 → TD-2.8
MVP-3:  TD-3.1 → TD-3.2 → {TD-3.3, TD-3.4} → TD-3.5
```

---

## 6. KHUYẾN NGHỊ TRIỂN KHAI

1. **Khởi động bằng nền tảng N1 (TD-1.1):** không có catalog mã vạch thì cả MVP-1 đứng yên — đây là việc đầu tiên cần làm.
2. **Cài đo lường (TD-1.5) ngay từ đầu:** vì hiện trạng không có baseline, đây là cách duy nhất để chứng minh hiệu quả các đợt sau.
3. **Quyết định nguồn lực cho MVP-3 sớm:** app khách (TD-3.1) là khoản đầu tư lớn nhất; nên thực hiện nghiên cứu khả thi/ước lượng chi phí riêng trước khi cam kết lớp này.
4. **Chuẩn hóa quy tắc đồng bộ dữ liệu Tanita lai (TD-3.2):** thống nhất nguồn ưu tiên (club vs khách tự nhập) để tránh xung đột.
5. **Rà soát lại ước lượng công sức** khi có baseline thực tế từ MVP-1.

---

## 7. KẾT THÚC QUY TRÌNH

Tài liệu này khép lại chuỗi As-Is → To-be → GAP → To-do. Các đầu vào tiếp theo có thể cân nhắc: nghiên cứu khả thi kỹ thuật & ước lượng chi phí (đặc biệt cho MVP-3), thiết kế chi tiết UX/UI từng màn hình, và kế hoạch đo lường (baseline) trước khi bước vào phát triển.
