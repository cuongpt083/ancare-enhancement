# E01 — Lead Management

- **Vai trò:** HLV
- **Mục tiêu:** Số hóa Bước 1–2 quy trình 12 bước — quản lý KH tiềm năng (DSKHTN), kết nối làm rõ chân dung (chạy DMO), mời gặp 2-1 để chốt gặp HLV.
- **Nguồn:** feature-tree §2.1.

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E01-01 | Xem DS KHTN ưu tiên hôm nay | Must |
| US-E01-02 | Tạo lead mới (form định danh) | Must |
| US-E01-03 | Chạy DMO kết nối làm rõ chân dung | Should |
| US-E01-04 | Mời gặp 2-1 / đặt lịch | Should |
| US-E01-05 | Chấm điểm & sắp xếp lead (AI) | Could (P1+) |
| US-E01-06 | Chống trùng lead / import danh bạ-MXH | Could |

## Exemplar — US-E01-01
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem danh sách KH tiềm năng được sắp xếp theo "ưu tiên tiếp cận hôm nay", để biết nên gọi/nhắn ai đầu tiên mà không phải tự suy tính.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có ≥1 lead, When HLV mở màn DS KHTN, Then thấy danh sách (khuôn T2) sắp xếp theo "ưu tiên hôm nay" giảm dần (dựa `lead_score` nội bộ, **không hiện số**).
  - AC2 — Given danh sách, When xem mỗi thẻ, Then thẻ hiện tối đa **2 nhãn** quan trọng (vd "Ưu tiên hôm nay" + giai đoạn Stage); DISC/nguồn/score chi tiết nằm ở màn chi tiết (T4).
  - AC3 — Given danh sách, When HLV bấm "Xem chi tiết", Then mở màn chi tiết lead (T4) với hành động nhanh ≤3 (Gọi · Nhắn · Mời 2-1).
  - AC4 — Given không có lead, When mở màn, Then hiện trạng thái rỗng kèm CTA "Tạo KH tiềm năng".
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-01_danh_sach.png` *(xem bản tham chiếu cũ trong archive/srs/mockups)*
  - Prototype: `docs/04-prototypes/coach/LEAD-01_danh_sach.html` *(chưa tạo)*
  - Khuôn màn: T2
  - Nghiệp vụ: `docs/00-foundation/business-rules/` (chưa có rule chấm điểm — Open question)
- **Open question:** Quy tắc chấm điểm `lead_score` cần đặc tả thành business-rule trong foundation.

## Open questions epic
- Copilot làm ấm/mời (AI) thuộc P1 hay P2? (theo định hướng: P1 thư viện kịch bản + Stage-of-Change → P3 RAG.)
- Cơ chế chống trùng lead: duy nhất theo SĐT hay + mã giới thiệu?
