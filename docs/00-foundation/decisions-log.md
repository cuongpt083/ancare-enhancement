# Decisions Log — Các quyết định đã chốt (Open Questions)

> **Vai trò:** Nguồn sự thật duy nhất cho mọi câu hỏi mở (open question) đã được chốt. Mỗi quyết định có ID (`D01`…`D30`), câu hỏi gốc, quyết định, và nơi tác động.
> **Trạng thái:** Đã chốt ngày 2026-07-01 qua vòng hỏi-đáp với PO.

## A — Kiến trúc & nền
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D01** | 1 shell chung (role-based) hay 2 app tách biệt (HLV + KH)? | **1 app chung role-based** — đăng nhập vào cùng app, UI đổi theo role HLV/KH. Mockup làm 1 bộ có 2 nhánh (coach/ + customer/). | vision-and-values § kiến trúc; mockups/prototypes 1 bộ |
| **D02** | Mục tiêu KH & mục tiêu KD HLV: chung hay tách model? | **Tách 2 model riêng** (`health_goal` cho KH, `business_goal` cho HLV) — rõ ràng, dễ query, không nhầm lẫn. | data model; US-E00-03, US-E00-04 |
| **D03** | Mục tiêu sức khỏe: KH tự đặt hay xác nhận gợi ý HLV? | **Hybrid** — KH xác nhận gợi ý HLV lúc onboarding, sau đó tự chỉnh/đổi được trong app (lưu lịch sử mục tiêu cũ). | US-E00-03, US-E02-05 |
| **D04** | Onboarding KH lần đầu gồm những bước gì? | **Đơn giản** — chào mừng → xác nhận mục tiêu (gợi ý HLV) → xem lộ trình/bữa ăn → disclaimer → trang chủ. | US-E02-08 onboarding |

## B — E02 Consultation
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D05** | Bảng tiêu chuẩn WHO/Tanita theo tuổi & giới? | **AI tìm/đề xuất bảng chuẩn WHO + Tanita chính thức** → đưa vào foundation (TODO: fetch dữ liệu). | business-rules mới `Body-Composition-Standards-v1.0.md`; US-E02-04 |
| **D06** | Bộ câu hỏi khảo sát rút gọn (DISC + Stage)? | **Dùng đúng 7 nhóm trong sample; DISC/Stage do HLV tự đánh giá ngoài form** (không số hóa câu hỏi DISC/Stage). | US-E02-02; Consultation-15min-Process §3 |
| **D07** | Objection Handler — 5 nhánh × 4 DISC mẫu câu? | **PO có sẵn mẫu câu (cung cấp sau)** — tạm chưng cất khung 5×4 + placeholder. | business-rules mới `Objection-Handler-Framework-v1.0.md`; US-E02-06 |
| **D08** | 3 chương trình theo mục tiêu — xác nhận chính thức? | **Xác nhận chính thức** — giảm→Cơ-Nước-Mỡ, tăng→Dinh dưỡng tế bào, giữ→Bữa ăn lành mạnh. Đưa vào business-rule làm logic chuẩn. | Consultation-15min-Process §6 (đã có) |
| **D09** | Công thức % khả thi đạt mục tiêu? | **Dựa tốc độ an toàn (kg/tuần chuẩn) × thời gian đã chọn** — đủ thời gian = "Khả thi", thiếu = "Tham vọng". Không in số ra UI (L4). | US-E02-05; Calorie-Meal-Business-Rules (tốc độ an toàn) |
| **D10** | Danh sách đội ngũ & kết quả tiêu biểu (US-E02-01)? | **HLV tự nhập/tùy chỉnh** danh sách đội ngũ + kết quả tiêu biểu của team mình (lưu theo HLV). | US-E02-01 |
| **D11** | Vị trí & dạng disclaimer "không thần dược"? | **Inline** — dòng chữ nhỏ nằm dưới nội dung bản phân tích/chốt gói; không modal, không cản trở flow. | US-E02-09 |

## C — E01 Lead Management
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D12** | Quy tắc chấm điểm lead_score (yếu tố & trọng số)? | **P0: HLV gắn cờ "ưu tiên thủ công"**; chấm điểm tự động làm sau (không có công thức ở P0). | US-E01-01, US-E01-05; không cần business-rule chấm điểm ở P0 |
| **D13** | Catalog DMO cụ thể (hình thức kết nối)? | **PO có sẵn catalog (cung cấp sau)** — tạm chưng cất khung placeholder. | US-E01-03; business-rules placeholder |
| **D14** | Copilot làm ấm/mời (AI) — P1 hay P2/P3? | **P1: rule-based** (thư viện kịch bản gắn thẻ DISC + Stage) — đủ cho MVP-2; nâng cấp RAG sau. | US-E01-03, US-E01-05; định hướng AI phân tầng |
| **D15** | Chống trùng lead: SĐT hay + mã giới thiệu/email? | **Duy nhất theo SĐT** (đơn giản, đủ cho P0). | US-E01-02, US-E01-06 |
| **D16** | Nguồn import lead? | **P0: chỉ nhập tay (form)**; import làm sau (chậm trễ vì quyền riêng tư/consent). | US-E01-06 (xuống P2 sau) |

## D — E03 Customer Care
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D17** | Chọn talking point theo Stage hay theo tuần cố định? | **Hybrid** — mặc định theo tuần, HLV có thể đổi talking point phù hợp Stage của KH cụ thể. | US-E03-01; business-rules talking-point |
| **D18** | Catalog 21 talking point + chuyên sâu bệnh lý? | **PO có sẵn 21 talking point (cung cấp sau)** — tạm chưng cất khung placeholder. | US-E03-01; business-rules placeholder |
| **D19** | Nhắc 72h: tự động gửi hay HLV xác nhận? | **Tự động gửi nhắc đến HLV** (push notification); HLV tự thực hiện hành động kết nối rồi đánh dấu hoàn thành. | US-E03-09 |
| **D20** | Metric báo cáo hành trình (tinh thần, thói quen, lan tỏa)? | **Tinh thần** = câu trả lời talking point (2 câu hỏi); **thói quen** = tỷ lệ check-in đúng giờ; **lan tỏa** = số người KH đã chia sẻ/giới thiệu. | US-E03-07 |

## E — E04 Team Operations
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D21** | Ánh xạ 12 bước → DMO "bước tiếp" / Vòng tròn thành công? | **PO có sẵn bản ánh xạ (cung cấp sau)** — tạm chưng cất khung placeholder. | US-E04-02; business-rules placeholder |
| **D22** | Phân quyền xem tuyến dưới: bao nhiêu cấp? | **Tuyến trực tiếp + cấp 2 (cháu)** — đủ cho Vòng tròn thành công. | US-E04-01, US-E04-02 |
| **D23** | "Vòng tròn thành công" là gì? | **= synonym quy trình 12 bước Herbalife** (Bước 1-12: thu hút → nhân bản thành Giám sát viên). Đưa vào glossary. | glossary.md; US-E04-02 |

## F — E05 Self-Development
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D24** | Gamification: tách học tập vs sức khỏe hay gộp? | **Gộp 1 hệ thống điểm chung (credit)** dùng cho cả sức khỏe + học tập — đơn giản hơn. | E05, E06; business-rules gamification |
| **D25** | Sơ đồ trả thưởng: tĩnh hay động? | **Tĩnh** — hiển thị cấu trúc cấp bậc + điều kiện lên cấp cố định (Herbalife cung cấp). P0 đơn giản. | US-E05-02 |
| **D26** | Catalog micro-course 5 mảng? | **PO có sẵn catalog (cung cấp sau)** — tạm chưng cất khung placeholder. | US-E05-01, US-E05-03; business-rules placeholder |

## G — E06 Personal Health
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D27** | Cơ chế streak & credit thưởng (gamification sức khỏe)? | **P0: chỉ điểm check-in (3/2/1/0)**; credit/streak/badge làm sau. | US-E06-01 (giữ điểm check-in); credit/badge sau |
| **D28** | Đồng hồ sinh học — quy tắc tô màu / quản gia ảo? | **Quy tắc đơn giản** — tô màu trạng thái (đã làm/chờ/quá giờ) + gợi ý nhiệm vụ tiếp theo; không làm quản gia ảo phức tạp ở P0. | US-E06-01 |
| **D29** | AI companion chat: proactively hay reactive? | **Proactively gợi ý nhẹ** khi phát hiện KH cần hỗ trợ (bỏ bữa, không check-in) — không phán xét, không thao túng. | US-E06-05 |

## H — Foundation
| ID | Câu hỏi | Quyết định | Tác động |
|---|---|---|---|
| **D30** | 3 persona lõi (tên + avatar)? | **Định nghĩa lại 3 persona mới** (PO cung cấp input sau) — tạm placeholder trong personas.md. | personas.md |

---

## TODO chưng cất tiếp (cần thêm input từ PO)
- **D05**: fetch bảng chuẩn WHO + Tanita → tạo `business-rules/Body-Composition-Standards-v1.0.md`
- **D07**: PO cung cấp mẫu câu 5 nhánh × 4 DISC → điền vào `Objection-Handler-Framework-v1.0.md`
- **D13**: PO cung cấp catalog DMO → điền vào business-rules mới
- **D18**: PO cung cấp 21 talking point → điền vào business-rules mới
- **D21**: PO cung cấp bản ánh xạ 12 bước → điền vào business-rules mới
- **D26**: PO cung cấp catalog micro-course → điền vào business-rules mới
- **D30**: PO cung cấp input 3 persona mới → cập nhật `personas.md`
