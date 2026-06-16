# **MEAL RECOMMENDATION RULE ENGINE — PSEUDO CODE (Java)**
## Tính Calo kỳ diệu & Xây dựng Gợi ý Bữa ăn

**Phiên bản:** v1.0  
**Cơ sở:** `02.Tinh-Calories-Goi-y-bua-an.md`  
**Mục đích:** Pseudo code Java để lập trình rule engine tính Calo & gợi ý bữa ăn dựa trên sức khỏe, thói quen, bệnh lý, nhu cầu.

---

## I. DATA MODELS

### 1. HealthProfile — Hồ sơ sức khỏe
```java
class HealthProfile {
  // Thông tin cá nhân
  String gender;           // "MALE", "FEMALE"
  int age;
  double weightKg;         // Cân nặng (kg)
  double heightCm;         // Chiều cao (cm)
  double currentBMI;       // BMI hiện tại
  
  // RMR/AMR (tính toán từ công thức)
  double rmr;              // Năng lượng nghỉ ngơi (kcal)
  double amr;              // Năng lượng hoạt động (kcal)
  
  // Hoạt động thể dục (lifestyle)
  boolean exerciseDaily;   // Tập luyện hàng ngày?
  double exerciseCalories; // Calo tiêu hao từ tập luyện (kcal)
  String exerciseType;     // "CARDIO", "STRENGTH", "MIXED", "NONE"
  int exerciseMinutes;     // Phút/ngày
  
  // Thói quen sinh hoạt
  double waterLitersPerDay; // Lượng nước uống/ngày (lít)
  int sleepHoursPerDay;    // Giờ ngủ/ngày
  String activityLevel;    // "SEDENTARY", "LIGHTLY_ACTIVE", "MODERATELY_ACTIVE", "VERY_ACTIVE"
  
  // Bệnh lý & điều kiện sức khỏe
  List<String> medicalConditions; // ["KIDNEY_DISEASE", "LUNG_DISEASE", "DIABETES", "HYPERTENSION", ...]
  boolean hasAllergies;
  List<String> foodAllergies;     // ["NUTS", "SHELLFISH", ...]
  
  // Nhu cầu mong muốn
  String goal;             // "LOSE_WEIGHT", "GAIN_WEIGHT", "MAINTAIN", "REJUVENATE"
  double targetWeightKg;   // Cân nặng mục tiêu (kg)
  int timeframeWeeks;      // Khung thời gian (tuần)
  
  // Thói quen ăn uống
  List<String> preferredFoods;
  String mealFrequency;    // "FOUR_MEALS", "FIVE_MEALS"
}
```

### 2. CalorieCalculation — Kết quả tính calo
```java
class CalorieCalculation {
  double rmr;              // Năng lượng nghỉ ngơi
  double amr;              // Năng lượng hoạt động
  double exerciseCalories; // Năng lượng thể dục
  double tmr;              // Tổng năng lượng tiêu hao
  double magicCalories;    // Calo kỳ diệu (sau điều chỉnh)
  
  String goalStrategy;     // Chiến lược mục tiêu
  double dailyCalorieTarget; // Mục tiêu calo/ngày
  double weeklyCalorieDeficit; // Thâm hụt calo/tuần (nếu giảm cân)
  double estimatedWeeklyWeightChange; // Thay đổi cân nặng dự kiến/tuần (kg)
  
  List<String> notes;      // Ghi chú (cảnh báo, khuyến cáo)
}
```

### 3. MealRecommendation — Gợi ý bữa ăn
```java
class MealRecommendation {
  double totalDailyCalories;  // Tổng calo/ngày
  String mealPlan;             // "FOUR_MEALS" hoặc "FIVE_MEALS"
  
  List<Meal> meals;            // Danh sách các bữa ăn
  
  // Cấu trúc dinh dưỡng
  double proteinGrams;         // Đạm (grams)
  double carbsGrams;           // Carbs (grams)
  double fatGrams;             // Chất béo (grams)
  double fiberGrams;           // Chất xơ (grams)
  
  // Khuyến cáo đặc biệt
  List<String> medicalRestrictions; // ["LOW_SODIUM", "LOW_POTASSIUM", ...]
  List<String> dietaryRecommendations; // Gợi ý (chọn protein trắng, tránh thịt đỏ, ...)
  double minWaterIntake;       // Lượng nước tối thiểu/ngày (lít)
}

class Meal {
  String mealName;        // "Breakfast", "Morning Snack", "Lunch", ...
  String mealTime;        // "07:00", "09:00", "12:00", ...
  double targetCalories;  // Calo mục tiêu bữa ăn này
  
  List<MealItem> items;   // Các thành phần bữa ăn
  
  double totalCalories;   // Tổng calo thực tế
  double proteinGrams;
  double carbsGrams;
  double fatGrams;
}

class MealItem {
  String name;            // "2 scoops F1", "1 grilled chicken breast", ...
  String category;        // "PROTEIN", "CARBS", "FRUIT", "VEGETABLE", ...
  double servingSize;     // Kích thước phục vụ
  String unit;            // "grams", "ml", "portion", ...
  double calories;        // Calo của mục này
  double proteinGrams;
  double carbsGrams;
  double fatGrams;
}
```

---

## II. CORE ENGINE — TÍNH CALO KỲ DIỆU

### 1. RMR/BMR Calculator
```java
class CalorieCalculationEngine {
  
  /**
   * Bước 1: Tính Năng lượng nghỉ ngơi (RMR/BMR)
   * Công thức Harris-Benedict
   */
  public double calculateRMR(HealthProfile profile) {
    double rmr;
    
    if (profile.gender.equals("FEMALE")) {
      rmr = 10 * profile.weightKg 
          + 6.25 * profile.heightCm 
          - 5 * profile.age 
          - 161;
    } else { // MALE
      rmr = 10 * profile.weightKg 
          + 6.25 * profile.heightCm 
          - 5 * profile.age 
          + 5;
    }
    
    // Cảnh báo nếu RMR quá thấp
    if (rmr < 1000) {
      LOG.warn("RMR < 1000 kcal — thay đổi dữ liệu health profile");
    }
    
    return Math.max(rmr, 1000); // Tối thiểu 1000 kcal
  }
  
  /**
   * Bước 2: Tính Năng lượng hoạt động (AMR)
   * Dựa trên giới tính & hoạt động hàng ngày
   */
  public double calculateAMR(HealthProfile profile, double rmr) {
    double multiplier;
    
    if (profile.gender.equals("FEMALE")) {
      multiplier = 0.25;
    } else {
      multiplier = 0.30;
    }
    
    return rmr * multiplier;
  }
  
  /**
   * Bước 3: Tính Năng lượng thể dục (Ex)
   * Chỉ tính nếu tập luyện hàng ngày & có dữ liệu
   */
  public double calculateExerciseCalories(HealthProfile profile) {
    if (!profile.exerciseDaily || profile.exerciseCalories == 0) {
      return 0;
    }
    
    // Hoặc tính dựa trên loại & thời gian tập luyện
    double caloriesPerMinute = getExerciseCaloriesBurnRate(
      profile.exerciseType, 
      profile.gender, 
      profile.weightKg
    );
    
    return caloriesPerMinute * profile.exerciseMinutes;
  }
  
  private double getExerciseCaloriesBurnRate(
    String exerciseType, 
    String gender, 
    double weightKg
  ) {
    // Ước tính calo tiêu hao/phút dựa trên loại tập luyện
    // (Ví dụ: đi bộ 3 km/h = 3-4 kcal/phút)
    switch (exerciseType) {
      case "CARDIO":   // Chạy bộ, bộ lạc, cycling
        return 0.10 * weightKg; // 0.1 * kg/phút (ước tính)
      case "STRENGTH": // Tạ, yoga
        return 0.08 * weightKg;
      case "MIXED":
        return 0.09 * weightKg;
      default:
        return 0;
    }
  }
  
  /**
   * Bước 4: Tính Tổng Năng lượng Tiêu hao (TMR)
   */
  public double calculateTMR(
    double rmr, 
    double amr, 
    double exerciseCalories
  ) {
    return rmr + amr + exerciseCalories;
  }
  
  /**
   * Bước 5: Xác định Con số Calo kỳ diệu cuối cùng
   * Điều chỉnh theo mục tiêu + các yếu tố khác
   */
  public CalorieCalculation calculateMagicCalories(
    HealthProfile profile, 
    double tmr
  ) {
    CalorieCalculation calc = new CalorieCalculation();
    calc.rmr = calculateRMR(profile);
    calc.amr = calculateAMR(profile, calc.rmr);
    calc.exerciseCalories = calculateExerciseCalories(profile);
    calc.tmr = tmr;
    
    double magicCalories = tmr;
    List<String> notes = new ArrayList<>();
    
    // Điều chỉnh theo mục tiêu
    if (profile.goal.equals("LOSE_WEIGHT")) {
      double calorieDeduction;
      
      if (profile.age >= 40) {
        calorieDeduction = 300; // Người >= 40 tuổi: -300 calo
      } else {
        calorieDeduction = 500; // Người < 40 tuổi: -500 calo
      }
      
      magicCalories = tmr - calorieDeduction;
      
      // Đảm bảo không dưới 1000 kcal
      if (magicCalories < 1000) {
        notes.add("⚠️ CẢNH BÁO: Calo target < 1000 kcal. Điều chỉnh mục tiêu giảm cân hoặc tăng tập luyện.");
        magicCalories = 1000;
      }
      
      calc.goalStrategy = "CALORIC_DEFICIT";
      double weeklyDeficit = (magicCalories - tmr) * 7; // Âm số
      calc.weeklyCalorieDeficit = Math.abs(weeklyDeficit);
      calc.estimatedWeeklyWeightChange = -calc.weeklyCalorieDeficit / 7700; // 7700 kcal = 1 kg
      
      notes.add(String.format(
        "Giảm cân: Mục tiêu calo/ngày = %.0f kcal (thâm hụt %.0f kcal/tuần, giảm ~%.2f kg/tuần)",
        magicCalories, calc.weeklyCalorieDeficit, calc.estimatedWeeklyWeightChange
      ));
      
    } else if (profile.goal.equals("GAIN_WEIGHT")) {
      double calorieAddition;
      
      if (profile.age >= 40) {
        calorieAddition = 300;
      } else {
        calorieAddition = 500;
      }
      
      magicCalories = tmr + calorieAddition;
      calc.goalStrategy = "CALORIC_SURPLUS";
      calc.estimatedWeeklyWeightChange = (calorieAddition * 7) / 7700; // Dương số
      
      notes.add(String.format(
        "Tăng cân: Mục tiêu calo/ngày = %.0f kcal (thặng dư %.0f kcal/tuần, tăng ~%.2f kg/tuần)",
        magicCalories, calorieAddition * 7, calc.estimatedWeeklyWeightChange
      ));
      
    } else if (profile.goal.equals("REJUVENATE")) {
      // Trẻ hóa: Giữ TMR nhưng ưu tiên protein, anti-aging foods
      magicCalories = tmr;
      calc.goalStrategy = "MAINTENANCE_WITH_REJUVENATION";
      notes.add("Trẻ hóa: Giữ calo không đổi, ưu tiên protein, chất chống oxy hóa, uống đủ nước.");
      
    } else { // MAINTAIN
      magicCalories = tmr;
      calc.goalStrategy = "MAINTENANCE";
      notes.add(String.format(
        "Giữ cân: Mục tiêu calo/ngày = %.0f kcal",
        magicCalories
      ));
    }
    
    // Điều chỉnh dựa trên bệnh lý
    notes.addAll(applyMedicalAdjustments(profile, magicCalories));
    
    // Điều chỉnh dựa trên thói quen uống nước
    notes.addAll(applyWaterIntakeAdvisory(profile));
    
    calc.magicCalories = magicCalories;
    calc.dailyCalorieTarget = magicCalories;
    calc.notes = notes;
    
    return calc;
  }
  
  /**
   * Điều chỉnh dựa trên bệnh lý
   */
  private List<String> applyMedicalAdjustments(
    HealthProfile profile, 
    double baseCalories
  ) {
    List<String> adjustments = new ArrayList<>();
    
    for (String condition : profile.medicalConditions) {
      switch (condition) {
        case "KIDNEY_DISEASE":
          adjustments.add("🚫 Bệnh thận: Hạn chế Sodium, Potassium. Kiểm soát protein (~0.8g/kg).");
          break;
        case "LUNG_DISEASE":
          adjustments.add("🚫 Bệnh phổi: Tăng chất chống oxy hóa (Vitamin C, E). Hạn chế thực phẩm viêm.");
          break;
        case "DIABETES":
          adjustments.add("🚫 Tiểu đường: Ưu tiên carbs chỉ số đường huyết thấp (GI < 55). Tăng chất xơ.");
          break;
        case "HYPERTENSION":
          adjustments.add("🚫 Huyết áp cao: Hạn chế Sodium < 2300 mg/ngày. Tăng Potassium, Calcium.");
          break;
        case "ACID_REFLUX":
          adjustments.add("🚫 Trào ngược acid: Tránh đồ cay, thực phẩm béo, cà phê. Ăn bữa nhỏ thường xuyên.");
          break;
      }
    }
    
    return adjustments;
  }
  
  /**
   * Khuyến cáo về uống nước
   */
  private List<String> applyWaterIntakeAdvisory(HealthProfile profile) {
    List<String> advisories = new ArrayList<>();
    
    // Lượng nước tối thiểu: 0.4 lít / 10kg cân nặng
    double minWater = (profile.weightKg / 10) * 0.4;
    
    // Nếu giảm cân, tăng lên 0.6-0.7 lít/10kg
    double recommendedWater = minWater;
    if (profile.goal.equals("LOSE_WEIGHT")) {
      recommendedWater = (profile.weightKg / 10) * 0.6;
    }
    
    // Kiểm tra lượng nước thực tế
    if (profile.waterLitersPerDay < minWater) {
      advisories.add(String.format(
        "💧 Uống nước không đủ: Hiện tại %.1f L/ngày. Tối thiểu cần %.1f L/ngày (0.4 L/10kg).",
        profile.waterLitersPerDay, minWater
      ));
    } else if (profile.goal.equals("LOSE_WEIGHT") && profile.waterLitersPerDay < recommendedWater) {
      advisories.add(String.format(
        "💧 Để giảm cân hiệu quả, nên uống %.1f L/ngày (0.6-0.7 L/10kg) thay vì %.1f L.",
        recommendedWater, profile.waterLitersPerDay
      ));
    }
    
    advisories.add(String.format(
      "Lượng nước khuyến cáo: %.1f - %.1f L/ngày (tránh nước có calo: trà đường, bia, cà phê đậm).",
      minWater, recommendedWater
    ));
    
    return advisories;
  }
}
```

---

## III. MEAL RECOMMENDATION ENGINE — XÂY DỰNG GỢI Ý BỮA ĂN

### 1. Meal Template Builder (Base 1200 kcal)
```java
class MealRecommendationEngine {
  
  /**
   * Xây dựng gợi ý bữa ăn dựa trên calo mục tiêu
   * Bắt đầu từ template 1200 kcal, sau đó điều chỉnh
   */
  public MealRecommendation buildMealPlan(
    HealthProfile profile, 
    double targetCalories
  ) {
    MealRecommendation plan = new MealRecommendation();
    plan.totalDailyCalories = targetCalories;
    plan.mealPlan = profile.mealFrequency;
    
    // Bước 1: Lấy template 1200 kcal cơ bản (4 hoặc 5 bữa)
    List<Meal> baseMeals = getBaseMealTemplate(profile.mealFrequency);
    
    // Bước 2: Điều chỉnh calo từ 1200 → targetCalories
    List<Meal> adjustedMeals = adjustCalories(baseMeals, targetCalories);
    
    // Bước 3: Áp dụng ràng buộc bệnh lý & dị ứng
    List<Meal> finalMeals = applyMedicalRestrictions(
      adjustedMeals, 
      profile.medicalConditions, 
      profile.foodAllergies, 
      profile.preferredFoods
    );
    
    plan.meals = finalMeals;
    
    // Bước 4: Tính tổng dinh dưỡng
    double[] macros = calculateMacros(finalMeals);
    plan.proteinGrams = macros[0];
    plan.carbsGrams = macros[1];
    plan.fatGrams = macros[2];
    plan.fiberGrams = macros[3];
    
    // Bước 5: Thêm khuyến cáo
    plan.medicalRestrictions = getMedicalRestrictions(profile.medicalConditions);
    plan.dietaryRecommendations = getDietaryRecommendations(profile);
    plan.minWaterIntake = (profile.weightKg / 10) * 0.4;
    
    return plan;
  }
  
  /**
   * Template 1200 kcal chuẩn (4-5 bữa/ngày)
   */
  private List<Meal> getBaseMealTemplate(String mealFrequency) {
    List<Meal> meals = new ArrayList<>();
    
    // Bữa 1: Sáng (07:00) — ~120 kcal
    Meal breakfast = new Meal();
    breakfast.mealName = "Bữa sáng";
    breakfast.mealTime = "07:00";
    breakfast.targetCalories = 120;
    breakfast.items = Arrays.asList(
      new MealItem("2 muỗng F1 pha 300ml nước lạnh", "PROTEIN", 2, "scoops", 120, 24, 5, 1)
    );
    meals.add(breakfast);
    
    // Bữa 2: Phụ sáng (09:00) — ~100 kcal
    Meal morningSnack = new Meal();
    morningSnack.mealName = "Phụ sáng";
    morningSnack.mealTime = "09:00";
    morningSnack.targetCalories = 100;
    morningSnack.items = Arrays.asList(
      new MealItem("1 quả táo hoặc 1 ly F1", "FRUIT", 1, "portion", 100, 0, 25, 0)
    );
    meals.add(morningSnack);
    
    // Bữa 3: Trưa (12:00) — ~500 kcal
    Meal lunch = new Meal();
    lunch.mealName = "Bữa trưa";
    lunch.mealTime = "12:00";
    lunch.targetCalories = 500;
    lunch.items = Arrays.asList(
      new MealItem("1,5-2 lạng ức gà nướng", "PROTEIN", 150, "grams", 300, 45, 0, 12),
      new MealItem("1 bát cơm rau hấp", "CARBS", 150, "grams", 200, 4, 40, 1)
    );
    meals.add(lunch);
    
    if (mealFrequency.equals("FIVE_MEALS")) {
      // Bữa 4: Phụ chiều (15:00) — ~100 kcal
      Meal afternoonSnack = new Meal();
      afternoonSnack.mealName = "Phụ chiều";
      afternoonSnack.mealTime = "15:00";
      afternoonSnack.targetCalories = 100;
      afternoonSnack.items = Arrays.asList(
        new MealItem("2 muỗng F1 hoặc 1 phần hoa quả", "PROTEIN/FRUIT", 1, "portion", 100, 10, 15, 0)
      );
      meals.add(afternoonSnack);
    }
    
    // Bữa 5: Tối (18:00) — ~380 kcal (tương tự trưa, ưu tiên đạm thực vật)
    Meal dinner = new Meal();
    dinner.mealName = "Bữa tối";
    dinner.mealTime = "18:00";
    dinner.targetCalories = 380;
    dinner.items = Arrays.asList(
      new MealItem("150g đậu phụ hấp hoặc cá hế", "PROTEIN", 150, "grams", 250, 35, 0, 10),
      new MealItem("1 bát rau xanh luộc", "VEGETABLE", 100, "grams", 130, 2, 30, 3)
    );
    meals.add(dinner);
    
    return meals;
  }
  
  /**
   * Điều chỉnh calo từ 1200 kcal → targetCalories
   * Ưu tiên: cộng vào sáng/trưa, trừ vào tối
   */
  private List<Meal> adjustCalories(List<Meal> baseMeals, double targetCalories) {
    double baseTotal = 1200;
    double diff = targetCalories - baseTotal;
    
    List<Meal> adjusted = new ArrayList<>(baseMeals);
    
    if (diff > 0) {
      // Thêm calo: ưu tiên sáng + trưa
      // Cứ 300 kcal = 1 miếng đạm trắng (gà/cá)
      // Cứ 100 kcal = 1 ly F1 hoặc 1 phần hoa quả
      
      double remaining = diff;
      
      // Thêm vào bữa sáng
      if (remaining >= 100) {
        adjusted.get(0).targetCalories += 100;
        adjusted.get(0).items.add(
          new MealItem("1 ly F1 thêm", "PROTEIN", 1, "scoop", 100, 20, 4, 0.5)
        );
        remaining -= 100;
      }
      
      // Thêm vào bữa trưa
      while (remaining >= 300) {
        adjusted.get(2).targetCalories += 300;
        adjusted.get(2).items.add(
          new MealItem("1 miếng ức gà thêm", "PROTEIN", 150, "grams", 300, 45, 0, 12)
        );
        remaining -= 300;
      }
      
      // Thêm sót
      if (remaining > 0) {
        adjusted.get(2).targetCalories += remaining;
        // Thêm một mục tùy chỉnh
      }
      
    } else if (diff < 0) {
      // Giảm calo: ưu tiên tối, giảm carbs trước protein
      double diffAbs = Math.abs(diff);
      
      // Giảm tối (cắt carbs, giữ protein)
      Meal dinnerMeal = adjusted.get(adjusted.size() - 1);
      dinnerMeal.targetCalories += diff; // diff âm
      
      // Xóa mục carbs/vegetable từ tối
      if (dinnerMeal.items.size() > 1) {
        MealItem veg = dinnerMeal.items.get(dinnerMeal.items.size() - 1);
        if (veg.category.contains("VEGETABLE") || veg.category.contains("CARBS")) {
          dinnerMeal.items.remove(dinnerMeal.items.size() - 1);
        }
      }
    }
    
    return adjusted;
  }
  
  /**
   * Áp dụng ràng buộc bệnh lý & dị ứng
   */
  private List<Meal> applyMedicalRestrictions(
    List<Meal> meals,
    List<String> medicalConditions,
    List<String> foodAllergies,
    List<String> preferredFoods
  ) {
    List<Meal> restricted = new ArrayList<>();
    
    for (Meal meal : meals) {
      Meal newMeal = new Meal(meal); // Copy
      
      List<MealItem> filteredItems = new ArrayList<>();
      
      for (MealItem item : meal.items) {
        boolean isAllowed = true;
        String itemName = item.name.toLowerCase();
        
        // Kiểm tra dị ứng
        for (String allergy : foodAllergies) {
          if (itemName.contains(allergy.toLowerCase())) {
            isAllowed = false;
            break;
          }
        }
        
        // Kiểm tra bệnh lý
        if (isAllowed) {
          for (String condition : medicalConditions) {
            // Ví dụ: KIDNEY_DISEASE → tránh nước cứng, cà chua
            if (condition.equals("KIDNEY_DISEASE") && 
                (itemName.contains("potassium") || itemName.contains("salt"))) {
              isAllowed = false;
              break;
            }
            // Ví dụ: DIABETES → ưu tiên GI thấp
            if (condition.equals("DIABETES") && 
                (itemName.contains("white rice") || itemName.contains("sugar"))) {
              isAllowed = false;
              break;
            }
          }
        }
        
        if (isAllowed) {
          filteredItems.add(item);
        }
      }
      
      newMeal.items = filteredItems;
      restricted.add(newMeal);
    }
    
    return restricted;
  }
  
  /**
   * Tính tổng dinh dưỡng (Protein, Carbs, Fat, Fiber)
   */
  private double[] calculateMacros(List<Meal> meals) {
    double protein = 0, carbs = 0, fat = 0, fiber = 0;
    
    for (Meal meal : meals) {
      for (MealItem item : meal.items) {
        protein += item.proteinGrams;
        carbs += item.carbsGrams;
        fat += item.fatGrams;
      }
    }
    
    return new double[]{protein, carbs, fat, fiber};
  }
  
  /**
   * Lấy danh sách ràng buộc dinh dưỡng theo bệnh lý
   */
  private List<String> getMedicalRestrictions(List<String> conditions) {
    List<String> restrictions = new ArrayList<>();
    
    for (String condition : conditions) {
      switch (condition) {
        case "KIDNEY_DISEASE":
          restrictions.addAll(Arrays.asList(
            "LOW_SODIUM (< 2300 mg/ngày)",
            "LOW_POTASSIUM (nếu eGFR < 30)",
            "CONTROLLED_PROTEIN (0.8 g/kg)",
            "LIMIT_PHOSPHORUS"
          ));
          break;
        case "LUNG_DISEASE":
          restrictions.addAll(Arrays.asList(
            "HIGH_ANTIOXIDANT (Vitamin C, E, Selenium)",
            "ANTI_INFLAMMATORY",
            "AVOID_FOOD_TRIGGERS"
          ));
          break;
        case "DIABETES":
          restrictions.addAll(Arrays.asList(
            "LOW_GI (Glycemic Index < 55)",
            "HIGH_FIBER (25-30 g/ngày)",
            "LIMIT_SIMPLE_SUGARS",
            "CONTROLLED_CARBS"
          ));
          break;
      }
    }
    
    return restrictions;
  }
  
  /**
   * Gợi ý ăn uống chung
   */
  private List<String> getDietaryRecommendations(HealthProfile profile) {
    List<String> recs = new ArrayList<>();
    
    recs.add("✓ Ưu tiên đạm trắng (ức gà, cá trắng, tôm, đậu phụ, nấm)");
    recs.add("✓ Hạn chế thịt đỏ (bò, lợn), đồ chiên xào");
    recs.add("✓ Chọn carbs chỉ số đường huyết thấp (gạo lứt, yến mạch, khoai)");
    recs.add("✓ Tăng rau xanh, hoa quả tươi");
    recs.add("✓ Nấu hấp/luộc thay vì xào chiên");
    recs.add("✓ Tránh đồ nếp (bánh chưng, banh trôi)");
    recs.add("✓ Uống nước lọc, tránh nước có calo (trà đường, nước ngọt, bia)");
    
    if (profile.goal.equals("LOSE_WEIGHT")) {
      recs.add("✓ Chia nhỏ bữa ăn (4-5 bữa/ngày) để kiểm soát cơn đói");
      recs.add("✓ Khoảng cách giữa các bữa: ~4 giờ");
    }
    
    recs.add("✓ Dùng đĩa (plate method): 1/2 rau, 1/4 protein, 1/4 carbs");
    
    return recs;
  }
}
```

---

## IV. RULE ENGINE INTEGRATIONS

### 1. Main Engine — Tích hợp toàn bộ
```java
class AnCareMealRecommendationService {
  
  private CalorieCalculationEngine calorieEngine;
  private MealRecommendationEngine mealEngine;
  
  /**
   * Quy trình chính: Input HealthProfile → Output CalorieCalculation + MealRecommendation
   */
  public RecommendationResponse generateRecommendation(HealthProfile profile) {
    // Bước 1: Tính Calo kỳ diệu
    double rmr = calorieEngine.calculateRMR(profile);
    double amr = calorieEngine.calculateAMR(profile, rmr);
    double exerciseCalories = calorieEngine.calculateExerciseCalories(profile);
    double tmr = calorieEngine.calculateTMR(rmr, amr, exerciseCalories);
    
    CalorieCalculation calorieCalc = calorieEngine.calculateMagicCalories(profile, tmr);
    
    // Bước 2: Xây dựng Gợi ý Bữa ăn
    MealRecommendation mealRec = mealEngine.buildMealPlan(
      profile, 
      calorieCalc.dailyCalorieTarget
    );
    
    // Bước 3: Validate & tổng hợp thông báo
    RecommendationResponse response = new RecommendationResponse();
    response.calorieCalculation = calorieCalc;
    response.mealRecommendation = mealRec;
    response.status = "SUCCESS";
    response.generatedAt = LocalDateTime.now();
    
    return response;
  }
}

class RecommendationResponse {
  CalorieCalculation calorieCalculation;
  MealRecommendation mealRecommendation;
  String status; // "SUCCESS", "WARNING", "ERROR"
  LocalDateTime generatedAt;
  List<String> warnings; // Cảnh báo (BMI quá cao, calo quá thấp, ...)
}
```

---

## V. VALIDATION & ERROR HANDLING

### 1. Health Profile Validator
```java
class HealthProfileValidator {
  
  public ValidationResult validate(HealthProfile profile) {
    ValidationResult result = new ValidationResult();
    
    // Kiểm tra tuổi
    if (profile.age < 13 || profile.age > 120) {
      result.addError("Age phải trong khoảng 13-120");
    }
    
    // Kiểm tra cân nặng & chiều cao
    if (profile.weightKg < 30 || profile.weightKg > 250) {
      result.addError("Weight phải trong khoảng 30-250 kg");
    }
    
    if (profile.heightCm < 100 || profile.heightCm > 250) {
      result.addError("Height phải trong khoảng 100-250 cm");
    }
    
    // Kiểm tra nước uống
    if (profile.waterLitersPerDay < 0 || profile.waterLitersPerDay > 10) {
      result.addWarning("Water intake bất thường (< 0 hoặc > 10 L/ngày)");
    }
    
    // Kiểm tra mục tiêu cân nặng
    if (profile.goal.equals("LOSE_WEIGHT") && profile.targetWeightKg >= profile.weightKg) {
      result.addError("Target weight phải nhỏ hơn current weight cho LOSE_WEIGHT goal");
    }
    
    return result;
  }
}

class ValidationResult {
  List<String> errors = new ArrayList<>();
  List<String> warnings = new ArrayList<>();
  
  public boolean isValid() {
    return errors.isEmpty();
  }
}
```

---

## VI. USAGE EXAMPLE (PSEUDO CODE)

```java
// Ví dụ sử dụng
public static void main(String[] args) {
  // 1. Tạo HealthProfile
  HealthProfile profile = new HealthProfile();
  profile.gender = "FEMALE";
  profile.age = 35;
  profile.weightKg = 65;
  profile.heightCm = 165;
  profile.goal = "LOSE_WEIGHT";
  profile.targetWeightKg = 58;
  profile.exerciseDaily = true;
  profile.exerciseType = "CARDIO";
  profile.exerciseMinutes = 30;
  profile.waterLitersPerDay = 2.0;
  profile.mealFrequency = "FIVE_MEALS";
  profile.medicalConditions = Arrays.asList("HYPERTENSION");
  profile.foodAllergies = new ArrayList<>();
  profile.preferredFoods = Arrays.asList("gà, cá, tôm, đậu phụ");
  
  // 2. Validate
  HealthProfileValidator validator = new HealthProfileValidator();
  ValidationResult validation = validator.validate(profile);
  if (!validation.isValid()) {
    System.out.println("Errors: " + validation.errors);
    return;
  }
  
  // 3. Tính Calo & gợi ý bữa ăn
  AnCareMealRecommendationService service = new AnCareMealRecommendationService();
  RecommendationResponse response = service.generateRecommendation(profile);
  
  // 4. In kết quả
  System.out.println("=== CALO KỲ DIỆU ===");
  System.out.println("RMR: " + response.calorieCalculation.rmr);
  System.out.println("TMR: " + response.calorieCalculation.tmr);
  System.out.println("Mục tiêu calo/ngày: " + response.calorieCalculation.dailyCalorieTarget);
  System.out.println("Dự kiến giảm: " + response.calorieCalculation.estimatedWeeklyWeightChange + " kg/tuần");
  System.out.println();
  
  System.out.println("=== GỢI Ý BỮA ĂN ===");
  for (Meal meal : response.mealRecommendation.meals) {
    System.out.println(meal.mealTime + " - " + meal.mealName + ": " + meal.targetCalories + " kcal");
    for (MealItem item : meal.items) {
      System.out.println("  • " + item.name + " (" + item.calories + " kcal)");
    }
  }
  
  System.out.println();
  System.out.println("=== KHUYẾN CÁO ===");
  for (String rec : response.mealRecommendation.dietaryRecommendations) {
    System.out.println(rec);
  }
  
  System.out.println();
  System.out.println("=== CHÚ Ý BỆNH LÝ ===");
  for (String restriction : response.mealRecommendation.medicalRestrictions) {
    System.out.println(restriction);
  }
}
```

---

## VII. DATABASE SCHEMA (Optional)

Nếu cần lưu dữ liệu:

```sql
-- Health Profiles
CREATE TABLE health_profiles (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  gender VARCHAR(10),
  age INT,
  weight_kg DECIMAL(5,2),
  height_cm DECIMAL(5,2),
  rmr DECIMAL(7,2),
  amr DECIMAL(7,2),
  goal VARCHAR(50), -- LOSE_WEIGHT, GAIN_WEIGHT, MAINTAIN, REJUVENATE
  target_weight_kg DECIMAL(5,2),
  exercise_daily BOOLEAN,
  exercise_type VARCHAR(50),
  water_liters_per_day DECIMAL(3,1),
  medical_conditions TEXT[], -- ARRAY of conditions
  food_allergies TEXT[],
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Calorie Calculations (Log)
CREATE TABLE calorie_calculations (
  id UUID PRIMARY KEY,
  profile_id UUID REFERENCES health_profiles(id),
  calculated_rmr DECIMAL(7,2),
  calculated_amr DECIMAL(7,2),
  calculated_tmr DECIMAL(7,2),
  magic_calories DECIMAL(7,2),
  goal_strategy VARCHAR(100),
  weekly_deficit_surplus DECIMAL(7,2),
  estimated_weight_change_per_week DECIMAL(4,2),
  created_at TIMESTAMP
);

-- Meal Recommendations (Log)
CREATE TABLE meal_recommendations (
  id UUID PRIMARY KEY,
  calculation_id UUID REFERENCES calorie_calculations(id),
  total_daily_calories DECIMAL(7,2),
  meal_plan_type VARCHAR(50), -- FOUR_MEALS, FIVE_MEALS
  total_protein_g DECIMAL(5,1),
  total_carbs_g DECIMAL(5,1),
  total_fat_g DECIMAL(5,1),
  created_at TIMESTAMP
);

-- Meals
CREATE TABLE meals (
  id UUID PRIMARY KEY,
  recommendation_id UUID REFERENCES meal_recommendations(id),
  meal_name VARCHAR(100),
  meal_time TIME,
  target_calories DECIMAL(5,1),
  sequence_order INT
);

-- Meal Items
CREATE TABLE meal_items (
  id UUID PRIMARY KEY,
  meal_id UUID REFERENCES meals(id),
  item_name VARCHAR(200),
  category VARCHAR(50), -- PROTEIN, CARBS, FRUIT, VEGETABLE
  calories DECIMAL(5,1),
  protein_g DECIMAL(4,1),
  carbs_g DECIMAL(4,1),
  fat_g DECIMAL(4,1)
);
```

---

## VIII. SUMMARY

**Quy trình chính:**

1. **Input:** `HealthProfile` (sức khỏe, thói quen, bệnh lý, nhu cầu)
2. **Processing:** 
   - Tính RMR/BMR → AMR → Ex → TMR
   - Điều chỉnh theo mục tiêu (gain/lose/maintain/rejuvenate)
   - Áp dụng ràng buộc bệnh lý & dị ứng
   - Xây dựng meal plan từ template 1200 kcal
3. **Output:** `CalorieCalculation` + `MealRecommendation` + Khuyến cáo

**Ưu điểm:**
- ✓ Modular: Dễ test & maintain từng phần
- ✓ Flexible: Hỗ trợ nhiều bệnh lý, dị ứng, mục tiêu
- ✓ Traceable: Log tất cả tính toán, quyết định
- ✓ Scalable: Có thể mở rộng thêm rule mới

**Tiếp theo:**
- Integrate vào API backend (Spring Boot, Node.js, etc.)
- Lập trình UI (React, Vue) để nhập HealthProfile
- Thêm AI/ML để optimize meal recommendations
- Notification system khi cần điều chỉnh

---
