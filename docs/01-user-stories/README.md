# 01 — User Stories

Tầng **User Stories** — khởi đầu của pipeline thiết kế lại. Mỗi story truy vết: **Persona → Epic → Story → Mockup → Prototype**.

## Định dạng mỗi User Story

```markdown
### US-<EPIC>-<nn> — <tên ngắn>
- **Epic:** E0x — <tên epic>
- **Vai trò:** HLV / KH / Founder
- **Story:** Là <vai>, tôi muốn <hành động>, để <lợi ích>.
- **Ưu tiên:** Must / Should / Could  (tương đương P0 / P1 / P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given <bối cảnh>, When <hành động>, Then <kết quả>.
  - AC2 — ...
- **Truy vết:**
  - Mockup: `docs/03-mockups/<role>/S-<MODULE>-<nn>_<tên>.png`
  - Prototype: `docs/04-prototypes/<role>/<MODULE>-<nn>_<tên>.html`
  - Khuôn màn: T1 / T2 / T3 / T4  (xem `docs/02-design-system/screen-templates.md`)
  - Nghiệp vụ: `docs/00-foundation/business-rules/<file>` (nếu liên quan)
- **Ghi chú / Open question:** ...
```

## Quy ước ID

- **Epic**: `E00` … `E06` (xem bảng dưới).
- **Story**: `US-<EPIC>-<nn>` (vd `US-E02-03`).
- **Module code** (cho mockup/prototype): `AUTH · LEAD · CONS · CARE · TEAM · DEV · HLTH`.

## Danh sách Epic

| Epic | Tên | Vai trò | Nguồn (feature-tree) |
|---|---|---|---|
| **E00** | Platform Shell (xác thực, shell, mục tiêu, sự kiện) | HLV + KH | "Mục tiêu", "Kho sự kiện", "UI Main Screen" |
| **E01** | Lead Management (DS KHTN, làm rõ chân dung, mời 2-1) | HLV | §2.1 |
| **E02** | Consultation 15 phút (cân, khảo sát, tư vấn, chốt gói, bữa ăn, tài khoản) | HLV | §2.2 |
| **E03** | Customer Care (21 talking point, chăm sóc, báo cáo, infographic) | HLV | §2.3 |
| **E04** | Team Operations (DS thành viên, DMO club, đào tạo TV) | HLV | §2.4 |
| **E05** | Self-Development (sơ đồ trả thưởng, đào tạo KD/tâm thế/SP) | HLV + KH | §2.5 |
| **E06** | Personal Health (sức khỏe tổng thể, đồng hồ sinh học, bữa ăn, chat) | KH (+ HLV làm gương) | §2.6 + trải nghiệm KH (Thân–Tâm–Trí) |

## Definition of Ready (DoR)
Story sẵn sàng khi: có vai trò + lợi ích rõ; ≥1 AC dạng Given/When/Then; đã gán epic + ưu tiên; INVEST đạt ≥5/6.

## Definition of Done (DoD)
Story hoàn tất khi: có mockup tuân khuôn + prototype nối điều hướng + AC kiểm thử được + truy vết đầy đủ.

## Cách làm việc
1. Mở file epic trong `epics/` → thêm/sửa story theo định dạng trên.
2. Mỗi epic có sẵn **1 exemplar story đầy đủ AC** làm khuôn mẫu — copy định dạng đó cho story mới.
3. Khi chuyển sang tầng mockup, cập nhật trường **Truy vết** ở story.
