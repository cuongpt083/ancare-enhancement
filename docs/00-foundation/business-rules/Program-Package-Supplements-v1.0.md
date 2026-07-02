# Danh mục Sản phẩm bổ sung — Chương trình × Gói (9 tổ hợp) — v1.0

> **Quyết định:** Q31b (PO chốt 2026-07-02) — quan hệ **phân cấp**: Chương trình (theo mục tiêu) → Gói (Tối ưu/Nâng cao/Cơ bản) → danh mục SP bổ sung.
> **Nguồn SP:** `docs/00-foundation/products-index.md` (Product Knowledge Index — goals của từng SP). **Đề xuất dựa trên goals, chờ PO xác nhận.**
> **Mục đích:** lưu danh mục SP bổ sung cho 9 tổ hợp. Dùng cho: Xem lộ trình (US-E02-05), bữa ăn (US-E02-07), Check-in KH (US-E06-10 Card 2), RFM M (Q31b).

## Cấu trúc phân cấp

```
Chương trình (theo mục tiêu — Consultation-15min-Process §6.1)
├── Giảm cân → Cơ — Nước — Mỡ
├── Tăng cân → Dinh dưỡng tế bào
└── Giữ cân → Bữa ăn lành mạnh

Gói (trong từng chương trình — RFM M)
├── Cơ bản (M=1) — core essentials (3-4 SP)
├── Nâng cao (M=2) — core + SP hỗ trợ (5-6 SP)
└── Tối ưu (M=3) — đầy đủ SP (7-8 SP)
```

## Ma trận 3×3 (đề xuất dựa trên products-index — chờ PO xác nhận)

> **Quy tắc điền:** core (F1+PPP+F2) có ở mọi tổ hợp. SP chuyên biệt theo chương trình. Gói cao hơn = thêm SP hỗ trợ.
> **Ký hiệu:** ⭐ core (mọi gói) · ➕ hỗ trợ (Nâng cao+) · ✨ premium (Tối ưu)

| Chương trình | Gói Cơ bản (M=1) | Gói Nâng cao (M=2) | Gói Tối ưu (M=3) |
|---|---|---|---|
| **Cơ — Nước — Mỡ**<br>(giảm cân) | ⭐ F1 (thay bữa, giảm cân)<br>⭐ PPP (giữ cơ)<br>⭐ F2 Multivitamin | + ➕ Cell-U-Loss (giải độc)<br>+ ➕ Trà Thảo Mộc (tỉnh táo, oxy hóa)<br>+ ➕ Chất Xơ Hoạt Hóa (đường ruột) | + ✨ Lô Hội (uống nước)<br>+ ✨ Cell Activator (bảo vệ tế bào)<br>+ ✨ Herbalifeline (omega-3, tim mạch) |
| **Dinh dưỡng tế bào**<br>(tăng cân) | ⭐ F1 (tăng cân, thay bữa)<br>⭐ PPP (tăng cơ)<br>⭐ F2 Multivitamin | + ➕ Cell Activator (bảo vệ tế bào — "tế bào")<br>+ ➕ Trà N-R-G (tỉnh táo)<br>+ ➕ Hỗn Hợp Chất Xơ (đường ruột) | + ✨ Rebuild Strength (phục hồi sau tập, tăng cơ)<br>+ ✨ Formula 1 Sport (nền tảng người vận động)<br>+ ✨ Hydrate (bù nước điện giải) |
| **Bữa ăn lành mạnh**<br>(giữ cân) | ⭐ F1 (duy trì cân)<br>⭐ PPP (duy trì cơ)<br>⭐ F2 Multivitamin | + ➕ Trà Thảo Mộc (tỉnh táo)<br>+ ➕ Chất Xơ Hoạt Hóa (đường ruột)<br>+ ➕ Lô Hội (uống nước) | + ✨ Cell Activator (bảo vệ tế bào)<br>+ ✨ Xtra-Cal Advanced (xương chắc)<br>+ ✨ Ocular Defense (thị lực) |

### Ghi chú suy luận (từ products-index goals)
- **F1 / PPP / F2** = core mọi tổ hợp (goals: thay bữa/đạm/vitamin — nền tảng).
- **Cơ — Nước — Mỡ**: SP giải độc (Cell-U-Loss), chống oxy hóa (Trà Thảo Mộc), xơ (đường ruột), omega-3 (Herbalifeline — mỡ nội tạng/tim mạch).
- **Dinh dưỡng tế bào**: SP tế bào (Cell Activator — đúng tên), phục hồi cơ (Rebuild Strength), vận động (F1 Sport, Hydrate).
- **Bữa ăn lành mạnh**: SP duy trì (Trà, Xơ, Lô Hội) + bảo vệ dài hạn (Cell Activator, Xtra-Cal, Ocular).
- **Prolessa Duo** (source-gap, gợi ý giảm mỡ) — chưa đưa vào (thiếu dữ liệu).
- **SP chuyên biệt theo bệnh lý** (Joint Support, Niteworks, Beauty Powder) — bổ sung theo nhu cầu KH, không cố định theo gói.

> ⚠️ **Đề xuất này dựa trên goals trong products-index. PO cần xác nhận + điều chỉnh theo thực tế gói bán hàng Herbalife.**

## Quy tắc sử dụng
- SP bổ sung hiển thị trong **Xem lộ trình** (US-E02-05) — không hiện giá (HLV giải thích ngoài app).
- SP bổ sung hiển thị trong **bữa ăn** (US-E02-07, US-E06-10 Card 2) — mục "Thực phẩm bổ sung".
- Đổi gói → cập nhật `customer.package_tier` + `customer.supplements[]` → tính lại RFM M.
- SP chuyên biệt bệnh lý (Joint Support, Niteworks...) = bổ sung riêng theo KH, không cố định ma trận.

## Cấu trúc dữ liệu (Q31b)
- `customer.program` — Cơ-Nước-Mỡ / Dinh dưỡng tế bào / Bữa ăn lành mạnh
- `customer.package_tier` — Tối ưu / Nâng cao / Cơ bản
- `customer.supplements[]` — danh mục SP (tra từ ma trận trên + SP bệnh lý riêng)

---
*Q31b ✅ (đề xuất). TODO: PO xác nhận/điều chỉnh ma trận 3×3 + bổ sung SP bệnh lý theo KH.*
