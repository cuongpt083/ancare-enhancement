# E00 — Platform Shell

- **Vai trò:** HLV + KH (+ Founder/Admin)
- **Mục tiêu:** Nền tảng chung — xác thực, shell điều hướng, mục tiêu cá nhân/kinh doanh, kho sự kiện, màn hình chính (menu shortcut / floating bubble tùy biến).
- **Nguồn:** feature-tree — "Mục tiêu" (§2.7), "Kho sự kiện" (§2.8), "UI Main Screen" (§3).

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E00-01 | Đăng nhập / xác thực | Must |
| US-E00-02 | Shell điều hướng + floating bubble | Must |
| US-E00-03 | Đặt mục tiêu cá nhân (KH) | Should |
| US-E00-04 | Đặt mục tiêu kinh doanh (HLV) | Should |
| US-E00-05 | Kho sự kiện | Could |

---

### US-E00-01 — Đăng nhập / xác thực
- **Epic:** E00 — Platform Shell
- **Vai trò:** HLV + KH
- **Story:** Là HLV/KH, tôi muốn đăng nhập nhanh bằng SĐT/Email và mật khẩu (password), để vào ứng dụng trong ≤30 giây. Ứng dụng cho phép nhớ mật khẩu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given chưa đăng nhập, When mở ứng dụng, Then thấy màn welcome với 2 lựa chọn: "Đăng nhập HLV" / "Tôi là khách hàng".
  - AC2 — Given chọn đăng nhập, When nhập SĐT or Email and Password; nhập đúng → vào màn hình chính.
  - AC3 — Given đã đăng nhập, When mở lại ứng dụng, Then phiên còn hạn → vào thẳng màn hình chính (không hỏi lại).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-AUTH-01_dang_nhap.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/AUTH-01_dang_nhap.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —

---

### US-E00-02 — Shell điều hướng + floating bubble tùy biến
- **Epic:** E00 — Platform Shell
- **Vai trò:** HLV (và KH tương tự)
- **Story:** Là HLV, tôi muốn một màn hình chính có thanh điều hướng gọn + nút truy cập nhanh (floating bubble) tùy biến theo việc tôi hay làm, để mở tính năng cần trong ≤2 chạm ngay khi đang ngồi cạnh khách.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ (bubble tùy biến) · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV đã đăng nhập, When mở ứng dụng, Then thấy màn hình chính (khuôn T3) với 1 focus card "việc nổi bật hôm nay" + ≤3 lối tắt + danh sách cần chú ý.
  - AC2 — Given màn hình chính, When HLV bấm floating bubble, Then mở nhanh tính năng được cấu hình (mặc định: Tạo KH tiềm năng).
  - AC3 — Given cài đặt shell, When HLV chọn "tùy biến lối tắt", Then đổi được ≤3 lối tắt & hành vi bubble; lựa chọn được lưu theo HLV.
  - AC4 — Given KH (role khác), When mở ứng dụng, Then thấy shell phía KH (màu `--accent-customer`), không lộ chức năng HLV.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-AUTH-02_shell.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/AUTH-02_shell.html` *(chưa tạo)*
  - Khuôn màn: T3
  - Nghiệp vụ: —
- **Open question:** Floating bubble giữ 1 hành vi cố định (L5), tùy biến chỉ ở cài đặt — không đổi đích theo Stage.

---

### US-E00-03 — Đặt mục tiêu cá nhân (KH)
- **Epic:** E00 — Platform Shell
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn đặt mục tiêu sức khỏe cá nhân (giảm cân / tăng cơ / kiểm soát đường huyết…) với thời gian mong muốn, để có lộ trình phù hợp và biết mình cần đạt gì.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH vào mục tiêu, When chọn mục tiêu + thời gian, Then hệ thống gợi ý mức khả thi (dựa tốc độ an toàn) & hiển thị nhãn ngôn ngữ ("Khả thi" / "Tham vọng").
  - AC2 — Given đã đặt mục tiêu, When xem trang chủ, Then focus card hiển thị tiến độ mục tiêu hiện tại.
  - AC3 — Given muốn đổi mục tiêu, When KH chọn "đổi mục tiêu", Then cập nhật & lưu lịch sử mục tiêu cũ.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-03_dat_muc_tieu.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-03_dat_muc_tieu.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (tốc độ an toàn).
- **Open question:** Mục tiêu do KH tự đặt hay chỉ xác nhận gợi ý từ HLV (luồng tư vấn US-E02-04)?

---

### US-E00-04 — Đặt mục tiêu kinh doanh (HLV)
- **Epic:** E00 — Platform Shell
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn đặt mục tiêu kinh doanh (số KH mới / doanh thu / số thành viên mới), để theo dõi tiến độ theo tuần/tháng và biết mình cần đẩy gì.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV vào mục tiêu KD, When đặt mục tiêu tuần/tháng, Then lưu & hiển thị tiến độ trên màn tổng quan (T3).
  - AC2 — Given có mục tiêu, When hết kỳ, Then tự động tổng kết đạt/chưa đạt + gợi ý hành động điều chỉnh.
  - AC3 — Given HLV có tuyến dưới, When đặt mục tiêu tập thể, Then các thành viên thấy mục tiêu chung (không lộ số của người khác).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-AUTH-04_muc_tieu_kd.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/AUTH-04_muc_tieu_kd.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Mục tiêu KD gắn La bàn quy trình (PSM) hay tách biệt?

---

### US-E00-05 — Kho sự kiện
- **Epic:** E00 — Platform Shell
- **Vai trò:** HLV + KH
- **Story:** Là HLV/KH, tôi muốn xem kho sự kiện (HOM, training, giao lưu club) sắp tới để đăng ký tham gia, để không bỏ lỡ hoạt động cộng đồng.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given vào kho sự kiện, When xem, Then thấy danh sách (khuôn T2) sự kiện sắp tới theo thời gian, mỗi thẻ ≤2 nhãn (loại + ngày).
  - AC2 — Given sự kiện, When bấm "Tham gia", Then đăng ký & nhận nhắc trước sự kiện.
  - AC3 — Given HLV, When tạo sự kiện, Then nhập tên/thời gian/địa điểm/nhóm đối tượng & đăng cho thành viên/KH.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-AUTH-05_kho_su_kien.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/AUTH-05_kho_su_kien.html` *(chưa tạo)*
  - Khuôn màn: T2
  - Nghiệp vụ: —
- **Open question:** Sự kiện đồng bộ Google Calendar (xem định hướng Lịch 168 trong archive)?

---

## Open questions epic
- 1 shell chung HLV/KH hay 2 app tách biệt? (Feasibility: app KH React Native, app HLV nâng cấp — cần chốt.)
- Mục tiêu KH và mục tiêu kinh doanh HLV có dùng chung mô hình dữ liệu hay tách?
- Floating bubble: chốt danh sách tính năng có thể gán (Tư vấn 15p · CSKH · Đào tạo · Cộng đồng · Xử lý từ chối — feature-tree §3).
