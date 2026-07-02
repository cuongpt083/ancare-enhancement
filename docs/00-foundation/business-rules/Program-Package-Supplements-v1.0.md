# Danh mục Sản phẩm bổ sung — Chương trình × Gói (9 tổ hợp) — v1.0

> **Quyết định:** Q31b (PO chốt 2026-07-02) — quan hệ **phân cấp**: Chương trình (theo mục tiêu) → Gói (Tối ưu/Nâng cao/Cơ bản) → danh mục SP bổ sung.
> **Mục đích:** lưu danh mục SP bổ sung cho từng tổ hợp 3 chương trình × 3 gói (9 tổ hợp). Dùng cho: Xem lộ trình (US-E02-05), bữa ăn (US-E02-07), Check-in KH (US-E06-10 Card 2), RFM M (Q31b).
> **Trạng thái:** ⏳ **PLACEHOLDER — chờ PO cung cấp nội dung SP thật** (Herbalife). Khung 3×3 sẵn sàng.

## Cấu trúc phân cấp

```
Chương trình (theo mục tiêu — Consultation-15min-Process §6.1)
├── Giảm cân → Cơ — Nước — Mỡ
├── Tăng cân → Dinh dưỡng tế bào
└── Giữ cân → Bữa ăn lành mạnh

Gói (trong từng chương trình — RFM M, Q31b)
├── Tối ưu (M=3) — đầy đủ SP nhất
├── Nâng cao (M=2)
└── Cơ bản (M=1) — ít SP nhất

Danh mục SP bổ sung (theo tổ hợp Chương trình × Gói) ← ĐIỀN BÊN DƯỚI
```

## Ma trận 3×3 (PLACEHOLDER — PO điền)

| | Gói Cơ bản (M=1) | Gói Nâng cao (M=2) | Gói Tối ưu (M=3) |
|---|---|---|---|
| **Cơ — Nước — Mỡ** (giảm cân) | `[TBD PO]` | `[TBD PO]` | `[TBD PO]` |
| **Dinh dưỡng tế bào** (tăng cân) | `[TBD PO]` | `[TBD PO]` | `[TBD PO]` |
| **Bữa ăn lành mạnh** (giữ cân) | `[TBD PO]` | `[TBD PO]` | `[TBD PO]` |

> Mỗi ô = danh sách SP bổ sung (vd: F1, PPP, Omega-3, Niteworks, Aloe...). Gói Tối ưu = đầy đủ nhất; Cơ bản = ít nhất.

## Quy tắc
- SP bổ sung hiển thị trong **Xem lộ trình** (US-E02-05) — không hiện giá (HLV giải thích ngoài app).
- SP bổ sung hiển thị trong **bữa ăn** (US-E02-07, US-E06-10 Card 2) — mục "Thực phẩm bổ sung".
- Đổi gói → cập nhật `customer.package_tier` + `customer.supplements[]` → tính lại RFM M.

## Cấu trúc dữ liệu (Q31b)
- `customer.program` — Cơ-Nước-Mỡ / Dinh dưỡng tế bào / Bữa ăn lành mạnh
- `customer.package_tier` — Tối ưu / Nâng cao / Cơ bản
- `customer.supplements[]` — danh mục SP (tra từ ma trận trên)

---
*TODO Q31b: PO cung cấp danh mục SP thật cho 9 tổ hợp → điền vào ma trận trên.*
