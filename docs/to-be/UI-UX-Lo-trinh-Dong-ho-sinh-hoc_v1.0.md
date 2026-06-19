# Đặc tả UI-UX — Màn "Sức khỏe tổng thể" (Lộ trình cá nhân hóa phía Khách hàng)

> **Tên màn hình:** "**Sức khỏe tổng thể**" (trước đây gọi "Đồng hồ sinh học" — nay là tên *widget trung tâm* trong màn này). Prototype: `prototypes/kh/suc_khoe_tong_the.html`.

**Phiên bản:** v1.1 (draft) · **Cập nhật:** 2026-06-18
**Mục đích:** Đặc tả giao diện & trải nghiệm cho màn "Trải nghiệm lộ trình cá nhân hóa" của Khách hàng, lấy cảm hứng từ **"Cỏ ba lá Sức khỏe" (Huawei Health)** nhưng **thay biểu tượng Cỏ ba lá bằng "Đồng hồ sinh học"** — vòng tròn 24h chia múi theo hoạt động trong ngày.
**Bám sát:**
- Luồng nghiệp vụ: `docs/to-be/Workflow-KH.md` (Quy trình 002 — Cá nhân hóa lộ trình & gợi ý bữa ăn).
- Tham chiếu thiết kế: `docs/to-be/Huawei-Health-Clover-case-study.md`.
- Quy tắc Calo/bữa ăn: `docs/business-rules/Calorie-Meal-Business-Rules-v1.0.md`.

> ⚠️ **Lưu ý phạm vi:** `Workflow-KH.md` hiện **chưa** mô tả luồng **chụp ảnh / khai báo danh sách món ăn** trong ngày. Tài liệu này **đặc tả bổ sung** luồng đó (§2.4c, §3.3) và đề xuất cập nhật lại `Workflow-KH.md` cho khớp (§6).

---

## 1. Tổng quan tính năng

Trung tâm màn hình là **"Đồng hồ sinh học"** — một **vòng tròn 24 giờ** chia thành các **múi (segment)** theo trình tự sinh hoạt **chiều kim đồng hồ** (thức dậy → sáng → trưa → chiều → tối → ngủ). Mỗi múi đại diện cho **một hoạt động trong lộ trình** mà KH đã tự cấu hình giờ.

Khác biệt cốt lõi so với Cỏ ba lá: thay vì 3 cánh theo nhóm chỉ số, **Đồng hồ sinh học hiển thị toàn bộ nhịp ngày theo thời gian thực** — múi nào tới giờ/đã làm sẽ đổi màu trạng thái. Mục tiêu UX: KH nhìn một vòng là biết "hôm nay đang đi đúng nhịp sinh học chưa".

**Triết lý lộ trình — Thân · Tâm · Trí:** toàn bộ lộ trình giúp KH thay đổi & đạt kết quả tốt hơn trên 3 trụ cột, các hoạt động trong ngày đều quy về một trong ba:
- **Thân** (sức khỏe thể chất & tinh thần): thức dậy, thải độc/uống nước, bữa ăn, thể dục, ngủ.
- **Tâm** (lối sống lành mạnh, yêu thương, biết ơn, quản trị cảm xúc): thư giãn, thiền, nghỉ ngơi tích cực.
- **Trí** (kiến thức, hiểu biết — quản trị tài chính, đầu tư, kinh doanh…): **PTBT — Phát triển bản thân** (đọc sách, Zoom đào tạo kỹ năng/kiến thức).

Mỗi hoạt động được gắn thẻ Thân/Tâm/Trí; đồng hồ có thể hiển thị **chú giải 3 trụ cột** (3 màu/nhãn) để KH thấy cân bằng giữa Thân–Tâm–Trí trong ngày.

---

## 1bis. Màn "Cá nhân hóa thời gian biểu" (cấu hình trước khi dùng hằng ngày)

Prototype: `prototypes/kh/ca_nhan_hoa_thoi_gian_bieu.html`. Truy cập một lần trước khi dùng màn "Sức khỏe tổng thể" (chỉnh lại được).

- **Bộ chọn số bữa ăn** (3/4/5) → quyết định **số nhiệm vụ ăn** ở màn hằng ngày.
- **Danh sách hoạt động** với **time picker giờ bắt đầu/kết thúc**; mỗi dòng hiển thị **khung giờ tối ưu** và **huy hiệu điểm tối đa** (tối đa 3đ/2đ/1đ).
- **Thanh "Mức tối ưu đồng hồ sinh học (%)"** + **tổng điểm tối đa/ngày**, cập nhật trực tiếp khi đổi giờ/số bữa.
- **Quy tắc:** lệch khung tối ưu → giảm trần điểm (đúng=3, lệch vừa=2, lệch nhiều=1). Khuyến khích sắp lịch gần nhịp sinh học nhưng vẫn linh hoạt.

## 2. Thiết kế Giao diện (UI Components)

### 2.1. Thanh điều hướng thời gian (Time Navigation Bar)
- **Vị trí:** Trên cùng.
- **Thành phần:** thứ + ngày hiện tại; hàng ngang 7 ngày (CN→T7), mỗi ngày là **một đồng hồ sinh học thu nhỏ** đã tô màu theo mức hoàn thành ngày đó.
- **Trạng thái:** ngày hiện tại highlight; vuốt ngang để xem lịch sử (đổi toàn bộ dữ liệu bên dưới).

### 2.2. Khu vực trung tâm: Widget "Đồng hồ sinh học"
- **Hình dáng:** vòng tròn 24h, chia **múi theo hoạt động**, sắp xếp **theo chiều kim đồng hồ** đúng thứ tự sinh học (xem bảng §2.5). Đỉnh (12h trên) = mốc **Thức dậy / Vệ sinh**.
- **Tô màu trạng thái mỗi múi** (theo bản nháp):

  | Màu | Ý nghĩa | Khi nào |
  |---|---|---|
  | 🟢 Xanh | **Tốt** ✓ | Hoàn thành đúng/đủ (vd đã check-in, đủ nước, đủ đạm) |
  | 🟡 Vàng | **Lưu ý** | Hoàn thành một phần / trễ giờ / chưa đạt mục tiêu |
  | 🔴 Đỏ | **Cảnh báo** ✗ | Bỏ lỡ / vượt ngưỡng (vd Calo in vượt, bỏ hoạt động) |
  | ⚪ Xám | Chưa tới giờ | Hoạt động trong tương lai của ngày |

- **Kim chỉ thời gian thực:** một kim/điểm sáng chạy theo giờ hiện tại để KH biết "đang ở múi nào".
- **Tâm vòng tròn (Quick Stats):** tổng quan nhanh — **% hoàn thành ngày**, **Calo in / out**, **Lượng nước (đã/đích)**. (Tương đương Quick Stats Panel của Huawei nhưng đặt ở tâm.)
- **Cuộn:** khi cuộn danh sách bên dưới, đồng hồ thu nhỏ dần để nhường chỗ (giống hành vi Huawei).

### 2.2bis. Widget thu nhỏ + Tổng kết điểm (Hero)
- **Đồng hồ sinh học được thu nhỏ** và đặt cạnh khối tổng kết để dành diện tích cho danh sách hoạt động.
- **Màu các múi sinh động hơn** (dùng **gradient**) thay vì màu phẳng.
- Khối tổng kết hiển thị **Điểm hôm nay** (lớn), Calo in/out, **số cốc nước**.

### 2.3. Danh sách Hoạt động trong ngày — chia 2 vùng
Danh sách thẻ chia thành **2 vùng** để tạo động lực:
- **"Đã thực hiện (n) · +X điểm"** — đặt **trên**, thẻ **to & nổi bật hơn** (nền xanh nhạt, viền trái theo điểm, có **huy hiệu điểm** +3đ/+2đ/+1đ).
- **"Chờ thực hiện (n)"** — đặt dưới, thẻ **gọn & mờ nhẹ**.
- Khi KH **tick "xong"**, thẻ **trôi từ vùng chờ lên vùng đã thực hiện** (và ngược lại nếu bỏ tick). Mục tiêu UX: vùng "đã thực hiện" luôn được tôn lên để khích lệ.

Mỗi thẻ gồm: **icon minh họa sinh động** (mỗi hoạt động một icon riêng), **Tiêu đề** + **nhãn trụ cột** (Thân/Tâm/Trí), **giờ cấu hình**, **nút thao tác** (📷 với bữa ăn, ✓ với tick). Thẻ chờ có thêm liên kết **"Hoàn thành một phần"** (ghi 1 điểm).

### 2.3bis. Thẻ "Uống nước" — ghi nhận nhiều lần trong ngày
Nước là hoạt động **lặp lại nhiều lần**, nên có **thẻ riêng nổi bật** (không nằm trong 2 vùng trên):
- Hiển thị **dãy cốc** (vd 8 cốc = mục tiêu 2,0L), **mỗi cốc ~250ml**.
- Nút lớn **"+ Cốc nước"**: mỗi lần bấm = **một lần check-in (1 cốc)**, làm đầy thêm 1 cốc và **ghi 1 bản ghi nhật ký** uống nước.
- Tiến độ `cốc đã uống / mục tiêu` đồng bộ lên Quick Stats. Đạt mục tiêu → tính hoàn thành (cộng điểm).

### 2.4. Bottom Sheets / Giao diện nhập liệu

**a) Cấu hình giờ hoạt động (khi tạo/sửa lộ trình)** — Wheel Time Picker chọn Giờ bắt đầu/Hoàn thành cho từng hoạt động; với hoạt động có lựa chọn (vd Luyện trí: tại NĐD / qua Zoom) có thêm chọn hình thức.

**b) Uống nước** — hàng biểu tượng ly; nút lớn **"+ Uống nước"** cộng dồn; mục tiêu tính theo `0.4–0.7 × cân nặng (kg)`.

**c) Bữa ăn — Chụp ảnh & Khai báo món ăn** *(luồng bổ sung)*
- Mở từ thẻ **Bữa ăn** hoặc khi nhận nhắc giờ ăn. **Số nhiệm vụ ăn = số bữa** cấu hình ở màn "Cá nhân hóa thời gian biểu".
- **Hai cách nhập (kết hợp được):**
  1. **📷 Chụp/Upload ảnh → API AI bóc tách:** tự nhận diện **tên món** + **ước lượng đơn vị (bát/lạng)** + số lượng → các trường **sửa được** (gắn nhãn "AI"); KH chỉnh nếu sai.
  2. **Nhập tay theo form:** mỗi dòng món gồm **Tên món** (gà/cá/tôm/rau/nấm…), **Đơn vị đo** (bát/lạng/cốc…), **Số lượng** → **gọi API tính Calo** nạp vào.
- Mỗi dòng món hiển thị **kcal do API tính**; tổng **Calo in/đạm** tạm tính đối chiếu mục tiêu.
- **Lưu** → ghi nhật ký bữa ăn (meal log + ảnh + ai_analysis + danh sách món/đơn vị) → cập nhật múi "Bữa ăn" + Calo in.

**d) Check-in tick** — với hoạt động loại ✓ (thải độc, ngủ trưa, thư giãn/thiền, ngủ tối): bottom sheet xác nhận hoàn thành (+ ghi chú/ảnh tùy chọn).

### 2.5. Bản đồ múi đồng hồ ↔ hoạt động (theo chiều kim đồng hồ)

| Vị trí (giờ trên đồng hồ) | Hoạt động | Trụ cột | Xác nhận |
|---|---|---|---|
| Đỉnh (~12h trên) | **Thức dậy / Vệ sinh** | Thân | 📷 |
| Phải-trên | **Buổi sáng / Ăn sáng** | Thân | 📷 (bữa ăn) |
| Phải | **Giữa buổi** (làm việc/học) | Trí | — |
| Phải-dưới (~12h trưa) | **Ăn trưa** | Thân | 📷 (bữa ăn) |
| Đáy (chiều) | **Luyện tập / Làm việc** | Thân/Trí | 📷 |
| Trái-dưới (~19h) | **Ăn tối** | Thân | 📷 (bữa ăn) |
| Trái | **Tối — Thư giãn / Thiền** | Tâm | ✓ |
| Trái-trên | **PTBT — Phát triển bản thân** (đọc sách, Zoom đào tạo) → rồi **Ngủ** | Trí → Thân | ✓ |

> **PTBT = Phát triển bản thân** (thuộc trụ cột **Trí**): đọc sách, tham gia Zoom đào tạo kỹ năng/kiến thức (quản trị tài chính, đầu tư, kinh doanh…). Hoạt động **thiền/thư giãn** thuộc trụ cột **Tâm**.

---

## 3. Quy trình Tương tác & UX (Scenarios)

### 3.1. Tạo lộ trình cá nhân hóa
1. Vào **Lộ trình & Bữa ăn → tab Cá nhân hóa → "Tạo Lộ trình cá nhân"**.
2. Đồng hồ sinh học hiện các múi hoạt động mẫu (giờ trống, màu xám).
3. KH chạm từng múi/thẻ → **chọn giờ** (Time Picker §2.4a).
4. Hệ thống tính **lượng nước/ngày** + gắn **Gợi ý bữa ăn** theo mục tiêu → lưu → **gửi HLV phản hồi**.

### 3.2. Trong ngày — nhận nhắc & xác nhận
- Tới mốc giờ, hệ thống **nhắc**; KH **📷 chụp ảnh** hoặc **✓ tick** ngay từ thông báo/thẻ.
- Múi tương ứng đổi sang 🟢/🟡 theo kết quả; tâm đồng hồ cập nhật % & Calo/nước.

### 3.3. Ghi nhận bữa ăn (chụp ảnh + khai báo món) — *bổ sung*
1. Chạm thẻ **Bữa ăn** → Bottom Sheet §2.4c.
2. **📷 Chụp/chọn ảnh** → AI nhận diện món & Calo/đạm → KH sửa nếu cần; **hoặc/và** **khai báo danh sách món** thủ công.
3. Xác nhận → lưu nhật ký; múi bữa ăn 🟢 (hoặc 🔴 nếu Calo in vượt ngưỡng); Calo in ở tâm tăng.

### 3.4. Trang chủ tổng kết (≈ 22h)
- Đồng hồ "đầy màu" theo ngày; thẻ tổng kết: **đủ đạm/Calo/nước/ngủ?**, **% hoàn thành**, **chấm điểm từng hoạt động**, **lưu ý cải thiện**.

### 3.5. Xem lịch sử ngày/tuần
- Vuốt thanh thời gian → đồng hồ co giãn nhẹ và tô lại theo dữ liệu ngày đó; xem xu hướng **% hoàn thành theo tuần**.

---

## 4. Quy tắc Logic & Chấm điểm

**Mỗi lần tick/ghi nhận = một bản ghi nhật ký** `{hoạt động, thời điểm, điểm}` — dùng cho đánh giá hoàn thành, **tính streak & credit thưởng** (credit *chưa* triển khai ở giai đoạn này).

**Thang điểm mỗi hoạt động:**

| Điểm | Trạng thái | Màu múi/thẻ |
|---|---|---|
| **3** | Hoàn thành **đúng lịch** (đúng khung giờ) | 🟢 xanh |
| **2** | Hoàn thành nhưng **không đúng giờ** (trễ) | 🟡 vàng |
| **1** | Hoàn thành **một phần** | 🟠 cam |
| **0** | **Chưa hoàn thành** / chờ | ⚪ xám |

- **Tổng điểm hôm nay** = Σ điểm các hoạt động (gồm nước khi đạt mục tiêu) → hiển thị ở khối tổng kết; lũy kế phục vụ **streak/credit** sau này.
- **Logic tô màu múi đồng hồ** theo điểm ở trên (gradient cho sinh động); ⚪ cho hoạt động chưa tới giờ.
- **Lượng nước mục tiêu** = `0.4–0.7 × cân nặng (kg)` ≈ số cốc 250ml; mỗi lần "+ Cốc nước" ghi 1 bản ghi.
- **Calo in/out** đối chiếu mục tiêu (R) từ `Calorie-Meal-Business-Rules`.
- **Đồng bộ:** mỗi lần check-in (ảnh/tick/nước/bữa ăn) cập nhật **đồng thời** múi đồng hồ + tổng điểm + chuyển thẻ giữa 2 vùng.

---

## 5. Bảng đối chiếu Huawei → AnCare

| Thành phần Huawei (Cỏ ba lá) | Tương ứng AnCare (Đồng hồ sinh học) |
|---|---|
| Cỏ ba lá 3 cánh | Vòng tròn 24h chia múi theo hoạt động |
| Cánh tô đầy theo % nhóm nhiệm vụ | Múi tô màu trạng thái 🟢🟡🔴 theo hoạt động |
| Quick Stats bên phải | Quick Stats ở **tâm** đồng hồ (%/Calo/nước) |
| Thẻ nhiệm vụ (nước, ngủ, bước…) | Thẻ hoạt động lộ trình (8 hoạt động §B Workflow-KH) |
| Bottom sheet Uống nước (+250ml) | Bottom sheet Uống nước (theo 0.4–0.7×kg) |
| — (Huawei không có) | **Bottom sheet Bữa ăn: chụp ảnh + khai báo món** (bổ sung) |
| Mini cỏ ba lá theo tuần | Mini đồng hồ sinh học theo tuần |

---

## 6. Đề xuất cập nhật Workflow-KH.md
Bổ sung một nhánh/luồng con cho **ghi nhận bữa ăn**: từ thẻ Bữa ăn → (chụp ảnh ➜ AI nhận diện ➜ xác nhận) và/hoặc (khai báo danh sách món) → lưu nhật ký → cập nhật Calo in & múi đồng hồ. Đây là phần `Workflow-KH.md` đang thiếu.

---
*Draft v1.0 — cần chốt với nghiệp vụ: ngưỡng màu 🟡/🔴, công thức % hoàn thành, và cách hiển thị cân bằng Thân–Tâm–Trí trên đồng hồ.*
