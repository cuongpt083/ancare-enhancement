# GAP Analysis — E06 Personal Health (Khách hàng)

> **As-Is:** `docs/00-foundation/as-is-current/as-is-notes.md` §3-4 (10 màn KH từ video `screen-record-KH.mp4`) + `screenshots-kh/` (10 ảnh: dashboard, dashboard scroll, ghi nhận bữa ăn, check-in, check-in scroll, upload empty, upload error, chi tiết bữa ăn AI, modal thêm món, bữa ăn xác nhận).
> **To-Be:** `docs/03-mockups/draft-requirements-kh.md` + mockup `docs/03-mockups/customer/S-HLTH-*.html` (7 màn).
> **Phương pháp:** As-Is → To-Be → Hành động (KẾ THỪA/SỬA/THÊM/XÓA).

## 1. So sánh luồng tổng thể

### As-Is (app KH hiện tại — 10 màn từ video mới)
```
Trang chủ (chào+VIP+hạn gói, check-in 1/5 mục, tiến trình trống, mục tiêu Ngày 1/11, calo 1988)
→ cuộn: bảng chỉ số cơ thể (8 chỉ số) + thực đơn (đạm/rau/tinh bột + calo từng món + check + camera)
→ [Thẻ Check-in] Chi tiết check-in (chỉ số + thực đơn + "chạm để cân lại" + thêm ảnh)
→ [Camera bữa] Upload empty → [chụp] Ghi nhận bữa ăn thành công (tick xanh + thumbnail)
  → [lỗi] Upload error & retry
→ [bữa có ảnh] Chi tiết bữa ăn + nút "Phỏng đoán món ăn"
  → [Phỏng đoán] Modal thêm món (tên/định lượng/đơn vị/calo/đạm) → Lưu
  → Bữa ăn đã xác nhận (tổng tạm tính kcal + đạm)
```
> Đặc điểm As-Is mới (quan trọng — khác archive cũ):
- **Đã có check-in hằng ngày** (chỉ số + thực đơn + nước +/- ly) — không phải THÊM từ đầu.
- **Đã có AI phỏng đoán món ăn** (upload ảnh → modal thêm món → xác nhận) — không phải THÊM từ đầu.
- **Đã có bảng chỉ số cơ thể** (8 chỉ số) + thực đơn chi tiết (đạm/rau/tinh bột + calo).
- **Đã có upload ảnh bữa ăn** + xử lý lỗi/retry.
- **4 tab**: Trang chủ / Chat / Lịch sử / Hồ sơ.
- **Hạn chế**: tiến trình trống (chưa có line-chart), mục tiêu trống (chờ HLV), nước 21 ly (không quy đổi ml/l), chỉ số dạng ô thẻ nhỏ (chưa có bảng 5 cột + màu + mũi tên), chưa có đồng hồ sinh học 24h, chưa có Báo cáo (3 tab + Infographic), chưa có Đào tạo, chưa có AI companion chat.

### To-Be (draft-kh + mockup)
```
Trang chủ (avatar+chào+chuông+gói+RFM, check-in row→màn Check-in, đồng hồ sinh học, line-chart, bảng 8 chỉ số 5 cột+mũi tên)
→ Check-in (4 card: chỉ số/thực đơn+AI/hoạt động/kiến thức)
→ Báo cáo (3 tab + Infographic dọc) → Đào tạo (bài học nhóm + 3 câu hỏi)
```

### Chênh lệch (nhỏ hơn archive cũ — As-Is mới đã có nhiều thứ)
- As-Is mới **đã có**: check-in, AI phỏng đoán món, upload ảnh, bảng chỉ số, thực đơn, nước +/-.
- As-Is mới **thiếu**: đồng hồ sinh học 24h, line-chart, bảng 5 cột+mũi tên, Báo cáo (3 tab + Infographic), Đào tạo, AI companion chat, header avatar/RFM, Card kiến thức (video + 3 câu), Card hoạt động (giấc ngủ + thể thao tìm).
- **Kế thừa cao hơn** archive cũ → GAP nhỏ hơn, ít THÊM hơn.

---

## 2. GAP từng màn

### 2.1 Trang chủ KH — To-Be S-HLTH-02 ↔ As-Is Màn 01+02 (dashboard + scroll)
- **As-Is:** chào "Mipt01" + VIP + hạn gói HH 02/10/2026 · thẻ Check-in 1/5 mục (Nước/Bữa/Ngủ/Cân) · tiến trình trống · mục tiêu Ngày 1/11 + calo 1988 · cuộn: bảng chỉ số 8 (Cân/Chiều cao/BMI/Mỡ/Cơ/Nước/Xương/MỡNT/TuổiTĐC/BMR) + thực đơn (đạm/rau/tinh bột + calo + check + camera).
- **To-Be:** header (avatar+chào+chuông+gói+RFM) · check-in row (→ màn Check-in) · đồng hồ sinh học · line-chart · bảng 8 chỉ số (5 cột + mũi tên).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Header avatar + chào + hạn gói | có (VIP + HH 02/10/2026) | có + chuông + RFM status | SỬA+THÊM | thêm chuông, RFM |
| 2 | Thẻ Check-in (1/5 mục) | có (tiến độ 5 chấm) | check-in row → mở màn Check-in | SỬA | đổi dạng |
| 3 | Tiến trình | trống (chờ HLV xuất báo cáo) | line-chart xu hướng 10 ngày | SỬA | tự động thay chờ HLV |
| 4 | Mục tiêu (Ngày 1/11 + calo) | có | (giữ, enrich) | KẾ THỪA | |
| 5 | Bảng chỉ số 8 | ô thẻ nhỏ (Cân/Chiều cao/BMI/Mỡ/Cơ/Nước/Xương/MỡNT/TuổiTĐC/BMR) | bảng 5 cột (Tên/Mục tiêu/Đầu/Gần nhất/Thay đổi) + màu xanh/đỏ + mũi tên | SỬA | enrich lớn |
| 6 | Thực đơn chi tiết | có (đạm/rau/tinh bột + calo + check + camera) | (chuyển vào màn Check-in Card 2) | DI CHUYỂN | |
| 7 | Đồng hồ sinh học 24h | không | widget 24h chấm điểm | THÊM | D28 |
| 8 | Đánh giá 3 trụ cột Thân-Tâm-Trí | không | có | THÊM | |
| 9 | Bottom nav | 4 tab (Trang chủ/Chat/Lịch sử/Hồ sơ) | 4 tab (Trang chủ/Báo cáo/Đào tạo/Hồ sơ) | SỬA | đổi tab |

**Tóm tắt:** KẾ THỪA (chào+VIP+hạn gói, mục tiêu+calo, dữ liệu chỉ số, thực đơn) · SỬA (header +chuông+RFM, check-in→row, tiến trình→line-chart, bảng chỉ số→5 cột+mũi tên, bottom nav) · THÊM (đồng hồ sinh học, 3 trụ cột) · DI CHUYỂN (thực đơn → màn Check-in).

---

### 2.2 Check-in hôm nay — To-Be S-HLTH-06 ↔ As-Is Màn 04+05 (check-in details + scroll)
- **As-Is:** bảng chỉ số (Cân 80/Chiều cao --/BMI --/Mỡ 38/Cơ 28/Nước 55/Xương 2.7/MỡNT 4/TuổiTĐC 25/BMR 1400) + "chạm để cân lại" + thực đơn (đã log có tick xanh + thumbnail + thêm ảnh) + phỏng đoán bữa ăn (đã xác nhận) + nước 0/21 ly (+/-).
- **To-Be:** 4 card (chỉ số/thực đơn+AI/hoạt động/kiến thức).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Card 1 Chỉ số cơ thể | có (ô thẻ nhỏ) + "chạm để cân lại" | bảng 3 cột + nút nhập lại ghi đè | SỬA | gom + đổi dạng |
| 2 | Card 2 Thực đơn + AI phỏng đoán | có (thực đơn + camera + AI phỏng đoán + modal thêm món + xác nhận) | gom 1 card + cấu trúc Calo/gam Đạm-Tinh bột-Chất béo + check xanh | KẾ THỪA+SỬA | đã có AI! |
| 3 | Upload ảnh + xử lý lỗi | có (Màn 06/07/03) | (giữ, trong Card 2) | KẾ THỪA | |
| 4 | Modal thêm món (tên/định lượng/đơn vị/calo/đạm) | có (Màn 09) | (giữ) | KẾ THỪA | |
| 5 | Bữa ăn xác nhận (tổng tạm tính) | có (Màn 10) | (giữ) | KẾ THỪA | |
| 6 | Nước +/- ly | có (0/21 ly) | +/- cốc 200ml + quy đổi ml/l | SỬA | quy đổi |
| 7 | Giấc ngủ (nhập giờ ngủ/thức) | không | có (tự tính giờ) | THÊM | |
| 8 | Thể thao (tìm + chọn + phút + calo) | không | có | THÊM | |
| 9 | Card kiến thức (video + 3 câu) | không | có | THÊM | E05 |
| 10 | SP hỗ trợ (số viên/ml) | không rõ | có (nếu KH dùng SP) | THÊM | Q31b |

**Tóm tắt:** KẾ THỪA NHIỀU (bảng chỉ số, thực đơn, AI phỏng đoán món, upload+error, modal thêm món, xác nhận, nước +/-) · SỬA (chỉ số→bảng 3 cột, nước→quy đổi ml/l) · THÊM (giấc ngủ, thể thao, Card kiến thức, SP hỗ trợ).

---

### 2.3 Báo cáo — To-Be S-HLTH-07 ↔ As-Is: KHÔNG có (tiến trình trống)
- **As-Is:** tiến trình trống ("Chưa có báo cáo tiến trình. HLV sẽ xuất báo cáo đánh giá tiến độ cho bạn theo định kỳ.").
- **To-Be:** 3 tab (Tổng kết ngày 21h / Tiến trình gói / Đề xuất) + phân tích chuyên sâu + lý do + lời khuyên + nâng cấp gói + Infographic dọc.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tab Tổng kết ngày 21h | không (tiến trình trống) | phân tích chuyên sâu + lý do + lời khuyên + nâng cấp gói | THÊM | |
| 2 | Tab Tiến trình gói | trống (chờ HLV xuất) | bảng tiến trình (chỉ số/mục tiêu/đầu/gần nhất/thay đổi) — tự động | THÊM | tự động thay chờ HLV |
| 3 | Tab Đề xuất (SP/gói) | không | có | THÊM | |
| 4 | Nút tạo Infographic dọc | không | có (chia sẻ Zalo/FB) | THÊM | PoC |

**Tóm tắt:** **gần như toàn bộ THÊM** (As-Is chỉ có placeholder trống). Lợi ích: thay "chờ HLV xuất báo cáo" → tự động + Infographic.

---

### 2.4 Đào tạo — To-Be S-DEV-02 ↔ As-Is: KHÔNG có
- **As-Is:** không có màn Đào tạo KH.
- **To-Be:** danh sách bài học theo nhóm + 3 câu hỏi trước/sau.

**Tóm tắt:** **toàn bộ THÊM**.

---

### 2.5 Chat — To-Be S-HLTH-05 ↔ As-Is: có nút "Nhắn HLV"
- **As-Is:** nút "Nhắn HLV" trong mục Tiến trình (trang chủ) → chat 1-1 HLV.
- **To-Be:** chat HLV + AI companion proactively gợi ý nhẹ (D29) + nhãn AI minh bạch.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Chat 1-1 HLV | có (nút Nhắn HLV) | có | KẾ THỪA | |
| 2 | AI companion (proactively gợi ý nhẹ) | không | có + nhãn AI | THÊM | D29 |

**Tóm tắt:** KẾ THỪA chat 1-1 · THÊM AI companion.

---

### 2.6 Đồng hồ sinh học — To-Be S-HLTH-01 ↔ As-Is: KHÔNG có
- **As-Is:** không có widget đồng hồ sinh học 24h (chỉ có check-in 5 chấm tròn).
- **To-Be:** vòng tròn 24h + chấm điểm 3/2/1/0 + tô màu trạng thái.

**Tóm tắt:** **toàn bộ THÊM** (D27 điểm, D28 tô màu). As-Is có check-in 5 chấm nhưng không phải đồng hồ 24h.

---

### 2.7 Hồ sơ — As-Is: tab Hồ sơ (chưa chi tiết trong video)
- **As-Is:** có tab Hồ sơ nhưng video không đi sâu.
- **To-Be:** Hồ sơ = tài khoản/cài đặt/gói dịch vụ/liên kết HLV.

**Tóm tắt:** KẾ THỪA (có tab) · SỬA (tập trung tài khoản, không lặp trang chủ). (Chưa có mockup — TODO.)

---

### 2.8 Upload ảnh + AI phỏng đoán (As-Is Màn 06/07/08/09/10) — KẾ THỪA TOÀN BỘ
- **As-Is:** upload empty (Màn 06) → upload error + retry (Màn 07) → ghi nhận thành công (Màn 03) → chi tiết bữa ăn + "Phỏng đoán món ăn" (Màn 08) → modal thêm món (Màn 09) → bữa ăn xác nhận (Màn 10).
- **To-Be:** gom vào Card 2 Check-in.

**Tóm tắt:** KẾ THỪA TOÀN BỘ luồng upload + AI phỏng đoán (đã có sẵn, hoạt động tốt). Chỉ enrich: thêm cấu trúc Calo/gam 3 nhóm + SP hỗ trợ.

---

## 3. Tổng hợp GAP (E06) — cập nhật theo As-Is mới

### KẾ THỪA (nhiều hơn archive cũ)
- Header: chào + VIP + hạn gói.
- Mục tiêu + calo/ngày.
- Bảng chỉ số cơ thể (8-10 chỉ số: Cân/Chiều cao/BMI/Mỡ/Cơ/Nước/Xương/MỡNT/TuổiTĐC/BMR).
- **Check-in hằng ngày** (chỉ số + thực đơn + nước +/- ly + "chạm để cân lại").
- **Thực đơn chi tiết** (đạm/rau/tinh bột + calo từng món + check xanh + camera).
- **AI phỏng đoán món ăn** (upload ảnh → modal thêm món: tên/định lượng/đơn vị/calo/đạm → xác nhận + tổng tạm tính).
- **Upload ảnh bữa ăn** + xử lý lỗi/retry.
- Chat 1-1 HLV (nút Nhắn HLV).
- 4 tab bottom nav (cấu trúc).

### SỬA
- Header: + chuông thông báo + RFM status.
- Check-in: 5 chấm → row nút → mở màn Check-in riêng.
- Tiến trình: trống (chờ HLV) → line-chart tự động.
- Bảng chỉ số: ô thẻ nhỏ → bảng 5 cột + màu xanh/đỏ + mũi tên.
- Nước: 21 ly → +/- cốc 200ml + quy đổi ml/l.
- Bottom nav: 4 tab (Trang chủ/Chat/Lịch sử/Hồ sơ) → (Trang chủ/Báo cáo/Đào tạo/Hồ sơ).
- Hồ sơ: tập trung tài khoản (không lặp trang chủ).

### THÊM (nhỏ hơn archive cũ)
- Đồng hồ sinh học 24h + chấm điểm 3/2/1/0.
- Đánh giá 3 trụ cột Thân-Tâm-Trí.
- Màn Báo cáo (3 tab + phân tích chuyên sâu + Infographic dọc).
- Màn Đào tạo (bài học nhóm + 3 câu hỏi).
- AI companion chat (proactively gợi ý nhẹ + nhãn AI).
- Card hoạt động: Giấc ngủ (nhập giờ + tự tính) + Thể thao (tìm + chọn + phút + calo).
- Card kiến thức (video + 3 câu khảo sát sau học).
- SP hỗ trợ (số viên/ml — Q31b).

### XÓA
- (không có XÓA lớn — As-Is mới khá khớp To-Be)

### PoC kỹ thuật
- Sinh Infographic dọc (Báo cáo).
- (AI bóc tách món đã có As-Is → không cần PoC mới!)

---

## 4. Reconciliation — lệch draft-kh vs E06 stories/mockups

| # | Lệch | Hiện tại | Draft To-Be | As-Is mới | Hành động |
|---|---|---|---|---|---|
| R1 | Số card Check-in | draft: Card 1/2/3/5 | 4 card | As-Is đã có Card 1 (chỉ số) + Card 2 (thực đơn+AI) + nước (Card 3 phần) | ✅ Giữ 4 card (1/2/3/5); draft bỏ số 4 = OK. THÊM giấc ngủ + thể thao (Card 3) + kiến thức (Card 5). |
| R2 | Báo cáo KH | US-E06-07 | 3 tab + Infographic | As-Is trống (chờ HLV) | ✅ đã enrich S-HLTH-07 |
| R3 | Đào tạo KH | US-E05-01 chung | màn riêng | As-Is không có | ✅ đã tạo S-DEV-02 |
| R4 | Infographic | US-E06-08 Could | nút trong Báo cáo | As-Is không có | ✅ đã đưa nút vào S-HLTH-07 |
| R5 | Hồ sơ KH | chưa mockup | draft không chi tiết | As-Is có tab nhưng video không sâu | ⏳ TODO mockup khi cần |
| R6 | Ảnh vóc dáng (trước/sau) | archive Màn 06 | draft không nhắc | As-Is mới không có (video tập check-in) | ⏳ PO xác nhận: giữ/bỏ? |
| R7 | AI phỏng đoán món | US-E06-04 (THÊM) | draft Card 2 | **As-Is ĐÃ CÓ** (Màn 08/09/10) | ✅ Đổi US-E06-04 từ THÊM → KẾ THỪA (đã có)! |
| R8 | Nước 21 ly | — | +/- cốc 200ml | As-Is 0/21 ly | ✅ SỬA: quy đổi ml/l (21 ly × 200ml = 4.2L) |
| R9 | Tiến trình "chờ HLV" | — | line-chart tự động | As-Is trống chờ HLV | ✅ SỬA: tự động line-chart |
| R10 | Bottom nav | mockup 4 tab khác | draft 4 tab | As-Is 4 tab (Trang chủ/Chat/Lịch sử/Hồ sơ) | ✅ SỬA: Trang chủ/Báo cáo/Đào tạo/Hồ sơ |

> **Insight quan trọng:** As-Is KH mới **đã có check-in + AI phỏng đoán món + upload ảnh** → GAP E06 nhỏ hơn dự kiến. Phần THÊM lớn nhất giờ là: đồng hồ sinh học 24h, Báo cáo (3 tab + Infographic), Đào tạo, AI companion. US-E06-04 (bữa ăn + AI) chuyển từ THÊM → KẾ THỪA.
