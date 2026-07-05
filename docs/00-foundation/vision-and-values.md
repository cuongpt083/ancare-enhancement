# Tầm nhìn · Sứ mệnh · Giá trị cốt lõi — AnCare DXP

> Chưng cất từ README gốc (lịch sử: commit trước `47905ed`). Đây là bản canonical duy nhất.

## Tầm nhìn

AnCare Digital User Experience Platform (DXP) là nền tảng trải nghiệm số chăm sóc sức khỏe chủ động cho hàng triệu người Việt Nam — trở thành nền tảng chăm sóc khách hàng xuất sắc phục vụ những người quan tâm đến sức khỏe, muốn phát triển bản thân và tìm kiếm cơ hội kinh doanh trong lĩnh vực chăm sóc sức khỏe chủ động.

## Sứ mệnh

AnCare DXP là cầu nối giữa khách hàng tiềm năng, khách hàng hiện tại với hệ sinh thái chăm sóc sức khỏe chủ động của AnCare. Khách hàng được cung cấp kiến thức sức khỏe, trải nghiệm dịch vụ cá nhân hóa, được tư vấn thay đổi thói quen/lối sống và được phát triển bản thân cùng định hướng cơ hội kinh doanh hấp dẫn, nhân văn.

AnCare lấp đầy khoảng trống giữa các app phục vụ HLV Herbalife (VNHUB, Herbalife Learning, Herbalife SHOP) và app phục vụ khách hàng (Herbalife Pro2col) — vì các app hiện tại chưa bám sát trải nghiệm thực tế tại Nhóm dinh dưỡng, chưa hiểu văn hóa & tâm lý nhiều phân khúc khách hàng Việt.

## 4 Giá trị cốt lõi (Module)

1. **Ứng dụng chăm sóc sức khỏe chủ động** — nội dung hữu ích để thay đổi thói quen ăn uống, vận động, quản lý cân nặng; không gian truyền cảm hứng & chia sẻ câu chuyện.
2. **Ứng dụng phát triển bản thân & cơ hội kinh doanh** — kỹ năng mềm/bán hàng/lãnh đạo; phễu thu hút khách, khơi gợi quan tâm giải pháp chăm sóc sức khỏe bền vững & cơ hội khởi nghiệp nhân văn.
3. **Nền tảng giao tiếp & kết nối** — kết nối khách ↔ HLV ↔ thành viên Nhóm dinh dưỡng.
4. **Module phát triển bản thân cho KH và HLV** — gợi ý nội dung/khóa học cá nhân hóa theo sức khỏe, thói quen, mục tiêu, sở thích.

## Định hướng thiết kế (đã chốt)

1. **Bám Quy trình 12 bước kinh doanh** — AnCare là công cụ thực thi quy trình 12 bước (Bước 1–2 thu hút → Bước 6–12 nhân bản thành Giám sát viên).
2. **La bàn quy trình (Process State Model)** là xương sống — số hóa "Sơ đồ dẫn", xác định mỗi người ở bước nào, điều khiển cả 4 module. Cùng GNV (giấy nhắc việc) và DSKHTN tạo bộ 3 công cụ KD số hóa.
3. **Trọng tâm Bước 1–2: Trợ lý phát triển KH (AI-assisted)** — DSKHTN số, chấm điểm lead, copilot làm ấm/mời, phễu + chatbot, đặt lịch 2/1, số hóa buổi trải nghiệm. Engine cá nhân hóa phân tầng theo độ trưởng thành dữ liệu (P1→P4). **AI hỗ trợ, không thay người.**
4. **Kết nối khách ↔ HLV theo công sức (Content-Attribution Matching)** — HLV chia sẻ nội dung kèm mã giới thiệu → khách tự gắn về HLV; thuật toán chỉ phân phối lead "mồ côi". Khách luôn được quyền chọn/đổi HLV.
5. **Độc lập, không trùng lặp Herbalife apps** — không tích hợp kỹ thuật với VNHUB/Learning/SHOP/Pro2col; không làm POS bán lẻ, quản lý kho, dashboard quản trị kinh doanh.
6. **Số hóa MLM có rà soát rủi ro** — 15 rủi ro đã rà soát. Nguyên tắc giảm thiểu: **trao quyền không thâu tóm; AI hỗ trợ không thay người & không thao túng; tuân thủ là ràng buộc thiết kế; minh bạch & quyền người dùng; cấu hình được; thắng nhỏ tạo niềm tin trước khi mở rộng.**

## Giới hạn phạm vi (Non-goals)

- **Không** làm POS bán lẻ, quản lý kho, dashboard quản trị kinh doanh (thuộc VNHUB).
- **Không** tích hợp kỹ thuật với VNHUB / Herbalife Learning / SHOP / Pro2col (chỉ bổ trợ phạm vi).
- AI **hỗ trợ, không thay** con người ở vòng quyết định; **không thao túng**; mọi xử lý dữ liệu cá nhân tuân thủ consent.

## Lộ trình MVP (tham chiếu)

- **MVP-1** — Nền tảng PSM + Lan tỏa & Gắn kết: La bàn quy trình/GNV, chia sẻ câu chuyện thành công, nhắc nhở chủ động, phễu (DSKHTN số, đặt lịch 2/1).
- **MVP-2** — Học tập, Nội dung & AI hỗ trợ chuyển đổi: Module Đào tạo micro-course + gamification; copilot làm ấm/mời; attribution nội dung; pipeline 12 bước.
- **MVP-3** — Phễu lạnh, Matching fallback, Cá nhân hóa, Nhân bản & Sự nghiệp.
- **Sau MVP-3** — lớp tối ưu AI (uplift + Next-Best-Action) khi đủ dữ liệu.
