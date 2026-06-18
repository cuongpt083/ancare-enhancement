# **BUSINESS RULES — TÍNH CALO KỲ DIỆU & LẬP GỢI Ý BỮA ĂN**
## Dạng Mô Tả BPMN & Decision Tables (Không Code)

**Phiên bản:** v1.0  
**Định dạng:** Business Process & Decision Rules  
**Mục đích:** Mô tả quy trình tính Calo & lập gợi ý bữa ăn dưới dạng BPMN-style process flows & decision tables

---

## I. BUSINESS PROCESS FLOW — TÍNH CALO KỲ DIỆU

### Process 1.1: Tính Năng Lượng Nghỉ Ngơi (RMR/BMR)

```
┌─────────────────────────────────────────────────┐
│  INPUT: HealthProfile                           │
│  - Gender, Age, Weight, Height                  │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Xác định Giới tính?   │
        └────┬───────────────┬───┘
             │ FEMALE        │ MALE
             ▼               ▼
    ┌─────────────────┐  ┌──────────────────┐
    │ RMR = 10×W +   │  │ RMR = 10×W +    │
    │ 6.25×H - 5×A  │  │ 6.25×H - 5×A + 5│
    │ - 161          │  │                  │
    └────────┬────────┘  └────────┬─────────┘
             │                    │
             └────────┬───────────┘
                      │
                      ▼
          ┌─────────────────────────┐
          │  RMR < 1000 kcal?       │
          └────┬──────────────────┬─┘
           YES │                  │ NO
               ▼                  ▼
          ┌─────────────┐    ┌──────────────┐
          │ RMR = 1000  │    │ RMR accepted │
          │ (warning!)  │    │              │
          └──────┬──────┘    └──────┬───────┘
                 │                  │
                 └────────┬─────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │ OUTPUT: RMR (kcal/day)   │
              └──────────────────────────┘
```

**Business Rules — RMR Calculation:**

| Giới Tính | Công Thức | Ghi Chú |
|-----------|-----------|---------|
| Nữ | RMR = 10×Cân nặng + 6.25×Chiều cao - 5×Tuổi - 161 | Harris-Benedict |
| Nam | RMR = 10×Cân nặng + 6.25×Chiều cao - 5×Tuổi + 5 | Harris-Benedict |

**Constraints:**
- RMR tối thiểu: 1000 kcal/ngày (cảnh báo nếu dưới)
- RMR tối đa: 4000 kcal/ngày (warning)

---

### Process 1.2: Tính Năng Lượng Hoạt Động Hàng Ngày (AMR)

```
┌──────────────────────────────────────────┐
│  INPUT: RMR, Gender                      │
└────────────────────┬─────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Xác định Giới tính?   │
        └────┬───────────────┬───┘
             │ FEMALE        │ MALE
             ▼               ▼
    ┌─────────────────┐  ┌──────────────┐
    │ AMR = RMR × 0.25│  │ AMR =RMR × 0.30│
    └────────┬────────┘  └────────┬─────┘
             │                    │
             └────────┬───────────┘
                      │
                      ▼
              ┌──────────────────────────┐
              │ OUTPUT: AMR (kcal/day)   │
              └──────────────────────────┘
```

**Business Rule — AMR Calculation:**

| Giới Tính | Hệ Số | Công Thức |
|-----------|-------|-----------|
| Nữ | 0.25 | AMR = RMR × 0.25 |
| Nam | 0.30 | AMR = RMR × 0.30 |

---

### Process 1.3: Tính Năng Lượng Thể Dục (Ex)

```
┌─────────────────────────────────────────────┐
│  INPUT: Exercise Profile                    │
│  - Exercise Daily? (Y/N)                    │
│  - Exercise Type, Minutes/day               │
│  - Weight, Gender                           │
└────────────────────┬────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  Có tập luyện hàng ngày?   │
        └────┬──────────────────┬────┘
             │ NO               │ YES
             ▼                  ▼
        ┌─────────────┐    ┌──────────────────┐
        │ Ex = 0 kcal │    │ Xác định loại    │
        │             │    │ tập luyện?       │
        └──────┬──────┘    └────┬────────┬────┘
               │           CARDIO│       │STRENGTH/MIXED
               │                ▼       ▼
               │         ┌─────────┐  ┌──────────┐
               │         │ Rate=   │  │ Rate=    │
               │         │0.10×W   │  │0.08×W    │
               │         │kcal/min │  │kcal/min  │
               │         └────┬────┘  └────┬─────┘
               │              │           │
               │              └─────┬─────┘
               │                    │
               │         Ex = Rate × Minutes/day
               │                    │
               └────────┬───────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │  OUTPUT: Ex (kcal/day)        │
        │  (0 nếu không tập luyện)      │
        └───────────────────────────────┘
```

**Business Rules — Exercise Calories:**

| Loại Tập Luyện | Calo/phút | Công Thức |
|-----------------|-----------|-----------|
| Cardio (chạy, xe đạp) | 0.10 × Cân nặng (kg) | Ex = 0.10×W×Minutes |
| Strength (tạ, yoga) | 0.08 × Cân nặng (kg) | Ex = 0.08×W×Minutes |
| Mixed | 0.09 × Cân nặng (kg) | Ex = 0.09×W×Minutes |

**Constraint:**
- Chỉ tính nếu `exerciseDaily = TRUE` và `exerciseMinutes > 0`
- Nếu không, `Ex = 0`

---

### Process 1.4: Tính Tổng Năng Lượng Tiêu Hao (TMR)

```
┌──────────────────────────────────────┐
│  INPUT: RMR, AMR, Ex                 │
└────────────────┬──────────────────────┘
                 │
                 ▼
        ┌─────────────────────────┐
        │ TMR = RMR + AMR + Ex    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Validate TMR >= 1200?   │
        └────┬──────────────────┬─┘
         YES │                  │ NO
             ▼                  ▼
        ┌──────────┐      ┌─────────────────┐
        │ TMR OK   │      │ TMR = 1200      │
        │          │      │ (warning issued)│
        └────┬─────┘      └────────┬────────┘
             │                     │
             └────────┬────────────┘
                      │
                      ▼
        ┌─────────────────────────────┐
        │ OUTPUT: TMR (kcal/day)      │
        └─────────────────────────────┘
```

**Business Rule — TMR Calculation:**
- **Formula:** TMR = RMR + AMR + Ex
- **Minimum:** TMR ≥ 1200 kcal/day (enforce)
- **Maximum:** TMR ≤ 5000 kcal/day (warning)

---

### Process 1.5: Xác Định Calo Kỳ Diệu Cuối Cùng (Magic Calories)

```
┌──────────────────────────────────────────┐
│  INPUT: TMR, Goal, Age, Current BMI      │
└─────────────────┬────────────────────────┘
                  │
                  ▼
     ┌────────────────────────────┐
     │  Mục tiêu là gì?           │
     └──┬─────────┬──────┬────────┘
   LOSE │ GAIN  │MAINTAIN│REJUVENATE
        ▼        ▼       ▼         ▼
   ┌─────────┐┌──────┐┌──────┐┌────────────┐
   │Giảm cân ││Tăng  ││Giữ   ││Trẻ hóa     │
   │         ││cân   ││cân   ││            │
   └────┬────┘└──┬───┘└──┬───┘└─────┬──────┘
        │        │      │          │
        ▼        ▼      ▼          ▼
   ┌─────────────────────────────────────────┐
   │  Tính toán Adjustment                   │
   └─────────────────────────────────────────┘
                 │
                 ▼
   ┌─────────────────────────────────────────┐
   │  Magic Calories = TMR + Adjustment      │
   └─────────────────────────────────────────┘
                 │
                 ▼
   ┌─────────────────────────────────────────┐
   │  Magic Calories < 1000?                 │
   └──┬───────────────────────────────────┬──┘
    YES                                  NO
      │                                   │
      ▼                                   ▼
   ┌──────────────┐           ┌───────────────────┐
   │ ERROR!       │           │ Magic Calories OK │
   │ Set = 1000   │           │                   │
   │ + WARNING    │           │                   │
   └──────┬───────┘           └────────┬──────────┘
          │                            │
          └──────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────────┐
    │ OUTPUT: Magic Calories + Notes       │
    │ - Weekly deficit/surplus             │
    │ - Estimated weight change            │
    │ - Medical adjustments                │
    │ - Water intake advisory              │
    └──────────────────────────────────────┘
```

**Business Rules — Magic Calories Adjustment:**

| Mục Tiêu | Điều Kiện | Công Thức | Ghi Chú |
|----------|-----------|-----------|---------|
| **LOSE_WEIGHT** | Age ≥ 40 | Magic Cal = TMR - 300 | Thâm hụt 2100 kcal/tuần → ~0.27 kg/tuần |
| **LOSE_WEIGHT** | Age < 40 | Magic Cal = TMR - 500 | Thâm hụt 3500 kcal/tuần → ~0.45 kg/tuần |
| **GAIN_WEIGHT** | Age ≥ 40 | Magic Cal = TMR + 300 | Thặng dư 2100 kcal/tuần → ~0.27 kg/tuần |
| **GAIN_WEIGHT** | Age < 40 | Magic Cal = TMR + 500 | Thặng dư 3500 kcal/tuần → ~0.45 kg/tuần |
| **MAINTAIN** | Any | Magic Cal = TMR | Giữ nguyên cân nặng |
| **REJUVENATE** | Any | Magic Cal = TMR | Focus vào chất lượng, protein, antioxidant |

**Constraints:**
- Magic Calories ≥ 1000 kcal/day (enforce, warning nếu adjust)
- Magic Calories ≤ 4500 kcal/day (warning)

---

### Process 1.6: Điều Chỉnh Bệnh Lý

```
┌─────────────────────────────────┐
│  INPUT: Magic Calories,         │
│  Medical Conditions             │
└────────────────┬────────────────┘
                 │
                 ▼
    ┌────────────────────────────┐
    │  Có bệnh lý nào không?     │
    └────┬──────────────────┬────┘
     NO  │                  │ YES
         ▼                  ▼
    ┌──────────┐      ┌───────────────────┐
    │ No adj   │      │ Loop qua từng     │
    │ needed   │      │ bệnh lý           │
    └────┬─────┘      └─────────┬─────────┘
         │                      │
         │              ┌───────▼────────┐
         │              │ KIDNEY:        │
         │              │ Cal = Weight   │
         │              │ × 32 kcal/kg   │
         │              └────────┬───────┘
         │                       │
         │              ┌────────▼────────┐
         │              │ LUNG:           │
         │              │ Cal += 15%      │
         │              └────────┬────────┘
         │                       │
         │              ┌────────▼────────┐
         │              │ DIABETES:       │
         │              │ (No cal change) │
         │              │ But: Low GI     │
         │              │ requirement     │
         │              └────────┬────────┘
         │                       │
         │              ┌────────▼────────┐
         │              │ HTN/HEART/etc   │
         │              │ (No cal change) │
         │              └────────┬────────┘
         │                       │
         └───────┬───────────────┘
                 │
                 ▼
    ┌──────────────────────────────┐
    │ OUTPUT: Adjusted Magic Cal   │
    │ + Medical Notes              │
    └──────────────────────────────┘
```

**Business Rules — Medical Adjustments:**

| Bệnh Lý | Điều Chỉnh Calo | Constraints |
|---------|-----------------|-------------|
| **KIDNEY (Stage 3-5)** | Cal = Weight × 32 kcal/kg | Protein 0.6-0.8g/kg; Sodium/K hạn chế |
| **LUNG** | Cal += 15% (để duy trì weight) | Antioxidant ↑; Omega-3 ↑ |
| **DIABETES** | Cal = TMR (no change) | Low GI carbs; Fiber 30g |
| **HYPERTENSION** | Cal -= 10% (if overweight) | Sodium <1500mg; K/Mg/Ca ↑ |
| **HEART** | Cal = TMR (no change) | Sat fat <7%; Cholesterol <200mg |
| **GERD** | Cal = TMR (no change) | Bữa nhỏ, tránh trigger |

---

### Process 1.7: Khuyến Cáo Uống Nước

```
┌──────────────────────────────┐
│  INPUT: Weight, Goal         │
└────────────────┬─────────────┘
                 │
                 ▼
    ┌─────────────────────────────┐
    │ Min Water = Weight/10 × 0.4 │
    │ (Minimum: 0.4L/10kg)        │
    └────────────────┬────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Goal = LOSE_WEIGHT?    │
        └────┬──────────────┬────┘
        NO   │              │ YES
             ▼              ▼
        ┌────────┐    ┌──────────────┐
        │Rec =   │    │Rec = Weight  │
        │Min     │    │/10 × 0.6-0.7 │
        └────┬───┘    └────────┬─────┘
             │                 │
             └────────┬────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │ Check: Current Water    │
        │ Intake < Recommended?   │
        └────┬──────────────┬─────┘
        YES  │              │ NO
             ▼              ▼
        ┌──────────┐  ┌────────────┐
        │WARNING!  │  │ OK / Remind│
        │Increase  │  │ for goal   │
        └────┬─────┘  └──────┬─────┘
             │                │
             └────────┬───────┘
                      │
                      ▼
        ┌─────────────────────────────┐
        │ OUTPUT: Water Advisory      │
        │ - Min/recommended liters    │
        │ - Warning message if low    │
        └─────────────────────────────┘
```

**Business Rules — Water Intake:**

| Scénario | Công Thức | Ghi Chú |
|----------|-----------|---------|
| **Normal** | Min = Weight/10 × 0.4 L | Baseline 0.4 L/10kg cân nặng |
| **Lose Weight** | Rec = Weight/10 × 0.6-0.7 L | Tăng để tăng metabolism |
| **Current < Min** | ⚠️ WARNING | Khuyên tăng nước lên tối thiểu |
| **Avoid** | Nước có calo, trà đường, cà phê đặc | Chỉ nước lọc, trà không đường |

---

## II. BUSINESS PROCESS FLOW — LẬP GỢI Ý BỮA ĂN

### Process 2.1: Chọn Template Bữa Ăn Cơ Bản

```
┌────────────────────────────────────┐
│  INPUT: Meal Frequency             │
│  (4-meal hoặc 5-meal plan)         │
└────────────────┬───────────────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ 4 or 5 meals?          │
    └────┬──────────────┬────┘
    4    │              │ 5
         ▼              ▼
    ┌──────────┐  ┌───────────┐
    │Template: │  │Template:  │
    │- Sáng   │  │- Sáng     │
    │- Trưa   │  │- Phụ sáng │
    │- Tối    │  │- Trưa     │
    │- Phụ 1  │  │- Phụ chiều│
    │  (100kcal)  │- Tối     │
    └────┬────┘  └─────┬─────┘
         │             │
         └──────┬──────┘
                │
    Base Meals: ~1200 kcal
    - Sáng: 120 kcal
    - Phụ: 100 kcal each
    - Trưa: 500 kcal
    - Tối: 380 kcal
                │
                ▼
    ┌─────────────────────────────┐
    │ OUTPUT: Base Meal Plan      │
    │ (4-5 meals @ 1200 kcal)     │
    └─────────────────────────────┘
```

**Business Rule — Base Meal Template (1200 kcal):**

| Bữa Ăn | Giờ | Calo | Thành Phần |
|--------|-----|------|-----------|
| **Sáng** | 07:00 | 120 | 2 muỗng F1 + 300ml nước |
| **Phụ Sáng** | 09:00 | 100 | 1 quả táo hoặc 1 ly F1 |
| **Trưa** | 12:00 | 500 | 150g đạm + 150g cơm rau |
| **Phụ Chiều** | 15:00 | 100 | 2 muỗng F1 hoặc hoa quả (nếu 5 bữa) |
| **Tối** | 18:00 | 380 | 150g đạm thực vật + rau hấp |

---

### Process 2.1b: Cấu trúc MỘT BỮA theo 3 NHÓM THỰC PHẨM (core gợi ý)

> Mỗi bữa ăn được gợi ý dựa trên **3 nhóm thực phẩm**. Mỗi nhóm hiển thị **lượng Calo mục tiêu** và lấy món gợi ý từ **danh mục món ăn tương ứng**. Riêng **nhóm đạm** còn hiển thị thêm **lượng đạm (protein, g) mục tiêu**.

| Nhóm | Thông tin hiển thị | Nguồn món gợi ý (catalog) |
|---|---|---|
| **1. Nhóm đạm (Protein)** | **Calo mục tiêu** + **Đạm (g) mục tiêu** | Danh mục món cung cấp **đạm** (gà, cá, tôm, trứng, đậu, thịt nạc…) |
| **2. Nhóm xơ (Rau xanh, Vitamin)** | **Calo mục tiêu** | Danh mục món cung cấp **chất xơ & vitamin** (rau luộc, salad, rau hấp…) |
| **3. Nhóm đường/bột (Carb)** | **Calo mục tiêu** | Danh mục món cung cấp **tinh bột, đường** (cơm, khoai, ngô, yến mạch, trái cây…) |

```
BỮA ĂN
 ├─ Nhóm đạm   : target_calo, target_dam(g) → chọn món từ catalog PROTEIN
 ├─ Nhóm xơ    : target_calo               → chọn món từ catalog FIBER_VITAMIN
 └─ Nhóm đường/bột : target_calo           → chọn món từ catalog CARB
Tổng calo bữa = Σ calo 3 nhóm
```

**Business Rules — phân bổ & chọn món theo nhóm:**
- Calo mỗi bữa được **chia về 3 nhóm** theo tỉ lệ chuẩn của Nutrition club (đạm ưu tiên đủ mục tiêu protein; phần còn lại chia cho xơ & đường-bột).
- Mỗi nhóm chọn **1+ món** từ đúng catalog của nhóm; tổng calo các món ≈ calo mục tiêu của nhóm.
- Nhóm đạm phải đáp ứng **đạm (g) mục tiêu**; nếu thiếu → tăng khẩu phần/đổi món đạm.
- Áp dụng **Process 2.3** (lọc theo bệnh lý/dị ứng) trên từng món trong cả 3 nhóm.

**Ví dụ thực tế (phiếu Nutrition club — "Con số kỳ diệu 1.700 Cal/ngày"):**

> Tính: **RMR 1390 + AMR 347 + EX 0 = TMR 1737** → Magic Calories ~**1.700 kcal/ngày** (≈1.711 phân bổ qua các bữa).

| Bữa | Nhóm đạm | Nhóm xơ | Nhóm đường/bột |
|---|---|---|---|
| **Sáng** | 3 lòng trắng trứng (50) | — | Bữa ăn lành mạnh (110) + 2 thìa vừng đen (100) + sữa đậu nành không đường (60); ½ củ khoai/bắp ngô (100) |
| **Trưa** | 1 phần thức ăn gà/cá… (400) | ½ bát rau (100) | ½ bát cơm (100) |
| **Chiều (16h)** | — | — | Bữa ăn lành mạnh (90) + ½ củ khoai/ngô luộc (100) + 1 quả táo/ổi |
| **Tối** | 1 phần thức ăn gà/cá… (400) | ½ bát rau (100) | ½ bát cơm (100) |

**Lưu ý chế độ (đính kèm phiếu):**
1. **Hạn chế** thịt đỏ, đồ chiên/xào/rán/nướng.
2. **Uống nước tối thiểu 0,4 L / 10 kg trọng lượng / ngày** (vd 50 kg → ~2,0 L/ngày).
3. **Chương trình áp dụng 10 ngày → đo lại → điều chỉnh** (gắn với cơ chế gợi ý bữa ăn **đa phiên bản 10 ngày** — xem `docs/to-be/Workflow-HLV.md §3`).

---

### Process 2.2: Điều Chỉnh Calo từ 1200 → Target

```
┌──────────────────────────────────────┐
│  INPUT: Base Meals (1200 kcal)       │
│  Target Calories                     │
└────────────────┬─────────────────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ Delta = Target - 1200  │
    └────┬──────────────┬────┘
    <0   │              │ >0
    NEED │              │ NEED
    LESS │              │ MORE
         ▼              ▼
    ┌──────────┐  ┌─────────────┐
    │Reduce:   │  │Add to:      │
    │- Tối 1st│  │- Sáng 1st   │
    │- Carbs  │  │(+100 kcal/  │
    │  b4     │  │ 1 ly F1)    │
    │  Protein│  │- Trưa       │
    │         │  │(+300 kcal/  │
    │         │  │ 1 đạm)      │
    └────┬────┘  └──────┬──────┘
         │              │
         └──────┬───────┘
                │
    ┌───────────▼──────────────┐
    │ OUTPUT: Adjusted Meals   │
    │ (targeting exact calorie)│
    └──────────────────────────┘
```

**Business Rules — Calorie Adjustment:**

| Điều Chỉnh | Ưu Tiên | Chi Tiết |
|-----------|---------|---------|
| **Cộng (+) Calo** | Sáng → Trưa | +100 kcal = 1 ly F1; +300 kcal = 1 miếng đạm |
| **Trừ (-) Calo** | Tối → Sáng | Giảm carbs/rau TRƯỚC protein. Giảm từ tối để không ảnh hưởng metabolism sáng |

---

### Process 2.3: Lọc Thực Phẩm Theo Bệnh Lý

```
┌──────────────────────────────────────┐
│  INPUT: Adjusted Meals,              │
│  Medical Conditions, Allergies       │
└────────────────┬─────────────────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ Có bệnh lý không?      │
    └────┬──────────────┬────┘
     NO  │              │ YES
         ▼              ▼
    ┌──────────┐  ┌──────────────────┐
    │No filter │  │ Loop qua từng    │
    │needed    │  │ meal item        │
    └────┬─────┘  └────────┬─────────┘
         │                 │
         │        ┌────────▼────────┐
         │        │KIDNEY:          │
         │        │- Remove: K-high │
         │        │  (banana, ...)  │
         │        │- Remove: P-high │
         │        │  (milk, ...)    │
         │        │- Remove: Red meat│
         │        └────────┬────────┘
         │                 │
         │        ┌────────▼────────┐
         │        │LUNG:            │
         │        │- Remove: Fried  │
         │        │- Remove: Red    │
         │        │- Keep: Antioxidant│
         │        └────────┬────────┘
         │                 │
         │        ┌────────▼────────┐
         │        │DIABETES:        │
         │        │- Remove: High GI│
         │        │  (white rice)   │
         │        │- Keep: Low GI   │
         │        └────────┬────────┘
         │                 │
         │        ┌────────▼────────┐
         │        │HTN/HEART/GERD:  │
         │        │- Remove: trigger│
         │        └────────┬────────┘
         │                 │
         └────────┬────────┘
                  │
        ┌─────────▼────────────────┐
        │ ALLERGIES CHECK          │
        │ - Remove: allergen items │
        └─────────┬────────────────┘
                  │
    ┌─────────────▼──────────────┐
    │ OUTPUT: Filtered Meals     │
    │ (safe for medical/allergy) │
    └───────────────────────────┘
```

**Business Rules — Food Filtering by Condition:**

| Bệnh Lý | Xóa (Remove) | Giữ (Keep) |
|---------|--------------|-----------|
| **KIDNEY** | Chuối, cam, kiwi, sữa, phô mai, thịt đỏ | Cá trắng, ức gà, đậu phụ |
| **LUNG** | Đồ chiên, thịt đỏ, đường | Cá hồi, bông cải, quả mọng |
| **DIABETES** | Bánh trắng, cơm trắng, nước ngọt | Gạo lứt, đậu, táo |
| **HYPERTENSION** | Muối, mắm, xúc xích, phô mai | Rau xanh, khoai, cá |
| **HEART** | Bơ, kem, thịt đỏ, chiên xào | Cá, hạt, dầu ô-liu |
| **GERD** | Cà phê, cà chua, cay, béo | Ức gà, khoai, rau luộc |

---

### Process 2.4: Tính Tổng Dinh Dưỡng

```
┌────────────────────────┐
│  INPUT: Filtered Meals │
└────────────────┬───────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ Loop qua từng meal     │
    │ Loop qua từng item     │
    │                        │
    │ Sum:                   │
    │ - Protein (grams)      │
    │ - Carbs (grams)        │
    │ - Fat (grams)          │
    │ - Fiber (grams)        │
    └────────────┬───────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ Validate Macros:       │
    │ - Protein: OK?         │
    │ - Carbs: GI OK?        │
    │ - Fat: <10% sat fat?   │
    │ - Fiber: >= 25g?       │
    └────────────┬───────────┘
                 │
    ┌────────────▼─────────────┐
    │ OUTPUT: Meal Nutrition   │
    │ - Total Protein          │
    │ - Total Carbs            │
    │ - Total Fat              │
    │ - Total Fiber            │
    └──────────────────────────┘
```

**Business Rules — Nutritional Validation:**

| Dinh Dưỡng | Chuẩn | Điều Chỉnh Nếu |
|-----------|-------|----------------|
| **Protein** | 0.8-1.2g/kg | Kidney: 0.6g/kg; Lung: 1.0g/kg |
| **Carbs** | 45-50% calo | Diabetes: 40-50% với Low GI |
| **Fat** | 25-35% calo | Heart: <20%; GERD: <20% |
| **Sat Fat** | <10% calo | Heart: <7% |
| **Fiber** | 25-30g | Diabetes: 30g; All: >=25g |

---

## III. DECISION TABLES — CÁC QUY ĐỊNH CHÍNH

### Decision Table 3.1: Xác Định Stage Bệnh Thận

| Điều Kiện (eGFR) | Stage | Ràng Buộc Protein | Sodium | Potassium | Phosphorus |
|-----------------|-------|-------------------|--------|-----------|-----------|
| >= 90 | 1 | 0.8g/kg | 2300mg | 3500mg | None |
| 60-89 | 2 | 0.8g/kg | 2300mg | 3500mg | None |
| 45-59 | 3A | 0.8g/kg | 1500mg | 2600mg | 1200mg |
| 30-44 | 3B | 0.8g/kg | 1500mg | 2600mg | 1200mg |
| 15-29 | 4 | **0.6g/kg** | **1200mg** | **2000mg** | **1000mg** |
| <15 | 5 | **0.6g/kg** | **1000mg** | **1500mg** | **800mg** |

---

### Decision Table 3.2: Xác Định Kiểm Soát Glucose (Diabetes)

| HbA1c Range | Mức Kiểm Soát | Carbs Target | GI Target | Adjustment |
|-------------|---------------|--------------|-----------|-----------|
| < 5.7% | Excellent | 50% calo | Normal | Maintain current |
| 5.7-6.4% | Good | 50% calo | < 55 | Monitor, maintain |
| 6.5-7.9% | Fair | 45% calo | **< 55** | Increase fiber |
| 8.0-8.9% | Poor | **40% calo** | **< 55** | Reduce carbs, add protein |
| > 9% | Very Poor | **40% calo** | **< 55** | **Strict control, review meds** |

---

### Decision Table 3.3: Xác Định Mức Huyết Áp

| Systolic BP (mmHg) | Diastolic BP | Phân Loại | Sodium Limit | Action |
|-------------------|--------------|----------|--------------|---------|
| < 120 | < 80 | Normal | 2300mg | Maintain DASH |
| 120-129 | < 80 | Elevated | 2300mg | Monitor closely |
| 130-139 | 80-89 | Stage 1 HTN | **1500mg** | Aggressive diet |
| >= 140 | >= 90 | Stage 2 HTN | **1500mg** | Medication + diet |

---

### Decision Table 3.4: Xác Định Loại Tập Luyện

| Exercise Type | Intensity | Calo/phút | Duration | Frequency |
|---------------|-----------|-----------|----------|-----------|
| Walk (slow) | Low | 0.04×W | 30-60 min | 3-5x/week |
| Jog/Run | High | 0.10×W | 30-45 min | 3-4x/week |
| Cycling | Moderate | 0.09×W | 30-60 min | 3-4x/week |
| Yoga/Stretch | Low | 0.05×W | 30-45 min | 3-5x/week |
| Weight Training | High | 0.08×W | 30-45 min | 3x/week |
| Swimming | High | 0.10×W | 30-45 min | 3-4x/week |

---

## IV. BUSINESS RULES — THAY ĐỔI BỮA ĂN

### Rule 4.1: Thêm Calo

**IF** Target > 1200 kcal **THEN**

1. **Thêm vào bữa sáng trước tiên:**
   - Cứ 100 kcal → +1 ly F1 hoặc +1 phần hoa quả

2. **Sau đó, thêm vào bữa trưa:**
   - Cứ 300 kcal → +1 miếng đạm trắng (gà/cá)

3. **Ưu tiên protein hơn carbs** (giúp satiety + chuyển hóa)

**Example:** Target = 1800 kcal (Δ +600)
- Sáng: +100 kcal (1 ly F1)
- Trưa: +300 kcal (1 miếng gà)
- Trưa: +200 kcal (thêm rau, nước sốt)

---

### Rule 4.2: Giảm Calo

**IF** Target < 1200 kcal **THEN**

1. **Giảm từ bữa tối trước tiên** (không ảnh hưởng sáng)

2. **Giảm carbs/rau TRƯỚC protein:**
   - Xóa cơm → xóa carbs đầu tiên
   - Giữ lại đạm (protein essential)

3. **Không bao giờ** cắt giảm dưới 1000 kcal

**Example:** Target = 900 kcal (Δ -300)
- ❌ **CÓ THỂ:** Xóa 300g cơm tối (300 kcal)
- ✅ **KHÔNG:** Xóa 150g gà (vẫn giữ protein)

---

## V. BUSINESS WORKFLOW — FLOW TOÀN DIỆN

```
┌──────────────────────────────────────────────────────┐
│                  START PROCESS                        │
│         (User Input HealthProfile)                    │
└──────────────────┬───────────────────────────────────┘
                   │
      ┌────────────▼─────────────┐
      │ PHASE 1: CALORIE        │
      │ ───────────────────────  │
      │ • Calculate RMR         │
      │ • Calculate AMR         │
      │ • Calculate Ex          │
      │ • Calculate TMR         │
      │ • Calculate Magic Cal   │
      │ • Apply Medical Adj     │
      │ • Water Advisory        │
      └────────────┬─────────────┘
                   │
                   ▼
      ┌──────────────────────────┐
      │ OUTPUT: CalorieProfile   │
      │ - Magic Calories         │
      │ - Weekly deficit/surplus │
      │ - Est. weight change     │
      │ - Medical notes          │
      │ - Water intake advisory  │
      └────────────┬──────────────┘
                   │
      ┌────────────▼──────────────┐
      │ PHASE 2: MEAL PLANNING   │
      │ ───────────────────────  │
      │ • Select base template   │
      │ • Adjust calories 1200→T │
      │ • Filter by medical cond │
      │ • Check allergies        │
      │ • Calculate nutrition    │
      │ • Apply recommendations  │
      └────────────┬──────────────┘
                   │
                   ▼
      ┌──────────────────────────┐
      │ OUTPUT: MealPlan         │
      │ - 4-5 meals/day          │
      │ - Food items + nutrition │
      │ - Medical restrictions   │
      │ - Dietary recommendations│
      └────────────┬──────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│                  END PROCESS                         │
│    (Return CalorieProfile + MealPlan to User)        │
└──────────────────────────────────────────────────────┘
```

---

## VI. DATA OBJECTS — INPUT/OUTPUT SPEC

### Input: HealthProfile

```
HealthProfile {
  // Demographics
  gender: "MALE" | "FEMALE"
  age: Integer (13-120)
  weightKg: Decimal (30-250)
  heightCm: Decimal (100-250)
  
  // Health Metrics
  currentBMI: Decimal (calculated or input)
  eGFR: Decimal (0-120) [for kidney]
  hbA1c: Decimal (4-14) [for diabetes]
  systolicBP: Integer (80-200) [for hypertension]
  diastolicBP: Integer (50-120)
  
  // Lifestyle
  goal: "LOSE_WEIGHT" | "GAIN_WEIGHT" | "MAINTAIN" | "REJUVENATE"
  targetWeightKg: Decimal (if goal = LOSE/GAIN)
  exerciseDaily: Boolean
  exerciseType: "CARDIO" | "STRENGTH" | "MIXED" | "NONE"
  exerciseMinutes: Integer (0-180)
  waterLitersPerDay: Decimal (0-10)
  sleepHoursPerDay: Integer (0-12)
  
  // Medical
  medicalConditions: List["KIDNEY_DISEASE", "LUNG_DISEASE", 
                           "DIABETES", "HYPERTENSION", 
                           "HEART_DISEASE", "ACID_REFLUX", ...]
  foodAllergies: List["NUTS", "SHELLFISH", ...]
  preferredFoods: List[...]
  
  // Preference
  mealFrequency: "FOUR_MEALS" | "FIVE_MEALS"
}
```

### Output: Recommendation Response

```
RecommendationResponse {
  
  calorie: {
    rmr: Decimal                           // Kcal/day
    amr: Decimal                           // Kcal/day
    exerciseCalories: Decimal              // Kcal/day
    tmr: Decimal                           // Kcal/day
    magicCalories: Decimal                 // Final target kcal/day
    
    weeklyCalorieDeficit: Decimal (if LOSE_WEIGHT)  // Total kcal/week
    weeklyCalorieSurplus: Decimal (if GAIN_WEIGHT)  // Total kcal/week
    estimatedWeeklyWeightChange: Decimal   // kg/week
    
    notes: List[String]                    // Warnings, caveats
  }
  
  meal: {
    totalDailyCalories: Decimal
    mealPlan: "FOUR_MEALS" | "FIVE_MEALS"
    meals: [
      {
        mealName: "Bữa sáng"
        mealTime: "07:00"
        targetCalories: Decimal
        items: [
          { name: "2 muỗng F1", calories: 120, protein: 24, ... }
        ]
      }
    ]
    
    // Aggregate nutrition
    totalProteinGrams: Decimal
    totalCarbsGrams: Decimal
    totalFatGrams: Decimal
    totalFiberGrams: Decimal
    
    // Restrictions & advice
    medicalRestrictions: List[String]      // Sodium <1500mg, etc
    dietaryRecommendations: List[String]   // Thực phẩm nên tránh, etc
    minWaterIntakePerDay: Decimal          // Liters
  }
  
  status: "SUCCESS" | "WARNING" | "ERROR"
  generatedAt: DateTime
  warnings: List[String]                   // Calo quá thấp, BMI quá cao, etc
}
```

---

## VII. VALIDATION RULES

### Validation 7.1: Input Validation

| Field | Min | Max | Rule |
|-------|-----|-----|------|
| Age | 13 | 120 | Reject if outside |
| Weight | 30kg | 250kg | Reject if outside |
| Height | 100cm | 250cm | Reject if outside |
| Exercise Minutes | 0 | 180 | Reject if >180 |
| Water Intake | 0 | 10L | Warning if >8L |

### Validation 7.2: Output Validation

| Output | Min | Max | Action |
|--------|-----|-----|--------|
| RMR | 1000 | 4000 | Enforce min, warn max |
| TMR | 1200 | 5000 | Enforce min, warn max |
| Magic Cal | 1000 | 4500 | Enforce min, warn max |
| Protein | 0.6g/kg | 2.0g/kg | Warn if outside |

---

## VIII. SUMMARY — QUY TRÌNH TÍNH TOÁN NHANH

```
Input: HealthProfile
  ↓
[PHASE 1] Tính Calo
  RMR = 10×W + 6.25×H - 5×A ± 161/5
  AMR = RMR × 0.25/0.30 (F/M)
  Ex = Rate × Minutes (nếu tập luyện)
  TMR = RMR + AMR + Ex
  Magic Cal = TMR ± 300/500 (theo goal & age)
  Adjust = Medical conditions (x1.0-1.15)
  ↓
Output: CalorieProfile (magic kcal, weekly change, water advisory)
  ↓
[PHASE 2] Lập Bữa Ăn
  Template = Base 1200 kcal (4-5 meals)
  Adjust = Scale từ 1200 → Magic Cal
  Filter = Remove by Medical/Allergies
  Validate = Protein, GI, Fiber, Fat targets
  ↓
Output: MealPlan (5 meals, nutrition, restrictions)
```

---
