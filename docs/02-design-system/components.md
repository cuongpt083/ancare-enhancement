# Component Library (mầm)

> Kho component tăng dần khi mockup tiến triển. Mỗi component khai báo tokens + khuôn màn áp dụng. Hiện là **mầm** — bổ sung khi `docs/03-mockups/` chốt hình ảnh.

## Atoms
| Component | Mô tả | Tokens |
|---|---|---|
| `Button` | nút chính/phụ/icon; full-width ở chân màn (T1) | `--accent-*`, vùng chạm ≥44px |
| `Chip` | nhãn gọn, nền nhạt + chữ đậm cùng tông; tối đa 2/thẻ | `--state-*` |
| `Card` | khối nội dung, gập được | `--bg`, `--radius-md`, `--shadow-card` |
| `AppBar` | tên bước + ⓘ; cố định đỉnh | `--bg`, `--text` |
| `FAB` | nút hành động nổi, 1 hành vi cố định | `--accent-*`, `--shadow-fab` |
| `Input` | trường nhập, label trên, hint dưới | `--text`, `--text-muted` |
| `AffordanceWhy` | nút "Vì sao?" — chỉ ở điểm quyết tiền | `--text-muted` |

## Molecules
| Component | Dùng cho | Khuôn |
|---|---|---|
| `FocusCard` | "việc nổi bật nhất hôm nay" | T3 |
| `LeadCard` | thẻ KH tiềm năng (≤2 nhãn: ưu tiên + giai đoạn) | T2 |
| `MealRow` | 1 bữa trong thực đơn | T1/T4 |
| `MetricBar` | chỉ số đối chiếu chuẩn | T1 |
| `StepHeader` | tên bước + tiến trình luồng | T1 |

## Organisms (luồng phức tạp)
| Component | Mô tả |
|---|---|
| `ConsultationFlow` | xương luồng tư vấn 15 phút (chuỗi bước T1) |
| `BioClock` | đồng hồ sinh học 24h (màn "Sức khỏe tổng thể" KH) |
| `ObjectionHandler` | FAB "Khách đang băn khoăn" — mở nhánh xử lý từ chối |
| `CompanionChat` | chat đồng hành, lớp "Vì sao?" |

> **Quy ước**: không tạo component mới nếu chưa có trong danh sách — thêm vào đây kèm tokens + khuôn trước khi dùng trong mockup.
