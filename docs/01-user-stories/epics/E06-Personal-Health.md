# E06 — Personal Health (Trải nghiệm KH · Thân–Tâm–Trí)

- **Vai trò:** KH (+ HLV làm gương)
- **Mục tiêu:** Trải nghiệm sống khỏe phía KH theo Thân–Tâm–Trí — trang chủ cá nhân hóa, "Sức khỏe tổng thể" (đồng hồ sinh học), cá nhân hóa thời gian biểu, gợi ý bữa ăn, chat HLV, chia sẻ. HLV cũng tự thực hiện lộ trình & chia sẻ.
- **Nguồn:** feature-tree §2.6 + trải nghiệm KH (README §A).

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E06-01 | Check-in đồng hồ sinh học 24h | Must |
| US-E06-02 | Trang chủ cá nhân hóa (% hoàn thành, tổng kết cuối ngày) | Must |
| US-E06-03 | Cá nhân hóa thời gian biểu (số bữa, giờ hoạt động) | Should |
| US-E06-04 | Gợi ý bữa ăn cá nhân hóa (3 nhóm + chụp ảnh AI) | Must |
| US-E06-05 | Chat với HLV | Must |
| US-E06-06 | Chia sẻ tiến bộ / truyền cảm hứng | Should |
| US-E06-07 | Xem kết quả cân quét & báo cáo hành trình | Should |
| US-E06-08 | Nhật ký infographic | Could |

## Exemplar — US-E06-01
- **Epic:** E06 — Personal Health
- **Vai trò:** KH
- **Story:** Là KH, tôi muốn check-in từng nhiệm vụ trên đồng hồ sinh học 24h và được chấm điểm theo độ đúng giờ, để giữ nhịp sinh học & tích lũy streak phần thưởng.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given KH mở màn "Sức khỏe tổng thể", When xem, Then thấy vòng tròn 24h chia múi theo hoạt động, tô màu trạng thái (khuôn T3, focus card là đồng hồ).
  - AC2 — Given đến giờ nhiệm vụ, When KH bấm check-in, Then chấm điểm theo độ đúng giờ (3/2/1/0) — nền tảng streak & credit thưởng.
  - AC3 — Given nhiệm vụ "uống nước", When KH ghi nhận nhiều lần, Then mỗi cốc ~250ml cộng dồn; hiển thị tiến độ nước/ngày.
  - AC4 — Given danh sách nhiệm vụ, When xem, Then chia 2 vùng "đã thực hiện" / "chờ thực hiện" để tạo động lực.
- **Truy vết:**
  - Mockup: `docs/03-mockups/customer/S-HLTH-01_dong_ho_sinh_hoc.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/customer/HLTH-01_dong_ho_sinh_hoc.html` *(chưa tạo)*
  - Khuôn màn: T3 (widget trung tâm)
  - Nghiệp vụ: `docs/00-foundation/business-rules/Calorie-Meal-Business-Rules-v1.1.md` (nước ≥ 0,4 L/10kg).
- **Open question:** Đồng hồ sinh học có tham chiếu case study Huawei Health Clover (trong archive) — chưng cất quy tắc tô màu/quản gia ảo khi chốt.

## Open questions epic
- Cơ chế streak & credit thưởng (gamification) cần đặc tả business-rule.
- Ảnh trước–sau / testimonial cho tông giọng I (DISC) — kho nội dung cần xây.
