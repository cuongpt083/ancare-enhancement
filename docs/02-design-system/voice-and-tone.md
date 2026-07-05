# Voice & Tone

> Khái niệm kỹ thuật **giữ trong dữ liệu/logic**, **không in ra UI**. Dùng bảng dịch chuẩn dưới đây.

## Bảng dịch "khái niệm hệ thống → ngôn ngữ người dùng"

| Khái niệm hệ thống (chỉ nội bộ) | Hiển thị ra người dùng |
|---|---|
| Feasibility Score = 78 (vàng) | "Thực đơn này **hơi khó áp dụng**" + 1 dòng cách dễ hơn |
| `meal_plan` hết hiệu lực / "cần làm mới TĐ" | "**Đến hạn đo lại**" |
| Persona-fit / lọc theo persona | (không nói) — chỉ hiện thực đơn đã hợp khẩu vị |
| Stage-of-Change = contemplation | "Khách **đang cân nhắc**" |
| DISC = C | (không nói) — chỉ đổi *cách trình bày* |
| Next-Best-Action | "**Việc nên làm tiếp**" |
| lead_score = 82 | (ẩn số) — chỉ dùng để **sắp xếp** thứ tự; hiện nhãn "Ưu tiên hôm nay" |
| `ai_data_sharing_enabled = false` | "Bật trợ lý AI để nhận gợi ý" (lời mời, không lỗi) |

## Quy tắc số

**Không** bày con số kỹ thuật (điểm 0–100) ra UI; quy về **nhãn ngôn ngữ**:
- Khả thi: Dễ / Hơi khó / Khó
- Trạng thái: Tốt / Cần lưu ý / Cảnh báo
- Số chi tiết chỉ hiện khi người dùng chủ động "Xem chi tiết".

## Tông giọng

- **Ấm, đồng hành, không phán xét**; tránh từ "xấu / thừa / lỗi / sai".
- Ưu tiên động từ dẫn dắt hành động.
- Ngắn: mỗi mục ≤ 1 dòng; mô tả ≤ 2 dòng.
- Tôn trọng quyền người dùng: gợi ý không phải lệnh; mọi mẫu câu AI là **gợi ý chỉnh sửa được**, không auto-gửi, không tạo áp lực sai sự thật.
