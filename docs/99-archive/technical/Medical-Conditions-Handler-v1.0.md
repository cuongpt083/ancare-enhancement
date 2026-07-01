# **MEDICAL CONDITIONS HANDLER — CHI TIẾT XỬ LÝ CÁC BỆNH LÝ**
## Cách Xử lý Thận, Phổi, Tiểu Đường, Huyết Áp, Tim, GERD trong Rule Engine

**Phiên bản:** v1.0  
**Cơ sở:** Meal-Recommendation-Rule-Engine-v1.0.md  
**Mục đích:** Chi tiết hóa cách xử lý từng bệnh lý — ràng buộc dinh dưỡng, điều chỉnh calo, danh sách thực phẩm

---

## I. OVERVIEW — CHIẾN LƯỢC XỬ LÝ BỆNH LÝ

Mỗi bệnh lý được xử lý qua 4 lớp:

```
┌─────────────────────────────────────────┐
│ 1. CALORIE ADJUSTMENT                   │  (điều chỉnh calo mục tiêu)
├─────────────────────────────────────────┤
│ 2. MACRONUTRIENT CONSTRAINTS            │  (protein, carbs, fat, fiber)
├─────────────────────────────────────────┤
│ 3. MICRONUTRIENT REQUIREMENTS           │  (vitamin, mineral, antioxidant)
├─────────────────────────────────────────┤
│ 4. FOOD SUBSTITUTION & RESTRICTIONS     │  (thực phẩm cho phép/tránh)
└─────────────────────────────────────────┘
```

---

## II. KIDNEY DISEASE — BỆNH THẬN

### 2.1. Phân loại Bệnh Thận (CKD Stages)

```
Stage 1: GFR > 90 (Normal/High) — Chức năng thận bình thường
Stage 2: GFR 60-89 (Mild decrease) — Giảm nhẹ, ít hoặc không có triệu chứng
Stage 3a: GFR 45-59 (Moderate decrease) — Giảm vừa phải
Stage 3b: GFR 30-44 (Moderate decrease) — Giảm vừa phải (trầm trọng hơn)
Stage 4: GFR 15-29 (Severe decrease) — Giảm nặng, chuẩn bị lọc máu
Stage 5: GFR < 15 (Kidney failure) — Suy thận giai đoạn cuối, cần lọc máu
```

### 2.2. Ràng Buộc Dinh Dưỡng Theo Stage

```java
class KidneyDiseaseHandler {
  
  enum CKDStage {
    STAGE_1 (90, null),    // GFR >= 90
    STAGE_2 (60, 89),      // GFR 60-89
    STAGE_3A (45, 59),     // GFR 45-59
    STAGE_3B (30, 44),     // GFR 30-44
    STAGE_4 (15, 29),      // GFR 15-29
    STAGE_5 (0, 14);       // GFR < 15
    
    int minGFR;
    Integer maxGFR;
    
    CKDStage(int minGFR, Integer maxGFR) {
      this.minGFR = minGFR;
      this.maxGFR = maxGFR;
    }
  }
  
  /**
   * Xác định stage dựa trên GFR (eGFR)
   */
  public CKDStage determineStage(double eGFR) {
    if (eGFR >= 90) return CKDStage.STAGE_1;
    if (eGFR >= 60 && eGFR < 90) return CKDStage.STAGE_2;
    if (eGFR >= 45 && eGFR < 60) return CKDStage.STAGE_3A;
    if (eGFR >= 30 && eGFR < 45) return CKDStage.STAGE_3B;
    if (eGFR >= 15 && eGFR < 30) return CKDStage.STAGE_4;
    return CKDStage.STAGE_5; // eGFR < 15
  }
  
  /**
   * Ràng buộc dinh dưỡng theo stage
   */
  public NutrientConstraints getNutrientConstraints(
    CKDStage stage, 
    double weightKg,
    double eGFR
  ) {
    NutrientConstraints constraints = new NutrientConstraints();
    
    switch (stage) {
      case STAGE_1:
      case STAGE_2:
        // Giai đoạn sớm: chủ yếu kiểm soát áp lực, cholesterol
        constraints.proteinGPerKg = 0.8; // Normal protein 0.8g/kg
        constraints.sodiumMgPerDay = 2300; // Normal sodium
        constraints.potassiumMgPerDay = 3500; // Normal potassium
        constraints.phosphorusMgPerDay = null; // Không cần hạn chế
        constraints.notes = "Kiểm soát huyết áp, cholesterol. Protein bình thường.";
        break;
        
      case STAGE_3A:
      case STAGE_3B:
        // Giai đoạn vừa phải: bắt đầu hạn chế protein, sodium, potassium
        constraints.proteinGPerKg = 0.8; // 0.8g/kg (hoặc 0.6-0.7g/kg nếu muốn giảm)
        constraints.sodiumMgPerDay = 1500; // Hạn chế: < 1500mg (hoặc < 2300mg)
        constraints.potassiumMgPerDay = 2600; // Bắt đầu hạn chế
        constraints.phosphorusMgPerDay = 1200; // Hạn chế
        constraints.notes = "Hạn chế sodium, potassium, phosphorus. Protein 0.8g/kg.";
        break;
        
      case STAGE_4:
        // Giai đoạn nặng: hạn chế nghiêm ngặt protein, sodium, potassium, phosphorus
        constraints.proteinGPerKg = 0.6; // Giảm protein: 0.6g/kg (mục tiêu suy thận)
        constraints.sodiumMgPerDay = 1200; // Nghiêm ngặt: < 1200mg
        constraints.potassiumMgPerDay = 2000; // Hạn chế mạnh: < 2000mg
        constraints.phosphorusMgPerDay = 1000; // Hạn chế mạnh: < 1000mg
        constraints.fluidLitersPerDay = 1.5; // Có thể cần hạn chế nước nếu có sưng
        constraints.notes = "Hạn chế mạnh mẽ protein, sodium, potassium, phosphorus. Protein 0.6g/kg.";
        break;
        
      case STAGE_5:
        // Suy thận giai đoạn cuối: hạn chế rất nghiêm ngặt
        constraints.proteinGPerKg = 0.6; // 0.6g/kg (có thể < 0.6g nếu chưa lọc máu)
        constraints.sodiumMgPerDay = 1000; // Rất nghiêm ngặt: < 1000mg
        constraints.potassiumMgPerDay = 1500; // Rất hạn chế: < 1500mg
        constraints.phosphorusMgPerDay = 800; // Rất hạn chế: < 800mg
        constraints.fluidLitersPerDay = 1.0; // Hạn chế nước: ~1 L/ngày + lượng nước trong thức ăn
        constraints.notes = "Hạn chế RẤT NGHIÊM NGẶT. Protein 0.6g/kg. Cần giám sát bác sĩ.";
        break;
    }
    
    return constraints;
  }
  
  /**
   * Điều chỉnh calo dựa trên trạng thái dinh dưỡng
   */
  public double adjustCalorieForKidneyDisease(
    double baseMagicCalories,
    double weightKg,
    CKDStage stage
  ) {
    // Bệnh thận cần 30-35 kcal/kg (để duy trì cân nặng, không sử dụng muscle)
    double recommendedCalories = weightKg * 32; // Trung bình 32 kcal/kg
    
    if (stage == CKDStage.STAGE_4 || stage == CKDStage.STAGE_5) {
      // Giai đoạn nặng: có thể cần giảm calo để giảm beban thận
      // Nhưng vẫn đảm bảo đủ năng lượng để giữ protein
      return Math.max(recommendedCalories, baseMagicCalories * 0.9);
    }
    
    return baseMagicCalories;
  }
  
  /**
   * Thay thế thực phẩm — xóa những thực phẩm không phù hợp
   */
  public List<MealItem> filterFoodItemsForKidney(
    List<MealItem> items,
    CKDStage stage
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> highKaliumFoods = Arrays.asList(
      "banana", "orange", "avocado", "potato", "spinach", "tomato", 
      "coconut", "raisins", "dates", "nuts", "seeds"
    );
    
    List<String> highPhosphorusFoods = Arrays.asList(
      "milk", "cheese", "yogurt", "chocolate", "cola", "peanut butter",
      "whole grain", "organ meat", "red meat"
    );
    
    List<String> highSodiumFoods = Arrays.asList(
      "canned", "processed", "pickled", "salt", "soy sauce", "fish sauce",
      "sausage", "bacon", "ham"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      if (stage == CKDStage.STAGE_3B || stage == CKDStage.STAGE_4 || stage == CKDStage.STAGE_5) {
        // Hạn chế kalium
        for (String food : highKaliumFoods) {
          if (itemName.contains(food)) {
            isAllowed = false;
            break;
          }
        }
      }
      
      if (stage == CKDStage.STAGE_4 || stage == CKDStage.STAGE_5) {
        // Hạn chế phosphorus (sữa, phô mai)
        for (String food : highPhosphorusFoods) {
          if (itemName.contains(food)) {
            isAllowed = false;
            break;
          }
        }
        
        // Hạn chế sodium
        for (String food : highSodiumFoods) {
          if (itemName.contains(food)) {
            isAllowed = false;
            break;
          }
        }
      }
      
      // Luôn tránh thịt đỏ, mồi
      if (itemName.contains("beef") || itemName.contains("pork") || itemName.contains("organ")) {
        isAllowed = false;
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm phù hợp
   */
  public List<String> getRecommendedFoods(CKDStage stage) {
    List<String> foods = new ArrayList<>();
    
    // Protein:
    foods.add("🐟 Cá trắng (cá basa, cá hồi giới hạn), tôm");
    foods.add("🍗 Ức gà (không da), thỏ");
    foods.add("🥚 Trắng trứng");
    foods.add("🥬 Đậu phụ (phosphorus thấp)");
    
    // Carbs:
    foods.add("🍚 Gạo trắng (phosphorus < gạo lứt), mì");
    foods.add("🍞 Bánh mì trắng (ít phosphorus)");
    
    if (stage == CKDStage.STAGE_1 || stage == CKDStage.STAGE_2) {
      foods.add("🥔 Khoai tây (luộc, tránh muối)");
    }
    // Giai đoạn sau: tránh khoai tây (high kalium)
    
    // Rau (low potassium):
    foods.add("🥬 Bắp cải, cà rốt, dưa chuột, hành");
    foods.add("🧅 Tỏi, hành tây, bông cải xanh (luộc)");
    
    // Hoa quả (low potassium):
    if (stage == CKDStage.STAGE_1 || stage == CKDStage.STAGE_2) {
      foods.add("🍎 Táo, lê, dâu tây (giới hạn)");
    } else {
      foods.add("🍎 Táo, lê (low potassium)");
    }
    
    // Tránh:
    foods.add("\n❌ Tránh: Chuối, cam, kiwi, dừa, hạt, các loại hạt");
    foods.add("❌ Tránh: Sữa, phô mai, sữa chua, chocolate");
    foods.add("❌ Tránh: Thịt đỏ (bò, lợn), lòng, xúc xích");
    foods.add("❌ Tránh: Cà chua, cà chua sốt (high potassium & phosphorus)");
    foods.add("❌ Tránh: Nước ngọt Cola, nước trái cây đậm đặc");
    
    return foods;
  }
}

class NutrientConstraints {
  Double proteinGPerKg;          // Protein g/kg cân nặng
  Integer sodiumMgPerDay;        // Sodium mg/ngày
  Integer potassiumMgPerDay;     // Potassium mg/ngày
  Integer phosphorusMgPerDay;    // Phosphorus mg/ngày
  Double fluidLitersPerDay;      // Nước (nếu cần hạn chế)
  String notes;
}
```

### 2.3. Ví Dụ Meal Plan — Bệnh Thận Stage 4

```
👥 Input:
- Bệnh: Kidney Disease Stage 4 (GFR = 25)
- Cân nặng: 70 kg
- Mục tiêu: Maintain (giữ cân)

📊 Tính toán:
- Base calories: 70 kg × 32 kcal/kg = 2240 kcal
- Protein: 70 kg × 0.6 g/kg = 42g
- Sodium: < 1200 mg/ngày
- Potassium: < 2000 mg/ngày
- Phosphorus: < 1000 mg/ngày

🍽️ Meal Plan (1 ngày):
- Sáng 07:00: 2 muỗng F1 + 300ml nước (~120 kcal, 24g protein, 200mg sodium)
  • Proteins thấp sodium
  
- Phụ sáng 09:00: Táo 1 quả (~100 kcal, 0g protein, 2mg sodium)
  
- Trưa 12:00: 
  • 100g cá basa nướng (không muối) (~150 kcal, 25g protein, 50mg sodium)
  • 1 bát cơm trắng + rau cà rốt luộc (~250 kcal, 4g protein, 80mg sodium)
  • Tổng: 400 kcal
  
- Phụ chiều 15:00: 1 ly F1 hoặc 1 táo (~100 kcal)
  
- Tối 18:00:
  • 100g tôm hấp (~90 kcal, 20g protein, 60mg sodium)
  • 1 bát rau hấp (bắp cải, cà rốt, hành) (~100 kcal, 2g protein, 40mg sodium)
  • Tổng: 190 kcal

🔴 Tránh hoàn toàn:
- Chuối, cam, kiwi, dừa
- Sữa, phô mai, sữa chua
- Thịt đỏ, lòng
- Cà chua, cà chua sốt
- Muối, nước mắm, nước cốt
```

---

## III. LUNG DISEASE — BỆNH PHỔI

### 3.1. Phân loại Bệnh Phổi

```
COPD (Chronic Obstructive Pulmonary Disease) — Bệnh phổi tắc nghẽn mãn tính
Asthma — Hen suyễn
Pulmonary Fibrosis — Xơ hóa phổi
ILD (Interstitial Lung Disease) — Bệnh phổi kẽ
```

### 3.2. Ràng Buộc Dinh Dưỡng

```java
class LungDiseaseHandler {
  
  /**
   * Xác định loại bệnh phổi
   */
  enum LungDiseaseType {
    COPD, ASTHMA, PULMONARY_FIBROSIS, ILD
  }
  
  /**
   * Ràng buộc dinh dưỡng cho bệnh phổi
   */
  public NutrientConstraints getNutrientConstraints(
    LungDiseaseType type,
    double weightKg
  ) {
    NutrientConstraints constraints = new NutrientConstraints();
    
    // Chung cho bệnh phổi:
    constraints.proteinGPerKg = 1.0; // Tăng protein (giữ khối cơ)
    constraints.fiberGPerDay = 30; // Cao chất xơ (giảm viêm)
    constraints.vitaminC_mgPerDay = 500; // Antioxidant: Vitamin C 500mg
    constraints.vitaminE_IUPerDay = 400; // Vitamin E 400 IU
    constraints.seleniumMcgPerDay = 200; // Selenium 200 mcg
    constraints.omega3FattyAcidGPerDay = 2; // Omega-3: 2g/ngày
    
    // Tránh viêm:
    constraints.saturatedFatPercentOfCal = 10; // < 10% calo từ saturated fat
    constraints.transFat = "0"; // Hoàn toàn tránh trans fat
    
    // Giữ nước:
    constraints.fluidLitersPerDay = 2.0; // 2L nước/ngày (làm mỏng khí thải)
    
    constraints.notes = "Tăng antioxidant, omega-3. Giảm viêm. Protein 1.0g/kg.";
    
    return constraints;
  }
  
  /**
   * Điều chỉnh calo dựa trên chuyển hóa cao
   */
  public double adjustCalorieForLungDisease(
    double baseMagicCalories,
    double weightKg
  ) {
    // Bệnh phổi có thể tăng chuyển hóa 10-20% do đổi khí khó
    double metabolicIncrease = baseMagicCalories * 0.15; // +15%
    
    return baseMagicCalories + metabolicIncrease;
  }
  
  /**
   * Lọc thực phẩm — tránh các thực phẩm gây viêm
   */
  public List<MealItem> filterFoodItemsForLung(
    List<MealItem> items
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> inflammatoryFoods = Arrays.asList(
      "fried", "fast food", "processed", "white bread", "white rice",
      "sugar", "soda", "candy", "trans fat", "saturated fat",
      "red meat", "processed meat", "sausage", "bacon"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      for (String food : inflammatoryFoods) {
        if (itemName.contains(food)) {
          isAllowed = false;
          break;
        }
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm chống viêm & rich antioxidant
   */
  public List<String> getRecommendedFoods() {
    return Arrays.asList(
      "🐟 Cá có dầu (cá hồi, cá trích, cá ngừ) — Omega-3 cao",
      "🥦 Bông cải xanh, súp lơ — Antioxidant cao",
      "🥕 Cà rốt, bí đỏ — Beta carotene",
      "🍓 Dâu tây, blueberry, quả mọng — Anthocyanin (chống viêm mạnh)",
      "🥬 Rau bina, rau cải — Lutein, zeaxanthin (bảo vệ phổi)",
      "🍎 Táo, lê — Quercetin (chống viêm)",
      "🧄 Tỏi, hành — Allicin (kháng khuẩn, chống viêm)",
      "🫒 Dầu ô-liu (extra virgin) — Polyphenol (antioxidant)",
      "🌰 Hạt hạnh nhân, hạt macadamia — Vitamin E, Selenium",
      "🌾 Gạo lứt, lúa mạch, yến mạch — Chất xơ, Selenium",
      
      "\n❌ Tránh: Đồ chiên, đồ rán, thức ăn nhanh",
      "❌ Tránh: Thịt đỏ, thịt xử lý, xúc xích",
      "❌ Tránh: Bánh trắng, cơm trắng, đường",
      "❌ Tránh: Nước ngọt, nước cam (gas → khó tiêu)",
      "❌ Tránh: Sữa/phomat quá nhiều (có thể tăng chất nhầy)"
    );
  }
}
```

---

## IV. DIABETES — TIỂU ĐƯỜNG

### 4.1. Phân loại Tiểu Đường

```
Type 1: Tự miễn, tuyến tụy không sản xuất insulin
Type 2: Kháng insulin, tuyến tụy sản xuất insulin nhưng cơ thể không sử dụng hiệu quả
Gestational: Thai kỳ
Prediabetes: HbA1c 5.7-6.4%
```

### 4.2. Ràng Buộc Dinh Dưỡng

```java
class DiabetesHandler {
  
  /**
   * Xác định kiểm soát glucose dựa trên HbA1c
   */
  enum GlucoseControl {
    EXCELLENT (new double[]{0, 5.7}),      // HbA1c < 5.7% — bình thường
    GOOD (new double[]{5.7, 6.5}),         // 5.7-6.4% — tiền tiểu đường / kiểm soát tốt
    FAIR (new double[]{6.5, 8.0}),         // 6.5-7.9% — kiểm soát vừa phải
    POOR (new double[]{8.0, 9.0}),         // 8.0-8.9% — kiểm soát yếu
    VERY_POOR (new double[]{9.0, 15.0});   // > 9% — kiểm soát rất yếu
    
    double minHbA1c;
    double maxHbA1c;
    
    GlucoseControl(double[] range) {
      this.minHbA1c = range[0];
      this.maxHbA1c = range[1];
    }
  }
  
  /**
   * Ràng buộc dinh dưỡng cho tiểu đường
   */
  public NutrientConstraints getNutrientConstraints(
    double hbA1c,
    double weightKg
  ) {
    GlucoseControl control = determineGlucoseControl(hbA1c);
    NutrientConstraints constraints = new NutrientConstraints();
    
    // Chung cho tiểu đường:
    constraints.carbsPercentOfCal = 45; // 45% calo từ carbs (< 50%)
    constraints.lowGICarbs = true; // Ưu tiên GI < 55
    constraints.fiberGPerDay = 30; // Cao chất xơ: 30g/ngày
    constraints.proteinGPerKg = 1.2; // Tăng protein nhẹ (giữ cơ, tăng satiety)
    constraints.sodiumMgPerDay = 2300; // Kiểm soát huyết áp (thường có liên quan)
    
    // Điều chỉnh theo HbA1c:
    if (control == GlucoseControl.POOR || control == GlucoseControl.VERY_POOR) {
      // Kiểm soát kém: cắt giảm carbs, tăng chất xơ
      constraints.carbsPercentOfCal = 40;
      constraints.fiberGPerDay = 35;
      constraints.notes = "⚠️ Kiểm soát glucose yếu. Cắt giảm carbs, tăng chất xơ, protein.";
    } else if (control == GlucoseControl.FAIR) {
      constraints.carbsPercentOfCal = 45;
      constraints.fiberGPerDay = 30;
      constraints.notes = "Kiểm soát vừa phải. Chia nhỏ bữa ăn, ưu tiên GI thấp.";
    } else {
      constraints.carbsPercentOfCal = 50;
      constraints.fiberGPerDay = 25;
      constraints.notes = "Kiểm soát tốt. Tiếp tục duy trì chế độ ăn hiện tại.";
    }
    
    return constraints;
  }
  
  private GlucoseControl determineGlucoseControl(double hbA1c) {
    if (hbA1c < 5.7) return GlucoseControl.EXCELLENT;
    if (hbA1c < 6.5) return GlucoseControl.GOOD;
    if (hbA1c < 8.0) return GlucoseControl.FAIR;
    if (hbA1c < 9.0) return GlucoseControl.POOR;
    return GlucoseControl.VERY_POOR;
  }
  
  /**
   * Tính Glycemic Index (GI) của carbs
   * GI < 55: Low GI (ưu tiên)
   * GI 56-69: Medium GI (giới hạn)
   * GI >= 70: High GI (tránh)
   */
  public double calculateMealGI(List<MealItem> carbItems) {
    double totalGI = 0;
    double totalCarbs = 0;
    
    for (MealItem item : carbItems) {
      if (item.category.equals("CARBS") || item.category.equals("FRUIT")) {
        int gi = getFoodGI(item.name);
        totalGI += (gi * item.carbsGrams);
        totalCarbs += item.carbsGrams;
      }
    }
    
    return totalCarbs > 0 ? totalGI / totalCarbs : 0;
  }
  
  /**
   * Bảng GI của các thực phẩm
   */
  private int getFoodGI(String foodName) {
    String nameLower = foodName.toLowerCase();
    
    // Low GI (< 55)
    if (nameLower.contains("brown rice") || nameLower.contains("oat")) return 50;
    if (nameLower.contains("whole wheat")) return 48;
    if (nameLower.contains("apple") || nameLower.contains("pear")) return 38;
    if (nameLower.contains("lentil") || nameLower.contains("bean")) return 32;
    if (nameLower.contains("sweet potato")) return 63; // Medium
    if (nameLower.contains("corn")) return 60;
    
    // Medium GI (56-69)
    if (nameLower.contains("white bread")) return 75; // High
    if (nameLower.contains("white rice")) return 73;
    if (nameLower.contains("juice") && !nameLower.contains("no sugar")) return 90;
    
    // High GI (>= 70)
    if (nameLower.contains("candy") || nameLower.contains("sugar")) return 100;
    if (nameLower.contains("soda")) return 95;
    
    return 60; // Default: Medium
  }
  
  /**
   * Lọc thực phẩm — tránh high GI & high sugar
   */
  public List<MealItem> filterFoodItemsForDiabetes(
    List<MealItem> items
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> highGIFoods = Arrays.asList(
      "white rice", "white bread", "candy", "sugar", "soda", "juice",
      "donut", "cake", "cookie", "sweet", "fried rice", "instant noodles"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      for (String food : highGIFoods) {
        if (itemName.contains(food)) {
          isAllowed = false;
          break;
        }
      }
      
      // Kiểm tra Glycemic Index nếu carbs
      if (isAllowed && (item.category.equals("CARBS") || item.category.equals("FRUIT"))) {
        int gi = getFoodGI(itemName);
        if (gi >= 70) { // High GI
          isAllowed = false;
        }
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm low GI & high fiber
   */
  public List<String> getRecommendedFoods() {
    return Arrays.asList(
      "🍚 Gạo lứt, lúa mạch, yến mạch (GI 45-50) — Low GI",
      "🍞 Bánh lúa mạch, bánh đen (GI 45-60)",
      "🫘 Đậu đen, đậu xanh, đậu gàu (~GI 30-35) — Rất thấp",
      "🥬 Rau xanh (bina, cải, bó xôi) — GI gần 0",
      "🥦 Bông cải xanh, súp lơ — GI 0",
      "🥕 Cà rốt — GI 35",
      "🍎 Táo, lê, quả mọng (GI 30-50) — Carb thấp",
      "🥒 Dưa chuột, dưa hấu — Carb rất thấp",
      "🐟 Cá, tôm — Protein, không ảnh hưởng glucose",
      "🥚 Trứng — Protein, không ảnh hưởng glucose",
      
      "\n❌ Tránh hoàn toàn: Candy, sơ-cô-la, nước ngọt, bánh ngọt",
      "❌ Tránh: Nước trái cây, juice (ngay cả no sugar)",
      "❌ Tránh: Bánh trắng, cơm trắng, mì ăn liền",
      "❌ Tránh: Corn flakes, granola (high sugar)",
      "❌ Tránh: Mật ong, rượu, bia"
    );
  }
}
```

---

## V. HYPERTENSION — HUYẾT ÁP CAO

### 5.1. Mục tiêu Huyết Áp

```
Normal: < 120/80 mmHg
Elevated: 120-129/<80 mmHg
Stage 1 Hypertension: 130-139/80-89 mmHg
Stage 2 Hypertension: >= 140/90 mmHg
```

### 5.2. Ràng Buộc Dinh Dưỡng

```java
class HypertensionHandler {
  
  /**
   * Ràng buộc dinh dưỡng cho huyết áp cao
   * DASH diet (Dietary Approaches to Stop Hypertension)
   */
  public NutrientConstraints getNutrientConstraints(
    int systolicBP,
    double weightKg
  ) {
    NutrientConstraints constraints = new NutrientConstraints();
    
    // DASH diet
    constraints.sodiumMgPerDay = 2300; // Hạn chế: < 2300mg (hoặc 1500mg nếu stage 2)
    constraints.potassiumMgPerDay = 3500; // Tăng: 3500-4700mg
    constraints.magnesiumMgPerDay = 420; // Tăng: 420mg (nam)
    constraints.calciumMgPerDay = 1200; // Tăng: 1200mg
    constraints.fiberGPerDay = 30; // Chất xơ cao
    constraints.proteinGPerKg = 1.0; // 1.0g/kg
    constraints.saturatedFatPercentOfCal = 10; // < 10%
    
    // Điều chỉnh theo BP
    if (systolicBP >= 140) {
      // Stage 2: Hạn chế cắt cứu sodium
      constraints.sodiumMgPerDay = 1500;
      constraints.notes = "🔴 Stage 2 Hypertension. Hạn chế RẤT NGHIÊM NGẶT sodium < 1500mg.";
    } else if (systolicBP >= 130) {
      // Stage 1: Hạn chế sodium
      constraints.sodiumMgPerDay = 1500;
      constraints.notes = "🟡 Stage 1 Hypertension. Hạn chế sodium < 1500mg.";
    } else {
      constraints.sodiumMgPerDay = 2300;
      constraints.notes = "✅ Huyết áp cao bình thường. Hạn chế sodium < 2300mg, tăng K, Mg.";
    }
    
    return constraints;
  }
  
  /**
   * Điều chỉnh calo — có thể cần giảm nếu thừa cân
   */
  public double adjustCalorieForHypertension(
    double baseMagicCalories,
    double currentBMI,
    String goal
  ) {
    // Nếu BMI > 25 (thừa cân) & chưa giảm cân, khuyến cáo giảm calo
    if (currentBMI > 25 && !goal.equals("LOSE_WEIGHT")) {
      return baseMagicCalories * 0.9; // Giảm 10%
    }
    
    return baseMagicCalories;
  }
  
  /**
   * Lọc thực phẩm — tránh high sodium
   */
  public List<MealItem> filterFoodItemsForHypertension(
    List<MealItem> items
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> highSodiumFoods = Arrays.asList(
      "canned", "processed", "pickled", "salt", "soy sauce", "fish sauce",
      "sausage", "bacon", "ham", "cured", "smoked", "broth", "stock",
      "cheese", "bread", "butter with salt", "seasoning salt", "monosodium glutamate"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      for (String food : highSodiumFoods) {
        if (itemName.contains(food)) {
          isAllowed = false;
          break;
        }
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm — DASH diet
   */
  public List<String> getRecommendedFoods() {
    return Arrays.asList(
      "🥗 Rau xanh tươi (không mặn) — High K, Mg, Ca",
      "🥦 Bông cải xanh, súp lơ, bí xanh",
      "🍎 Táo, lê, cam, bưởi (HIGH POTASSIUM)",
      "🥑 Bơ — Potassium, chất béo tốt",
      "🍌 Chuối — Potassium rất cao",
      "🍓 Dâu tây, blueberry — Antioxidant",
      "🥕 Cà rốt, khoai ngọt (luộc, không muối)",
      "🫘 Đậu đen, đậu gàu, đậu hộp (rửa để giảm sodium)",
      "🐟 Cá (không muối) — Omega-3, protein",
      "🥚 Trứng (không thêm muối)",
      "🌰 Hạt (không muối): Hạnh nhân, hạt sunflower",
      "🥛 Sữa low-fat, sữa không mặn — Calcium",
      "🫒 Dầu ô-liu — Chất béo tốt",
      
      "\n❌ Tránh hoàn toàn: Muối, nước mắm, sốt xà lách",
      "❌ Tránh: Thực phẩm đóng hộp, xúc xích, thịt xử lý",
      "❌ Tránh: Phô mai, mỡ động vật, bơ (saturated fat)",
      "❌ Tránh: Nước ngọt, coffee quá nhiều",
      "❌ Tránh: Rượu, bia"
    );
  }
}
```

---

## VI. HEART DISEASE — BỆNH TIM

### 6.1. Các Loại Bệnh Tim

```
Coronary Artery Disease (CAD) — Bệnh tim mạch vành
Heart Failure — Suy tim
Arrhythmia — Rối loạn nhịp tim
Valvular Heart Disease — Bệnh van tim
```

### 6.2. Ràng Buộc Dinh Dưỡng

```java
class HeartDiseaseHandler {
  
  /**
   * Ràng buộc dinh dưỡng cho bệnh tim
   */
  public NutrientConstraints getNutrientConstraints(
    String heartDiseaseType,
    double weightKg
  ) {
    NutrientConstraints constraints = new NutrientConstraints();
    
    // Chung cho bệnh tim:
    constraints.sodiumMgPerDay = 2300; // Hạn chế sodium (hoặc < 1500 nếu suy tim)
    constraints.potassiumMgPerDay = 3500; // Tăng potassium
    constraints.proteinGPerKg = 1.0; // Normal protein
    constraints.saturatedFatPercentOfCal = 7; // < 7% (rất hạn chế)
    constraints.transFat = "0"; // Hoàn toàn tránh trans fat
    constraints.cholesterolMgPerDay = 200; // < 200mg cholesterol/ngày
    constraints.fiberGPerDay = 30; // Chất xơ cao (giảm cholesterol)
    constraints.omega3FattyAcidGPerDay = 2; // Omega-3: 2g/ngày
    
    if (heartDiseaseType.equals("HEART_FAILURE")) {
      // Suy tim: hạn chế nước & sodium
      constraints.sodiumMgPerDay = 1500;
      constraints.fluidLitersPerDay = 1.5; // Hạn chế nước (phù nề)
      constraints.notes = "Suy tim: Hạn chế SODIUM < 1500mg, NƯỚC < 1.5L/ngày.";
    } else {
      constraints.notes = "Bệnh tim: Giảm saturated fat, cholesterol. Tăng omega-3, chất xơ.";
    }
    
    return constraints;
  }
  
  /**
   * Lọc thực phẩm — tránh saturated fat & cholesterol cao
   */
  public List<MealItem> filterFoodItemsForHeartDisease(
    List<MealItem> items
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> unhealthyFoods = Arrays.asList(
      "butter", "cream", "whole milk", "cheese (high fat)", "red meat",
      "pork", "fried", "fast food", "trans fat", "coconut oil", "palm oil",
      "egg yolk (excess)", "organ meat", "processed meat", "sausage"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      for (String food : unhealthyFoods) {
        if (itemName.contains(food)) {
          isAllowed = false;
          break;
        }
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm — Heart Healthy
   */
  public List<String> getRecommendedFoods() {
    return Arrays.asList(
      "🐟 Cá có dầu (cá hồi, cá trích) — Omega-3 cao",
      "🥦 Rau xanh (bina, cải, bó xôi)",
      "🥬 Salad xanh — Chất xơ, vitamin",
      "🍎 Táo (với vỏ) — Pectin (giảm cholesterol)",
      "🥕 Cà rốt — Beta carotene",
      "🍊 Cam, quýt — Vitamin C",
      "🫘 Đậu, lạc — Chất xơ, protein thực vật",
      "🌾 Yến mạch — Soluble fiber (giảm LDL)",
      "🥑 Bơ — Monounsaturated fat",
      "🌰 Hạt hạnh nhân, hạt óc chó — Vitamin E, phytosterol",
      "🫒 Dầu ô-liu (extra virgin) — Polyphenol",
      "🧄 Tỏi — Allicin (giảm cholesterol nhẹ)",
      "🍵 Trà xanh — Antioxidant",
      
      "\n❌ Tránh hoàn toàn: Bơ, kem, sữa toàn phần",
      "❌ Tránh: Thịt đỏ (bò, lợn), lòng",
      "❌ Tránh: Đồ chiên, đồ rán",
      "❌ Tránh: Nước ngọt, bánh ngọt",
      "❌ Tránh: Rượu, bia"
    );
  }
}
```

---

## VII. ACID REFLUX / GERD — TRÀO NGƯỢC ACID

### 7.1. Ràng Buộc Dinh Dưỡng

```java
class AcidRefluxHandler {
  
  /**
   * Ràng buộc dinh dưỡng cho GERD
   */
  public NutrientConstraints getNutrientConstraints(double weightKg) {
    NutrientConstraints constraints = new NutrientConstraints();
    
    constraints.mealFrequency = "SMALL_FREQUENT"; // Bữa nhỏ, thường xuyên
    constraints.fatGPerDay = 50; // Giảm chất béo (từ bình thường)
    constraints.proteinGPerKg = 1.0;
    constraints.notes = "Ăn bữa nhỏ mỗi 2-3 giờ. Tránh đồ cay, đồ béo.";
    
    return constraints;
  }
  
  /**
   * Lọc thực phẩm — tránh trigger foods
   */
  public List<MealItem> filterFoodItemsForAcidReflux(
    List<MealItem> items
  ) {
    List<MealItem> filtered = new ArrayList<>();
    
    List<String> triggerFoods = Arrays.asList(
      "spicy", "chili", "curry", "onion", "garlic", "tomato", "citrus",
      "orange", "lemon", "pineapple", "vinegar", "coffee", "tea (strong)",
      "chocolate", "mint", "fatty", "fried", "greasy", "heavy sauce"
    );
    
    for (MealItem item : items) {
      String itemName = item.name.toLowerCase();
      boolean isAllowed = true;
      
      for (String food : triggerFoods) {
        if (itemName.contains(food)) {
          isAllowed = false;
          break;
        }
      }
      
      if (isAllowed) {
        filtered.add(item);
      }
    }
    
    return filtered;
  }
  
  /**
   * Gợi ý thực phẩm — GERD-friendly
   */
  public List<String> getRecommendedFoods() {
    return Arrays.asList(
      "🍗 Ức gà (không da) — Protein, ít chất béo",
      "🐟 Cá trắng (cá basa, cá hồi) — Omega-3, ít béo",
      "🍚 Gạo trắng, lúa mạch — Carbs trung tính",
      "🥕 Cà rốt, khoai tây (luộc) — Dễ tiêu",
      "🥦 Bông cải xanh, súp lơ (luộc mềm)",
      "🥒 Dưa chuột, đậu — Alkaline",
      "🥛 Sữa low-fat — Tăng pH dạ dày",
      "🍌 Chuối — Bảo vệ dạ dày",
      "🍎 Táo (không da) — Có pectin",
      "🍚 Oatmeal, yến mạch — Dễ tiêu",
      "🍗 Trứng (luộc, không rán)",
      
      "\n❌ Tránh hoàn toàn: Cà chua, nước cà chua, salad sốt",
      "❌ Tránh: Cà phê, trà đặc, soda",
      "❌ Tránh: Chocolate, caramel, bạc hà",
      "❌ Tránh: Đồ cay, cà ri, tiêu",
      "❌ Tránh: Hành, tỏi (nếu trigger)",
      "❌ Tránh: Đồ chiên, đồ béo, kem",
      "❌ Tránh: Rượu, bia"
    );
  }
}
```

---

## VIII. MEDICAL CONDITION MANAGER — TÍCH HỢP TẤT CẢ

```java
class MedicalConditionManager {
  
  private KidneyDiseaseHandler kidneyHandler = new KidneyDiseaseHandler();
  private LungDiseaseHandler lungHandler = new LungDiseaseHandler();
  private DiabetesHandler diabetesHandler = new DiabetesHandler();
  private HypertensionHandler hypertensionHandler = new HypertensionHandler();
  private HeartDiseaseHandler heartHandler = new HeartDiseaseHandler();
  private AcidRefluxHandler acidHandler = new AcidRefluxHandler();
  
  /**
   * Xử lý từng bệnh lý
   */
  public MealRecommendation applyMedicalConditions(
    MealRecommendation basePlan,
    HealthProfile profile
  ) {
    MealRecommendation plan = basePlan;
    
    for (String condition : profile.medicalConditions) {
      switch (condition) {
        case "KIDNEY_DISEASE":
          plan = applyKidneyDisease(plan, profile);
          break;
        case "LUNG_DISEASE":
          plan = applyLungDisease(plan, profile);
          break;
        case "DIABETES":
          plan = applyDiabetes(plan, profile);
          break;
        case "HYPERTENSION":
          plan = applyHypertension(plan, profile);
          break;
        case "HEART_DISEASE":
          plan = applyHeartDisease(plan, profile);
          break;
        case "ACID_REFLUX":
          plan = applyAcidReflux(plan, profile);
          break;
      }
    }
    
    return plan;
  }
  
  private MealRecommendation applyKidneyDisease(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    // Lấy stage thận từ profile (giả sử có eGFR)
    double eGFR = profile.eGFR; // Giả sử HealthProfile có eGFR
    KidneyDiseaseHandler.CKDStage stage = kidneyHandler.determineStage(eGFR);
    
    // Lọc thực phẩm
    for (Meal meal : plan.meals) {
      meal.items = kidneyHandler.filterFoodItemsForKidney(meal.items, stage);
    }
    
    // Điều chỉnh calo
    plan.totalDailyCalories = kidneyHandler.adjustCalorieForKidneyDisease(
      plan.totalDailyCalories,
      profile.weightKg,
      stage
    );
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(kidneyHandler.getRecommendedFoods(stage));
    
    return plan;
  }
  
  private MealRecommendation applyLungDisease(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    // Lọc thực phẩm
    for (Meal meal : plan.meals) {
      meal.items = lungHandler.filterFoodItemsForLung(meal.items);
    }
    
    // Điều chỉnh calo (tăng 15%)
    plan.totalDailyCalories = lungHandler.adjustCalorieForLungDisease(
      plan.totalDailyCalories,
      profile.weightKg
    );
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(lungHandler.getRecommendedFoods());
    
    return plan;
  }
  
  private MealRecommendation applyDiabetes(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    double hbA1c = profile.hbA1c; // Giả sử có HbA1c
    
    // Lọc thực phẩm (tránh high GI)
    for (Meal meal : plan.meals) {
      meal.items = diabetesHandler.filterFoodItemsForDiabetes(meal.items);
    }
    
    // Tính Glycemic Index của bữa
    for (Meal meal : plan.meals) {
      double mealGI = diabetesHandler.calculateMealGI(meal.items);
      meal.notes = String.format("Meal GI: %.1f", mealGI);
    }
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(diabetesHandler.getRecommendedFoods());
    
    return plan;
  }
  
  private MealRecommendation applyHypertension(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    // Lọc thực phẩm (tránh high sodium)
    for (Meal meal : plan.meals) {
      meal.items = hypertensionHandler.filterFoodItemsForHypertension(meal.items);
    }
    
    // Điều chỉnh calo nếu thừa cân
    plan.totalDailyCalories = hypertensionHandler.adjustCalorieForHypertension(
      plan.totalDailyCalories,
      profile.currentBMI,
      profile.goal
    );
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(hypertensionHandler.getRecommendedFoods());
    
    return plan;
  }
  
  private MealRecommendation applyHeartDisease(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    // Lọc thực phẩm (tránh saturated fat)
    for (Meal meal : plan.meals) {
      meal.items = heartHandler.filterFoodItemsForHeartDisease(meal.items);
    }
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(heartHandler.getRecommendedFoods());
    
    return plan;
  }
  
  private MealRecommendation applyAcidReflux(
    MealRecommendation plan,
    HealthProfile profile
  ) {
    // Lọc thực phẩm (tránh trigger foods)
    for (Meal meal : plan.meals) {
      meal.items = acidHandler.filterFoodItemsForAcidReflux(meal.items);
    }
    
    // Chia bữa nhỏ hơn, thường xuyên hơn
    // (implement logic để chia 5-6 bữa thay vì 4-5)
    
    // Thêm gợi ý
    plan.dietaryRecommendations.addAll(acidHandler.getRecommendedFoods());
    
    return plan;
  }
}
```

---

## IX. VALIDATION & CONFLICT RESOLUTION

```java
class MedicalConditionValidator {
  
  /**
   * Kiểm tra xung đột giữa các bệnh lý
   */
  public List<String> detectConflicts(List<String> conditions) {
    List<String> conflicts = new ArrayList<>();
    
    // Kidney Disease + Hypertension: OK (cùng hạn chế sodium)
    // Lung Disease + Diabetes: OK (cùng chất xơ cao)
    // Heart Disease + Diabetes: OK (cùng giảm saturated fat)
    
    // Kidney Disease (high potassium restriction) vs Hypertension (low sodium + HIGH potassium)
    if (conditions.contains("KIDNEY_DISEASE") && conditions.contains("HYPERTENSION")) {
      // Nếu Kidney Stage 4-5 (potassium strict), conflict với HYPERTENSION (potassium high)
      conflicts.add("⚠️ Kidney Disease vs Hypertension: Cần cân bằng Sodium hạn chế nhưng Potassium cũng hạn chế (nếu kidney stage nặng)");
    }
    
    return conflicts;
  }
  
  /**
   * Xử lý ưu tiên khi có xung đột
   */
  public List<String> resolvePriority(List<String> conditions) {
    // Thứ tự ưu tiên (Severity-based):
    // 1. KIDNEY_DISEASE (Stage 4-5)
    // 2. HEART_DISEASE
    // 3. DIABETES
    // 4. HYPERTENSION
    // 5. LUNG_DISEASE
    // 6. ACID_REFLUX
    
    List<String> prioritized = new ArrayList<>();
    
    if (conditions.contains("KIDNEY_DISEASE")) prioritized.add("KIDNEY_DISEASE");
    if (conditions.contains("HEART_DISEASE")) prioritized.add("HEART_DISEASE");
    if (conditions.contains("DIABETES")) prioritized.add("DIABETES");
    if (conditions.contains("HYPERTENSION")) prioritized.add("HYPERTENSION");
    if (conditions.contains("LUNG_DISEASE")) prioritized.add("LUNG_DISEASE");
    if (conditions.contains("ACID_REFLUX")) prioritized.add("ACID_REFLUX");
    
    return prioritized;
  }
}
```

---

## X. SUMMARY TABLE — CỰC KỲ NHANH

| Bệnh Lý | Protein | Sodium | Potassium | Carbs | Chất Xơ | Ghi Chú |
|---------|---------|--------|-----------|-------|---------|---------|
| **KIDNEY** | 0.6-0.8g/kg | <1200mg | <2000mg | Normal | Normal | Tránh: K, P cao |
| **LUNG** | 1.0g/kg | Normal | Normal | Normal | 30g | Tăng: Antioxidant, Omega-3 |
| **DIABETES** | 1.2g/kg | Normal | Normal | 40-50% | 30g | Low GI < 55 |
| **HYPERTENSION** | 1.0g/kg | <1500mg | 3500-4700mg | Normal | 30g | DASH diet |
| **HEART** | 1.0g/kg | <2300mg | Normal | Normal | 30g | Sat fat < 7%, Omega-3 |
| **GERD** | 1.0g/kg | Normal | Normal | Normal | Normal | Bữa nhỏ, tránh trigger |

---

## XI. USAGE EXAMPLE — ÁP DỤNG THỰC TẾ

```java
// Ví dụ: Khách hàng có 2 bệnh (Kidney + Diabetes)
HealthProfile profile = new HealthProfile();
profile.gender = "FEMALE";
profile.weightKg = 65;
profile.medicalConditions = Arrays.asList("KIDNEY_DISEASE", "DIABETES");
profile.eGFR = 35; // Stage 3B
profile.hbA1c = 7.5; // Fair control

MedicalConditionManager manager = new MedicalConditionManager();

// 1. Kiểm tra xung đột
List<String> conflicts = manager.detectConflicts(profile.medicalConditions);
// Output: "⚠️ Kidney Disease vs Diabetes: Cần cân bằng..."

// 2. Xác định ưu tiên
List<String> priority = manager.resolvePriority(profile.medicalConditions);
// Output: [KIDNEY_DISEASE, DIABETES]

// 3. Tính calo base
CalorieCalculation calorieCalc = calorieEngine.calculateMagicCalories(profile, tmr);
// Base: 1800 kcal

// 4. Xây dựng meal plan base
MealRecommendation basePlan = mealEngine.buildMealPlan(profile, 1800);

// 5. Áp dụng bệnh lý
MealRecommendation finalPlan = manager.applyMedicalConditions(basePlan, profile);

// Kết quả:
// - Protein: 65 × 0.6 = 39g (Kidney priority)
// - Potassium: < 2000mg (Kidney)
// - Sodium: < 1200mg (Kidney)
// - Carbs: Low GI (Diabetes)
// - Fiber: 30g (Diabetes)
```

---
