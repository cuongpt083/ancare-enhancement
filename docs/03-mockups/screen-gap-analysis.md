# Screen GAP Analysis — As-Is → To-Be → GAP cho từng màn

> **Mục đích:** Mô tả song song **hiện trạng app (As-Is)** + **màn mong muốn (To-Be)** + **GAP cần xử lý**, để team dev biết chính xác cái gì **kế thừa** (giữ), cái gì **sửa/thêm/xóa**.
> **Nguồn As-Is:** screenshots + phân tích UX trong `docs/99-archive/as-is/` (13 màn HLV `screenshots-hlv/`, 9 màn KH `screenshots-kh/`, `ui_ux_analysis_hlv.md`, `ui_ux_analysis_kh.md`).
> **Nguồn To-Be:** mockup wireframe trong `docs/03-mockups/<role>/S-*.html`.
> **Quy trình:** AI chưng cất sẵn As-Is + To-Is → PO xác nhận + đánh GAP (cột Hành động) → AI cập nhật mockup.

## Cách đánh giá GAP (cột Hành động)

| Hành động | Ý nghĩa | Ước lượng effort |
|---|---|---|
| **KẾ THỪA** | As-Is đã ổn, giữ nguyên (không đụng) | 0 (không đổi) |
| **SỬA** | As-Is có nhưng cần đổi (nhãn/bố cục/logic) | vừa |
| **THÊM** | As-Is chưa có, To-Be cần (mới) | lớn |
| **XÓA** | As-Is có nhưng To-Be bỏ | nhỏ (gỡ) |

> Nguyên tắc: **tối đa kế thừa** — chỉ đánh SỬA/THÊM/XÓA khi thực sự cần, có lý do rõ.

---

## TEMPLATE (copy cho mỗi màn)

### S-<MODULE>-<nn>_<tên> — <tên màn>
- **Story:** US-<EXX>-<nn> · **Khuôn To-Be:** T1/T2/T3/T4 · **Role:** HLV/KH
- **Wireframe To-Be:** `<role>/S-...html`
- **As-Is screenshot:** `docs/99-archive/as-is/screenshots-<role>/<nn>_<tên>.png` (nếu có màn tương đương)
- **As-Is UX note:** tóm từ `ui_ux_analysis_<role>.md` §<n>

#### Bảng GAP
| # | Thành phần | As-Is (hiện tại) | To-Be (mong muốn) | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | <tên> | <có gì / “chưa có”> | <muốn gì> | KẾ THỪA/SỬA/THÊM/XÓA | <lý do/chi tiết> |

#### Tóm tắt GAP
- **Kế thừa:** <danh sách>
- **Cần xử lý:** <danh sách SỬA/THÊM/XÓA — đây là công việc dev>

---

## VÍ DỤ ĐIỀN SẴN — S-AUTH-02_shell (Trang chủ HLV)

### S-AUTH-02_shell — Trang chủ HLV (Shell + FAB)
- **Story:** US-E00-02 · **Khuôn To-Be:** T3 · **Role:** HLV
- **Wireframe To-Be:** `coach/S-AUTH-02_shell.html`
- **As-Is screenshot:** `docs/99-archive/as-is/screenshots-hlv/03_dashboard.png`
- **As-Is UX note:** (`ui_ux_analysis_hlv.md` §3) Hiển thị 3 KPI (KH, NPP, Doanh thu) + danh sách việc hôm nay. **Hạn chế:** KPI dày đặc 1 dòng (“0 Khách hàng — NPP 0đ Doanh thu”), bottom tab label/icon lỗi font, không có focus card nổi bật.

#### Bảng GAP
| # | Thành phần | As-Is (hiện tại) | To-Be (mong muốn) | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | AppBar lời chào | chưa có | “Xin chào, Thủy 👋” + ⚙ | THÊM | cá nhân hóa (L2) |
| 2 | KPI (KH/NPP/Doanh thu) | 1 dòng dày đặc “0 KH — NPP 0đ Doanh thu” | gom 1 hàng nhỏ, không phải 4 ô lớn | SỬA | L2/L6 — giảm nhiễu |
| 3 | Focus card “việc nổi bật hôm nay” | chưa có | “3 KH nên tiếp cận” + CTA | THÊM | cốt lõi T3 (L2) |
| 4 | Danh sách việc hôm nay | có (vd “KH 02: Cập nhật Tanita”) | chuyển thành “Cần chú ý” (≤3 thẻ, chip trạng thái) | SỬA | gắn chip good/warn/alert |
| 5 | Lối tắt nhanh (≤3) | chưa có | KH tiềm năng · Tư vấn 15p · Chăm sóc KH | THÊM | quick-row |
| 6 | Floating bubble (FAB) | chưa có | nút + (mặc định: Tạo KH tiềm năng) | THÊM | D01/D10 — tùy biến |
| 7 | Bottom nav (5 tab) | có: Trang Chủ/Team/Chat/HLV/Hồ Sơ — icon ký tự lỗi font | 4 tab + icon Tabler chuẩn | SỬA | đổi icon + gộp tab HLV vào KH tiềm năng? |
| 8 | Tông màu | xanh lá đậm #1E3322 | --accent-coach #2f6f4f (sáng hơn) | SỬA | design tokens |

#### Tóm tắt GAP — S-AUTH-02
- **Kế thừa:** bottom nav 5 tab (cấu trúc), danh sách việc hôm nay (dữ liệu/logic), KPI (dữ liệu KH/NPP/Doanh thu)
- **Cần xử lý:** THÊM focus card, FAB, lối tắt, lời chào · SỬA KPI (gom hàng nhỏ), danh sách (chip), bottom nav (icon), tông màu · (không XÓA gì lớn)

---

## DANH SÁCH 20 MÀN + MAP AS-IS TƯƠNG ĐƯƠNG

> `[x]` = đã làm GAP analysis. AI sẽ chưng cất As-Is sẵn; PO xác nhận + đánh GAP.

| To-Be màn | Story | As-Is screenshot tương đương | Trạng thái |
|---|---|---|---|
| S-AUTH-01_dang_nhap | E00-01 | screenshots-hlv/02_login.png | [ ] |
| S-AUTH-02_shell | E00-02 | screenshots-hlv/03_dashboard.png | [x] ví dụ trên |
| S-LEAD-01_danh_sach | E01-01 | screenshots-hlv/05_team.png (danh sách KH) | [ ] |
| S-LEAD-02_tao_lead | E01-02 | screenshots-hlv/06_moi_kh_moi.png | [ ] |
| S-CONS-01_pha_bang | E02-01 | (chưa có — màn mới) | [ ] |
| S-CONS-02_khao_sat | E02-02 | (chưa có — màn mới) | [ ] |
| S-CONS-03_tanita | E02-03 | screenshots-hlv/04_tanita_update.png | [ ] |
| S-CONS-04_phan_tich | E02-04 | (chưa có — màn mới, kết quả Tanita rải ở dashboard) | [ ] |
| S-CONS-05_giai_phap | E02-05 | (chưa có — màn mới) | [ ] |
| S-CONS-06_xu_ly_tu_choi | E02-06 | (chưa có — màn mới) | [ ] |
| S-CONS-07_bua_an | E02-07 | (chưa có — màn mới) | [ ] |
| S-CONS-08_tao_tk | E02-08 | screenshots-hlv/06_moi_kh_moi.png (gần) | [ ] |
| S-CARE-01_talking_point | E03-01 | (chưa có — màn mới) | [ ] |
| S-CARE-03_dieu_chinh_bua_an | E03-03 | screenshots-hlv/04_tanita_update.png (gần) | [ ] |
| S-CARE-09_nhac_72h | E03-09 | (chưa có — màn mới) | [ ] |
| S-DEV-01_microcourse | E05-01 | (chưa có — màn mới) | [ ] |
| S-HLTH-01_dong_ho_sinh_hoc | E06-01 | screenshots-kh/03_dashboard.png (chỉ số cơ thể) | [ ] |
| S-HLTH-02_trang_chu | E06-02 | screenshots-kh/03_dashboard.png | [ ] |
| S-HLTH-04_bua_an | E06-04 | (chưa có — màn mới) | [ ] |
| S-HLTH-05_chat | E06-05 | screenshots-kh/08_chat.png | [ ] |

> **Nhận xét:** ~10 màn có As-Is tương đương (kế thừa cao), ~10 màn là mới (chủ yếu THÊM). Phân bổ GAP rõ → dễ ước lượng effort & ưu tiên.

---

## QUY TRÌNH LÀM VIỆC

1. **AI chưng cất As-Is** cho từng màn (từ screenshots + ui_ux_analysis) → điền sẵn 2 cột “As-Is” + “To-Be” (từ mockup).
2. **PO xác nhận + đánh GAP**: kiểm tra As-Is đúng không, điền cột **Hành động** (KẾ THỪA/SỬA/THÊM/XÓA) + ghi chú, đánh `[x]`.
3. **AI cập nhật mockup** theo GAP (chỉ phần SỬA/THÊM), giữ nguyên phần KẾ THỪA.
4. **Kết quả**: mockup cuối = kế thừa As-Is ổn + đổi đúng GAP → team dev có spec triển khai chính xác.

> Có thể làm từng nhóm (vd “E02 trước”, “E06 sau”) — không cần làm hết 20 màn cùng lúc.
## Danh sách GAP analysis đã làm
| Nhóm | File | Trạng thái |
|---|---|---|
| E01 + E02 (Quản lý KH + Tư vấn 15p) | `gap-analysis-E01-E02.md` | ✅ xong (chờ PO chốt Q31-Q35 + cập nhật mockup) |
| E00 Shell/Auth | — | ⏳ chờ As-Is |
| E03 Customer Care | — | ⏳ chờ As-Is |
| E04 Team Ops | — | ⏳ chờ As-Is |
| E05 Self-Dev | — | ⏳ chờ As-Is |
| E06 Personal Health | `gap-analysis-E06.md` | ✅ HOÀN THIỆN (As-Is mới 10 màn từ video screen-record-KH.mp4) |
