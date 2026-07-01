# E05 — Self-Development

- **Vai trò:** HLV + KH
- **Mục tiêu:** Phát triển bản thân — sơ đồ trả thưởng, đào tạo kinh doanh/tâm thế/sản phẩm/mạng lưới/thấu hiểu, 3 câu hỏi trước & sau khi học (micro-course).
- **Nguồn:** feature-tree §2.5; gắn Module Đào tạo (README §3).

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E05-01 | Học 1 micro-course (3 câu hỏi trước/sau) | Must |
| US-E05-02 | Xem sơ đồ trả thưởng | Should |
| US-E05-03 | Gợi ý khóa học cá nhân hóa | Should |
| US-E05-04 | Theo dõi lộ trình đào tạo (điều kiện + chứng nhận) | Could |

## Exemplar — US-E05-01
- **Epic:** E05 — Self-Development
- **Vai trò:** KH (và HLV)
- **Story:** Là người học, tôi muốn học 1 micro-course ngắn với 3 câu hỏi định hướng trước & 3 câu phản tỉnh sau, để nắm được điều đáng nhớ & việc sẽ áp dụng.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given người học mở micro-course, When bắt đầu, Then hiện 3 câu hỏi trước học (mục tiêu/ky vọng/câu hỏi mang theo).
  - AC2 — Given đã trả lời trước, When vào nội dung, Then trình bày ngắn (khuôn T1, ≤3 khối above-the-fold) + CTA "Hoàn thành".
  - AC3 — Given hoàn thành nội dung, When kết thúc, Then hiện 3 câu hỏi sau: *"Hôm nay bạn ấn tượng nhất điều gì?"*, *"Bạn sẽ chia sẻ cho ai?"*, *"Bạn sẽ áp dụng điều gì?"*.
  - AC4 — Given đã trả lời sau, When lưu, Then cập nhật lộ trình đào tạo & ghi nhận hoàn thành.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-DEV-01_microcourse.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/DEV-01_microcourse.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: Module Đào tạo micro-course — cần đặc tả catalog (Open question).
- **Open question:** Catalog micro-course + điều kiện/điều kiện tiên quyết cần đưa vào foundation.

## Open questions epic
- Gamification (điểm/streak/badge) thuộc epic này hay E06?
- Sơ đồ trả thưởng: nội dung tĩnh hay tính toán động theo tuyến dưới?
