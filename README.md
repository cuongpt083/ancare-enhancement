# ancare-enhancement

Phân tích & thiết kế **AnCare DXP** — nền tảng trải nghiệm số chăm sóc sức khỏe chủ động, đồng hành quy trình kinh doanh 12 bước của Nutrition Club (Herbalife).

> Tầm nhìn/sứ mệnh/giá trị cốt lõi đầy đủ: [`docs/00-foundation/vision-and-values.md`](docs/00-foundation/vision-and-values.md).

---

## ⚡ Trạng thái: đã khởi động lại (restart baseline)

Repo từng bị phân mảnh sau nhiều lần chỉnh sửa (trùng phiên bản, trùng định dạng .md/.docx, prototype rải nhiều thư mục, UI-UX trộn lẫn). Ngày **2026-07-01** đã thực hiện chiến lược **Lưu trữ & Tái lập nền**:

- **Commit đóng băng**: `47905ed` — toàn bộ hiện trạng dời vào `docs/99-archive/` (git rename, bảo toàn lịch sử).
- **Nền móng mới** dựng theo pipeline: **User Stories → Design System → Mockups → Prototypes**, có truy vết xuyên suốt *Persona → Epic → Story → Screen → Prototype*.

## Cấu trúc tài liệu

| Thư mục | Vai trò | Trạng thái |
|---|---|---|
| `docs/00-foundation/` | **Nguồn sự thật duy nhất**: tầm nhìn, personas, glossary, cây chức năng, business-rules. | ✅ chưng cất xong |
| `docs/01-user-stories/` | User stories theo epic (E00–E06), mỗi epic có 1 exemplar story đầy đủ AC. | ✅ sườn + exemplar |
| `docs/02-design-system/` | UI-UX system: 7 nguyên tắc Lean, design tokens, 4 khuôn màn (T1–T4), voice & tone, components. | ✅ sườn |
| `docs/03-mockups/` | Mockup từng màn (gắn user story + khuôn). | 🔜 sẵn sàng làm |
| `docs/04-prototypes/` | Prototype HTML tương tác (gắn mockup). | 🔜 sẵn sàng làm |
| `docs/99-archive/` | Hiện trạng trước restart — **chỉ đọc**, tham chiếu. | 🧊 đóng băng |

## Pipeline thiết kế (thứ tự làm)

1. **Foundation** — đã chưng cất (mỗi khái niệm 1 phiên bản).
2. **User Stories** — đã có sườn 7 epic + exemplar; tiếp tục viết đầy đủ story theo định dạng trong `docs/01-user-stories/README.md`.
3. **Design System** — đã có; bổ sung component khi mockup tiến triển.
4. **Mockups** — mỗi user story → 1 mockup theo khuôn T1–T4 (xem `docs/03-mockups/README.md`).
5. **Prototypes** — chuyển mockup → HTML tương tác, nối điều hướng (xem `docs/04-prototypes/README.md`).

**Cổng kiểm tra (gate)** sau mỗi giai đoạn: review chéo để giữ nhất quán.

## Quy ước
- Ngôn ngữ: tiếng Việt. Định dạng: Markdown.
- Một khái niệm = một phiên bản (sửa tại foundation, không tạo bản song song).
- Tầng 01–04 tham chiếu foundation, không định nghĩa lại.
- `node_modules/` đang bị git theo dõi (playwright) — TODO dọn dẹp (`git rm -r --cached node_modules` + thêm `.gitignore`).
