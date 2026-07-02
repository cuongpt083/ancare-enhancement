# GAP Analysis — E06 Personal Health (Khách hàng)

> **As-Is:** `docs/99-archive/as-is/screenshots-kh/` (9 màn) + `ui_ux_analysis_kh.md` (archive). Lưu ý: bản cũ có thể lỗi thời — chờ PO nộp As-Is hiện tại vào `docs/00-foundation/as-is-current/screenshots-kh/`.
> **To-Be:** `docs/03-mockups/draft-requirements-kh.md` + mockup `docs/03-mockups/customer/S-HLTH-*.html` (7 màn).
> **Phương pháp:** As-Is → To-Be → Hành động (KẾ THỪA/SỬA/THÊM/XÓA).

## 1. So sánh luồng tổng thể

### As-Is (app KH hiện tại — archive 9 màn)
```
Welcome → Login → Dashboard (chỉ số cơ thể + giấc ngủ + ảnh vóc dáng + "Hôm nay nổi bật")
→ Chi tiết chỉ số → Nhật ký giấc ngủ → Thêm ảnh vóc dáng → Lộ trình → Chat → Hồ sơ
```
> Đặc điểm: 4 tab (Trang chủ/?. /Chat/Hồ sơ); chỉ số dạng số liệu khô khan; nhiệm vụ dạng nút thô sơ; **Trang chủ ≈ Hồ sơ** (trùng lặp nghiêm trọng); lộ trình dạng text; thiếu gamification, check-in sinh động, line-chart, Infographic.

### To-Be (draft-kh + mockup)
```
Trang chủ (avatar+chào+chuông+gói, check-in → màn Check-in, đồng hồ sinh học, line-chart, bảng 8 chỉ số)
→ Check-in (4 card: chỉ số/thực đơn+AI/hoạt động/kiến thức) → Báo cáo (3 tab + Infographic) → Đào tạo (bài học nhóm)
```
> Đặc điểm: 4 tab (Trang chủ/Báo cáo/Đào tạo/Hồ sơ); check-in tổng hợp 4 card; AI bóc tách món; line-chart tiến trình; bảng chỉ số có màu + mũi tên; Infographic dọc chia sẻ MXH; gamification điểm.

### Chênh lệch lớn
- As-Is **không có** màn Check-in tổng hợp, Báo cáo (3 tab), Đào tạo, Infographic.
- As-Is **Trang chủ ≈ Hồ sơ** (trùng) → To-Be tách rõ: Trang chủ = tổng quan + check-in; Hồ sơ = tài khoản/cài đặt.
- As-Is chỉ số khô khan → To-Be bảng có màu + mũi tên + line-chart.

---

## 2. GAP từng màn

### 2.1 Trang chủ KH — To-Be S-HLTH-02 ↔ As-Is Màn 03 (dashboard)
- **As-Is:** thẻ chỉ số cơ thể (16/06) nhồi nhét số liệu viết tắt (C.Nặng 60.0, Mỡ% 14.0...); thẻ giấc ngủ, thêm ảnh; "Hôm nay nổi bật" text thô; icon ký tự đặc biệt.
- **To-Be:** header (avatar+chào+chuông+gói+RFM) · check-in row (→ màn Check-in) · đồng hồ sinh học · line-chart · bảng 8 chỉ số (mục tiêu/đầu/gần nhất/thay đổi + mũi tên xanh/đỏ).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Header avatar+chào+chuông | không rõ | có | THÊM | cá nhân hóa |
| 2 | Gói giải pháp + RFM status | không | có (tên gói + trạng thái RFM + thời gian còn lại) | THÊM | Q31 |
| 3 | Check-in row (→ màn Check-in) | nút thô sơ | row nút + link mở màn Check-in | SỬA+THÊM | |
| 4 | Đồng hồ sinh học 24h | không | widget 24h chấm điểm | THÊM | D28 |
| 5 | Line-chart tiến trình | không | biểu đồ xu hướng 10 ngày | THÊM | |
| 6 | Bảng chỉ số 8 dòng | thẻ nhồi số liệu khô | bảng 5 cột + màu xanh/đỏ + mũi tên | SỬA | enrich lớn |
| 7 | Thẻ giấc ngủ/ảnh vóc dáng | có (riêng) | (chuyển vào Check-in Card 3 / Báo cáo) | DI CHUYỂN | |
| 8 | "Hôm nay nổi bật" | text thô | (chuyển vào Báo cáo tổng kết ngày) | DI CHUYỂN | |

**Tóm tắt:** KẾ THỪA dữ liệu chỉ số · SỬA bảng chỉ số (màu+mũi tên) · THÊM header, check-in row, đồng hồ, line-chart · DI CHUYỂN giấc ngủ/ảnh/"nổi bật" sang Check-in/Báo cáo.

---

### 2.2 Check-in hôm nay — To-Be S-HLTH-06 ↔ As-Is: KHÔNG có màn tổng hợp
- **As-Is:** không có màn Check-in tổng hợp (nhiệm vụ rải ở dashboard: giấc ngủ riêng, ảnh riêng, chỉ số riêng).
- **To-Be:** màn Check-in 4 card (chỉ số/thực đơn+AI/hoạt động/kiến thức).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Card 1 Chỉ số cơ thể (bảng 3 cột + nhập lại) | thẻ riêng ở dashboard | card trong Check-in + nút nhập lại ghi đè | SỬA+THÊM | gom |
| 2 | Card 2 Thực đơn hôm nay (số bữa + AI chụp ảnh) | không | có | THÊM | PoC AI |
| 3 | Card 3 Uống nước/Giấc ngủ/Thể thao | giấc ngủ riêng, nước không | gom 1 card + +/- cốc + tự tính giờ + tìm hoạt động | THÊM | |
| 4 | Card 5 Kiến thức (video + 3 câu) | không | có | THÊM | E05 |

**Tóm tắt:** **gần như toàn bộ THÊM** (As-Is không có màn tổng hợp). KẾ THỪA duy nhất: dữ liệu chỉ số + ý tưởng giấc ngủ (gom vào Check-in).

---

### 2.3 Báo cáo — To-Be S-HLTH-07 ↔ As-Is Màn 07 (lộ trình) + "Hôm nay nổi bật"
- **As-Is:** lộ trình dạng text tuần tự; "Hôm nay nổi bật" text thô (Điểm tốt/Cần cải thiện); không có phân tích chuyên sâu, Infographic.
- **To-Be:** 3 tab (Tổng kết ngày 21h / Tiến trình gói / Đề xuất) + phân tích chuyên sâu + lý do + lời khuyên + nâng cấp gói + nút Infographic dọc.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tab Tổng kết ngày (21h) | "Hôm nay nổi bật" text | phân tích chuyên sâu + lý do + lời khuyên + nâng cấp gói | SỬA+THÊM | enrich |
| 2 | Tab Tiến trình gói | lộ trình text | bảng tiến trình (chỉ số/mục tiêu/đầu/gần nhất/thay đổi) | SỬA | |
| 3 | Tab Đề xuất (SP/gói) | không | có | THÊM | |
| 4 | Nút tạo Infographic dọc | không | có (chia sẻ Zalo/FB) | THÊM | PoC |
| 5 | Lộ trình timeline gamified | text thô | (cải tiến thành journey map — Gợi ý archive) | SỬA | |

**Tóm tắt:** KẾ THỪA dữ liệu tiến trình · SỬA "Hôm nay nổi bật"→Tổng kết ngày, lộ trình→timeline · THÊM tab Đề xuất, Infographic.

---

### 2.4 Đào tạo — To-Be S-DEV-02 ↔ As-Is: KHÔNG có
- **As-Is:** không có màn Đào tạo KH.
- **To-Be:** danh sách bài học theo nhóm + 3 câu hỏi trước/sau.

**Tóm tắt:** **toàn bộ THÊM**.

---

### 2.5 Chat — To-Be S-HLTH-05 ↔ As-Is Màn 08 (chat)
- **As-Is:** chat 1-1 HLV + phòng Cộng đồng; avatar nhỏ, giãn cách chưa tối ưu; tab /qna nhãn "Chat".
- **To-Be:** chat HLV + AI companion proactively gợi ý nhẹ (D29) + nhãn AI minh bạch.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Chat 1-1 HLV | có | có | KẾ THỪA | |
| 2 | Chat cộng đồng | có | (giữ, enrich) | KẾ THỪA | |
| 3 | AI companion (proactively gợi ý nhẹ) | không | có + nhãn AI | THÊM | D29 |
| 4 | Avatar/giãn cách | nhỏ, chưa tối ưu | cải thiện | SỬA | |

**Tóm tắt:** KẾ THỪA chat 1-1 + cộng đồng · THÊM AI companion · SỬA visual.

---

### 2.6 Đồng hồ sinh học — To-Be S-HLTH-01 ↔ As-Is: KHÔNG có
- **As-Is:** không có widget đồng hồ sinh học 24h.
- **To-Be:** vòng tròn 24h + chấm điểm 3/2/1/0 + tô màu trạng thái.

**Tóm tắt:** **toàn bộ THÊM** (D27 điểm, D28 tô màu).

---

### 2.7 Hồ sơ — As-Is Màn 09 (trùng dashboard)
- **As-Is:** Hồ sơ ≈ Trang chủ (lặp thẻ chỉ số/giấc ngủ/ảnh) — trùng lặp nghiêm trọng.
- **To-Be:** Hồ sơ = tài khoản/cài đặt/gói dịch vụ/liên kết HLV (tách khỏi trang chủ).

**Tóm tắt:** SỬA lớn — tách Hồ sơ khỏi Trang chủ, tập trung tài khoản/cài đặt. (Chưa có mockup riêng — TODO khi PO nộp As-Is hiện tại.)

---

## 3. Tổng hợp GAP (E06)

### KẾ THỪA
- Dữ liệu chỉ số cơ thể (Tanita).
- Chat 1-1 HLV + cộng đồng.
- Ý tưởng giấc ngủ / ảnh vóc dáng (gom vào Check-in/Báo cáo).
- Dữ liệu tiến trình lộ trình.

### SỬA
- Bảng chỉ số: khô khan → màu + mũi tên + line-chart.
- "Hôm nay nổi bật" → Tổng kết ngày (phân tích chuyên sâu).
- Lộ trình text → timeline gamified.
- Hồ sơ: tách khỏi Trang chủ.
- Chat: avatar/giãn cách.

### THÊM (lớn)
- Màn Check-in tổng hợp (4 card) — gần như toàn bộ.
- Đồng hồ sinh học 24h + chấm điểm.
- AI bóc tách món ăn (Card 2 Check-in) — PoC.
- AI companion chat (proactively).
- Màn Báo cáo (3 tab + phân tích + Infographic dọc).
- Màn Đào tạo (bài học nhóm + 3 câu hỏi).
- Header avatar/chào/chuông/gói/RFM.
- Line-chart tiến trình.

### XÓA
- Trùng lặp Trang chủ ≈ Hồ sơ (giữ Hồ sơ = tài khoản).

### PoC kỹ thuật
- AI bóc tách món ăn (Card 2 Check-in).
- Sinh Infographic dọc.

---

## 4. Reconciliation — lệch draft-kh vs E06 stories/mockups

| # | Lệch | Hiện tại | Draft To-Be | Hành động |
|---|---|---|---|---|
| R1 | Số card Check-in | draft liệt kê Card 1,2,3,5 (thiếu Card 4?) | draft ghi Card 1/2/3/5 | ⏳ PO xác nhận: có Card 4 không? (có thể draft bỏ số 4) |
| R2 | Báo cáo KH | US-E06-07 "kết quả cân quét & báo cáo hành trình" | draft: 3 tab + Infographic | ✅ đã enrich S-HLTH-07 |
| R3 | Đào tạo KH | US-E05-01 micro-course (chung HLV+KH) | draft: màn Đào tạo KH riêng | ✅ đã tạo S-DEV-02 (E05-KH) |
| R4 | Infographic | US-E06-08 (Could) | draft: nút trong Báo cáo | ✅ đã đưa nút vào S-HLTH-07 |
| R5 | Hồ sơ KH | chưa có mockup | draft: không mô tả chi tiết | ⏳ TODO mockup khi PO nộp As-Is |
| R6 | Ảnh vóc dáng (trước/sau) | As-Is Màn 06 | draft không nhắc | ⏳ PO xác nhận: giữ/ bỏ/ chuyển? |

> **Cần PO chốt:** R1 (Card 4?), R5 (Hồ sơ), R6 (ảnh vóc dáng).
