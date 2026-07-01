# 7 Nguyên tắc Lean (luật bắt buộc)

> Bối cảnh người dùng cốt lõi: HLV trung niên, **chưa quen công nghệ**, **bận**, sợ *"tồn thời gian – không hiệu quả"*; thường dùng máy **khi đang ngồi cạnh khách thật**. → Giao diện phải **nhẹ, liếc-là-dùng, ít chữ**.

| # | Nguyên tắc | Luật áp dụng | Phản-ví dụ cần tránh |
|---|---|---|---|
| **L1** | **Một màn = một quyết định** | Mỗi màn có **đúng 1 việc chính** + tối đa **1 CTA chính**. Việc phụ → bước sau hoặc "Xem thêm". | "Thiết lập mục tiêu" gánh 8 khối trong 1 màn. |
| **L2** | **Liếc-là-dùng (3 giây)** | Vùng nhìn đầu tiên (above-the-fold) **≤ 3 khối**. Dùng được khi đang nói chuyện trực tiếp. | "Bản tư vấn" 5 lớp cuộn dài, không liếc được. |
| **L3** | **Mặc định thông minh, ẩn nâng cao** | Hệ thống **chọn sẵn** (gói đề xuất, mục tiêu khả thi, thực đơn). Người dùng **xác nhận**; tinh chỉnh nằm sau nút **"Chỉnh"**. | Bày sẵn +/- từng mục tiêu, % từng dòng ngay màn đầu. |
| **L4** | **Ngôn ngữ người dùng, không thuật ngữ** | Dùng tiếng nói của HLV/KH. Cấm lộ từ kỹ thuật ra UI. | "Feasibility Score 78", "cần làm mới TĐ", "Persona-fit". |
| **L5** | **Hành vi nhất quán** | 1 nút = 1 việc, **không đổi đích theo ngữ cảnh**. Cần 2 việc → 2 nút rõ ràng. | FAB đổi đích theo tab; FAB ẩn/hiện theo Stage. |
| **L6** | **Tiết chế nhãn & màu** | Mỗi thẻ tối đa **2 nhãn** quan trọng nhất; còn lại vào màn chi tiết. Màu trạng thái dùng **1 hệ thống** (xem `design-tokens.md`). | Thẻ lead 5 tag (DISC+Stage+nguồn+score+việc). |
| **L7** | **Giải thích đúng chỗ** | Affordance **"Vì sao?"** chỉ đặt ở **điểm quyết định tiền** (gói/giá, % cam kết). Không rải khắp nơi. | "Vì sao?" gắn vào *mọi* kết quả. |

## Nguyên tắc xuyên suốt (kỹ thuật)

- **Tiết lộ dần (Progressive Disclosure)**: chi tiết gập mặc định, mở khi cần — quy ước thống nhất ở mọi khuôn màn.
- **Có đường lui**: khi `ai_data_sharing_enabled = false` hoặc offline → rơi về template tĩnh, app vẫn chạy.
- **Minh bạch**: mọi diễn đạt truy được về bằng chứng (`provenance.evidence`) → đúng nguyên tắc *"AI hỗ trợ không thao túng; minh bạch & quyền người dùng"*.
