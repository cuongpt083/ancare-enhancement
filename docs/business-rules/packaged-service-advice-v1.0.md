# **BUSINESS RULES — ĐỀ XUẤT GÓI GIẢI PHÁP (PACKAGED SERVICE ADVICE)**
## Dạng Mô Tả BPMN & Decision Tables (Không Code)

**Phiên bản:** v1.0 (draft — *cần bổ sung dữ liệu thực tế*)
**Định dạng:** Business Process & Decision Rules
**Mục đích:** Đặc tả logic hệ thống dùng để **đề xuất gói giải pháp** và **tính % mục tiêu đạt được** cho KH tiềm năng, căn cứ trên **mục tiêu · thời gian trải nghiệm mong muốn · chân dung khách hàng**.
**Liên quan:**
- Màn "Thiết lập mục tiêu": `docs/to-be/Workflow-HLV.md §A.1.4`.
- Chân dung KH & dữ liệu: `docs/technical/customer-persona-data-model_v1.0.md`, `docs/to-be/customer-persona-disc-framework_v1.0.md`.
- Tính calo & lộ trình: `docs/business-rules/Calorie-Meal-Business-Rules-v1.0.md`.

> 🔶 **Các ô đánh dấu `‹CẦN BỔ SUNG›`** là nơi đội nghiệp vụ phải điền dữ liệu thật (catalog gói, ngưỡng, hệ số). Tài liệu cung cấp **khung quy tắc**; số liệu minh họa chỉ để mô tả cấu trúc.

---

## I. INPUT / OUTPUT

**INPUT:**
| Nhóm | Trường | Nguồn |
|---|---|---|
| Mục tiêu | `primary_goal`, danh sách mục tiêu + `desired_timeframe` mỗi mục tiêu, mục tiêu ưu tiên | `customer_personas` (màn Thiết lập mục tiêu) |
| Chỉ số | Tanita (cân nặng, mỡ, BMI, mỡ nội tạng…), khoảng cách tới ngưỡng chuẩn | `health_profiles.tanita_data` |
| Chân dung | `disc_primary`, `stage`, `budget_sensitivity`, `objections`, thói quen, bệnh lý | `customer_personas.persona_data` |
| Ràng buộc | tốc độ thay đổi an toàn, bệnh lý cần thận trọng | tài liệu này + Calorie-Meal Rules |

**Cấu trúc GÓI (2 chiều tách biệt):**
- **`package_name`** — đại diện **bộ sản phẩm hỗ trợ** KH được hưởng (vd Khởi đầu / Tăng cường / Toàn diện). Độc lập với thời gian.
- **`duration_months`** — **thời gian mua** (1 / 2 / 3 tháng), **mặc định 3 tháng** để có kết quả tốt nhất. Đây là biến điều khiển `cap`/% (duration = months × 30 ngày).
- **`route_days`** — **số ngày lộ trình**, suy từ **mục tiêu KH chọn** (thời hạn mong muốn); hiển thị thông tin & dùng cho thiết kế lộ trình.

**OUTPUT:**
- `recommended_package_name` + `recommended_duration_months` — **chỉ tên & thời gian**, không hiện chi tiết/giá trên app.
- `achievable_pct` — % mục tiêu đạt được trong `desired_timeframe`.
- `feasibility_flag` — `FEASIBLE` / `CHALLENGING` / `UNSAFE`.
- `rationale` — lý do chọn (để HLV xem & giải thích), kèm bằng chứng chỉ số.

---

## II. BUSINESS PROCESS FLOW — ĐỀ XUẤT GÓI

```
┌──────────────────────────────────────────────┐
│ INPUT: mục tiêu + desired_timeframe + persona │
└───────────────────┬──────────────────────────┘
                    ▼
        ┌───────────────────────────┐
        │ B1. Tính KHỐI LƯỢNG THAY  │
        │ ĐỔI cần thiết (gap)        │  vd: giảm 5 kg, mỡ nội tạng 8→4
        └───────────┬───────────────┘
                    ▼
        ┌───────────────────────────┐
        │ B2. Tính TỐC ĐỘ AN TOÀN   │  (Decision Table 1)
        │ theo mục tiêu + bệnh lý    │
        └───────────┬───────────────┘
                    ▼
        ┌───────────────────────────┐
        │ B3. Đối chiếu THỜI HẠN     │  achievable = tốc_độ × thời_hạn
        │ mong muốn → % đạt được     │  pct = achievable / gap
        └───────────┬───────────────┘
            ┌───────┴────────┐
       pct≥100%          pct<100%
            ▼                ▼
   ┌────────────────┐  ┌─────────────────────────┐
   │ FEASIBLE       │  │ CHALLENGING (hiện %)     │
   └───────┬────────┘  │ + gợi ý kéo dài thời gian│
           │           └───────────┬─────────────┘
           └───────────┬───────────┘
                       ▼
        ┌───────────────────────────┐
        │ B4. CHỌN GÓI theo thời hạn │  (Decision Table 2)
        │ + mục tiêu + mức cam kết   │
        └───────────┬───────────────┘
                    ▼
        ┌───────────────────────────┐
        │ B5. ĐIỀU CHỈNH theo CHÂN   │  (Decision Table 3)
        │ DUNG (DISC/Stage/ngân sách)│  → tinh chỉnh gói & cách trình bày
        └───────────┬───────────────┘
                    ▼
        ┌───────────────────────────┐
        │ OUTPUT: tên gói + % + lý do│
        └───────────────────────────┘
```

---

## III. DECISION TABLES

### Decision Table 1 — Tốc độ thay đổi an toàn (theo mục tiêu)

| Mục tiêu | Tốc độ an toàn khuyến nghị | Trần an toàn | Ghi chú |
|---|---|---|---|
| Giảm cân | `‹CẦN BỔ SUNG›` (vd 0.5–1.0 kg/tuần) | ≤ `‹X›` kg/tuần | Không giảm quá nhanh; theo Calorie-Meal Rules |
| Giảm mỡ nội tạng | `‹CẦN BỔ SUNG›` | — | Gắn với giảm cân + vận động |
| Tăng cơ | `‹CẦN BỔ SUNG›` (vd 0.25–0.5 kg cơ/tuần) | — | Chậm hơn giảm mỡ |
| Cải thiện tuổi sinh học | `‹CẦN BỔ SUNG›` | — | Hệ quả của nhiều chỉ số → dài hạn |
| Kiểm soát đường huyết / khác | `‹CẦN BỔ SUNG›` | — | Có thể cần lưu ý y tế |

> Nếu có **bệnh lý cần thận trọng** (`pain_points`/ghi chú y tế) → giảm trần tốc độ và gắn cờ cần tư vấn chuyên gia (không chẩn đoán).

### Decision Table 2a — Chọn TÊN GÓI (bộ sản phẩm) theo mục tiêu/độ phức tạp

| Mức gap / số mục tiêu | Tên gói đề xuất | Điều kiện |
|---|---|---|
| nhỏ / 1 mục tiêu | `‹Gói Khởi đầu›` | Nhu cầu cơ bản |
| vừa / nhiều mục tiêu | `‹Gói Tăng cường›` | Cần nhiều sản phẩm hỗ trợ hơn |
| lớn / toàn diện | `‹Gói Toàn diện›` | Mục tiêu thách thức, đa chỉ số |

### Decision Table 2b — Chọn THỜI GIAN (thời gian mua)

| Thời gian | Khi nào đề xuất |
|---|---|
| 1 tháng | KH muốn thử ngắn / ngân sách hạn chế |
| 2 tháng | Mục tiêu vừa |
| **3 tháng (mặc định)** | **Đề xuất mặc định — để có kết quả tốt nhất** |

> **Số ngày lộ trình (`route_days`)** suy từ **thời hạn mong muốn theo mục tiêu** KH chọn; hiển thị riêng. `% đạt được` tính theo `duration_months × 30`.
> 🔶 `‹CẦN BỔ SUNG›` **Catalog thực tế**: tên gói ↔ bộ sản phẩm, các mốc thời gian, (giá — nội bộ, không hiện app). Map `coaching_packages`.

### Decision Table 3 — Điều chỉnh theo chân dung khách hàng

| Yếu tố chân dung | Ảnh hưởng tới đề xuất | Hành động |
|---|---|---|
| `budget_sensitivity = cao` | Tránh gói dài/đắt ngay từ đầu | Ưu tiên gói trải nghiệm ngắn làm bước đệm |
| `stage = contemplation` (đang cân nhắc) | Chưa nên gói cam kết dài | Đề xuất gói trải nghiệm + nuôi dưỡng |
| `stage = preparation/action` | Sẵn sàng cam kết | Có thể đề xuất gói dài hơn |
| `disc_primary = D` | Muốn kết quả nhanh | Nhấn lộ trình ngắn, mốc rõ |
| `disc_primary = C` | Cần bằng chứng | Kèm cơ sở khoa học của lộ trình |
| `disc_primary = I` | Theo cảm xúc/cộng đồng | Nhấn trải nghiệm & cộng đồng |
| `disc_primary = S` | Cần an toàn, từng bước | Bắt đầu nhẹ, nhấn đồng hành |

> DISC/Stage **không đổi gói lõi** mà điều chỉnh **lựa chọn giữa các gói gần nhau + cách trình bày**. Chỉ áp dụng khi `ai_data_sharing_enabled = true`.

---

## IV. TÍNH % MỤC TIÊU ĐẠT ĐƯỢC (achievable_pct)

```
gap            = |giá_trị_hiện_tại − mục_tiêu|
safe_rate      = Decision Table 1 (theo mục tiêu + bệnh lý)
duration_weeks = desired_timeframe / 7
achievable     = min(gap, safe_rate × duration_weeks)
achievable_pct = round(achievable / gap × 100)
```

| achievable_pct | feasibility_flag | Hiển thị |
|---|---|---|
| ≥ 100% | FEASIBLE | "Đạt 100% mục tiêu trong thời gian chọn" |
| `‹ngưỡng›`–99% | CHALLENGING | Hiện **% đạt được** + gợi ý kéo dài thời gian |
| < `‹ngưỡng›` hoặc vượt trần an toàn | UNSAFE | Khuyến nghị điều chỉnh mục tiêu/thời hạn; có thể cần chuyên gia |

> 🔶 `‹CẦN BỔ SUNG›` ngưỡng phân loại CHALLENGING/UNSAFE.

### IV.1 Điều chỉnh mục tiêu để tối đa khả năng đáp ứng của gói

Để gói trải nghiệm đáp ứng **100%** trong thời hạn KH chọn, cho phép **giảm tính thách thức của mục tiêu**:

```
cap            = safe_rate × duration_weeks         (mức khả thi an toàn)
nếu target_set > cap  →  CHALLENGING (achievable_pct < 100)
hành động: hạ target_set về ≤ cap  →  achievable_pct = 100% (FEASIBLE)
```

- `adjusted_target` (mục tiêu sau điều chỉnh) ≤ `cap`; lưu vào `persona_data.aim.adjusted_target`.
- Không bao giờ **nâng** mục tiêu vượt `cap` (vi phạm tốc độ an toàn).
- Hai đòn bẩy đưa về FEASIBLE: (a) **giảm mục tiêu** trong cùng thời hạn, hoặc (b) **kéo dài thời hạn** giữ nguyên mục tiêu. Engine ưu tiên đề xuất theo `stage`/`budget_sensitivity` (Decision Table 3).

### IV.2 Hai đòn bẩy trên màn hình (gói = chính, mục tiêu = phụ)

Trên màn "Thiết lập mục tiêu", việc đạt FEASIBLE được điều khiển bằng 2 đòn bẩy:

| Đòn bẩy | Vai trò | Tác động |
|---|---|---|
| **Chọn gói** (chính) | Cố định **thời lượng/cường độ** (`duration`) | Đổi gói → `cap` đổi cho **mọi mục tiêu** → **tính lại % cho toàn bộ mục tiêu** cùng lúc |
| **Tinh chỉnh mục tiêu** (phụ) | Hạ `target_set` từng mục tiêu | Chỉ ảnh hưởng % của **mục tiêu đó**; đưa về ≤ `cap` → 100% |

- Mỗi mục tiêu `i`: `cap_i = safe_rate_i × (duration / 7)`; `pct_i = min(target_set_i, cap_i) / target_set_i × 100`.
- Gói "Đề xuất" = kết quả Decision Table 2 (mặc định); người dùng có thể **override** bằng cách chọn gói khác.

### IV.3 Liên kết đầu ra → Tính & gợi ý bữa ăn

Mục tiêu **cân nặng sau điều chỉnh** (`adjusted_target` của mục tiêu giảm/tăng cân) là **đầu vào bắt buộc** cho chức năng *Tính Calo & gợi ý bữa ăn*:

```
Δweight (kg) + duration  →  tốc độ thay đổi/tuần
                         →  thâm hụt/thặng dư Calo/ngày
                         →  số Calo/ngày + số bữa/ngày  (Calorie-Meal-Business-Rules)
```

→ Khi `adjusted_target` cân nặng thay đổi (do chọn gói khác hoặc tinh chỉnh), **phải tính lại** gợi ý bữa ăn. Tham chiếu: `docs/business-rules/Calorie-Meal-Business-Rules-v1.0.md`.

---

## V. RÀNG BUỘC & NGUYÊN TẮC

- **An toàn trên hết:** không đề xuất lộ trình vượt tốc độ an toàn; bệnh lý → thận trọng + gợi ý chuyên gia (không chẩn đoán y tế).
- **Minh bạch với HLV:** luôn trả `rationale` + bằng chứng chỉ số để HLV giải thích & quyết định cuối.
- **Không hiển thị chi tiết/giá gói trên app:** chỉ tên gói; chi tiết do HLV chia sẻ trực tiếp.
- **Consent:** phần cá nhân hóa theo chân dung chỉ chạy khi `ai_data_sharing_enabled = true`.
- **Tách bạch nghiệp vụ vs trình bày:** quy tắc chọn gói (tài liệu này) độc lập với tông giọng tư vấn (DISC ở framework persona).

---

## VI. HẠNG MỤC CẦN ĐỘI NGHIỆP VỤ BỔ SUNG

1. `‹Catalog gói›` — danh sách gói thật (tên, thời lượng, mục tiêu phù hợp, mức cam kết) → map `coaching_packages`.
2. `‹Tốc độ an toàn›` theo từng mục tiêu (Decision Table 1).
3. `‹Ngưỡng %›` phân loại FEASIBLE/CHALLENGING/UNSAFE.
4. `‹Quy tắc ưu tiên›` khi KH có nhiều mục tiêu mâu thuẫn (vd vừa giảm cân vừa tăng cơ).
5. `‹Nội dung Lợi ích chương trình›` (database hay tĩnh) hiển thị ở màn Lộ trình.

---
*Draft v1.0 — khung quy tắc, chờ dữ liệu nghiệp vụ thực tế để hoàn thiện.*
