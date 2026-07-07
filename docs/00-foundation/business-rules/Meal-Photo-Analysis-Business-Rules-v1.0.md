# BUSINESS RULES — BÓC TÁCH BỮA ĂN TỪ ẢNH & ĐÁNH GIÁ CẤU TRÚC BỮA ĂN
## Dạng Mô Tả BPMN & Decision Tables (Không Code)

**Phiên bản:** v1.0  
**Định dạng:** Business Process & Decision Rules  
**Mục đích:** Mô tả quy trình **luồng ngược** — KH chụp ảnh bữa ăn → AI bóc tách món & khẩu phần → tính Calo & macro → **đánh giá cấu trúc bữa ăn đồng nhất theo Calo** → đối chiếu mục tiêu → gợi ý điều chỉnh.

**Trạng thái:** v1.0 — PO đã chốt mode (A) & quy đổi fiber (xem §IX). **Macro sức khỏe giữ nguyên** theo `Calorie-Meal-Business-Rules-v1.1.md` (không thay thế).

**Liên quan:**
- Macro & mục tiêu Calo: `Calorie-Meal-Business-Rules-v1.1.md` (gốc, không đổi).
- User story: `US-E06-04`, `US-E06-10` (AC2/AC3); SRS `S-KH-LOG-MEAL`, `FR-MEAL-5`; Workflow `Workflow-KH §C.1`.
- Triết lý dự án: **AI đưa ước lượng + confidence; business rules quyết định kết quả** (kiểm chứng được). Mọi AI chỉ chạy khi `ai_data_sharing_enabled = true`; tắt → rơi về nhập tay + template trung tính.

---

## I. QUY ƯỚC QUY ĐỔI ĐƠN VỊ DINH DƯỠNG (Atwater) — *giải gap đơn vị*

> **Gap phát hiện:** `Calorie-Meal-Business-Rules-v1.1.md §2.4` đặt mục tiêu **Carbs/Fat theo % Calo** nhưng **Protein theo g/kg cân nặng** — không đồng nhất đơn vị → không thể trực tiếp đánh giá "cấu trúc bữa ăn" thống nhất theo Calo. Section này bổ sung **lớp quy đổi**, không sửa macro gốc.

### Decision Table 1.1 — Hệ số quy đổi (Atwater general factors)

| Chất | Năng lượng | Ghi chú |
|---|---|---|
| 1 g Carbohydrate | **4 kcal** | Tinh bột/đường tiêu thụ được |
| 1 g Protein | **4 kcal** | |
| 1 g Fat | **9 kcal** | |
| 1 g Fiber | **4 kcal** | **≡ tinh bột** (PO chốt: rau/củ/trái cây tính tương đương cơm trắng) |
| 1 g Alcohol | 7 kcal | Ngoài phạm vi bữa lành mạnh |

### Quy ước thống nhất đánh giá cấu trúc

```
// Fiber ≡ tinh bột (PO) → cùng 4 kcal/g; gộp vào nhóm carb khi đánh giá cấu trúc
Calo_carb    = g_carb    × 4
Calo_fiber   = g_fiber   × 4          // nhóm xơ (rau/củ/trái cây) ≡ cơm trắng
Calo_protein = g_protein × 4
Calo_fat     = g_fat     × 9
Calo_bữa     = Calo_carb + Calo_fiber + Calo_protein + Calo_fat
Calo_carb_group = Calo_carb + Calo_fiber               // fiber gộp nhóm carb
%_carb    = Calo_carb_group / Calo_bữa × 100
%_protein = Calo_protein   / Calo_bữa × 100
%_fat     = Calo_fat       / Calo_bữa × 100
```

> **Quan trọng:** quy đổi này dùng cho **đánh giá cấu trúc bữa (lens)**. Mục tiêu sức khỏe gốc (Protein 0.8–1.2 g/kg, v.v.) **vẫn kiểm tra theo g/kg** ở Process 3.6 — không bị thay thế. **fiberG vẫn theo dõi riêng** cho ràng buộc y khoa (Diabetes fiber ≥30g, kidney hạn chế K-cao qua rau, v.v. — v1.1 §2.4).

---

## II. CÔNG THỨC ĐÁNH GIÁ CẤU TRÚC BỮA ĂN (đồng nhất theo Calo)

> Cho một bữa thật (từ ảnh hoặc nhập tay): tính **cấu trúc % Calo** rồi đối chiếu **mục tiêu cấu trúc Mode A** → ra zone cảnh báo. **Mode A (y khoa chuẩn) là mode duy nhất** — PO đã chốt (§IX).

### Decision Table 2.1 — Mục tiêu cấu trúc: Mode A (y khoa chuẩn, quy đổi từ v1.1)

Mục tiêu cấu trúc được **quy đổi từ macro sức khỏe v1.1** sang % Calo (đồng nhất đơn vị đo):

| Macro | Mục tiêu v1.1 (gốc, không đổi) | Quy đổi sang % Calo (Mode A) |
|---|---|---|
| Protein | 0.8–1.2 g/kg × W | (target_g × 4) / Magic Cal × 100 |
| Carbs (+ fiber) | 45–50% Calo | 45–50% — fiber gộp vào nhóm carb (§I) |
| Fat | 25–35% Calo | 25–35% |

> PO đã chốt: **Mode A là mode duy nhất**. Tỷ lệ 4:3:4 (carb:protein:fat) đã xem xét và **loại** — mâu thuẫn macro y khoa (Protein 27.3% ≈ 1.9–2.3 g/kg vượt 0.8–1.2; Fat 36.4% vượt 25–35%). Xem §IX.
> KH có bệnh lý (kidney/heart/GERD/diabetes) → áp ràng buộc cứng v1.1 §2.3 **trước** khi tính zone (an toàn trước, theo nguyên tắc ưu tiên v1.1 §2.0).

### Process 2.2 — Công thức đánh giá một bữa

```
INPUT: macros thực (g_carb, g_fiber, g_protein, g_fat) + context(bệnh lý)
1. Quy đổi sang Calo: Cc, Cfiber, Cp, Cf  (theo §I; fiber ≡ tinh bột)
2. Calo_bữa = Cc + Cfiber + Cp + Cf
3. %_carb(=Cc+Cfiber), %_protein, %_fat  (theo công thức §I)
4. Lấy target Mode A (DT 2.1) → (t_%carb, t_%protein, t_%fat)
5. Lệch_m = |%_m − t_%m|, m ∈ {carb, protein, fat}   (ngưỡng đồng nhất ±10/25%)
6. Zone = zone xấu nhất trong 3 lệch  (Decision Table 4.2)
7. Nếu có bệnh lý → áp ràng buộc cứng (§3.5) TRƯỚC khi tính zone
OUTPUT: ratioCheck { %carb, %protein, %fat, lệch từng nhóm, zone, mode:"A" }
```

### Ví dụ — Mode A, KH 60kg, Magic Cal 1700, target protein 1.0 g/kg = 60g

Target quy đổi: protein = 60×4 = 240 kcal → 240/1700 = **14.1%**. Lấy fat 30% (giữa 25–35%) → carbs(+fiber) = 100 − 14.1 − 30 = **55.9%**. Vậy target cấu trúc ≈ **Carbs 56% : Protein 14% : Fat 30%**.

Bữa trưa thực (ảnh) — fiber tách riêng (g):
- 150g ức gà: P 46 · carb 0 · fiber 0 · F 1.5
- ½ bát cơm (~100g chín): carb 27 · fiber 1 · P 2.6 · F 0.4
- 1 bát rau luộc (~150g): carb 1 · fiber 4 · P 2 · F 0.3

Quy đổi (fiber ≡ tinh bột, §I):
- Calo_carb_group = (27+1 + 1+4 + 0) × 4 = 33×4 = **132**
- Calo_protein = (46 + 2.6 + 2) × 4 = 50.6×4 = **202.4**
- Calo_fat = (1.5 + 0.4 + 0.3) × 9 = 2.2×9 = **19.8**
- Calo_bữa = 132 + 202.4 + 19.8 = **354.2**

%carb = 37.3 · %protein = 57.1 · %fat = 5.6 → lệch carb −18.7 · protein +43.1 · fat −24.4 → **RED**.

→ **Bài học:** đánh giá per-meal dễ "nhiễu" (đạm tập trung 1 bữa là bình thường). Khuyến nghị: zone per-meal chỉ **mềm**; đánh giá chính thức **theo cả ngày** (Decision Table 4.3) mới phản ánh cấu trúc thật. fiberG cả ngày vẫn phải ≥25–30g (ràng buộc y khoa, v1.1 §2.4).

---

## III. PROCESS 3.0 — LUỒNG NGƯỢC (chụp ảnh → bóc tách → đánh giá)

### Gate 0 — Consent
`ai_data_sharing_enabled = true`? **NO** → fallback **nhập tay + template trung tính** (không gọi AI).

```
┌────────────────────────────────────────────────┐
│ INPUT: ảnh bữa + mealContext + customerId       │
│        + activeMealPlanRef + consent            │
└───────────────────────┬────────────────────────┘
        Gate 0: consent? ──NO──→ Fallback nhập tay
                            YES
                            ▼
3.1 Capture (ảnh + metadata bữa)
                            ▼
3.2 Detect món + phân vùng thành phần (AI)
                            ▼
3.3 Estimate khẩu phần (g/bát/lạng) (AI) → gán confidence
                            ▼
3.4 Tra cứu dinh dưỡng (catalog + hệ số đơn vị) → macro từng món
                            ▼
3.5 Apply ràng buộc cứng (bệnh lý/dị ứng — reuse v1.1 §2.3)
                            ▼
3.6 Đánh giá cấu trúc (§II) + kiểm mục tiêu y khoa (g/kg)
                            ▼
3.7 Decision verdict (DT 4.1) → ACCEPT / CONFIRM / FALLBACK_MANUAL
                            ▼
3.8 Human-in-the-loop: KH xác nhận/sửa → re-compute (re-run 3.6)
                            ▼
3.9 Daily aggregate + đối chiếu Magic Cal & target đạm (DT 4.3)
                            ▼
3.10 Feedback loop: lệch lớn → gợi ý bù bữa kế tiếp (DT 4.4)
                            ▼
OUTPUT: MealNutritionEstimate + dailyAggregate + warnings
```

---

## IV. DECISION TABLES (lớp quyết định — kiểm chứng được)

### 4.1 Verdict theo confidence (AI ước lượng, rules quyết)

| conf_detection | conf_portion | Verdict | Hành động UI |
|---|---|---|---|
| ≥ 0.85 | ≥ 0.70 | **ACCEPT** | Hiện kết quả; KH chỉ "Lưu" (cho phép sửa) |
| ≥ 0.60 | ≥ 0.45 | **CONFIRM** | Hiện + highlight trường yếu; **bắt** KH xác nhận |
| < 0.60 | — | **CONFIRM** | Nhấn mạnh tên món cần KH rà |
| — | < 0.45 | **FALLBACK_MANUAL** | Auto mở form nhập tay + gợi ý món AI đoán |

### 4.2 Zone cảnh báo cấu trúc bữa (mềm — áp khi Calo_bữa ≥ 250 kcal)

| Lệch % mục tiêu (cả 3 nhóm) | Zone | Hiển thị |
|---|---|---|
| ≤ ±10% mỗi nhóm | **GREEN** | "Cân đối" |
| ±10–25% | **YELLOW** | "Hơi lệch nhóm X — lưu ý bữa sau" |
| > ±25% | **RED** | "Lệch rõ nhóm X" + gợi ý bù (DT 4.4) |

> Ràng buộc cứng (bệnh lý/dị ứng, v1.1 §2.3) **ưu tiên hơn** zone: vd kidney không cảnh báo "thiếu protein" mà cảnh báo "vượt hạn chế protein".

### 4.3 Daily aggregate & đối chiếu mục tiêu

| Điều kiện | Trạng thái ngày | Hiển thị |
|---|---|---|
| ΣCalo trong ±10% Magic Cal **và** ΣProtein ≥ 90% target(g/kg) | **TỐT** | Xanh |
| Lệch 10–25% một trong hai | **CẦN LƯU Ý** | Vàng + gợi ý |
| Lệch >25% hoặc ΣProtein <75% target | **LỆCH** | Đỏ + gợi ý điều chỉnh + thông báo HLV |

> Đánh giá cấu trúc (§II) tính **theo cả ngày** mới phản ánh đúng; per-meal chỉ cảnh báo mềm.

### 4.4 Feedback loop (luồng ngược nuôi forward)

| Lệch ngày | Hành động gợi ý bữa kế tiếp (reuse v1.1 Rule 4.1/4.2) |
|---|---|
| ΣProtein < target | Ưu tiên **thêm đạm** bữa kế tiếp |
| ΣCalo > Magic Cal | **Giảm carbs/rau trước**, giữ đạm (v1.1 §4.2) |
| ΣCalo < Magic Cal | **Thêm bữa sáng/F1 trước**, rồi đạm trưa (v1.1 §4.1) |
| Fat % vượt (mode A) | Đổi nguồn fat sang lành mạnh (cá/hạt/dầu ô-liu) |

---

## V. DATA OBJECTS

```
INPUT MealPhotoAnalysisRequest {
  image: ImageRef(1+)
  mealContext: { mealType, mealTime, date }
  customerId, activeMealPlanRef
  userEdits?: List[{dishName, unit, qty}]
  consent: ai_data_sharing_enabled (bool)   // gate cứng
}

OUTPUT MealNutritionEstimate {
  dishes: [{ name, group("PROTEIN"|"FIBER_VITAMIN"|"CARB"),
             detectedUnit, estGrams, confidencePerField,
             source: "AI"|"MANUAL"|"AI_EDITED" }]
  macros: { calories, proteinG, carbsG, fatG, fiberG, satFatG }
  confidence: { overall, detection, portion }   // 0–1
  verdict: "ACCEPT"|"CONFIRM"|"FALLBACK_MANUAL"
  ratioCheck: { carbPct, proteinPct, fatPct, vsTarget, zone, mode }
  dailyAggregate: { cumCalories, cumProteinG, vsMagicCal, vsTargetProtein }
  warnings: List[String]
}
```

---

## VI. CATALOG MÓN & HỆ SỐ ĐƠN VỊ (giải open question `[TBD]`)

```
DishCatalogEntry {
  id, name_vi, aliases[]
  group: "PROTEIN"|"FIBER_VITAMIN"|"CARB"
  per100g: { calories, proteinG, carbsG, fatG, fiberG, satFatG, sodiumMg, gi, potassiumMg }
  units: [{ unit:"bát", defaultGram:200, variance }, { unit:"lạng", defaultGram:100 }, ...]
  diet_tags[], est_cost, availability         // tái dùng trường v1.1 §2.0
}
```

> Hệ số đơn vị (bát/lạng/lon) là **tham số cấu hình theo vùng**, không hard-code — khớp nguyên tắc v1.1 §2.0b. Cần PoC crowd-sourced hoặc đối chiếu nguồn official (Bộ Y tế VN / USDA FoodData).

---

## VII. VALIDATION RULES (an toàn)

| Trường | Min | Max | Action |
|---|---|---|---|
| Ước lượng gram/món | 0 | 2000g | Warn nếu >1000g (chắc sai) |
| Calo bữa | 0 | 3000 | Warn nếu >2000 |
| Protein bữa | 0 | 150g | Warn nếu >100g/bữa |
| Sat fat | 0 | <10% calo bữa | Warn (Heart/GERD cứng hơn: <7%) |
| Số món AI/phảnh | — | — | >12 → yêu cầu xác nhận |

---

## VIII. PoC (giải open question "AI bóc tách cần PoC")

**Giai đoạn 1 — Độ chính xác** trên ~200 ảnh bữa VN thật (có ground-truth gram): đo Top-1 detection, MAE% khẩu phần, phân phối confidence. Xác nhận "điểm gãy" là ước lượng khẩu phần (±20–50%).
**Giai đoạn 2 — ROI adherence**: so nhóm AI vs nhập tay về % ngày đủ đạm/đủ Calo + thời gian log. Sản phẩm hóa chỉ khi AI ≥ nhập tay ở adherence và ≤ 60s/bữa.

---

## IX. QUYẾT ĐỊNH PO & MỞ CÒN

### PO đã chốt
1. **Mode mặc định = A** (y khoa chuẩn, quy đổi từ v1.1) — mode duy nhất, không có mode khác.
2. **Bỏ tỷ lệ 4:3:4** (carb:protein:fat) — mâu thuẫn macro y khoa (Protein 27.3% ≈ 1.9–2.3 g/kg vượt 0.8–1.2; Fat 36.4% vượt 25–35%).
3. **Fiber ≡ tinh bột** = 4 kcal/g — nhóm xơ (rau/củ/trái cây) tính tương đương cơm trắng; gộp vào nhóm carb khi đánh giá cấu trúc. **fiberG vẫn theo dõi riêng** cho ràng buộc y khoa (Diabetes fiber ≥30g, kidney hạn chế K-cao qua rau, v.v. — v1.1 §2.4).
4. **Ngưỡng zone đồng nhất** (±10/25%) cho cả 3 macro — không chặt hơn cho protein.

### Còn mở (chờ PoC / dữ liệu)
5. **Verdict thresholds** (0.85/0.70…) — tune sau PoC Giai đoạn 1 (§VIII).
6. **Catalog nguồn** (crowd-source vs đối chiếu official Bộ Y tế VN / USDA) & bảo trì hệ số đơn vị theo vùng.

---

> **Ghi chú trace:** theo chỉ thị PO, **không cập nhật SRS/user-stories** tại thời điểm này — doc business-rule này đứng độc lập. Tham chiếu ngược từ `US-E06-04`/`US-E06-10`/`S-KH-LOG-MEAL`/`FR-MEAL-5` tới đây sẽ do PO quyết định khi muốn link (hiện các doc đó vẫn ghi open question `[TBD]` / "cần PoC").


