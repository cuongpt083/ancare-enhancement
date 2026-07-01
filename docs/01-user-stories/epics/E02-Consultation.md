# E02 — Consultation 15 phút

- **Vai trò:** HLV (với khách ngồi cạnh)
- **Mục tiêu:** Số hóa buổi tư vấn 15 phút theo công thức 1-7-2-3-2 — từ cân quét chỉ số → khảo sát chân dung → bản tư vấn đồng cảm → xác định mục tiêu → xử lý từ chối/chốt gói → gợi ý bữa ăn 10 ngày → tạo tài khoản KH → disclaimer.
- **Nguồn:** feature-tree §2.2; tham chiếu `docs/99-archive/to-be/Empathy-Consultation_v1.0.md`, `Objection-Handler_v1.0.md`.

## Candidate user stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E02-01 | Cân quét / nhập chỉ số Tanita (OCR ảnh) | Must |
| US-E02-02 | Khảo sát chân dung (bệnh lý, ăn, uống, vận động, DISC, mong muốn) | Must |
| US-E02-03 | Bản tư vấn đối chiếu chuẩn (5 lớp đồng cảm) | Must |
| US-E02-04 | Xác định mục tiêu + tính % khả thi | Must |
| US-E02-05 | Xử lý từ chối / chốt gói (3–6 tháng) | Must |
| US-E02-06 | Gợi ý bữa ăn 10 ngày đầu | Must |
| US-E02-07 | Tạo tài khoản KH | Must |
| US-E02-08 | Hiển thị disclaimer "không thần dược" | Must |

## Exemplar — US-E02-03
- **Epic:** E02 — Consultation
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn một bản tư vấn tự động đối chiếu chỉ số Tanita với chuẩn WHO/Tanita, chỉ ra điểm cần cải thiện & nguy cơ theo cấu trúc đồng cảm (5 lớp), để thuyết phục khách trong khi vẫn đang ngồi cạnh họ mà không phải tự tra cứu.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (5 lớp cần chốt mẫu) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given đã nhập đủ chỉ số Tanita, When HLV bấm "Tạo bản tư vấn", Then hiển thị bản tư vấn (khuôn T1) đối chiếu chuẩn & danh sách điểm cần cải thiện; thời gian thao tác mục tiêu ≤ ~7 phút/KH.
  - AC2 — Given bản tư vấn, When xem lớp đầu (above-the-fold), Then thấy ≤3 khối (nhận định tổng + 1 điểm nổi + CTA "Xem chi tiết") — đúng L2.
  - AC3 — Given khách thuộc DISC C, When trình bày, Then *cách trình bày* chuyển sang dữ liệu chi tiết/đối chiếu chuẩn; **không** in chữ "DISC = C" ra UI (L4).
  - AC4 — Given bản tư vấn, When HLV bấm "Vì sao?" tại điểm khuyến nghị gói, Then mở lời giải thích gắn bằng chứng (chỉ ở điểm quyết tiền — L7).
  - AC5 — Given mọi trường hợp, Then disclaimer "không thần dược…" hiển thị (liên kết US-E02-08).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-CONS-03_ban_tu_van.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/CONS-03_ban_tu_van.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: `docs/00-foundation/business-rules/packaged-service-advice-v1.0.md` (chốt gói); empathy 5 lớp — chưng cất tiếp từ archive.
- **Open question:** Cấu trúc 5 lớp đồng cảm cụ thể cần chốt mẫu câu (xem `Empathy-Consultation_v1.0.md` trong archive — đưa rule tóm lược vào foundation khi chốt).

## Open questions epic
- 5 lớp đồng cảm: chốt mẫu câu + catalog chỉ số cho Lớp 2.
- Objection Handler: gắn vào bước US-E02-05 như FAB "Khách đang băn khoăn" — chốt nhánh phản đối (đắt/rẻ, phụ thuộc SP, tái béo, đa cấp, đói).
- Catalog món ăn & hệ số đơn vị cho US-E02-06 (tham khảo anh Hoàng — `[TBD]`).
