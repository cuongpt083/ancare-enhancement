# GAP Analysis — E04 Team Operations (HLV quản lý Team & KH tiềm năng)

> **As-Is:** `docs/00-foundation/as-is-current/as-is-notes.md` §1.2 + 4 screenshots-hlv (09-12: Team KH của tôi, KH tiềm năng empty, KH tiềm năng list, Chi tiết KH HLV view).
> **To-Be:** `docs/03-mockups/draft-requirements-hlv.md` §2.1-2.3 (Team: tabs KHTN/KH + Summary RFM + Danh sách) + E04 stories (US-E04-01/02/03).
> **Phương pháp:** As-Is → To-Be → Hành động.

## 1. So sánh luồng

### As-Is (4 màn từ video screen-record-hlv-teams.mp4)
```
Trang chủ HLV → [tab Team] Màn 09 KH của tôi (KPI 5/Active 0/At Risk 0 + thẻ KH: tên/Day 0/streak/Reorder/check-in gần đây/Nurturing) → [tab KH tiềm năng] Màn 10 empty → [có lead] Màn 11 list (filter Tất cả/Nóng/Ấm/Lạnh/Cần theo dõi + thẻ lead + "Tiếp tục làm ấm") → [chọn KH] Màn 12 Chi tiết KH HLV (HH hạn + streak/rings/BMI + mục tiêu Giảm cân + calo + bảng chỉ số 8 + báo cáo trống + nút Tạo báo cáo)
```
> Đặc điểm As-Is E04:
- **Đã có tabs** KH tiềm năng / KH của tôi (đúng To-Be §2.1-2.2!).
- **Đã có KPI tóm tắt** (5 KH / Active 0 / At Risk 0) — gần Card Summary RFM To-Be.
- **Đã có filter KHTN theo nhiệt độ** (Nóng/Ấm/Lạnh/Cần theo dõi) — khác RFM (Tích cực/Có nguy cơ/Kém quan tâm) nhưng cùng ý.
- **Đã có thẻ KH**: tên/Day streak/Reorder/check-in gần đây/Nurturing.
- **Đã có Chi tiết KH HLV** (Màn 12): hạn gói + chỉ số 8 + mục tiêu + calo + nút Tạo báo cáo.
- **Hạn chế**: nhãn tiếng Anh "Nurturing"/"At Risk" chưa Việt hóa; KHTN filter nhiệt độ ≠ RFM trạng thái; báo cáo trống trùng lặp; thiếu gợi ý DMO/bước tiếp (US-E04-02); chưa có đào tạo thành viên (US-E04-03).

### To-Be (draft §2.1-2.3 + E04 stories)
```
[tab Team] tabs KHTN (default) / KH của tôi → KH của tôi: Card Summary RFM (filter Tên+RFM, thống kê 3 trạng thái+màu) + Card Danh sách (Tên/Gói+tiến độ+thời gian còn lại/Nhóm KH) → [thẻ] Chi tiết KH (T4) + gợi ý DMO club bước tiếp (US-E04-02) + đào tạo (US-E04-03)
```

### Chênh lệch (NHỎ — As-Is đã có nhiều)
- As-Is đã có tabs + KPI + filter + thẻ + chi tiết → **kế thừa cao**.
- Khác: KPI At Risk → RFM 3 trạng thái (Tích cực/Có nguy cơ/Kém quan tâm) + màu; filter Nóng/Ấm/Lạnh → RFM; thiếu gợi ý DMO/bước tiếp + đào tạo thành viên.

---

## 2. GAP từng màn

### 2.1 Team — KH của tôi — To-Be §2.3 ↔ As-Is Màn 09
- **As-Is:** tabs KHTN/KH; KPI 5/Active 0/At Risk 0 (đỏ nhạt); filter "Tất cả" + tìm tên; thẻ KH (tên/Day 0/streak 0 days/Reorder 0x/check-in gần đây/Nurturing vàng).
- **To-Be:** Card Summary RFM (filter Tên+Trạng thái RFM; thống kê 3 trạng thái + màu xanh/vàng/đỏ) + Card Danh sách (Tên + Gói/tiến độ/thời gian còn lại + Nhóm KH màu).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Tabs KHTN / KH của tôi | có | có (default KHTN) | KẾ THỪA | |
| 2 | KPI tóm tắt (số KH) | có (5/Active 0/At Risk 0) | 3 trạng thái RFM + màu | SỬA | RFM thay Active/At Risk |
| 3 | Filter | "Tất cả" + tìm tên | filter Tên + Trạng thái RFM | SỬA | thêm filter RFM |
| 4 | Thẻ KH | tên/Day/streak/Reorder/check-in/Nurturing | Tên + Gói+tiến độ+thời gian còn lại + Nhóm KH màu | SỬA | enrich (gói+tiến độ+nhóm) |
| 5 | Nhãn tiếng Anh | "Nurturing"/"At Risk" | Việt hóa (Đang chăm sóc/Có nguy cơ) | SỬA | |
| 6 | FAB thêm mới | có (+) | có | KẾ THỪA | |

**Tóm tắt:** KẾ THỪA (tabs, FAB, KPI cấu trúc, filter, thẻ) · SỬA (KPI→RFM 3 trạng thái+màu, filter+RFM, thẻ+gói/tiến độ/nhóm, Việt hóa).

---

### 2.2 KHTN — To-Be §2.1-2.2 ↔ As-Is Màn 10+11 (empty + list)
- **As-Is:** Màn 10 empty ("Chưa có KH" + nút thêm); Màn 11 list (filter Nóng/Ấm/Lạnh/Cần theo dõi + thẻ lead "Testkhtn01" + "lead 0" + "Tiếp tục làm ấm").
- **To-Be:** tab KHTN (default) + filter RFM + thẻ lead (≤2 nhãn, DISC/Stage chi tiết T4).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Empty state | có (rõ ràng) | có | KẾ THỪA | |
| 2 | Filter nhiệt độ (Nóng/Ấm/Lạnh/Cần theo dõi) | có | RFM trạng thái (Tích cực/Có nguy cơ/Kém quan tâm)? | SỬA? | ⏳ PO: giữ nhiệt độ hay đổi RFM? |
| 3 | Thẻ lead + gợi ý hành động ("Tiếp tục làm ấm") | có | có + ≤2 nhãn | KẾ THỪA+SỬA | |
| 4 | Bấm thẻ → chi tiết/cập nhật | có | → chi tiết lead (T4) | KẾ THỪA | |

**Tóm tắt:** KẾ THỪA (empty, thẻ, gợi ý hành động, bấm→chi tiết) · SỬA (filter nhiệt độ → RFM? ⏳ PO).

---

### 2.3 Chi tiết KH HLV view — To-Be US-E04-02 ↔ As-Is Màn 12
- **As-Is:** tên + HH hạn + streak/rings/BMI + mục tiêu Giảm cân + calo 1988 + bảng chỉ số 8 (02/07) + báo cáo trống + nút Tạo báo cáo.
- **To-Be:** T4 header + hành động nhanh ≤3 + gợi ý DMO club bước tiếp (US-E04-02) + đào tạo (US-E04-03).

| # | Thành phần | As-Is | To-Be | Hành động | Ghi chú |
|---|---|---|---|---|---|
| 1 | Header KH + hạn gói | có (HH 02/10/2026) | có | KẾ THỪA | |
| 2 | Chỉ số tổng quan (streak/rings/BMI) | có | có | KẾ THỪA | |
| 3 | Mục tiêu + calo | có (Giảm cân + 1988) | có | KẾ THỪA | |
| 4 | Bảng chỉ số 8 | có (02/07) | có (gập, T4) | KẾ THỪA+SỬA | gập |
| 5 | Gợi ý DMO club bước tiếp | KHÔNG | có (US-E04-02) | THÊM | D21 placeholder |
| 6 | Gợi ý nhóm Dinh dưỡng/Fit club | KHÔNG | có | THÊM | D21 |
| 7 | Báo cáo (gần đây + tiến trình) | có (trống, trùng lặp) | có (gom nhóm) | SỬA | tối ưu |
| 8 | Nút Tạo báo cáo | có | có | KẾ THỪA | |
| 9 | Đào tạo thành viên (US-E04-03) | KHÔNG | có | THÊM | Could |
| 10 | Hành động nhanh ≤3 (Gọi/Nhắn/Gặp 2-1) | KHÔNG rõ | có (T4) | THÊM | |

**Tóm tắt:** KẾ THỪA (header, chỉ số, mục tiêu, bảng 8, nút Tạo báo cáo) · SỬA (bảng gập, báo cáo gom nhóm) · THÊM (gợi ý DMO/bước tiếp D21, nhóm club, đào tạo thành viên, hành động nhanh).

---

## 3. Tổng hợp GAP (E04)

### KẾ THỪA (rất nhiều — As-Is đã khớp To-Be)
- Tabs KHTN / KH của tôi.
- KPI tóm tắt (số KH/Active/At Risk).
- FAB thêm mới.
- Filter + tìm tên.
- Thẻ KH (tên/streak/check-in/trạng thái).
- KHTN empty state + filter nhiệt độ + thẻ lead + gợi ý "Tiếp tục làm ấm".
- Chi tiết KH HLV: header + hạn gói + chỉ số + mục tiêu + calo + bảng 8 + nút Tạo báo cáo.

### SỬA
- KPI At Risk → RFM 3 trạng thái (Tích cực/Có nguy cơ/Kém quan tâm) + màu xanh/vàng/đỏ.
- Filter KHTN: Nóng/Ấm/Lạnh → RFM? (⏳ PO).
- Thẻ KH: + Gói/tiến độ/thời gian còn lại + Nhóm KH màu.
- Việt hóa nhãn (Nurturing/At Risk).
- Chi tiết KH: bảng gập (T4), báo cáo gom nhóm (không trùng lặp).

### THÊM (nhỏ)
- Gợi ý DMO club bước tiếp + nhóm Dinh dưỡng/Fit club (US-E04-02, D21 placeholder).
- Đào tạo thành viên (US-E04-03, Could).
- Hành động nhanh ≤3 (Gọi/Nhắn/Gặp 2-1) trong Chi tiết KH.

### XÓA
- (không)

---

## 4. Reconciliation

| # | Lệch | Hiện tại | As-Is | Hành động |
|---|---|---|---|---|
| R1 | KPI RFM vs Active/At Risk | US-E04-01 RFM | As-Is Active/At Risk | ✅ SỬA: RFM 3 trạng thái + màu (Q31) |
| R2 | Filter KHTN nhiệt độ vs RFM | US-E01-01 RFM | As-Is Nóng/Ấm/Lạnh | ⏳ PO: giữ nhiệt độ hay đổi RFM? |
| R3 | Gợi ý DMO (US-E04-02) | chưa mockup | As-Is KHÔNG | ✅ THÊM (D21 placeholder) |
| R4 | Đào tạo thành viên (US-E04-03) | chưa mockup | As-Is KHÔNG | ⏳ Could, làm sau |
| R5 | Thẻ KH + gói/tiến độ/nhóm | US-E04-01 | As-Is thiếu | ✅ SỬA enrich |
| R6 | Chi tiết KH mockup | chưa có | As-Is Màn 12 | ⏳ TODO mockup (kế thừa Màn 12) |

> **Insight:** E04 kế thừa RẤT cao (As-Is đã có tabs+KPI+filter+thẻ+chi tiết). GAP nhỏ — chủ yếu SỬA (RFM, Việt hóa) + THÊM gợi ý DMO. US-E04-01 gần như KẾ THỪA toàn bộ.
