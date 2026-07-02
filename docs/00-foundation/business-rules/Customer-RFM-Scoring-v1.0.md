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

> “Hoạt động” = login + khai báo bữa ăn + tương tác HLV (cả 3 cùng ngày mới đạt R=3). Nếu chỉ login/khai báo 1 phần → cần PO làm rõ (mặc định tạm: đủ cả 3 mới tính ngày đó). *(Xem Open question Q31a)*

### F — Frequency (hành động hằng ngày)
| Hành động trong ngày | Điểm |
|---|---|
| Làm đủ: check-in hằng ngày + chat HLV + đủ các nhiệm vụ | 3 |
| 2/3: chỉ check-in + chat HLV, **hoặc** chỉ check-in + làm nhiệm vụ | 2 |
| 1/3: chỉ check-in | 1 |
| Không làm hành động nào | 0 |

> “Đủ các nhiệm vụ” = hoàn thành các nhiệm vụ trên đồng hồ sinh học (US-E06-01) trong ngày.

### M — Monetary (giá trị gói khách dùng)
| Gói | Điểm |
|---|---|
| Tối ưu | 3 |
| Nâng cao | 2 |
| Cơ bản | 1 |

> Danh mục gói (Tối ưu / Nâng cao / Cơ bản) cần PO xác nhận ánh xạ từ `packaged-service-advice-v1.0.md`. *(Xem Open question Q31b)*

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
- **Q31a**: R=3 yêu cầu “login + khai báo bữa ăn + tương tác HLV” cả 3 cùng ngày — nếu KH chỉ làm 2/3 thì tính recency ngày đó là bao nhiêu? (mặc định tạm: chưa đủ 3 → không tính ngày đó vào recency, lấy ngày gần nhất đủ 3). Cần PO chốt.
- **Q31b**: Ánh xạ gói Tối ưu/Nâng cao/Cơ bản ↔ gói trong `packaged-service-advice-v1.0.md` (Cơ-Nước-Mỡ / Dinh dưỡng tế bào / Bữa ăn lành mạnh?). Cần PO chốt.
