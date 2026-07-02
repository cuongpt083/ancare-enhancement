# Chấm điểm RFM Khách hàng — v1.0

> **Quyết định:** Q31 (PO chốt 2026-07-02). Áp dụng cho E01 (DS KH, card Summary RFM) + E03 (chăm sóc).
> **Mục đích:** phân loại KH thành 3 trạng thái (tích cực / có nguy cơ / kém quan tâm) để HLV ưu tiên chăm sóc & hiển thị màu trong card Summary.
> **Quy tắc UX:** không in điểm số ra UI (L4) — chỉ quy về nhãn ngôn ngữ + màu (xanh/vàng/đỏ).

## 1. Ba thang đo (mỗi thang 0-3 điểm)

### R — Recency (lần cuối hoạt động)
| Hoạt động cuối | Điểm |
|---|---|
| Hôm nay (login **và** khai báo bữa ăn **và** tương tác HLV) | 3 |
| Hôm qua | 2 |
| 2 hôm trước | 1 |
| Quá 3 hôm | 0 |

> **Q31a (đã chốt):** R=3 yêu cầu **cả 3 hoạt động** cùng ngày: login + khai báo bữa ăn + tương tác HLV. Nếu thiếu bất kỳ hoạt động nào trong ngày → ngày đó **không đạt R=3** (xét ngày gần nhất đủ cả 3 để tính recency).

### F — Frequency (hành động hằng ngày)
| Hành động trong ngày | Điểm |
|---|---|
| Làm đủ: check-in hằng ngày + chat HLV + đủ các nhiệm vụ | 3 |
| 2/3: chỉ check-in + chat HLV, **hoặc** chỉ check-in + làm nhiệm vụ | 2 |
| 1/3: chỉ check-in | 1 |
| Không làm hành động nào | 0 |

> “Đủ các nhiệm vụ” = hoàn thành các nhiệm vụ trên đồng hồ sinh học (US-E06-01) trong ngày.

### M — Monetary (giá trị gói khách dùng)
| Gói (trong chương trình) | Điểm |
|---|---|
| Tối ưu | 3 |
| Nâng cao | 2 |
| Cơ bản | 1 |

> **Q31b (đã chốt) — Quan hệ phân cấp Chương trình → Gói (KHÔNG phải ánh xạ 1-1):**
>
> Có **2 cấp**:
> 1. **Chương trình** (theo mục tiêu — `Consultation-15min-Process-v1.0.md` §6.1):
>    - Giảm cân → **Cơ — Nước — Mỡ**
>    - Tăng cân → **Dinh dưỡng tế bào**
>    - Giữ cân → **Bữa ăn lành mạnh**
>    - Mỗi chương trình có **nhóm sản phẩm bổ sung khác nhau**.
> 2. **Gói** (trong từng chương trình): **Tối ưu / Nâng cao / Cơ bản** — khác nhau về **danh mục sản phẩm bổ sung** trong chương trình đó (Tối ưu = đầy đủ SP nhất; Cơ bản = ít SP nhất).
>
> **M (monetary) = cấp Gói**, độc lập với Chương trình: Tối ưu=3 / Nâng cao=2 / Cơ bản=1 **bất kể chương trình nào**. Vd: KH dùng chương trình "Cơ — Nước — Mỡ" gói Tối ưu → M=3; KH dùng "Dinh dưỡng tế bào" gói Cơ bản → M=1.
>
> **Cấu trúc dữ liệu đề xuất:** `customer.program` (Cơ-Nước-Mỡ / Dinh dưỡng tế bào / Bữa ăn lành mạnh) + `customer.package_tier` (Tối ưu / Nâng cao / Cơ bản) + `customer.supplements[]` (danh mục SP bổ sung theo gói trong chương trình).

## 2. Tổng điểm & 3 trạng thái

Tổng RFM = R + F + M (thang 0–9).

| Tổng điểm | Trạng thái | Nhãn hiển thị | Màu | Hành động gợi ý |
|---|---|---|---|---|
| 7–9 | **Tích cực** | “Tích cực” | xanh (`--state-good`) | duy trì, gợi ý nâng cấp/tương tác cộng đồng |
| 4–6 | **Có nguy cơ** | “Có nguy cơ” | vàng (`--state-warn`) | nhắc chủ động, kiểm tra lý do giảm tương tác |
| 0–3 | **Kém quan tâm** | “Kém quan tâm” | đỏ (`--state-alert`) | can thiệp, gợi ý DMO phục hồi hoặc chuyển bảo trợ |

## 3. Hiển thị trong card Summary (To-Be §2.3)
- Bộ lọc: Tên KH + Trạng thái RFM.
- Thống kê số lượng KH theo từng trạng thái + màu tương ứng.
- Mỗi thẻ danh sách hiện chip trạng thái (≤2 nhãn — L6): vd “Tích cực” + nhóm KH.

## 4. Tính lại khi nào
- **R**: cập nhật mỗi ngày (cuối ngày chốt recency).
- **F**: cập nhật cuối ngày dựa hành động đã log.
- **M**: cập nhật khi KH đổi gói.
- Tổng RFM + trạng thái: tính lại khi R/F/M đổi.

---
## Open question
- *(không còn — Q31a, Q31b đã chốt 2026-07-02)*
- **TODO chưng cất tiếp:** danh mục sản phẩm bổ sung cụ thể cho từng tổ hợp Chương trình × Gói (9 tổ hợp: 3 chương trình × 3 gói) → cần PO cung cấp nội dung.
