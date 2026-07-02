# As-Is Notes — Mô tả tổng quát PO + Phân tích AI

> PO điền phần “Mô tả tổng quát” + “Mỗi màn”. AI điền phần “AI phân tích” sau khi đọc ảnh.
> Xem hướng dẫn chụp/đặt ảnh: `README.md` cùng thư mục.

## 1. Sơ đồ luồng tổng quát

> PO vẽ/mô tả sơ đồ các màn nối nhau (text hoặc mermaid). Ưu tiên luồng trọng tâm.

**Luồng E02 — Tư vấn 15 phút (HLV):**
```
<dang_nhap> → <dashboard> → <...> → <...>
```

**Luồng E01 — KH tiềm năng (HLV):**
```
<...> → <...>
```

**Luồng E06 — Khách hàng (KH):**
```
<...> → <...>
```

---

## 2. Mỗi màn (PO điền, AI phân tích sau)

> Copy template dưới cho mỗi màn. PO chỉ điền 5 trường đầu; “AI phân tích” để trống.

### TEMPLATE
### Màn <nn> — <tên>
- **Path ảnh:** `screenshots-<hlv|kh>/<nn>_<tên>.png`
- **Vai trò:** HLV / KH
- **Luồng:** từ `<màn trước>` → tới `<màn sau>`
- **Trường thông tin hiển thị (PO liệt kê nhanh):**
  - <trường 1> — nguồn: <HLV nhập/KH nhập/động/tĩnh>
  - <trường 2> ...
- **Nhận xét PO (gì ổn / gì cần cải thiện):** <ngắn gọn, optional>
- **AI phân tích As-Is (điền sau):** _<AI đọc ảnh + mô tả → phân tích: bố cục, trường, trạng thái, điểm mạnh, hạn chế>_

---

### [đợi PO điền]

---

## 3. Tổng hợp AI (điền sau khi phân tích xong nhóm)

- **Phần kế thừa tốt (KẾ THỪA):** <danh sách màn/thành phần app đã ổn>
- **GAP chính (cần SỬA/THÊM/XÓA):** <danh sách>
- **Cập nhật vào:** `docs/03-mockups/screen-gap-analysis.md`
