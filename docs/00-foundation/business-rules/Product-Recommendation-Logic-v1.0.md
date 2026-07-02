# Logic Tư vấn Sản phẩm phù hợp — v1.0

> **Mục đích THẬT:** thay ma trận tĩnh 3×3 bằng **bộ quyết định động** — cho HLV/HE biết: KH có đặc điểm X + mục tiêu Y → gợi ý SP Z. Dùng cho: Xem lộ trình (US-E02-05), bữa ăn (US-E02-07), Check-in KH (US-E06-10), Báo cáo KH đề xuất nâng cấp (US-E06-07), chăm sóc nâng cấp SP (US-E03-05).
> **Nguồn:** `products-index.md` (goals + safety signals từng SP).
> **Quy tắc đạo đức:** gợi ý, không ép; tôn trọng safety signals (bệnh lý/ thai kỳ/... → hỏi bác sĩ); minh bạch lý do.

## 1. Luật chọn SP theo MỤC TIÊU (cốt lõi — mọi KH)

| Mục tiêu (tick ở Phân tích US-E02-04) | Chương trình | SP cốt lõi (mọi gói) | Lý do (goals) |
|---|---|---|---|
| **Giảm cân** | Cơ — Nước — Mỡ | F1 (thay bữa, giảm cân) + PPP (giữ cơ khi giảm) + F2 (vitamin nền) | F1=giảm cân, PPP=hỗ trợ cơ, F2=sức khỏe nền |
| **Tăng cân** | Dinh dưỡng tế bào | F1 (tăng cân, thay bữa) + PPP (tăng cơ) + F2 | F1=tăng cân, PPP=tăng cơ, F2=nền |
| **Giữ cân** | Bữa ăn lành mạnh | F1 (duy trì) + PPP (duy trì cơ) + F2 | F1=duy trì, PPP=cơ, F2=nền |

## 2. Luật chọn SP theo ĐẶC ĐIỂM KH (bổ sung — nâng cấp gói)

> Khi KH có đặc điểm dưới, **thêm** SP phù hợp (xếp vào gói Nâng cao/Tối ưu).

| Đặc điểm KH (từ Chân dung KH US-E02-02 / chỉ số) | SP gợi ý | Lý do (goals) | Gói |
|---|---|---|---|
| **Mỡ nội tạng cao** (>7 nam / >4 nữ) | Herbalifeline (omega-3, tim mạch) + Cell-U-Loss (giải độc) | mỡ nội tạng → tim mạch; giải độc | Nâng cao |
| **Tim mạch / huyết áp** (tiền sử) | Herbalifeline + Niteworks | omega-3 + huyết áp ổn định | Nâng cao (⚠️ hỏi bác sĩ nếu dùng thuốc) |
| **Thiếu năng lượng / mệt mỏi** | Trà Thảo Mộc / Trà N-R-G | tỉnh táo, oxy hóa | Nâng cao |
| **Vận động nhiều / tập thể thao** | Rebuild Strength + F1 Sport + Hydrate | phục hồi cơ, nền vận động, bù điện giải | Tối ưu |
| **Tiêu hóa / táo bón** | Chất Xơ Hoạt Hóa + Lô Hội | xơ + uống nước + đường ruột | Nâng cao |
| **Uống nước ít** | Lô Hội Thảo Mộc (hỗ trợ thói quen uống nước) | pha loãng, dễ uống | Nâng cao |
| **Da / tóc / móng** (quan tâm sắc đẹp) | Beauty Powder Drink | tóc/móng/da, chống lão hóa | Tối ưu (⚠️ có thành phần cá) |
| **Xương / người lớn tuổi** | Xtra-Cal Advanced | xương chắc, loãng xương | Tối ưu |
| **Khớp** (đau khớp) | Joint Support Advanced | khớp khỏe | Tối ưu (⚠️ có cua/tôm) |
| **Mắt** (thị lực) | Ocular Defense | thị lực | Tối ưu |
| **Miễn dịch yếu** | ImmuLift + F2 | đề kháng, oxy hóa | Nâng cao |
| **Bảo vệ tế bào / chống oxy hóa** | Cell Activator | bảo vệ tế bào (⚠️ KO thai kỳ/thận mạn/tiểu đường insulin) | Tối ưu |

## 3. Safety signals — KHI NÀO KHÔNG gợi ý / hỏi bác sĩ

| SP | Không dùng / thận trọng khi |
|---|---|
| Cell Activator | phụ nữ có thai/cho con bú · thận mạn · tiểu đường lệ thuộc insulin |
| Cell-U-Loss | mẫn cảm thành phần |
| Herbalifeline / Niteworks | dùng thuốc tim mạch/chống đông → hỏi bác sĩ |
| Joint Support | trẻ em · thai kỳ/cho con bú · dị ứng cua/tôm/đậu nành |
| Trà Thảo Mộc / Trà N-R-G | trẻ em · thai kỳ/cho con bú (caffeine) → hỏi bác sĩ |
| Beauty Powder | có thành phần cá |
| F1 / PPP / F1 Sport | có đậu nành/sữa · hỏi bác sĩ trước chương trình giảm cân |
| Xtra-Cal | bệnh thận/sỏi thận/rối loạn calci → hỏi bác sĩ |
| Hydrate | kiểm soát natri/kali → hỏi bác sĩ |
| ImmuLift | chồng liều vi chất nếu đang dùng supplement khác |

> **Luật:** khi KH có bất kỳ safety signal → hiện cảnh báo "Nên hỏi bác sĩ trước khi dùng [SP]" — không tự động thêm vào gói.

## 4. Cấu trúc gói (đầu ra)

```
Gợi ý gói cho KH =
  SP cốt lõi (theo mục tiêu — §1)
+ SP theo đặc điểm KH (§2) — nếu phù hợp & không vi phạm safety (§3)
→ xếp vào gói:
  - Cơ bản (M=1): chỉ SP cốt lõi (F1+PPP+F2)
  - Nâng cao (M=2): cốt lõi + 2-3 SP đặc điểm
  - Tối ưu (M=3): cốt lõi + 4-6 SP đặc điểm + premium (Beauty/Xtra-Cal/Cell Activator)
```

## 5. Khi nào dùng logic này
- **US-E02-05 Xem lộ trình**: sau tick mục tiêu + Chân dung KH → sinh gói SP đề xuất (hiển thị, không hiện giá).
- **US-E02-07 Bữa ăn**: mục "Thực phẩm bổ sung" = SP cốt lõi theo gói.
- **US-E03-05 Phân tích sức khỏe + nâng cấp SP**: khi KH có đặc điểm mới → gợi ý thêm SP (đề xuất nâng cấp gói).
- **US-E06-07 Báo cáo KH (tab Đề xuất)**: gợi ý SP KH quan tâm (dựa đặc điểm + mục tiêu).
- **US-E06-10 Check-in Card 2**: nhập số viên/ml SP hiện dùng.

---
*Logic động dựa trên products-index goals + safety. PO xác nhận/điều chỉnh. Thay thế ma trận tĩnh 3×3 (đã lưu ở `Program-Package-Supplements-v1.0.md` làm tham chiếu nhanh).*
