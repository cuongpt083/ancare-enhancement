# E01 — Lead Management

- **Vai trò:** HLV
- **Mục tiêu:** Số hóa Bước 1–2 quy trình 12 bước — quản lý KH tiềm năng (DSKHTN), kết nối làm rõ chân dung (chạy DMO), mời gặp 2-1 để chốt gặp HLV.
- **Nguồn:** feature-tree §2.1.

## Danh sách stories
| ID | Tên ngắn | Ưu tiên |
|---|---|---|
| US-E01-01 | Xem DS KHTN ưu tiên hôm nay | Must |
| US-E01-02 | Tạo lead mới (form định danh) | Must |
| US-E01-03 | Chạy DMO kết nối làm rõ chân dung | Should |
| US-E01-04 | Mời gặp 2-1 / đặt lịch | Should |
| US-E01-05 | Chấm điểm & sắp xếp lead (AI) | Could |
| US-E01-06 | Chống trùng lead / import danh bạ-MXH | Could |

---

### US-E01-01 — Xem DS KHTN ưu tiên hôm nay
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn xem danh sách KH tiềm năng được sắp xếp theo "ưu tiên tiếp cận hôm nay", để biết nên gọi/nhắn ai đầu tiên mà không phải tự suy tính.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có ≥1 lead, When HLV mở màn DS KHTN, Then thấy danh sách (khuôn T2) sắp xếp theo "ưu tiên hôm nay" giảm dần (dựa `lead_score` nội bộ, **không hiện số**).
  - AC2 — Given danh sách, When xem mỗi thẻ, Then thẻ hiện tối đa **2 nhãn** quan trọng (vd "Ưu tiên hôm nay" + giai đoạn Stage); DISC/nguồn/score chi tiết nằm ở màn chi tiết (T4).
  - AC3 — Given danh sách, When HLV bấm "Xem chi tiết", Then mở màn chi tiết lead (T4) với hành động nhanh ≤3 (Gọi · Nhắn · Mời 2-1).
  - AC4 — Given không có lead, When mở màn, Then hiện trạng thái rỗng kèm CTA "Tạo KH tiềm năng".
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-01_danh_sach.png` *(xem bản tham chiếu cũ trong archive/srs/mockups)*
  - Prototype: `docs/04-prototypes/coach/LEAD-01_danh_sach.html` *(chưa tạo)*
  - Khuôn màn: T2
  - Nghiệp vụ: `docs/00-foundation/business-rules/` (chưa có rule chấm điểm — Open question).
- **Open question:** Quy tắc chấm điểm `lead_score` cần đặc tả thành business-rule trong foundation.

---

### US-E01-02 — Tạo lead mới (form định danh)
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn tạo nhanh 1 KH tiềm năng với thông tin định danh tối thiểu, để lưu lead ngay khi đang nói chuyện hoặc vừa gặp, không bỏ sót.
- **Ưu tiên:** Must (P0)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV bấm "Tạo KH tiềm năng" (FAB), When mở form (khuôn T1), Then yêu cầu tối thiểu: Họ tên + SĐT; các trường khác (ngày sinh, giới tính, chiều cao) tùy chọn, gập trong "Thêm thông tin".
  - AC2 — Given nhập đủ Họ tên + SĐT, When bấm "Lưu", Then lead được tạo & tự động kiểm tra trùng SĐT → nếu trùng, gợi ý mở lead cũ thay vì tạo mới.
  - AC3 — Given lead đã tạo, When xem DS KHTN, Then lead mới xuất hiện ở đầu danh sách "mới thêm".
  - AC4 — Given đang nhập, When HLV thoát giữa chừng, Then tự động lưu nháp; lần sau mở lại tiếp tục.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-02_tao_lead.png` *(xem bản tham chiếu cũ)*
  - Prototype: `docs/04-prototypes/coach/LEAD-02_tao_lead.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Có cho phép tạo lead từ import danh bạ điện thoại hay chỉ nhập tay? (xem US-E01-06)

---

### US-E01-03 — Chạy DMO kết nối làm rõ chân dung
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn chạy các DMO (phương pháp vận hành hằng ngày) để kết nối & làm rõ chân dung lead, để biết lead quan tâm gì và chuyển sang mời 2-1 khi đúng thời điểm.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (DMO catalog) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given chi tiết lead (T4), When HLV bấm "Chạy DMO", Then hiện danh sách DMO phù hợp theo Stage-of-Change của lead (vd: kết bạn MXH, mời tham gia nhóm, chia sẻ nội dung).
  - AC2 — Given DMO đã chọn, When HLV đánh dấu hoàn thành, Then cập nhật Stage-of-Change & ghi vào timeline lead.
  - AC3 — Given đủ DMO đã chạy, When lead sẵn sàng, Then gợi ý "Mời gặp 2-1" (chuyển US-E01-04).
  - AC4 — Given DMO có AI copilot, When HLV bật trợ lý, Then gợi ý kịch bản tiếp cận theo DISC + Stage (gợi ý chỉnh sửa được, không auto-gửi).
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-03_dmo.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/LEAD-03_dmo.html` *(chưa tạo)*
  - Khuôn màn: T4 (launch) + T1 (DMO chi tiết)
  - Nghiệp vụ: Persona framework — `docs/00-foundation/personas.md` (Stage-of-Change).
- **Open question:** Catalog DMO cụ thể cần đặc tả (DMO = Daily Method of Operation — các hình thức kết nối).

---

### US-E01-04 — Mời gặp 2-1 / đặt lịch
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn mời lead đến buổi gặp 2-1 (2 người + 1 người dẫn) và đặt lịch tự động, để chốt gặp HLV mà không qua lại nhiều lần.
- **Ưu tiên:** Should (P1)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ✓ · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given lead sẵn sàng, When HLV bấm "Mời 2-1", Then mở form mời (T1) với gợi ý thời gian dựa lịch trống của HLV.
  - AC2 — Given đã chọn thời gian, When gửi mời, Then lead nhận lời mời (qua Zalo/SMS) kèm nút xác nhận tham gia.
  - AC3 — Given lead xác nhận, When đến ngày, Then cả HLV & lead nhận nhắc trước buổi gặp.
  - AC4 — Given sau buổi 2-1, When HLV đánh dấu kết quả, Then cập nhật Stage-of-Change & gợi ý chuyển sang tư vấn (E02) hoặc tiếp tục DMO.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-04_moi_2_1.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/LEAD-04_moi_2_1.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Đặt lịch đồng bộ Google Calendar (xem định hướng Lịch 168)?

---

### US-E01-05 — Chấm điểm & sắp xếp lead (AI)
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn hệ thống tự chấm điểm & sắp xếp lead theo mức độ sẵn sàng, để ưu tiên người có khả năng chuyển đổi cao nhất mà không tự đánh giá chủ quan.
- **Ưu tiên:** Could (P1+ — theo định hướng phân tầng AI)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (rule chấm điểm) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given có lead với dữ liệu DMO + Stage, When hệ thống chấm điểm, Then `lead_score` nội bộ cập nhật; **không** hiện số ra UI (L4) — chỉ dùng để sắp xếp & gán nhãn "Ưu tiên hôm nay".
  - AC2 — Given lead chưa có dữ liệu, When chấm điểm, Then gán nhãn "Chưa đủ thông tin" + gợi ý chạy DMO.
  - AC3 — Given `ai_data_sharing_enabled = false`, When tính điểm, Then dùng rule tĩnh (Stage + recency) thay vì AI — app vẫn chạy.
- **Truy vết:**
  - Mockup: *(không màn riêng — logic nền của US-E01-01)*
  - Prototype: —
  - Khuôn màn: — (backend logic)
  - Nghiệp vụ: Quy tắc chấm điểm cần đặc tả → `docs/00-foundation/business-rules/` (mới).
- **Open question:** Công thức `lead_score` (trọng số Stage, recency, engagement, DISC) cần chốt thành business-rule.

---

### US-E01-06 — Chống trùng lead / import danh bạ-MXH
- **Epic:** E01 — Lead Management
- **Vai trò:** HLV
- **Story:** Là HLV, tôi muốn import lead từ danh bạ/MXH và hệ thống chống trùng tự động, để không tạo lead trùng & nhanh chóng có danh sách làm việc.
- **Ưu tiên:** Could (P2)
- **INVEST:** Independent ✓ · Negotiable ✓ · Valuable ✓ · Estimable ⚠ (nguồn import) · Small ✓ · Testable ✓
- **Acceptance Criteria:**
  - AC1 — Given HLV chọn "Import danh bạ", When chọn nguồn (danh bạ điện thoại / danh sách Zalo), Then hệ thống import & phát hiện trùng theo SĐT.
  - AC2 — Given phát hiện trùng, When có lead cũ, Then gợi ý ghép vào lead cũ thay vì tạo mới.
  - AC3 — Given import xong, When xem DS KHTN, Then lead mới có nhãn "vừa import" & cần HLV xác nhận.
  - AC4 — Given quyền riêng tư, When import, Then yêu cầu consent trước khi truy cập danh bạ.
- **Truy vết:**
  - Mockup: `docs/03-mockups/coach/S-LEAD-06_import.png` *(chưa tạo)*
  - Prototype: `docs/04-prototypes/coach/LEAD-06_import.html` *(chưa tạo)*
  - Khuôn màn: T1
  - Nghiệp vụ: —
- **Open question:** Nguồn import cụ thể (danh bạ native, Zalo API, Facebook friends?) — `[TBD]`.

---

## Open questions epic
- Copilot làm ấm/mời (AI) thuộc P1 hay P2? (theo định hướng: P1 thư viện kịch bản + Stage-of-Change → P3 RAG.)
- Cơ chế chống trùng lead: duy nhất theo SĐT hay + mã giới thiệu?
- Quy tắc chấm điểm `lead_score` cần chốt thành business-rule trong foundation.
