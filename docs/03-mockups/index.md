# Mockups Index — 19 màn Must (P0)

> Mỗi mockup là wireframe HTML (mobile-first 375px), tuân khuôn T1-T4, dùng shared assets `_assets/_tokens.css` + `_assets/_base.css`.
> **Quy ước đặt tên:** `S-<MODULE>-<nn>_<tên>.html` ↔ `docs/04-prototypes/<role>/<MODULE>-<nn>_<tên>.html`.
> **Trạng thái:** wireframe (low-fi) — sẵn sàng review bố cục → hi-fi sau.

## Coach (HLV) — 15 màn
| File | Story | Khuôn | Tokens chính | AC chính |
|---|---|---|---|---|
| `S-AUTH-01_dang_nhap.html` | US-E00-01 | T1 | accent (role-based) | welcome → HLV/KH |
| `S-AUTH-02_shell.html` | US-E00-02 | T3 | accent-coach, focus-card, fab, bottom-nav | focus card + ≤3 lối tắt + cần chú ý |
| `S-LEAD-01_danh_sach.html` | US-E01-01 | T2 | list-item, chips ≤2, fab | sắp xếp ưu tiên (cờ thủ công D12), ≤2 nhãn/thẻ |
| `S-LEAD-02_tao_lead.html` | US-E01-02 | T1 | btn primary, search | tối thiểu Họ tên+SĐT, chống trùng SĐT (D15) |
| `S-CONS-02_chan_dung_kh.html` | US-E02-02 | T1 | progress-dots, search, focus-card | Card Chân dung KH: 10 câu hỏi + ô trả lời (Q35 gộp khảo sát mục tiêu) |
| `S-CONS-03_tanita.html` | US-E02-03 | T1 | progress-dots, list-item | checklist tư thế + OCR/nhập tay |
| `S-CONS-04_phan_tich.html` | US-E02-04 | T1 | focus-card, chip warn/alert, disclaimer | 5 bước + cảnh báo mỡ nội tạng (D05) |
| `S-CONS-05_giai_phap.html` | US-E02-05 | T1 | focus-card, chip good, why | logic 3 chương trình (D08) + khả thi (D09) |
| `S-CONS-06_chot_goi.html` | US-E02-06 | T1 | focus-card, disclaimer | Chốt gói đơn giản (Q34): Tạo TK / Đóng về DS KH; Objection P1+ |
| `S-CONS-07_bua_an.html` | US-E02-07 | T1 | tabs, focus-card, chip good | 10 ngày × 3 nhóm, persona-fit |
| `S-CONS-08_tao_tk.html` | US-E02-08 | T1 | focus-card, search, disclaimer | điền sẵn lead → gửi link (D04 onboarding) |
| `S-CARE-01_talking_point.html` | US-E03-01 | T1 | focus-card, btn ghost | talking point + 2 câu hỏi (D17 hybrid, D18 placeholder) |
| `S-CARE-03_dieu_chinh_bua_an.html` | US-E03-03 | T1 | focus-card, chip good | nhắc đến hạn đo lại (L4) + so sánh |
| `S-CARE-09_nhac_72h.html` | US-E03-09 | T1 | focus-card, list-item | tự động nhắc (D19) + 3 hành động |
| `S-DEV-01_microcourse.html` | US-E05-01 | T1 | accent-customer, progress-dots | 3 câu trước → nội dung → 3 câu sau |

## Customer (KH) — 4 màn
| File | Story | Khuôn | Tokens chính | AC chính |
|---|---|---|---|---|
| `S-HLTH-01_dong_ho_sinh_hoc.html` | US-E06-01 | T3 | clock (conic-gradient), chips good/warn/idle | đồng hồ 24h + điểm 3/2/1/0 (D27) + tô màu (D28) |
| `S-HLTH-02_trang_chu.html` | US-E06-02 | T3 | focus-card, chips Thân-Tâm-Trí | % hoàn thành + 3 trụ cột + cần chú ý |
| `S-HLTH-04_bua_an.html` | US-E06-04 | T1 | focus-card, btn primary | 3 nhóm + chụp ảnh AI + nhập tay |
| `S-HLTH-05_chat.html` | US-E06-05 | T1 | bubble in/out/ai | AI proactively gợi ý nhẹ (D29) + nhãn AI minh bạch |

## Notes
- **US-E02-09 (disclaimer)**: component inline, không màn riêng — hiện trong S-CONS-04, S-CONS-06, S-CONS-08 (D11 inline).
- **US-E02-01 (Phá băng) đã xóa** (Q33) — nội dung chuyển E05 đào tạo; S-CONS-01 xóa.
- **Role-based shell (D01)**: mọi màn HLV dùng `--accent-coach`; màn KH (`S-HLTH-*`, `S-DEV-01`) override `--accent: var(--accent-customer)`.
- Mở wireframe: mở file `.html` trong browser (375px viewport). Shared CSS tại `_assets/`.
