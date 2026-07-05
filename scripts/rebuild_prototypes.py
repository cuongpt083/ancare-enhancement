import os
import shutil

FLOW = [
  ('coach', 'AUTH-01_dang_nhap', 'Đăng nhập'),
  ('coach', 'AUTH-02_shell', 'Trang chủ HLV'),
  ('coach', 'LEAD-01_danh_sach', 'DS KH'),
  ('coach', 'LEAD-02_tao_lead', 'Thêm mới KH'),
  ('coach', 'CONS-02_chan_dung_kh', 'Chân dung KH'),
  ('coach', 'CONS-03_tanita', 'Khảo sát Tanita'),
  ('coach', 'CONS-04_phan_tich', 'Phân tích kết quả'),
  ('coach', 'CONS-05_giai_phap', 'Xem lộ trình'),
  ('coach', 'CONS-08_tao_tk', 'Tạo tài khoản'),
  ('coach', 'CONS-07_bua_an', 'Xây dựng bữa ăn'),
  ('coach', 'CARE-01_talking_point', 'Talking point'),
  ('coach', 'CARE-03_dieu_chinh_bua_an', 'Điều chỉnh bữa ăn'),
  ('coach', 'CARE-09_nhac_72h', 'Nhắc 72h'),
  ('coach', 'DEV-01_microcourse', 'Micro-course'),
  ('coach', 'CONS-09_ket_qua_kh', 'Kết quả của Hạnh'),
  ('coach', 'CONS-10_bao_cao_kh', 'Báo cáo kết quả'),
  ('coach', 'CONS-11_infographic', 'Tạo Infographic'),
  ('customer', 'HLTH-02_trang_chu', 'Trang chủ KH'),
  ('customer', 'HLTH-06_check_in', 'Check-in KH'),
  ('customer', 'HLTH-04_bua_an', 'Ghi nhận bữa ăn'),
  ('customer', 'DEV-02_dao_tao', 'Đào tạo KH'),
]

# Paths relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
mockups_src_dir = os.path.join(root_dir, 'docs', '03-mockups')
proto_dir = os.path.join(root_dir, 'docs', '04-prototypes')

# Target mockups directory inside prototypes to make it self-contained
proto_mockups_dir = os.path.join(proto_dir, '03-mockups')

# Rebuild directories
os.makedirs(os.path.join(proto_dir, '_assets'), exist_ok=True)
os.makedirs(os.path.join(proto_dir, 'coach'), exist_ok=True)
os.makedirs(os.path.join(proto_dir, 'customer'), exist_ok=True)

# Copy 03-mockups content to 04-prototypes/03-mockups to bundle them together
if os.path.exists(proto_mockups_dir):
    shutil.rmtree(proto_mockups_dir)

os.makedirs(proto_mockups_dir, exist_ok=True)
os.makedirs(os.path.join(proto_mockups_dir, '_assets'), exist_ok=True)
os.makedirs(os.path.join(proto_mockups_dir, 'coach'), exist_ok=True)
os.makedirs(os.path.join(proto_mockups_dir, 'customer'), exist_ok=True)

# Copy assets
for f in os.listdir(os.path.join(mockups_src_dir, '_assets')):
    src_f = os.path.join(mockups_src_dir, '_assets', f)
    if os.path.isfile(src_f):
        shutil.copy2(src_f, os.path.join(proto_mockups_dir, '_assets', f))

# Copy coach mockups
for f in os.listdir(os.path.join(mockups_src_dir, 'coach')):
    if f.endswith('.html'):
        shutil.copy2(os.path.join(mockups_src_dir, 'coach', f), os.path.join(proto_mockups_dir, 'coach', f))

# Copy customer mockups
for f in os.listdir(os.path.join(mockups_src_dir, 'customer')):
    if f.endswith('.html'):
        shutil.copy2(os.path.join(mockups_src_dir, 'customer', f), os.path.join(proto_mockups_dir, 'customer', f))

print("Copied 03-mockups files to 04-prototypes/03-mockups for standalone deployment.")

# Generate _proto-nav.css
with open(os.path.join(proto_dir, '_assets', '_proto-nav.css'), 'w', encoding='utf-8') as f:
    f.write('''@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');
.proto-nav{position:fixed;top:0;left:0;right:0;height:44px;background:#1f2933;color:#fff;display:flex;align-items:center;gap:8px;padding:0 16px;z-index:1000;font-size:12px;font-family:'Be Vietnam Pro',sans-serif;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.proto-nav .ttl{flex:1;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#f8fafc}
.proto-nav a{color:#9bb0c0;text-decoration:none;padding:6px 12px;border-radius:6px;font-size:12px;font-weight:500;transition:background .15s}
.proto-nav a:hover{background:#334155;color:#fff}
.proto-frame{margin-top:44px;border:none;width:100%;height:calc(100vh - 44px);display:block;background:#f8fafc}
''')

# Generate wrapper HTMLs
for i, (role, name, title) in enumerate(FLOW):
    prev = FLOW[i-1] if i > 0 else None
    nxt = FLOW[i+1] if i < len(FLOW)-1 else None
    prev_link = f'../{prev[0]}/{prev[1]}.html' if prev else '#'
    prev_txt = f'‹ {prev[2]}' if prev else ''
    next_link = f'../{nxt[0]}/{nxt[1]}.html' if nxt else '#'
    next_txt = f'{nxt[2]} ›' if nxt else ''
    
    html = f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — AnCare Prototype</title>
<link rel="stylesheet" href="../_assets/_proto-nav.css">
</head><body>
<div class="proto-nav">
  <a href="../index.html">☰ Menu</a>
  <span class="ttl">{title} · {i+1}/{len(FLOW)}</span>
  <a href="{prev_link}">{prev_txt}</a>
  <a href="{next_link}">{next_txt}</a>
</div>
<iframe class="proto-frame" src="../03-mockups/{role}/S-{name}.html"></iframe>
</body></html>
'''
    with open(os.path.join(proto_dir, role, f'{name}.html'), 'w', encoding='utf-8') as f:
        f.write(html)

# Generate index.html
index = '''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
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
'''
for idx, (role, name, title) in enumerate(FLOW[:10]):
    index += f'    <a class="card" href="coach/{name}.html"><div class="id">{idx+1}/{len(FLOW)}</div><div class="nm">{title}</div><div class="tpl">T1</div></a>\n'
index += '''  </div>
</div>

<div class="flow">
  <h2>📋 Chăm sóc KH (HLV) <span class="badge">7 màn</span></h2>
  <div class="grid">
'''
for role, name, title in FLOW[10:17]:
    index += f'    <a class="card" href="coach/{name}.html"><div class="id">{title}</div><div class="nm">{title}</div></a>\n'
index += '''  </div>
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
'''
for role, name, title in FLOW[17:]:
    index += f'    <a class="card kh" href="{role}/{name}.html"><div class="id">{title}</div><div class="nm">{title}</div></a>\n'
index += '''  </div>
</div>

<div class="note">
  <strong>Cách xem:</strong> mở file này trong browser → click từng màn. Mỗi prototype mở mockup trong iframe + nav prototype (‹ › Menu).<br>
  <strong>Luồng đầy đủ HLV:</strong> Đăng nhập → Trang chủ → DS KH → Thêm mới KH → Chân dung → Tanita → Phân tích → Xem lộ trình → Tạo TK → Bữa ăn.<br>
  <strong>Tổng:</strong> 21 mockup + 21 prototype. Wireframe đã rebuild theo design system mới (không emoji, SVG Tabler, semantic tokens, 8dp spacing).
</div>
</div></body></html>
'''

with open(os.path.join(proto_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index)

print(f'Prototypes generated: {len(FLOW)} wrappers + index.html')
