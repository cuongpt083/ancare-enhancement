# E03 — Customer Care

- **Vai trò:** HLV
- **Mục tiêu:** Chăm sóc KH sau chuyển đổi — 21 talking point + chuyên sâu bệnh lý, kỹ năng sống/mềm, điều chỉnh bữa ăn theo mốc trải nghiệm, nhắc tặng quà theo tuần, phân tích sức khỏe hằng ngày, cộng đồng/sự kiện, báo cáo hành trình, nhật ký infographic, nhắc kết nối 72h.
- **Nguồn:** feature-tree §2.3.

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E03-01 | Gửi talking point hằng ngày | Must |
| US-E03-02 | Kiểm tra kiến thức KH (2 câu hỏi) | Should |
| US-E03-03 | Điều chỉnh gợi ý bữa ăn theo mốc trải nghiệm | Must |
| US-E03-04 | Nhắc tặng quà theo tuần (theo nhu cầu) | Should |
| US-E03-05 | Phân tích sức khỏe hằng ngày + tư vấn nâng cấp SP | Should |
| US-E03-06 | Giao lưu cộng đồng / gợi ý sự kiện | Could |
| US-E03-07 | Báo cáo hành trình thay đổi (thể chất, tinh thần, thói quen) | Should |
| US-E03-08 | Hỗ trợ KH tạo Nhật ký infographic | Could |
| US-E03-09 | Nhắc kết nối KH sau 72h | Must |

## Exemplar — US-E03-01
- **Epic:** E03 — Customer Care
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn mỗi ngày nhận sẵn 1 talking point dinh dưỡng kèm kiến thức & gợi ý giới thiệu sản phẩm phù hợp với giai đoạn của KH, để chăm sóc nhất quán mà không phải tự nhớ 21 bài.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (catalog 21 bài) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có KH đang active, When đến lượt chăm sóc, Then HLV thấy talking point hôm nay (khuôn T1) với 1 khối nội dung + CTA "Gửi cho KH".
  - AC2 — Given talking point đã gửi, When KH đọc, Then KH thấy 2 câu hỏi kiểm tra: *"Hôm nay bạn ấn tượng nhất điều gì?"* và *"Bạn sẽ chia sẻ cho ai?"*.
  - AC3 — Given KH trả lời, When HLV xem, Then câu trả lời lưu vào hồ sơ KH (T4) làm bằng chứng hành trình.
  - AC4 — Given không có KH active, When mở màn, Then trạng thái rỗng kèm gợi ý tạo KH.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CARE-01_talking_point.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CARE-01_talking_point.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: catalog 21 talking point — cần đặc tả (Open question).
- **Open question:** Catalog 21 talking point + chủ đề chuyên sâu bệnh lý cần đưa vào `docs/00-foundation/business-rules/`.

## Open questions epic
- Cơ chế chọn talking point theo giai đoạn KH (Stage-of-Change) hay theo tuần cố định?
- Nhắc 72h: tự động hay HLV xác nhận?
