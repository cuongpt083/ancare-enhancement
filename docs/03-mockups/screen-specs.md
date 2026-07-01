# Screen Specs — Mô tả trường thông tin từng màn (để điều chỉnh mockup)

> **Mục đích:** File duy nhất để bạn mô tả chính xác các trường thông tin hiển thị trên mỗi màn, và chỉ rõ thay đổi mong muốn. Tôi sẽ đọc file này để sửa mockup HTML tương ứng.
> **Cách dùng:** Mỗi màn = 1 mục `###`. Copy template §0, điền vào. Chỉ cần điền cột **“Thay đổi mong muốn”** (cột khác đã có sẵn cấu trúc hiện tại — bạn có thể sửa luôn). Càng cụ thể (nhãn mới / ẩn-hiện / vị trí / nguồn dữ liệu) tôi sửa càng chuẩn.
> **Quy ước vị trí:** `above-fold` (thấy ngay khi mở) · `below` (cuộn xuống) · `hidden` (gập, bấm mới mở) · `footer` (CTA chân màn).
> **Quy ước loại:** `text` · `number` · `chip` (nhãn) · `btn` (nút) · `image` · `list` · `progress` · `chart`.

---

## 0. TEMPLATE (copy để điền cho mỗi màn)

### S-<MODULE>-<nn>_<tên> — <tên hiển thị>
- **Story:** US-<EXX>-<nn> · **Khuôn:** T1/T2/T3/T4 · **Role:** HLV/KH
- **Wireframe:** `coach/S-...html` hoặc `customer/S-...html`

| # | Trường | Vị trí | Loại | Nguồn dữ liệu | Hiện? | Thay đổi mong muốn |
|---|---|---|---|---|---|---|
| 1 | <tên/nhãn> | above-fold | text | <TBD/api/HLV nhập/KH nhập/động> | ✅ | <ghi rõ: đổi nhãn / ẩn / thêm / đổi vị trí / đổi nguồn…> |
| 2 | ... | | | | | |

**Ghi chú bố cục (nếu cấu trúc thay đổi):**
- <vd: tách màn thành 2 bước / gộp card / đổi CTA...>

---

## 1. DANH SÁCH MÀN CẦN ĐIỂN (20 màn Must P0)

> Đánh dấu `[x]` khi đã điền xong. Tôi sẽ chỉ sửa những màn đã đánh dấu `[x]`.

### [ ] S-AUTH-01_dang_nhap — Đăng nhập (US-E00-01, T1, HLV+KH)
### [ ] S-AUTH-02_shell — Shell HLV (US-E00-02, T3, HLV)
### [ ] S-LEAD-01_danh_sach — DS KHTN (US-E01-01, T2, HLV)
### [ ] S-LEAD-02_tao_lead — Tạo lead (US-E01-02, T1, HLV)
### [ ] S-CONS-01_pha_bang — Phá băng (US-E02-01, T1, HLV)
### [ ] S-CONS-02_khao_sat — Khảo sát (US-E02-02, T1, HLV)
### [ ] S-CONS-03_tanita — Đo Tanita (US-E02-03, T1, HLV)
### [x] S-CONS-04_phan_tich — Phân tích & Cảnh báo (US-E02-04, T1, HLV) ← VÍ DỤ ĐIỀN SẴN bên dưới
### [ ] S-CONS-05_giai_phap — Tư vấn giải pháp (US-E02-05, T1, HLV)
### [ ] S-CONS-06_xu_ly_tu_choi — Xử lý từ chối/Chốt gói (US-E02-06, T1, HLV)
### [ ] S-CONS-07_bua_an — Gợi ý bữa ăn (US-E02-07, T1, HLV)
### [ ] S-CONS-08_tao_tk — Tạo tài khoản KH (US-E02-08, T1, HLV)
### [ ] S-CARE-01_talking_point — Talking point (US-E03-01, T1, HLV)
### [ ] S-CARE-03_dieu_chinh_bua_an — Điều chỉnh bữa ăn (US-E03-03, T1, HLV)
### [ ] S-CARE-09_nhac_72h — Nhắc 72h (US-E03-09, T1, HLV)
### [ ] S-DEV-01_microcourse — Micro-course (US-E05-01, T1, KH+HLV)
### [ ] S-HLTH-01_dong_ho_sinh_hoc — Đồng hồ sinh học (US-E06-01, T3, KH)
### [ ] S-HLTH-02_trang_chu — Trang chủ KH (US-E06-02, T3, KH)
### [ ] S-HLTH-04_bua_an — Bữa ăn KH (US-E06-04, T1, KH)
### [ ] S-HLTH-05_chat — Chat KH (US-E06-05, T1, KH)

---

## 2. VÍ DỤ ĐIỀN SẴN (S-CONS-04 — để bạn thấy cách điền)

### S-CONS-04_phan_tich — Phân tích chỉ số & Cảnh báo
- **Story:** US-E02-04 · **Khuôn:** T1 · **Role:** HLV
- **Wireframe:** `coach/S-CONS-04_phan_tich.html`

| # | Trường | Vị trí | Loại | Nguồn dữ liệu | Hiện? | Thay đổi mong muốn |
|---|---|---|---|---|---|---|
| 1 | AppBar “Bản phân tích” | top | text | tĩnh | ✅ | (giữ) |
| 2 | Progress dots (5 chấm) | top | progress | động | ✅ | (giữ) |
| 3 | Focus card “Nhận định tổng: Thừa 1.4% mỡ · mỡ nội tạng cao” | above-fold | card | động (sinh từ Tanita) | ✅ | **Đổi nội dung → chỉ “Thừa 1.4% mỡ” (bỏ “mỡ nội tạng cao” khỏi focus, để vào card cảnh báo)** |
| 4 | Bước 1 · Cân nặng 64.8kg, Mỡ 18.9%, kg mỡ 12.2 | below | text+number | Tanita (động) | ✅ | **Thêm trường “BMI 23.7”** |
| 5 | Bước 2 · chip warn “Thừa 1.4% mỡ” + lý tưởng 17.5% | below | chip+text | động vs Body-Composition-Standards | ✅ | (giữ) |
| 6 | Bước 3 · Hai loại mỡ (dưới da / nội tạng) | below | text | tĩnh (giáo dục) | ✅ | **Ẩn mặc định → chuyển vào “Xem chi tiết”** |
| 7 | Bước 4 · Chiều cao + cân lý tưởng + hỏi KH | below | text | động | ✅ | **Thêm input “Cân mong muốn” để KH nhập** |
| 8 | Bước 5 · chip accent “Giảm cân” + 64.8→62 | below | chip+text | động | ✅ | (giữ) |
| 9 | Card cảnh báo mỡ nội tạng = 10 (ngưỡng 1-7) + hậu quả | below | card alert | động | ✅ | **Thêm nút “Ghi câu hỏi triệu chứng” (tê bì/mỏi cổ/đau lưng)** |
| 10 | Nước 57.7% + chip good + công thức 2.6 lít | below | chip+text | động | ✅ | (giữ) |
| 11 | Tuổi sinh học 37 + chip good “Trẻ hơn 5 tuổi” | below | chip+text | động | ✅ | (giữ) |
| 12 | “Vì sao?” affordance | below | btn | động | ✅ | (giữ) |
| 13 | Disclaimer “không thần dược…” | footer | text | tĩnh | ✅ | (giữ, inline — D11) |
| 14 | CTA “Tư vấn giải pháp →” | footer | btn | tĩnh | ✅ | (giữ) |

**Ghi chú bố cục:**
- Bước 3 (hai loại mỡ) nên gập vào “Xem chi tiết” để màn nhẹ hơn (L2).
- Có thể tách cảnh báo mỡ nội tạng thành focus card thứ 2 nếu muốn nổi bật hơn.

---

## 3. CÁCH ĐIỀN TỐI ƯU (để tôi sửa chuẩn)

1. **Mỗi trường = 1 dòng** trong bảng. Tên trường = nhãn/ nội dung bạn thấy trên màn.
2. **Cột “Thay đổi mong muốn”** là quan trọng nhất. Ghi cụ thể, ví dụ:
   - `Đổi nhãn “Khả thi” → “Đạt được”`
   - `Ẩn trường này (chuyển vào “Xem chi tiết”)`
   - `Thêm trường “Số ngày còn lại” (động, từ mốc 10 ngày)`
   - `Đổi vị trí: lên above-fold`
   - `Xóa hoàn toàn`
   - `(giữ)` nếu không thay đổi
3. **Nguồn dữ liệu** giúp tôi biết dữ liệu từ đâu tới: `tĩnh` (cố định) / `HLV nhập` / `KH nhập` / `động` (tính từ chỉ số/API) / `TBD`.
4. **Ghi chú bố cục** ở cuối mỗi mục — cho thay đổi cấu trúc (tách/gộp màn, đổi CTA, thêm bước).
5. Đánh dấu `[x]` ở danh sách §1 khi xong — tôi sẽ chỉ sửa màn đã đánh dấu.
6. Không cần điền tất cả 20 màn cùng lúc — có thể gửi từng nhóm (vd “E02 trước”), tôi sửa từng批.
