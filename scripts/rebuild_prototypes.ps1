$FLOW = @(
  [PSCustomObject]@{ role = 'coach'; name = 'AUTH-01_dang_nhap'; title = 'Đăng nhập' },
  [PSCustomObject]@{ role = 'coach'; name = 'AUTH-02_shell'; title = 'Trang chủ HLV' },
  [PSCustomObject]@{ role = 'coach'; name = 'LEAD-01_danh_sach'; title = 'DS KH' },
  [PSCustomObject]@{ role = 'coach'; name = 'LEAD-02_tao_lead'; title = 'Thêm mới KH' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-02_chan_dung_kh'; title = 'Chân dung KH' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-03_tanita'; title = 'Khảo sát Tanita' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-04_phan_tich'; title = 'Phân tích kết quả' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-05_giai_phap'; title = 'Xem lộ trình' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-08_tao_tk'; title = 'Tạo tài khoản' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-07_bua_an'; title = 'Xây dựng bữa ăn' },
  [PSCustomObject]@{ role = 'coach'; name = 'CARE-01_talking_point'; title = 'Talking point' },
  [PSCustomObject]@{ role = 'coach'; name = 'CARE-03_dieu_chinh_bua_an'; title = 'Điều chỉnh bữa ăn' },
  [PSCustomObject]@{ role = 'coach'; name = 'CARE-09_nhac_72h'; title = 'Nhắc 72h' },
  [PSCustomObject]@{ role = 'coach'; name = 'DEV-01_microcourse'; title = 'Micro-course' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-09_ket_qua_kh'; title = 'Kết quả của Hạnh' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-10_bao_cao_kh'; title = 'Báo cáo kết quả' },
  [PSCustomObject]@{ role = 'coach'; name = 'CONS-11_infographic'; title = 'Tạo Infographic' },
  [PSCustomObject]@{ role = 'customer'; name = 'HLTH-02_trang_chu'; title = 'Trang chủ KH' },
  [PSCustomObject]@{ role = 'customer'; name = 'HLTH-06_check_in'; title = 'Check-in KH' },
  [PSCustomObject]@{ role = 'customer'; name = 'HLTH-04_bua_an'; title = 'Ghi nhận bữa ăn' },
  [PSCustomObject]@{ role = 'customer'; name = 'DEV-02_dao_tao'; title = 'Đào tạo KH' }
)

# Paths relative to the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (!$scriptDir) { $scriptDir = "." }
$rootDir = (Get-Item (Join-Path $scriptDir "..")).FullName
$mockupsSrcDir = Join-Path $rootDir "docs/03-mockups"
$protoDir = Join-Path $rootDir "docs/04-prototypes"
$protoMockupsDir = Join-Path $protoDir "03-mockups"

# Rebuild directories
New-Item -ItemType Directory -Force -Path (Join-Path $protoDir "_assets") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $protoDir "coach") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $protoDir "customer") | Out-Null

# Copy 03-mockups to 04-prototypes/03-mockups
if (Test-Path $protoMockupsDir) {
    Remove-Item -Recurse -Force $protoMockupsDir | Out-Null
}

New-Item -ItemType Directory -Force -Path $protoMockupsDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $protoMockupsDir "_assets") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $protoMockupsDir "coach") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $protoMockupsDir "customer") | Out-Null

# Copy files
Copy-Item -Path (Join-Path $mockupsSrcDir "_assets/*") -Destination (Join-Path $protoMockupsDir "_assets") -Force
Copy-Item -Path (Join-Path $mockupsSrcDir "coach/*.html") -Destination (Join-Path $protoMockupsDir "coach") -Force
Copy-Item -Path (Join-Path $mockupsSrcDir "customer/*.html") -Destination (Join-Path $protoMockupsDir "customer") -Force

Write-Output "Copied 03-mockups files to 04-prototypes/03-mockups"

# Generate _proto-nav.css
$cssContent = @"
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');
.proto-nav{position:fixed;top:0;left:0;right:0;height:44px;background:#1f2933;color:#fff;display:flex;align-items:center;gap:8px;padding:0 16px;z-index:1000;font-size:12px;font-family:'Be Vietnam Pro',sans-serif;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.proto-nav .ttl{flex:1;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#f8fafc}
.proto-nav a{color:#9bb0c0;text-decoration:none;padding:6px 12px;border-radius:6px;font-size:12px;font-weight:500;transition:background .15s}
.proto-nav a:hover{background:#334155;color:#fff}
.proto-frame{margin-top:44px;border:none;width:100%;height:calc(100vh - 44px);display:block;background:#f8fafc}
"@
[System.IO.File]::WriteAllText((Join-Path $protoDir "_assets/_proto-nav.css"), $cssContent, [System.Text.Encoding]::UTF8)

# Generate HTML wrappers
for ($i = 0; $i -lt $FLOW.Count; $i++) {
    $item = $FLOW[$i]
    $role = $item.role
    $name = $item.name
    $title = $item.title
    
    $prev = $null
    if ($i -gt 0) { $prev = $FLOW[$i - 1] }
    
    $nxt = $null
    if ($i -lt ($FLOW.Count - 1)) { $nxt = $FLOW[$i + 1] }
    
    $prev_link = if ($prev) { "../$($prev.role)/$($prev.name).html" } else { "#" }
    $prev_txt = if ($prev) { "‹ $($prev.title)" } else { "" }
    $next_link = if ($nxt) { "../$($nxt.role)/$($nxt.name).html" } else { "#" }
    $next_txt = if ($nxt) { "$($nxt.title) ›" } else { "" }
    
    $htmlContent = @"
<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>$title — AnCare Prototype</title>
<link rel="stylesheet" href="../_assets/_proto-nav.css">
</head><body>
<div class="proto-nav">
  <a href="../index.html">☰ Menu</a>
  <span class="ttl">$title · $($i + 1)/$($FLOW.Count)</span>
  <a href="$prev_link">$prev_txt</a>
  <a href="$next_link">$next_txt</a>
</div>
<iframe class="proto-frame" src="../03-mockups/$role/S-$name.html"></iframe>
</body></html>
"@
    $targetPath = Join-Path $protoDir "$role/$name.html"
    [System.IO.File]::WriteAllText($targetPath, $htmlContent, [System.Text.Encoding]::UTF8)
}

# Generate index.html
$indexHeader = @"
<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AnCare Prototype — Sitemap</title>
<link rel="stylesheet" href="_assets/_proto-nav.css">
<style>
body{font-family:'Be Vietnam Pro',Inter,sans-serif;background:#f8fafc;color:#1e293b;margin:0;padding:24px}
.wrap{max-width:960px;margin:0 auto}
h1{font-size:24px;margin:0 0 4px;font-weight:700} .sub{color:#64748b;margin-bottom:24px}
.flow{background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:20px;margin-bottom:16px;box-shadow:0 1px 3px rgba(0,0,0,.04)}
.flow h2{font-size:16px;margin:0 0 14px;display:flex;align-items:center;gap:8px;font-weight:700}
.flow h2 .badge{font-size:11px;background:#e3efe8;color:#166534;padding:3px 10px;border-radius:99px;font-weight:600}
.flow.kh h2 .badge{background:#e6f7f5;color:#0f766e}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}
.card{display:block;text-decoration:none;color:#1e293b;background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:14px;transition:.15s}
.card:hover{border-color:#16a34a;background:#f0fdf4;transform:translateY(-1px)}
.card.kh:hover{border-color:#14b8a6;background:#f0fdfa}
.card .id{font-size:11px;color:#64748b;font-weight:600}
.card .nm{font-size:14px;font-weight:600;margin-top:3px}
.card .tpl{font-size:10px;color:#94a3b8;margin-top:5px}
.note{font-size:13px;color:#64748b;background:#fff;border:1px dashed #cbd5e1;border-radius:10px;padding:14px;margin-top:18px;line-height:1.6}
</style></head><body><div class="wrap">
<h1>AnCare — Prototype Sitemap</h1>
<div class="sub">Click từng màn để xem wireframe (iframe + nav prototype). Đã rebuild theo design system mới.</div>

<div class="flow">
  <h2>🟢 Luồng Tư vấn 15 phút (HLV) <span class="badge">10 màn</span></h2>
  <div class="grid">
"@

$indexBody1 = ""
for ($idx = 0; $idx -lt 10; $idx++) {
    $item = $FLOW[$idx]
    $indexBody1 += "    <a class=`"card`" href=`"coach/$($item.name).html`"><div class=`"id`">$($idx + 1)/$($FLOW.Count)</div><div class=`"nm`">$($item.title)</div><div class=`"tpl`">T1</div></a>`n"
}

$indexHeader2 = @"
  </div>
</div>

<div class="flow">
  <h2>📋 Chăm sóc KH (HLV) <span class="badge">7 màn</span></h2>
  <div class="grid">
"@

$indexBody2 = ""
for ($idx = 10; $idx -lt 17; $idx++) {
    $item = $FLOW[$idx]
    $indexBody2 += "    <a class=`"card`" href=`"coach/$($item.name).html`"><div class=`"id`">$($item.title)</div><div class=`"nm`">$($item.title)</div></a>`n"
}

$indexHeader3 = @"
  </div>
</div>

<div class="flow">
  <h2>🎓 Đào tạo (HLV) <span class="badge">1 màn</span></h2>
  <div class="grid">
    <a class="card" href="coach/DEV-01_microcourse.html"><div class="id">Micro-course</div><div class="nm">Micro-course</div></a>
  </div>
</div>

<div class="flow kh">
  <h2>🌿 Trải nghiệm Khách hàng (KH) <span class="badge">4 màn</span></h2>
  <div class="grid">
"@

$indexBody3 = ""
for ($idx = 17; $idx -lt $FLOW.Count; $idx++) {
    $item = $FLOW[$idx]
    $indexBody3 += "    <a class=`"card kh`" href=`"$($item.role)/$($item.name).html`"><div class=`"id`">$($item.title)</div><div class=`"nm`">$($item.title)</div></a>`n"
}

$indexFooter = @"
  </div>
</div>

<div class="note">
  <strong>Cách xem:</strong> mở file này trong browser → click từng màn. Mỗi prototype mở mockup trong iframe + nav prototype (‹ › Menu).<br>
  <strong>Luồng đầy đủ HLV:</strong> Đăng nhập → Trang chủ → DS KH → Thêm mới KH → Chân dung → Tanita → Phân tích → Xem lộ trình → Tạo TK → Bữa ăn.<br>
  <strong>Tổng:</strong> 21 mockup + 21 prototype. Wireframe đã rebuild theo design system mới (không emoji, SVG Tabler, semantic tokens, 8dp spacing).
</div>
</div></body></html>
"@

$indexFull = $indexHeader + $indexBody1 + $indexHeader2 + $indexBody2 + $indexHeader3 + $indexBody3 + $indexFooter
[System.IO.File]::WriteAllText((Join-Path $protoDir "index.html"), $indexFull, [System.Text.Encoding]::UTF8)

Write-Output "Prototypes generated: $($FLOW.Count) wrappers + index.html"
