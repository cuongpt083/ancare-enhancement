---
name: ancare-project
description: Bối cảnh dự án ancare-enhancement (GAP analysis app An-Care Herbalife Nutrition Club)
metadata: 
  node_type: memory
  type: project
  originSessionId: dbf1a0a9-f5f0-4a51-9acd-88faf69dfdd1
---

Dự án "ancare-enhancement": dùng quy trình As-is → To-be → GAP → To-do để cải tiến app An-Care (CRM + theo dõi sức khỏe cho Nutrition Club Herbalife). Quy trình brainstorm dùng skill sp-instructor-agent (SMART POLE).

**As-Is (chốt, doc: docs/as-is/As-Is study report_v1.0.md, đã lên v1.1):**
- App giai đoạn production có user thử nghiệm, KHÔNG có số liệu baseline.
- Chỉ có app cho HLV (5 tab: Trang chủ, Team, Chat, HLV, Hồ sơ). CHƯA có giao diện khách hàng — khách dùng sổ giấy để lại club.
- 3 persona: Nhà sáng lập (kinh doanh), Nhà vận hành = chính là persona HLV trong app, Khách hàng (member/vãng lai).

**TRẠNG THÁI: Đã hoàn tất chuỗi tài liệu As-Is → To-be → GAP → To-do → Feasibility (tất cả .md trong docs/).**
- docs/as-is/As-Is study report_v1.0.md (đã lên v1.1)
- docs/to-be/To-be brainstorm notes.md + docs/to-be/To-be study report_v1.0.md
- docs/gap/GAP analysis report_v1.0.md (20 GAP: N1-2, H1-6, K1-4, F1a-F5, D1-2)
- docs/to-do/To-do recommendations_v1.0.md (18 hạng mục TD-1.x→TD-3.x, có DoD + phụ thuộc)
- docs/feasibility/Feasibility study_v1.0.md

**Feasibility (chốt):** ~192 yêu cầu / 17 phân hệ / 6 actor / 3 kênh. Cloud. KHẢ THI kỹ thuật. ~11 tháng (10-12). Chi phí ~3,8-5,7 tỷ VND (điểm ~4,75 tỷ), chưa gồm cloud định kỳ ~15-40tr/tháng. Đội đỉnh ~10-11 người. App khách dùng React Native; app HLV nâng cấp; web Founder React. 2 hạng mục cần PoC: đồng bộ dữ liệu lai Tanita, sinh infographic. Khuyến nghị: chạy GĐ0 PoC trước, cổng quyết định sau MVP-2 mới giải ngân MVP-3.

**To-be (chi tiết, notes: docs/to-be/To-be brainstorm notes.md):**
- HLV: POS quét mã vạch (P1), kho gắn danh tính người xuất (P2), hồ sơ hành trình timeline+cột mốc (P3), cầu nối nhắc nhở 2 chiều (P4), chia sẻ tự động (P5), rút gọn khảo sát DISC.
- Khách hàng: sổ sức khỏe số (tự log tại nhà + Tanita đồng bộ từ club), nhắc nhở kết hợp HLV/khách, chia sẻ MXH tự động, onboarding do HLV mời, giữ chân = đồ thị cảm xúc + gamification + cộng đồng.
- Nhà sáng lập: dashboard riêng (1 hoặc nhiều club), tài chính 3 tầng (thu/chi→lời/lỗ→dự báo), chân dung KH (giá trị/gắn bó/kênh), tồn kho, CRM chăm sóc kết hợp.
- 2 foundation phải làm trước: catalog sản phẩm có mã vạch; app khách + mô hình tài khoản liên kết HLV–Khách.
- Quyết định phạm vi lớn: đợt này mở rộng thành hệ sinh thái đa app (HLV + Khách + Dashboard Founder).

**Lộ trình MVP đã chốt:** MVP-1 "Vận hành không thất thoát" (catalog mã vạch + POS P1 + kho P2 + thu/chi cơ bản F1); MVP-2 "Số hóa hồ sơ & quản trị" (P3 + UX DISC + dashboard Founder F1-F4 đầy đủ); MVP-3 "Hệ sinh thái khách hàng" (app khách + C1/C2/C3 + P4/P5). Thước đo chính: hiệu quả vận hành, cài đo lường từ MVP-1.

Bước kế tiếp khả dĩ: thiết kế chi tiết UX/UI từng màn hình; kế hoạch đo lường baseline trước khi dev; bản .docx của các báo cáo nếu cần trình stakeholder; lập kế hoạch GĐ0/PoC. (Ngôn ngữ tài liệu: tiếng Việt. Định dạng đang dùng: Markdown.)
