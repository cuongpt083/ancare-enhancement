# E00 — Platform Shell

- **Vai trò:** HLV + KH (+ Founder/Admin)
- **Mục tiêu:** Nền tảng chung — xác thực, shell điều hướng, mục tiêu cá nhân/kinh doanh, kho sự kiện, màn hình chính (menu shortcut / floating bubble tùy biến).
- **Nguồn:** feature-tree — "Mục tiêu", "Kho sự kiện", "UI Main Screen".

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E00-01 | Đăng nhập / xác thực (HLV & KH) | Must |
| US-E00-02 | Shell điều hướng + floating bubble tùy biến | Must |
| US-E00-03 | Đặt mục tiêu cá nhân (KH) | Should |
| US-E00-04 | Đặt mục tiêu kinh doanh (HLV) | Should |
| US-E00-05 | Xem Kho sự kiện | Could |

## Exemplar — US-E00-02
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
- **Open question:** floating bubble có thay đổi hành vi theo Stage-of-Change? (L5 cấm đổi đích theo ngữ cảnh — cần chốt bubble = 1 hành vi cố định, tùy biến chỉ ở cài đặt.)

## Open questions epic
- Có 1 shell chung HLV/KH hay 2 app tách biệt? (Feasibility: app KH React Native, app HLV nâng cấp — cần chốt.)
- Mục tiêu KH và mục tiêu kinh doanh HLV có dùng chung mô hình dữ liệu hay tách?
