# Ngôn ngữ thiết kế "Lean" — AnCare (chuẩn chung cho mọi màn HLV & KH)

**Phiên bản:** v1.0 · **Cập nhật:** 2026-06-26
**Mục đích:** Chốt **nguyên tắc & quy ước thiết kế tinh giản** áp dụng cho toàn bộ UI (HLV + KH), nhằm sửa lỗi "rườm rà / quá nhiều thông tin". Đây là **tài liệu nền** — mọi đặc tả màn (v2) phải tuân theo trước khi đào sâu luồng/logic.
**Bối cảnh người dùng cốt lõi:** HLV trung niên, **chưa quen công nghệ**, **bận**, sợ *"tốn thời gian – không hiệu quả"*; thường dùng máy **khi đang ngồi với khách thật**. → Giao diện phải **nhẹ, liếc-là-dùng, ít chữ**.

> **Tuyên ngôn:** *"Mỗi màn hỏi một điều. Hệ thống quyết sẵn — người dùng chỉ xác nhận. Chi tiết ẩn cho tới khi cần."*

---

## 1. Bảy nguyên tắc Lean (luật bắt buộc)

| # | Nguyên tắc | Luật áp dụng | Phản-ví dụ cần tránh (từ v1.1) |
|---|---|---|---|
| L1 | **Một màn = một quyết định** | Mỗi màn có **đúng 1 việc chính** + tối đa **1 CTA chính**. Việc phụ → bước sau hoặc "Xem thêm". | "Thiết lập mục tiêu" gánh 8 khối trong 1 màn. |
| L2 | **Liếc-là-dùng (3 giây)** | Khi mở màn, vùng nhìn đầu tiên (above-the-fold) **≤ 3 khối**. Dùng được khi đang nói chuyện trực tiếp. | "Bản tư vấn" 5 lớp cuộn dài, không liếc được. |
| L3 | **Mặc định thông minh, ẩn nâng cao** | Hệ thống **chọn sẵn** (gói đề xuất, mục tiêu khả thi, thực đơn). Người dùng **xác nhận**; tinh chỉnh nằm sau nút **"Chỉnh"**. | Bày sẵn +/- từng mục tiêu, % từng dòng ngay màn đầu. |
| L4 | **Ngôn ngữ người dùng, không thuật ngữ** | Dùng tiếng nói của HLV/KH. Cấm lộ từ kỹ thuật ra UI. | "Feasibility Score 78", "cần làm mới TĐ", "Persona-fit". |
| L5 | **Hành vi nhất quán** | 1 nút = 1 việc, **không đổi đích theo ngữ cảnh**. Cần 2 việc → 2 nút rõ ràng. | FAB đổi đích theo tab; FAB ẩn/hiện theo Stage. |
| L6 | **Tiết chế nhãn & màu** | Mỗi thẻ tối đa **2 nhãn** quan trọng nhất; còn lại vào màn chi tiết. Màu trạng thái dùng **1 hệ thống** (xem §4). | Thẻ lead 5 tag (DISC+Stage+nguồn+score+việc). |
| L7 | **Giải thích đúng chỗ** | Affordance **"Vì sao?"** chỉ đặt ở **điểm quyết định tiền** (gói/giá, % cam kết). Không rải khắp nơi. | "Vì sao?" gắn vào *mọi* kết quả. |

---

## 2. Khái niệm hệ thống → cách hiển thị ra người dùng (bản dịch ngôn ngữ)

> Khái niệm kỹ thuật **giữ trong dữ liệu/logic**, **không in ra UI**. Bảng dịch chuẩn:

| Khái niệm hệ thống (chỉ dùng nội bộ) | Hiển thị ra người dùng |
|---|---|
| Feasibility Score = 78 (vàng) | "Thực đơn này **hơi khó áp dụng**" + 1 dòng cách dễ hơn |
| `meal_plan` hết hiệu lực / "cần làm mới TĐ" | "**Đến hạn đo lại**" |
| Persona-fit / lọc theo persona | (không nói) — chỉ hiện thực đơn đã hợp khẩu vị |
| Stage-of-Change = contemplation | "Khách **đang cân nhắc**" |
| DISC = C | (không nói) — chỉ đổi *cách trình bày* |
| Next-Best-Action | "**Việc nên làm tiếp**" |
| lead_score = 82 | (ẩn số) — chỉ dùng để **sắp xếp** thứ tự; hiện nhãn "Ưu tiên hôm nay" |
| `ai_data_sharing_enabled=false` | "Bật trợ lý AI để nhận gợi ý" (lời mời, không lỗi) |

**Quy tắc số:** không bày con số kỹ thuật (điểm 0–100) ra UI; quy về **nhãn ngôn ngữ** (Dễ/Hơi khó/Khó · Tốt/Cần lưu ý). Số chi tiết chỉ hiện khi người dùng chủ động "Xem chi tiết".

---

## 3. Khuôn mẫu màn hình (Screen Templates)

Mọi màn thuộc 1 trong 4 khuôn:

**T1 — Màn "Quyết định" (1 việc + 1 CTA).** Dùng cho các bước trong luồng tư vấn.
- Cấu trúc: AppBar (tên bước + ⓘ tùy chọn) → **1 khối nội dung chính** → (gập "Chỉnh"/"Xem thêm") → **CTA chính cố định chân màn** (+ 1 nút phụ tối đa).

**T2 — Màn "Danh sách".** Dùng cho danh sách KH/lead/tài liệu.
- Cấu trúc: AppBar + tìm kiếm → (tab nếu cần) → **thẻ gọn (≤2 nhãn)** → FAB cố định (1 hành vi).

**T3 — Màn "Bảng điều khiển/Tổng quan".**
- Cấu trúc: lời chào → **1 việc nổi bật nhất hôm nay (focus card)** → lối tắt (≤3) → danh sách cần chú ý. KPI phụ gom 1 hàng nhỏ, không phải 4 ô lớn.

**T4 — Màn "Chi tiết" (hồ sơ).**
- Cấu trúc: header gọn → **hành động nhanh (≤3)** → các card thông tin **gập mặc định**, mở từng cái khi cần.

**Quy tắc above-the-fold:** T1 ≤ 3 khối; T2 thấy ≥ 3 thẻ; T3 focus card phải nằm trong màn đầu; T4 chỉ header + hành động nhanh mở sẵn.

---

## 4. Hệ màu & trạng thái (1 hệ thống duy nhất)

| Vai trò | Màu | Dùng cho |
|---|---|---|
| Accent (thương hiệu) | `#2f6f4f` (HLV) / `#2f9e6e` (KH) | CTA chính, nhấn |
| Tốt / đạt | xanh `#16a34a` | trạng thái tốt, hoàn thành đúng |
| Cần lưu ý | vàng `#d99a14` | một phần / trễ / hơi khó |
| Cảnh báo / quá | đỏ `#c5402f` | bỏ lỡ / vượt ngưỡng / đến hạn |
| Trung tính / chờ | xám `#cdd4db` | chưa tới / không liên quan |
| Trụ cột | Thân `#16a34a` · Tâm `#8b5cf6` · Trí `#f97316` | chỉ ở ngữ cảnh Thân–Tâm–Trí |

- **Một ý nghĩa = một màu**, dùng nhất quán mọi màn. Không dùng màu trang trí gây nhiễu.
- Chip/nhãn: nền nhạt + chữ đậm cùng tông; **không** quá 2 chip/thẻ.

---

## 5. Typography, cảm ứng, ngôn từ

- **Cỡ chữ tối thiểu 13px** cho nội dung (người trung niên); tiêu đề 15–18px; tránh chữ 9–10px cho thông tin quan trọng.
- **Vùng chạm ≥ 44px**; nút chính to, rõ, có icon + chữ.
- **Ít chữ:** mỗi mục ≤ 1 dòng; mô tả ≤ 2 dòng. Ưu tiên động từ ("Tạo bản tư vấn", "Lưu & gửi khách").
- **Tông giọng:** ấm, đồng hành, không phán xét; tránh từ "xấu/thừa/lỗi".

---

## 6. Tiết lộ dần (Progressive Disclosure) — quy ước thống nhất

- **"Xem thêm / Thu gọn"**: cho nội dung phụ trong cùng màn (vd bảng chỉ số chi tiết mặc định 2 dòng).
- **"Chỉnh"**: mở chế độ tinh chỉnh nâng cao (mục tiêu +/-, đổi gói) — **mặc định ẩn**.
- **"Vì sao?"**: chỉ ở điểm quyết định tiền; bung lời giải *căn cứ → quy tắc → bằng chứng*.
- **Card gập**: ở màn Chi tiết (T4) và form dài; mặc định gập trừ card ưu tiên.
- **Cấm**: ẩn hành vi quan trọng sau cử chỉ khó đoán; cấm nút "đổi nghĩa" theo ngữ cảnh.

---

## 7. Áp dụng nhanh cho các màn nặng nhất (định hướng v2 — chi tiết ở đặc tả riêng)

| Màn | Lỗi v1.1 | Hướng lean (sẽ đặc tả chi tiết sau) |
|---|---|---|
| **Bản tư vấn** | 5 lớp cuộn dài + DISC + FAB + Vì sao + bảng WHO | **1 màn liếc-là-nói:** 1 câu đồng cảm + **3 điểm chính** (1 tốt, 2 cần quan tâm) + 1 câu "làm được" + 1 CTA. Chi tiết/nguy cơ/số liệu vào "Xem chi tiết". |
| **Thiết lập mục tiêu** | 8 khối/1 màn | **Tách 2–3 bước nhỏ:** (a) mục tiêu + thời hạn; (b) gói đề xuất *chọn sẵn* (xác nhận) → % hiện gọn; "Chỉnh" để tinh chỉnh. Card "khả thi bữa ăn" → bước cấu hình riêng/ẩn. |
| **Gợi ý bữa ăn** | nhiều badge + thuật ngữ | Header gọn (Calo/ngày + "Dễ/Hơi khó áp dụng"); 3 nhóm/bữa giữ; chi phí & "người nấu" ẩn sau "Tùy chọn". |
| **Danh sách KH** | thẻ 5 tag, FAB đổi đích | Thẻ **2 nhãn** (giai đoạn + việc cần làm); **2 nút tạo tách bạch** thay vì FAB đổi nghĩa. |
| **Dashboard** | 4 KPI + jargon | **1 focus card "việc nên làm hôm nay"**; KPI gom 1 hàng nhỏ; đổi nhãn sang ngôn ngữ người dùng. |
| **Tạo KH tiềm năng** | card chân dung 6 nhóm | Bước đầu chỉ **Tên + 1 ghi chú**; chân dung khảo sát **bổ sung dần** (không bắt buộc), hỏi đúng lúc trong hội thoại. |

---

## 8. Checklist nghiệm thu Lean (áp cho mọi đặc tả/redesign màn)
- [ ] Màn có đúng **1 việc chính** & **1 CTA chính**?
- [ ] Above-the-fold **≤ 3 khối** (T1) / focus card hiện ngay (T3)?
- [ ] Không có **thuật ngữ kỹ thuật** lộ ra UI? (đối chiếu §2)
- [ ] Mỗi thẻ **≤ 2 nhãn**? Màu theo **1 hệ thống** (§4)?
- [ ] Có **mặc định thông minh** để người dùng chỉ xác nhận? Nâng cao đã **ẩn sau "Chỉnh"**?
- [ ] Mọi nút **1 hành vi cố định**? Không cử chỉ ẩn khó đoán?
- [ ] Chữ ≥ 13px, chạm ≥ 44px, mỗi mục ≤ 1–2 dòng?
- [ ] "Vì sao?" chỉ ở điểm quyết định tiền?

---
*v1.0 — Ngôn ngữ thiết kế nền. Bước tiếp: áp checklist này để viết lại đặc tả chi tiết (luồng + màn + logic) cho từng module, bắt đầu từ "Bản tư vấn" và "Thiết lập mục tiêu".*
