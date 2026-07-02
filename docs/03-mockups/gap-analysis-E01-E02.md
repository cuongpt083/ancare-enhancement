# GAP Analysis — E01 Quản lý KH + E02 Tư vấn 15 phút (HLV)

> **As-Is:** `docs/00-foundation/as-is-current/as-is-notes.md` + screenshots-hlv (8 màn từ video: đăng nhập, dashboard, team, wizard 4 bước, chi tiết KH).
> **To-Be:** `docs/03-mockups/draft-requirements-hlv.md` (PO mô tả chi tiết wireframe mong muốn cho trang chủ + luồng Team).
> **Phương pháp:** mỗi To-Be màn → map As-Is tương đương → bảng GAP (KẾ THỪA / SỬA / THÊM / XÓA) → tóm tắt GAP. Nguyên tắc: **tối đa kế thừa** logic/data đã ổn.

---

## 1. So sánh luồng tổng thể

### As-Is (luồng hiện tại — video)
```
Đăng nhập → Dashboard → [Tab Team] DS KH (1 list) → [FAB +] Wizard Đăng ký lộ trình:
  B1 Chọn gói + ngày → B2 Khảo sát số liệu (gt/ns/cao/nặng/mục tiêu/hoạt động→RMR+calo auto)
  → B3 Thực đơn auto + ảnh đại diện → B4 Tài khoản (họ tên/email/MK) → Chi tiết KH
```
> Đặc điểm: tạo **KH đã mua gói** ngay; KHÔNG có khái niệm KH tiềm năng; KHÔNG có đo Tanita trong luồng; KHÔNG có bản phân tích/tư vấn; chọn gói ở đầu; thực đơn auto đơn giản.

### To-Be (luồng mong muốn — draft-requirements)
```
Đăng nhập → Dashboard (KPI/Action center/Task + FAB radial) → [Tab Team] DS KH tiềm năng (default) | KH của tôi (Summary RFM + Danh sách) → [Thêm mới KH]
  Card Thông tin cơ bản (mời+KH) + Card Chân dung KH (10 câu hỏi) → Khảo sát Tanita (OCR/nhập tay 9 chỉ số)
  → Phân tích kết quả (bảng 9 dòng + drop-down + tick mục tiêu → tên chương trình) → Xem lộ trình (lợi ích/kết quả/1-3-trọn đời/gói SP/cam kết)
  → [Pop-up Tạo TK KH] → Xây dựng bữa ăn (mục tiêu calo/bữa +/- + cấu trúc 30/40/30 + 4 bữa chi tiết + nước + thời gian sinh hoạt) → DS KH
```
> Đặc điểm: tách **KH tiềm năng** vs **KH của tôi**; đo Tanita + phân tích/chương trình theo mục tiêu trong luồng; RFM status; attribution người mời; bữa ăn chi tiết 30/40/30; tạo TK ở cuối (sau chốt).

### Chênh lệch cấu trúc lớn
- As-Is = wizard **4 bước tuyến tính** tạo KH-mua-gói. To-Be = luồng **tư vấn 15 phút** (KH tiềm năng → khảo sát → Tanita → phân tích → chốt lộ trình → tạo TK → bữa ăn).
- As-Is chọn gói **đầu luồng**; To-Be chọn chương trình **sau phân tích** (theo mục tiêu) → đúng nghiệp vụ tư vấn.
- As-Is **không có** 4 màn then chốt của To-Be: Chân dung KH, Khảo sát Tanita, Phân tích kết quả, Xem lộ trình. Đây là phần **THÊM lớn nhất**.

---

## 2. GAP từng màn

### 2.1 Trang chủ (Dashboard) — To-Be §1 ↔ As-Is Màn 02
- **As-Is:** KPI 1 dòng (“0 KH — NPP 0đ Doanh thu”); to-do list; bottom nav 5 tab (Trang Chủ/Team/Chat/HLV/Hồ sơ, icon ký tự lỗi font).
- **To-Be:** Dashboard 3 phần (KPI · Action center · Task list); menu 4 tab (Trang chủ/Team/Chat/Hồ sơ); FAB radial menu tùy biến.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Lời chào HLV | không rõ | có (cá nhân hóa) | THÊM | L2 |
| 2 | KPI (KH/NPP/Doanh thu) | 1 dòng dày đặc | tách rõ 3 phần KPI | SỬA | giảm nhiễu |
| 3 | Action center | chưa có | 1 vùng hành động nổi bật hôm nay | THÊM | thành phần mới |
| 4 | Task list (to-do) | có | giữ | KẾ THỪA | data/logic |
| 5 | Bottom nav | 5 tab, icon lỗi font | 4 tab (bỏ tab HLV), icon Tabler | SỬA | gộp HLV vào Team? |
| 6 | FAB radial menu | chưa có (FAB chỉ ở Team) | FAB trên trang chủ, radial tùy biến | THÊM | D01/D10 |

**Tóm tắt:** KẾ THỪA task list + KPI data · SỬA KPI (tách), bottom nav (icon/4 tab) · THÊM action center, FAB radial, lời chào.

---

### 2.2 Tab Team — DS KH tiềm năng + KH của tôi — To-Be §2.1–2.3 ↔ As-Is Màn 03
- **As-Is:** 1 danh sách KH (toàn KH đã có gói); search; thẻ: avatar/tên/gói/tiến độ ngày; FAB +.
- **To-Be:** tabs “KH tiềm năng” (default) / “KH của tôi”; KH của tôi = 2 card (Summary RFM + Danh sách).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tabs KH tiềm năng / KH của tôi | 1 list chung | 2 tabs, default KH tiềm năng | THÊM | khái niệm KHTN mới |
| 2 | Thanh search | có | giữ | KẾ THỪA | |
| 3 | Card Summary (RFM) | chưa có | filter Tên + trạng thái RFM; thống kê số lượng + màu (xanh/vàng/đỏ) | THÊM | RFM = Recency/Frequency/Monetary — business-rule mới |
| 4 | Trạng thái KH RFM (tích cực/có nguy cơ/kém quan tâm) | chưa có | 3 trạng thái + màu | THÊM | logic tính RFM cần đặc tả |
| 5 | Card Danh sách KH | có thẻ cơ bản | thẻ: Tên + Gói(tên+tiến độ+thời gian còn lại) + Nhóm KH(màu) | SỬA | thêm thời gian còn lại + nhóm |
| 6 | Bấm thẻ → Chi tiết KH | (có implicit) | có | KẾ THỪA | |
| 7 | Nút “Thêm mới” (FAB) | có (+) | giữ | KẾ THỪA | dẫn tới §2.4 |

**Tóm tắt:** KẾ THỪA search + FAB + list pattern · THÊM tabs KHTN/KH, card Summary RFM, trạng thái RFM, nhóm KH, thời gian còn lại · SỬA thẻ danh sách.

---

### 2.3 Thêm mới KH — To-Be §2.4 ↔ As-Is Wizard B1+B2+B4
- **As-Is:** thông tin KH rải ở B2 (giới tính/ngày sinh/cao/nặng hiện tại/nặng mục tiêu/hoạt động) và B4 (họ tên/email/MK); không có SĐT/địa chỉ/người mời; không có câu hỏi khảo sát chất lượng.
- **To-Be:** 1 màn “Thêm mới KH” với Card Thông tin cơ bản + Card Chân dung KH (10 câu hỏi + ô trả lời + tự phân tích).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tên người mời (default HLV đăng nhập) | chưa có | có, editable | THÊM | Content-Attribution Matching |
| 2 | SĐT người mời | chưa có | có (default trống) | THÊM | |
| 3 | Họ tên KH * | có (ở B4) | có (đây, bắt buộc) | KẾ THỪA+DI CHUYỂN | đưa lên đầu |
| 4 | SĐT KH | chưa có | có (không bắt buộc) | THÊM | D15 chống trùng theo SĐT — cân nhắc bắt buộc? |
| 5 | Email KH | có (ở B4) | có (không bắt buộc) | KẾ THỪA+DI CHUYỂN | |
| 6 | Ngày sinh | có (B2) | có | KẾ THỪA+DI CHUYỂN | |
| 7 | Giới tính (default nam) | có (B2) | có, default nam | KẾ THỪA+DI CHUYỂN | |
| 8 | Chiều cao (cm) | có (B2) | có | KẾ THỪA+DI CHUYỂN | |
| 9 | Cân nặng (kg) | có (B2, là “hiện tại”) | có | KẾ THỪA+DI CHUYỂN | |
| 10 | Địa chỉ | chưa có | có | THÊM | |
| 11 | Cân nặng mục tiêu | có (B2) | (chuyển sang Phân tích — tick mục tiêu §2.6) | DI CHUYỂN/XÓA khỏi màn này | quyết mục tiêu sau phân tích |
| 12 | Mức hoạt động | có (B2) | (chưa nói — có thể giữ cho RMR) | KẾ THỪA? | cần xác nhận |
| 13 | Card Chân dung KH (10 câu hỏi + ô trả lời HLV + tự phân tích) | chưa có | có | THÊM | cốt lõi — thay “khảo sát số liệu” cũ |
| 14 | Nút Lưu → chuyển Khảo sát Tanita | (B2 → B3) | Lưu → Khảo sát Tanita | SỬA | đổi đích |

**Tóm tắt:** KẾ THỪA các trường định danh (họ tên/email/ns/gt/cao/nặng) · THÊM người mời + SĐT + địa chỉ + Card Chân dung KH (10 câu hỏi) · DI CHUYỂN “cân mục tiêu” sang Phân tích · SỬA luồng (Lưu → Tanita thay vì → thực đơn).

---

### 2.4 Khảo sát Tanita — To-Be §2.5 ↔ As-Is: KHÔNG có trong luồng wizard
- **As-Is:** wizard KHÔNG có bước Tanita (Tanita chỉ ở màn riêng ngoài luồng, xem archive `04_tanita_update.png`).
- **To-Be:** màn “Khảo sát Tanita” trong luồng — OCR ảnh + form nhập tay 9 chỉ số theo thứ tự cân.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Nút Chụp ảnh / Chọn ảnh (OCR) | chưa có (trong luồng) | có | THÊM | PoC OCR (Feasibility) |
| 2 | Form nhập tay 9 chỉ số theo thứ tự cân | chưa có (trong luồng) | Cân nặng, Mỡ %, Xương kg, Nước %, Cơ kg, Vóc dáng, Tuổi sinh học, RMR kcal, Mỡ nội tạng 1-50 | THÊM | thứ tự theo cân Tanita |
| 3 | “Sử dụng kết quả” / “Chỉnh sửa” sau OCR | chưa có | có | THÊM | |
| 4 | Nút “Tạo bản tư vấn” → Phân tích | chưa có | có | THÊM | |

**Tóm tắt:** **toàn bộ màn THÊM** (As-Is không có Tanita trong luồng tư vấn). Là một trong 2 phần THÊM lớn nhất.

---
### 2.5 Phân tích kết quả — To-Be §2.6 ↔ As-Is: KHÔNG có
- **As-Is:** wizard KHÔNG có màn phân tích/bản tư vấn (chỉ tính RMR + calo auto ở B2, không đối chiếu chuẩn, không bảng đánh giá).
- **To-Be:** bảng 4 cột (Hiện tại / Cần tăng giảm ẩn tên / Tiêu chuẩn / Đánh giá thừa-thiếu kg+%) × 9 dòng (Cân nặng, Cơ, Xương, Nước, Mỡ, Mỡ nội tạng, Vóc dáng, Tuổi sinh học, RMR); màu dòng (xanh tốt/vàng trung bình/đỏ nguy hiểm); drop-down 2 cột (Ý nghĩa + Rủi ro bệnh lý); tick mục tiêu (tăng/giảm/giữ cân) → hiện tên chương trình.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Bảng phân tích 4 cột × 9 dòng | chưa có | có | THÊM | cốt lõi |
| 2 | Màu dòng theo mức (xanh/vàng/đỏ) | chưa có | có | THÊM | dùng --state-good/warn/alert |
| 3 | Cột “Đánh giá” (thừa/thiếu kg+%) | chưa có | có | THÊM | tính vs Body-Composition-Standards (D05) |
| 4 | Drop-down chi tiết/dòng (Ý nghĩa + Rủi ro bệnh lý) | chưa có | có | THÊM | |
| 5 | Tick mục tiêu (tăng/giảm/giữ cân) | có “cân mục tiêu” ở B2 (nhập số) | tick 3 lựa chọn → sinh tên chương trình | SỬA+THÊM | đổi từ nhập số → chọn + auto chương trình (D08) |
| 6 | Auto đề xuất tên chương trình | chưa có | Dinh dưỡng tế bào / Cơ Nước Mỡ / Bữa sáng lành mạnh | THÊM | logic D08 |
| 7 | Nút “Xem lộ trình” / “Đóng” | chưa có | có | THÊM | |

**Tóm tắt:** **toàn bộ màn THÊM** (As-Is không có phân tích trong luồng). Phần THÊM lớn thứ 2. KẾ THỪA duy nhất: ý tưởng “cân mục tiêu” (nhưng đổi từ nhập → tick + auto chương trình).

---

### 2.6 Xem lộ trình — To-Be §2.7 ↔ As-Is Wizard B1 (Chọn gói)
- **As-Is (B1):** chọn gói dropdown + ngày bắt đầu → Tiếp tục. **Chọn gói ở ĐẦU luồng**, đơn giản.
- **To-Be:** màn “Xem lộ trình” SAU phân tích — lợi ích + kết quả + lộ trình (1/3/trọn đời, default 3) + gói sản phẩm (không giá) + cam kết disclaimer + nút “Tạo tài khoản”.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Chọn gói | đầu luồng (dropdown) | cuối luồng (sau phân tích) | DI CHUYỂN+SỬA | đúng nghiệp vụ tư vấn |
| 2 | Ngày bắt đầu | có (date picker) | (chuyển sang “loại lộ trình” 1/3/trọn đời) | SỬA | |
| 3 | Lợi ích chương trình (bullet) | chưa có | có | THÊM | |
| 4 | Kết quả đạt được | chưa có | có | THÊM | |
| 5 | Lộ trình 1/3/trọn đời (default 3) | chưa có | có | THÊM | |
| 6 | Gói sản phẩm đi kèm (không hiện giá) | chưa có | có | THÊM | giá giải thích ngoài app |
| 7 | Cam kết / disclaimer | chưa có | có | THÊM | D11 inline |
| 8 | Nút “Tạo tài khoản” → pop-up | (B4 Xác nhận) | có | SỬA | đổi dạng |

**Tóm tắt:** DI CHUYỂN chọn gói từ đầu → cuối luồng · THÊM lợi ích/kết quả/loại lộ trình/gói SP/cam kết · SỬA nút xác nhận → “Tạo tài khoản” (pop-up).

---

### 2.7 Pop-up Tạo Tài khoản KH — To-Be §2.8 ↔ As-Is Wizard B4
- **As-Is (B4):** màn full — Họ tên, Email, MK (3 trường, nhập tay).
- **To-Be:** **pop-up** — Tài khoản (SĐT/email auto từ KH, editable), MK auto random (editable), Xác nhận MK; gửi email cho KH.

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Dạng hiển thị | màn full | pop-up | SỬA | |
| 2 | Họ tên KH | có (nhập) | không (đã có ở Thêm mới KH) | XÓA | tránh lặp |
| 3 | Tài khoản (SĐT/email) | Email (nhập) | auto từ KH, editable | SỬA | auto-fill |
| 4 | Mật khẩu | nhập tay | auto random, editable | SỬA | |
| 5 | Xác nhận MK | chưa có | có | THÊM | |
| 6 | Gửi email chứa TK cho KH | chưa rõ | có | THÊM/THÊM | explicit |
| 7 | Sau tạo → “Xây dựng bữa ăn” | (→ Chi tiết KH) | → Xây dựng bữa ăn | SỬA | đổi đích |

**Tóm tắt:** SỬA thành pop-up + auto-fill + MK random · XÓA họ tên (tránh lặp) · THÊM xác nhận MK + gửi email · SỬA đích → bữa ăn.

---

### 2.8 Xây dựng gợi ý bữa ăn — To-Be §2.9 ↔ As-Is Wizard B3 (Thực đơn) + Chi tiết KH
- **As-Is (B3):** chọn số bữa (dropdown) → thực đơn auto theo calo (4 bữa: sáng/trưa/xế/tối, mỗi bữa vài món), editable, cuộn dài; + ảnh đại diện.
- **To-Be:** Card Mục tiêu (calo +/-, số bữa +/- default 4, nút “Tạo gợi ý bữa ăn”) + Card Gợi ý bữa ăn (cấu trúc 30/40/30 + con số calo kỳ diệu + nước; 4 bữa chi tiết: món đạm/bột/rau + số lượng + calo + món kèm + TPCN bổ sung + lưu ý HLV; nước/ngày lít+cốc; khuyến nghị thời gian sinh hoạt).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Số bữa (chọn) | có (dropdown) | có (+/- stepper, default 4) | SỬA | đổi control |
| 2 | Calo/ngày (điều chỉnh) | auto (B2) | có (+/- stepper) | SỬA | cho chỉnh |
| 3 | Nút “Tạo gợi ý bữa ăn” | (auto ngay) | nút explicit | SỬA | |
| 4 | Cấu trúc 30/40/30 (Đạm/Bột/Béo tốt) + con số calo kỳ diệu | ẩn | hiển thị rõ | THÊM | minh bạch |
| 5 | Nước khuyến nghị (công thức) | (hiện ml ở Chi tiết) | hiện lít + cốc + công thức | SỬA+THÊM | 0.4L/10kg |
| 6 | 4 bữa chi tiết (sáng/trưa/phụ/tối) | có (đơn giản) | có (đầy đủ) | SỬA | enrich |
| 7 | Mỗi bữa: món đạm + bột + rau (tên nhóm + số lượng bát/lạng/củ + calo) | có (ít cấu trúc) | có (cấu trúc 3 nhóm) | SỬA | 3 nhóm rõ |
| 8 | Món kèm (sữa chua, trái cây...) | chưa rõ | có | THÊM | |
| 9 | Thực phẩm bổ sung (sản phẩm gói: F1/PPP/Omega3...) | có (vd F1+PPP) | có (gắn gói chương trình) | KẾ THỪA+SỬA | liên kết gói |
| 10 | Lưu ý HLV mỗi bữa (ăn ngược, nhai kỹ...) | chưa có | có | THÊM | |
| 11 | Khuyến nghị thời gian sinh hoạt (giờ ăn/ngủ/vận động) | chưa có | có | THÊM | |
| 12 | Ảnh đại diện KH | có (ở B3) | (không đề cập — nên chuyển sang Thêm mới KH/Chi tiết) | DI CHUYỂN | |
| 13 | Nút “Hoàn thành” → DS KH | (→ Chi tiết KH) | → DS KH | SỬA | |

**Tóm tắt:** KẾ THỪA thực đơn auto + 4 bữa + TPCN · SỬA control (dropdown→+/-), hiển thị cấu trúc 30/40/30, thẻ bữa (3 nhóm), nước · THÊM món kèm, lưu ý HLV, thời gian sinh hoạt · DI CHUYỂN ảnh đại diện ra màn khác.

---

### 2.9 Chi tiết KH — As-Is Màn 08 (giữ + làm giàu)
- **As-Is:** tên + “Đã mua gói”, thời gian, kế hoạch dinh dưỡng (calo/đạm/nước/bữa), mục tiêu cân nặng, nút chỉnh bữa ăn/điều chỉnh mục tiêu/chat.
- **To-Be:** draft không mô tả lại nhưng nhắc “bấm thẻ → chi tiết KH”. **KẾ THỪA toàn bộ + làm giàu** (gắn RFM, timeline, lịch sử phiên bản thực đơn — E03).

**Tóm tắt:** KẾ THỪA · THÊM (sau): RFM status, timeline, lịch sử phiên bản bữa ăn, nút chăm sóc (E03).

### 2.10 Đăng nhập — As-Is Màn 01 (giữ + sửa nhỏ)
- **As-Is:** SĐT/Email + MK + Face ID; nút div (accessibility); link Quên MK/Đăng ký hẹp.
- **To-Be:** draft giả định đăng nhập, không redescribe.
- **GAP:** KẾ THỪA SĐT/Email + MK + Face ID · SỬA nút thành `<button>` chuẩn (accessibility), giãn link. (Tuân D01 role-based: chọn vai HLV/KH — hiện đã implicit.)

---

## 3. Tổng hợp GAP (E01 + E02)

### KẾ THỪA (giữ — không đụng, không regression)
- Đăng nhập: SĐT/Email + MK + Face ID, lưu phiên.
- Dashboard: task list (to-do) + KPI data (KH/NPP/Doanh thu).
- Team: search, FAB +, list pattern, bấm thẻ → chi tiết.
- Thêm mới KH: các trường định danh (họ tên/email/ngày sinh/giới tính/chiều cao/cân nặng).
- Wizard: tính RMR + calo mục tiêu auto (logic quan trọng).
- Bữa ăn: thực đơn auto theo calo, 4 bữa, TPCN (F1/PPP).
- Chi tiết KH: dashboard KH (calo/đạm/nước/bữa/mục tiêu), nút chỉnh bữa ăn/điều chỉnh mục tiêu/chat.
- Tài khoản: flow tạo TK cho KH.

### SỬA (đổi — focus công sức vừa)
- Dashboard: KPI tách rõ, bottom nav (4 tab + icon Tabler), thêm action center + FAB radial + lời chào.
- Team: thẻ danh sách (thêm thời gian còn lại + nhóm KH), tabs KHTN/KH.
- Thêm mới KH: gom trường định danh vào 1 card, di chuyển họ tên/email lên đầu, đổi luồng Lưu → Tanita.
- Bữa ăn: dropdown → +/- stepper, hiển thị cấu trúc 30/40/30, thẻ 3 nhóm, nước lít+cốc.
- Tạo TK: màn full → pop-up, auto-fill, MK random, gửi email, đích → bữa ăn.
- Đăng nhập: nút accessibility.

### THÊM (mới — phần lớn, effort lớn)
- **KH tiềm năng** (khái niệm + tab + luồng riêng).
- **Card Summary RFM** + 3 trạng thái (tích cực/có nguy cơ/kém quan tâm) + màu + filter.
- **Attribution người mời** (Tên + SĐT, default HLV).
- **Card Chân dung KH** (10 câu hỏi + ô trả lời + tự phân tích).
- **Khảo sát Tanita** (OCR + form 9 chỉ số) — toàn màn.
- **Phân tích kết quả** (bảng 9 dòng + màu + drop-down + tick mục tiêu → auto chương trình) — toàn màn.
- **Xem lộ trình** (lợi ích/kết quả/1-3-trọn đời/gói SP/cam kết).
- Bữa ăn: món kèm, lưu ý HLV, thời gian sinh hoạt, nước công thức.
- **Objection Handler** (FAB “Khách đang băn khoăn” — D07, draft nói “KH chưa đồng ý → Đóng về DS KH”, nên bổ sung nhánh xử lý).

### XÓA (gỡ — nhỏ)
- Họ tên khỏi pop-up Tạo TK (tránh lặp).
- “Cân nặng mục tiêu” khỏi Thêm mới KH (chuyển sang tick ở Phân tích).

### PoC kỹ thuật cần làm (Feasibility)
- OCR ảnh Tanita (độ chính xác).
- (sau) AI bóc tách món ăn, sinh infographic.

---

## 4. Reconciliation — lệch giữa draft To-Be và E01/E02 stories/mockups hiện có

> Draft-requirements là **mô tả chi tiết hơn, ưu tiên cao hơn**. E01/E02 stories + mockups hiện có cần cập nhật để khớp.

| # | Lệch | Hiện tại (stories/mockups) | Draft To-Be | Hành động đề xuất |
|---|---|---|---|---|
| R1 | Phá băng (US-E02-01) | có màn Phá băng checklist | KHÔNG có (draft bắt đầu tại Team → Thêm mới KH) | **Đổi US-E02-01 thành bước tùy chọn/off-app** (phá băng lời nói, không màn app) HOẶC gộp vào Card Chân dung. Chờ PO chốt. |
| R2 | Thứ tự Tanita vs Khảo sát | mockup S-CONS-02 khảo sát → S-CONS-03 Tanita | draft: Thêm mới KH (Chân dung) → Tanita | **Khớp** — giữ thứ tự Khảo sát(Chân dung) → Tanita. Đổi tên S-CONS-02 → “Chân dung KH” cho rõ. |
| R3 | Phân tích (S-CONS-04) | dạng 5 bước narrative | draft: bảng 4 cột × 9 dòng + drop-down + tick mục tiêu | **Cập nhật mockup S-CONS-04** sang dạng bảng draft (chi tiết hơn). |
| R4 | Giải pháp (S-CONS-05) | focus card 3 chương trình | draft: “Xem lộ trình” (lợi ích/kết quả/1-3-trọn đời/gói SP/cam kết) | **Cập nhật mockup S-CONS-05** thêm các thành phần draft. |
| R5 | Objection (S-CONS-06) | có FAB 5 nhánh | draft: chỉ “KH chưa đồng ý → Đóng về DS KH” | **Giữ Objection Handler** (D07) — draft chưa nói nhưng nghiệp vụ cần; bổ sung làm overlay. Chờ PO. |
| R6 | Bữa ăn (S-CONS-07) | đơn giản (3 nhóm + persona-fit) | draft: cấu trúc 30/40/30 + món kèm + lưu ý + thời gian sinh hoạt | **Cập nhật mockup S-CONS-07** enrich theo draft. |
| R7 | Tạo TK (S-CONS-08) | màn full điền sẵn | draft: pop-up + MK random + gửi email | **Cập nhật mockup S-CONS-08** sang pop-up. |
| R8 | E01 KH tiềm năng | mockup S-LEAD-01 (T2, cờ thủ công D12) | draft: tabs KHTN/KH + RFM Summary | **Cập nhật S-LEAD-01** thêm tabs + Summary RFM; **thêm business-rule RFM** (mới, chưa có trong decisions-log). |
| R9 | RFM trạng thái | chưa có | 3 trạng thái + màu | **Thêm Q31 vào decisions-log**: quy tắc tính RFM (Recency/Frequency/Monetary ngưỡng) — cần PO chốt. |
| R10 | Attribution người mời | Content-Attribution Matching (D?? chung) | draft cụ thể: Tên+SĐT người mời, default HLV | **Thêm Q32**: cơ chế attribution khi tạo KH (mặc định HLV, cho đổi) — cần PO chốt. |
| R11 | “Khảo sát mục tiêu” (draft §2.4 cuối) | — | draft nói “Lưu → Khảo sát mục tiêu” rồi §2.5 là “Khảo sát Tanita” | **Lệch tên** — cần PO xác nhận: có màn “Khảo sát mục tiêu” riêng hay đó là cùng Card Chân dung? |
| R12 | Cân mục tiêu | ở Thêm mới KH (B2 As-Is) | draft: tick ở Phân tích | **Di chuyển** — đã phản ánh trong GAP §2.3. |

> **Tóm lại:** 12 điểm lệch — 3 điểm cần PO chốt (R1 phá băng, R5 objection, R11 khảo sát mục tiêu) + 2 quy tắc mới cần PO (R9 RFM, R10 attribution) + 7 điểm cập nhật mockup (R2-R4,R6-R8). Khi PO chốt R1/R5/R9/R10/R11, tôi cập nhật stories + mockups cho khớp.
