# Product Knowledge Index

Use this file to route product-related questions to the correct profile in `knowledge_base/products/`.

## Retrieval Strategy

1. Match exact product name, alias, or English name first.
2. If multiple products match, prioritize the product whose `goals` align most closely with the user intent.
3. If the question includes disease, medication, pregnancy, breastfeeding, child use, allergy, or chronic conditions, prefer products whose profile has strong `Không phù hợp / cần thận trọng` or `Khi nào cần tham khảo bác sĩ`.
4. Load only 1-2 product files first; expand to nutrition or SOP files only if needed.
5. Treat files marked as source-gap as alias routers only, not factual product references.

## Fitness Routing Map

Use the same intent labels as `../nutrition/fitness_talking_points.md`:

- `nen tang dinh duong cho nguoi van dong`
  - Primary file: `hon-hop-dinh-duong-the-thao-cong-thuc-1.md`
  - Support file: `../nutrition/fitness_talking_points.md`
- `phuc hoi sau tap / tang protein sau tap`
  - Primary file: `herbalife-24-rebuild-strength-huong-so-co-la.md`
  - Support file: `../nutrition/fitness_talking_points.md`
- `bu nuoc / dien giai quanh tap`
  - Primary file: `herbalife-24-hydrate-huong-cam.md`
  - Support file: `../nutrition/fitness_talking_points.md`
- `tinh tao`
  - Primary files: `tra-n-r-g.md`, `tra-thao-moc-co-dac.md`
  - Disambiguation: use `tra-n-r-g.md` when the ask is directly about alertness; use `tra-thao-moc-co-dac.md` when the ask mixes alertness with the broader Herbalife tea routine
- `shake cho bua tien loi / kiem soat can nang`
  - Primary files: `formula_1.md`, `bot-protein.md`
  - Support file: `../nutrition/fitness_talking_points.md`

If the user starts from a coaching question rather than a product question, open `../nutrition/fitness_talking_points.md` first, then route into the product files above.

## Source Coverage

The product files below are split into two groups:

- `Source-backed`: detailed content verified against `docs/raw/herbalife_ocr_markdown_theo_tung_trang_v2.md`
- `Source-gap`: file exists for routing, but the current raw document does not contain enough information to support detailed claims

## Source-Backed Products

### Formula 1

- File: `formula_1.md`
- Aliases: `formula 1`, `f1`, `hỗn hợp dinh dưỡng công thức 1`, `shake herbalife`
- Main goals: `shake cho bua tien loi / kiem soat can nang`, `giảm cân`, `duy trì cân nặng`, `tăng cân`, `thay thế bữa ăn`
- Safety signals: `chỉ nêu cho người trưởng thành`, `nên hỏi bác sĩ trước khi bắt đầu chương trình giảm cân`, `có đậu nành và sữa`
- Related files: `../nutrition/tdee_macro_guide.md`, `../sop/SOP_TU_VAN_15_PHUT_V2_HERBALIFE.md`

### Bột Protein

- File: `bot-protein.md`
- Aliases: `bột protein`, `personalized protein powder`, `ppp`, `formula 3`
- Main goals: `shake cho bua tien loi / kiem soat can nang`, `phuc hoi sau tap / tang protein sau tap`, `bổ sung chất đạm`, `hỗ trợ duy trì khối cơ`
- Safety signals: `có đậu nành`, `có whey`, `người cần hạn chế đạm nên hỏi chuyên gia`
- Related files: `../nutrition/tdee_macro_guide.md`, `../nutrition/fitness_talking_points.md`

### Formula 2

- File: `hon-hop-vitamin-cong-thuc-2.md`
- Aliases: `formula 2`, `hỗn hợp vitamin công thức 2`, `multivitamin complex`
- Main goals: `bổ sung vitamin và khoáng chất`, `hỗ trợ tăng cường sức khỏe`, `hỗ trợ tăng cường sức đề kháng`
- Safety signals: `có đậu nành và lúa mì`, `có chứa sắt`, `để xa tầm tay trẻ em`

### Cell Activator

- File: `cell-activator.md`
- Aliases: `cell activator`
- Main goals: `hỗ trợ bảo vệ tế bào khỏi tổn thương do quá trình oxy hóa`
- Safety signals: `không dùng cho phụ nữ có thai/cho con bú`, `không dùng cho người có vấn đề thận mạn`, `không dùng cho người tiểu đường lệ thuộc insulin`

### Trà Thảo Mộc Cô Đặc

- File: `tra-thao-moc-co-dac.md`
- Aliases: `herbal tea concentrate`, `tea mix`, `instant herbal beverage`, `hương truyền thống`, `hương chanh tự nhiên`
- Main goals: `tinh tao`, `tăng cường sự tỉnh táo`, `hỗ trợ tăng cường tác dụng chống oxy hóa`
- Safety signals: `có caffeine`, `trẻ em và phụ nữ mang thai/cho con bú cần hỏi bác sĩ`

### Cell-U-Loss

- File: `cell-u-loss.md`
- Aliases: `cell-u-loss`, `cell u loss`
- Main goals: `hỗ trợ thanh nhiệt giải độc`
- Safety signals: `có đậu nành`, `không dùng nếu mẫn cảm với thành phần`

### Herbalifeline

- File: `herbalifeline.md`
- Aliases: `herbalifeline`
- Main goals: `hỗ trợ duy trì huyết áp ổn định`, `hỗ trợ sức khỏe hệ tim mạch`, `bổ sung omega-3`
- Safety signals: `có thành phần từ cá và đậu nành`, `người dùng thuốc tim mạch/chống đông nên hỏi bác sĩ`

### Niteworks

- File: `niteworks.md`
- Aliases: `niteworks`
- Main goals: `hỗ trợ duy trì huyết áp ổn định`, `hỗ trợ sức khỏe hệ tim mạch`
- Safety signals: `tài liệu hiện có chưa nêu liều dùng`, `người có bệnh tim mạch/huyết áp nên hỏi bác sĩ`

### Lô Hội Thảo Mộc Cô Đặc

- File: `lo-hoi-thao-moc-co-dac.md`
- Aliases: `aloe concentrate`, `herbal aloe concentrate`, `lô hội cô đặc`
- Main goals: `sản phẩm thảo mộc dùng pha loãng`, `hỗ trợ thói quen uống nước`
- Safety signals: `phải pha loãng`, `bảo quản lạnh sau khi mở`, `không dùng nếu mẫn cảm với thành phần`

### Hỗn Hợp Chất Xơ Hoạt Hóa

- File: `hon-hop-chat-xo-hoat-hoa-huong-tao.md`
- Aliases: `active fiber complex`, `hỗn hợp chất xơ`, `hương táo`
- Main goals: `bổ sung chất xơ`, `hỗ trợ giảm táo bón`, `tốt cho đường ruột`
- Safety signals: `có đậu nành`, `người cần hạn chế chất xơ nên hỏi bác sĩ`

### Xtra-Cal Advanced

- File: `xtra-cal-advanced.md`
- Aliases: `xtra-cal advanced`, `xtra-cal`, `canxi herbalife`
- Main goals: `hỗ trợ xương chắc khỏe`, `hỗ trợ giảm nguy cơ loãng xương ở người lớn`
- Safety signals: `người có bệnh thận/sỏi thận/rối loạn calci nên hỏi bác sĩ`

### Joint Support Advanced

- File: `joint-support-advanced.md`
- Aliases: `joint support advanced`, `joint support`
- Main goals: `hỗ trợ tăng cường sức khỏe khớp`, `hỗ trợ cho khớp khỏe mạnh`
- Safety signals: `không khuyên dùng cho trẻ em`, `không khuyên dùng cho phụ nữ có thai/cho con bú`, `có cua, tôm và đậu nành`

### Herbalife 24 Rebuild Strength

- File: `herbalife-24-rebuild-strength-huong-so-co-la.md`
- Aliases: `rebuild strength`, `h24 rebuild strength`
- Main goals: `phuc hoi sau tap / tang protein sau tap`, `hỗ trợ phát triển cơ bắp sau tập luyện`, `bổ sung protein, vitamin và khoáng chất`
- Safety signals: `có đậu nành và sữa`, `phù hợp nhất cho sau tập luyện`
- Related files: `../nutrition/fitness_talking_points.md`

### Formula 1 Sport

- File: `hon-hop-dinh-duong-the-thao-cong-thuc-1.md`
- Aliases: `formula 1 sport`, `f1 sport`, `hương vani nguyên kem`
- Main goals: `nen tang dinh duong cho nguoi van dong`, `cung cấp nền tảng dinh dưỡng cho người vận động`, `hỗ trợ khối cơ`, `hỗ trợ miễn dịch`
- Safety signals: `có đậu nành và sữa`, `nên hỏi bác sĩ trước khi bắt đầu chương trình kiểm soát cân nặng`
- Related files: `../nutrition/fitness_talking_points.md`

### Herbalife 24 Hydrate

- File: `herbalife-24-hydrate-huong-cam.md`
- Aliases: `hydrate`, `h24 hydrate`, `hương cam`
- Main goals: `bu nuoc / dien giai quanh tap`, `bổ sung chất điện giải`, `hỗ trợ bù nước cho cơ thể`
- Safety signals: `người cần kiểm soát natri/kali nên hỏi bác sĩ`
- Related files: `../nutrition/fitness_talking_points.md`

### Trà N-R-G

- File: `tra-n-r-g.md`
- Aliases: `n-r-g tea`, `trà nrg`, `trà n-r-g`
- Main goals: `tinh tao`, `hỗ trợ tăng cường sự tỉnh táo`
- Safety signals: `có caffeine`, `trẻ em và phụ nữ mang thai/cho con bú cần hỏi bác sĩ`

### Ocular Defense

- File: `ocular-defense.md`
- Aliases: `ocular defense`
- Main goals: `hỗ trợ tăng cường thị lực`
- Safety signals: `không thay thế khám mắt hoặc điều trị chuyên khoa`

### ImmuLift

- File: `immulift.md`
- Aliases: `immulift`
- Main goals: `hỗ trợ tăng cường sức đề kháng`, `hỗ trợ chống oxy hóa`
- Safety signals: `cần để ý chồng liều vi chất nếu đang dùng supplement khác`

### Beauty Powder Drink

- File: `thuc-uong-dang-bot-beauty-powder-drink-huong-cam.md`
- Aliases: `beauty powder drink`, `hương cam`
- Main goals: `hỗ trợ sức khỏe tóc, móng, làn da`, `hỗ trợ phục hồi làn da`, `hỗ trợ chống lại dấu hiệu lão hóa`
- Safety signals: `có thành phần từ cá`, `tài liệu hiện có chưa nêu liều dùng`

## Source-Gap Products

### Prolessa Duo

- File: `prolessa-duo.md`
- Aliases: `prolessa duo`
- Status: `source-gap`
- Rule: chỉ dùng để match tên sản phẩm; không dùng để sinh claim, thành phần hoặc cách dùng

### Simply Probiotic

- File: `simply-probiotic.md`
- Aliases: `simply probiotic`
- Status: `source-gap`
- Rule: chỉ dùng để match tên sản phẩm; không dùng để sinh claim, thành phần hoặc cách dùng

### Trà Tâm An

- File: `tra-tam-an.md`
- Aliases: `relaxation tea`, `trà tâm an`, `trà thư giãn`
- Status: `source-gap`
- Rule: chỉ dùng để match tên sản phẩm; không dùng để sinh claim, thành phần hoặc cách dùng
