import os

ICONS = {
    'chevron-left': '<path d="M15 6l-6 6 6 6"/>', 'chevron-right': '<path d="M9 6l6 6-6 6"/>',
    'info': '<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="8.01"/><line x1="12" y1="12" x2="12" y2="16"/>',
    'bell': '<path d="M10 5a2 2 0 0 1 4 0 7 7 0 0 1 4 6v3a4 4 0 0 0 1 2H5a4 4 0 0 0 1-2v-3a7 7 0 0 1 4-6M9 17v1a3 3 0 0 0 6 0v-1"/>',
    'home': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'chart': '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    'user': '<path d="M12 12a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM5 20a7 7 0 0 1 14 0"/>',
    'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'check': '<polyline points="20 6 9 17 4 12"/>',
    'camera': '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    'water': '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
    'moon': '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
    'run': '<path d="M4 15l3-3 2 2 2.5-3L14 12l2-2 3 4-3 2-1-1-2 3-4-2z"/><circle cx="17" cy="4" r="2"/>',
    'utensils': '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>',
    'scale': '<path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L2.5 7.5"/>',
    'trending-up': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    'trending-down': '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
    'alert': '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'sun': '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>', 'minus': '<path d="M5 12h14"/>',
    'search': '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>',
    'send': '<path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/>',
    'share': '<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/>',
    'image': '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>',
    'heart': '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    'clipboard': '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    'award': '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
}

def icon(name, size='md'):
    if name not in ICONS: return '<svg viewBox="0 0 24 24" class="icon"/>'
    cls = {'sm': 'icon-sm', 'md': 'icon', 'lg': 'icon-lg'}.get(size, 'icon')
    return f'<svg class="{cls}" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def appbar(title, back=False, info=False):
    b = f'<span class="back">{icon("chevron-left")}</span>' if back else '<span class="back" style="opacity:0">' + icon('chevron-left') + '</span>'
    i = f'<span class="info">{icon("info")}</span>' if info else '<span class="info" style="opacity:0">' + icon('info') + '</span>'
    return f'<div class="appbar">{b}<h1>{title}</h1>{i}</div>'

def bottom_nav(active, items):
    out = '<div class="bottom-nav">'
    for name, label, iname in items:
        cls = 'nav-item active' if active == name else 'nav-item'
        out += f'<div class="{cls}"><span class="icon">{icon(iname)}</span><span>{label}</span></div>'
    return out + '</div>'

def cta(primary, secondary=None, icon_name=None):
    s = f'<button class="btn secondary">{secondary}</button>' if secondary else ''
    ic = icon(icon_name) if icon_name else ''
    return f'<div class="cta-bar">{s}<button class="btn primary customer">{ic}{primary}</button></div>'

def html(title, body, has_nav=False, nav_active=None, nav_items=None, cta_html=None, extra_head=''):
    default_nav = [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')]
    nav = bottom_nav(nav_active, nav_items or default_nav) if has_nav else ''
    cta = cta_html or ''
    return f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../_assets/_tokens.css"><link rel="stylesheet" href="../_assets/_base.css">
<style>:root{{--accent:var(--accent-customer);--accent-hover:var(--accent-customer-hover);}}</style>
{extra_head}
</head><body><div class="screen">{body}{nav}{cta}</div></body></html>'''

out_dir = '/Users/cuongpt/Workspaces/ancare-enhancement/docs/03-mockups/customer'
os.makedirs(out_dir, exist_ok=True)

# 1. Clock
body = f'''
{appbar('Sức khỏe tổng thể', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card customer" style="margin-bottom:var(--s-16)">
    <div class="label">Thứ Tư, 2/7</div>
    <div class="title" style="font-size:var(--text-xl)">Hôm nay bạn đang làm tốt!</div>
  </div>
  <div class="card" style="display:flex;align-items:center;justify-content:center;position:relative;height:260px">
    <svg viewBox="0 0 200 200" width="200" height="200">
      <circle cx="100" cy="100" r="90" fill="none" stroke="var(--border)" stroke-width="12"/>
      <circle cx="100" cy="100" r="90" fill="none" stroke="var(--accent-customer)" stroke-width="12" stroke-dasharray="424" stroke-dashoffset="106" stroke-linecap="round" transform="rotate(-90 100 100)"/>
      <text x="100" y="95" text-anchor="middle" font-size="36" font-weight="700" fill="var(--text)">75%</text>
      <text x="100" y="120" text-anchor="middle" font-size="12" fill="var(--text-muted)">hoàn thành</text>
    </svg>
    <div style="position:absolute;bottom:24px;display:flex;gap:var(--s-16)">
      <div class="text-center"><div class="chip good">Tốt</div><div class="hint">Thân</div></div>
      <div class="text-center"><div class="chip good">Tốt</div><div class="hint">Tâm</div></div>
      <div class="text-center"><div class="chip warn">Cần lưu ý</div><div class="hint">Trí</div></div>
    </div>
  </div>
  <div class="card">
    <h2>Nhiệm vụ sắp tới</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('clock')}</span>
      <div class="flex-1"><div style="font-weight:600">20:00 — Uống nước</div><div class="hint">Cốc thứ 7</div></div>
      <button class="pill active" style="border-color:var(--accent-customer);background:var(--accent-customer);color:#fff">Check</button>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('moon')}</span>
      <div class="flex-1"><div style="font-weight:600">22:30 — Chuẩn bị ngủ</div><div class="hint">Đi ngủ trước 23h</div></div>
      <button class="pill">Check</button>
    </div>
  </div>
</div>
{bottom_nav('home', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-HLTH-01_dong_ho_sinh_hoc.html'), 'w', encoding='utf-8').write(html('Sức khỏe tổng thể — AnCare', body, has_nav=True))

# 2. Home
body = f'''
<div class="appbar" style="border:none;background:linear-gradient(135deg,var(--accent-customer),var(--accent-customer-hover));color:#fff">
  <span class="back" style="opacity:0">{icon('chevron-left')}</span>
  <div class="flex-1 flex items-center gap-12">
    <div style="width:44px;height:44px;border-radius:var(--radius-full);background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;border:2px solid rgba(255,255,255,.4)">{icon('user')}</div>
    <div>
      <div style="font-weight:600;font-size:var(--text-lg)">Xin chào, Hạnh</div>
      <div style="font-size:var(--text-sm);opacity:.9">Gói Cơ-Nước-Mỡ · Tối ưu · còn 8 ngày</div>
    </div>
  </div>
  <span class="info" style="color:#fff">{icon('bell')}</span>
</div>
<div class="content" style="padding-top:var(--s-12)">
  <div class="card" style="border-color:var(--accent-customer);background:linear-gradient(135deg,#f0fdfa,#e6f7f5)">
    <div class="flex justify-between items-center" style="margin-bottom:var(--s-12)">
      <h2 style="margin:0">Check-in hôm nay</h2>
      <a href="S-HLTH-06_check_in.html" style="font-size:var(--text-sm);color:var(--accent-customer);font-weight:600;text-decoration:none">Mở màn Check-in →</a>
    </div>
    <div class="flex" style="gap:var(--s-8);overflow-x:auto;padding-bottom:var(--s-8)">
      <div class="pill" style="border-color:var(--accent-customer);background:var(--accent-customer);color:#fff;height:36px">{icon('check', 'sm')} Bữa sáng</div>
      <div class="pill" style="border-color:var(--accent-customer);background:var(--accent-customer);color:#fff;height:36px">{icon('check', 'sm')} Nước</div>
      <div class="pill" style="height:36px">Vận động</div>
      <div class="pill" style="height:36px">Bữa trưa</div>
      <div class="pill" style="height:36px">Ngủ sớm</div>
    </div>
  </div>
  <div class="card">
    <h2>Đồng hồ sinh học 24h</h2>
    <div style="height:80px;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <svg viewBox="0 0 300 60" width="100%" height="60" preserveAspectRatio="none">
        <polyline points="0,50 30,40 60,45 90,30 120,35 150,20 180,25 210,15 240,18 270,10 300,8" fill="none" stroke="var(--accent-customer)" stroke-width="2.5" stroke-linejoin="round"/>
        <polyline points="0,50 30,40 60,45 90,30 120,35 150,20 180,25 210,15 240,18 270,10 300,8 300,60 0,60" fill="rgba(20,158,110,.12)" stroke="none"/>
        <circle cx="300" cy="8" r="4" fill="var(--accent-customer)"/>
      </svg>
    </div>
  </div>
  <div class="card">
    <h2>Tiến trình sức khỏe</h2>
    <div style="height:80px;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <svg viewBox="0 0 300 60" width="100%" height="60" preserveAspectRatio="none">
        <polyline points="0,55 30,48 60,44 90,40 120,36 150,32 180,28 210,24 240,20 270,16 300,12" fill="none" stroke="var(--accent-customer)" stroke-width="2.5" stroke-linejoin="round"/>
        <polyline points="0,55 30,48 60,44 90,40 120,36 150,32 180,28 210,24 240,20 270,16 300,12 300,60 0,60" fill="rgba(20,158,110,.12)" stroke="none"/>
        <circle cx="300" cy="12" r="4" fill="var(--accent-customer)"/>
      </svg>
    </div>
  </div>
  <div class="table-wrap">
    <table class="table">
      <thead><tr><th>Chỉ số</th><th>Mục tiêu</th><th>Đầu</th><th>Gần nhất</th><th>Thay đổi</th></tr></thead>
      <tbody>
        <tr><td>Cân nặng</td><td>54</td><td>58</td><td style="color:var(--state-good);font-weight:700">55.2</td><td style="color:var(--state-good)">{icon('trending-down', 'sm')} 2.8</td></tr>
        <tr><td>Mỡ cơ thể</td><td>17.5</td><td>18.9</td><td style="color:var(--state-good);font-weight:700">17.8</td><td style="color:var(--state-good)">{icon('trending-down', 'sm')} 1.1</td></tr>
        <tr><td>Mỡ nội tạng</td><td>≤7</td><td>10</td><td style="color:var(--state-good);font-weight:700">8</td><td style="color:var(--state-good)">{icon('trending-down', 'sm')} 2</td></tr>
        <tr><td>Cơ bắp</td><td>≥38%</td><td>52</td><td style="color:var(--state-good);font-weight:700">52.5</td><td style="color:var(--state-good)">{icon('trending-up', 'sm')} 0.5</td></tr>
        <tr><td>Xương</td><td>2.5-3.5</td><td>2.8</td><td>2.8</td><td>—</td></tr>
        <tr><td>Nước</td><td>>50</td><td>57.7</td><td style="color:var(--state-good);font-weight:700">58.1</td><td style="color:var(--state-good)">{icon('trending-up', 'sm')} 0.4</td></tr>
        <tr><td>Tuổi SH</td><td>≤42</td><td>37</td><td style="color:var(--state-good);font-weight:700">36</td><td style="color:var(--state-good)">{icon('trending-down', 'sm')} 1</td></tr>
        <tr><td>RMR</td><td>—</td><td>1276</td><td>1280</td><td>—</td></tr>
      </tbody>
    </table>
  </div>
</div>
{bottom_nav('home', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-HLTH-02_trang_chu.html'), 'w', encoding='utf-8').write(html('Trang chủ — AnCare KH', body, has_nav=True))

# 3. Meal (KH)
body = f'''
{appbar('Bữa ăn hôm nay', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card customer" style="margin-bottom:var(--s-16)">
    <div class="label">Mục tiêu calo</div>
    <div class="title" style="font-size:var(--text-xl)">1.359 kcal · 4 bữa</div>
  </div>
  <div class="card">
    <h2>Bữa sáng · 320 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:56px;height:56px;border-radius:var(--radius-md);background:var(--bg-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent-customer)">{icon('camera')}</div>
      <div class="flex-1">
        <div style="font-weight:600">F1 + PPP + trái cây</div>
        <div class="hint">87 + 120 + 40 kcal</div>
      </div>
      <button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Ảnh</button>
    </div>
  </div>
  <div class="card">
    <h2>Bữa trưa · 450 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:56px;height:56px;border-radius:var(--radius-md);background:var(--bg-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent-customer)">{icon('camera')}</div>
      <div class="flex-1">
        <div style="font-weight:600">Cơm lứt + ức gà + rau</div>
        <div class="hint">150 + 250 + 50 kcal</div>
      </div>
      <button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Ảnh</button>
    </div>
  </div>
  <div class="card">
    <h2>Bữa phụ · 150 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:56px;height:56px;border-radius:var(--radius-md);background:var(--bg-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent-customer)">{icon('camera')}</div>
      <div class="flex-1">
        <div style="font-weight:600">Trái cây ít ngọt</div>
        <div class="hint">150 kcal</div>
      </div>
      <button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Ảnh</button>
    </div>
  </div>
  <div class="card">
    <h2>Bữa tối · 390 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <div style="width:56px;height:56px;border-radius:var(--radius-md);background:var(--bg-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent-customer)">{icon('camera')}</div>
      <div class="flex-1">
        <div style="font-weight:600">Cá hấp + rau luộc</div>
        <div class="hint">300 + 90 kcal</div>
      </div>
      <button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Ảnh</button>
    </div>
  </div>
  <div class="card">
    <h2>SP bổ sung</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('scale')}</span>
      <div class="flex-1"><div style="font-weight:600">PPP</div><div class="hint">1 muỗng · bữa sáng</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('heart')}</span>
      <div class="flex-1"><div style="font-weight:600">Omega-3</div><div class="hint">2 viên · bữa tối</div></div>
    </div>
  </div>
</div>
{bottom_nav('home', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-HLTH-04_bua_an.html'), 'w', encoding='utf-8').write(html('Bữa ăn — AnCare KH', body, has_nav=True))

# 4. Chat
body = f'''
{appbar('Chat', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12);padding-bottom:120px">
  <div class="card subtle" style="margin-bottom:var(--s-16)">
    <div class="flex items-center gap-12">
      <span style="color:var(--accent-customer)">{icon('award')}</span>
      <span class="hint" style="margin:0">Trợ lý AI sẽ gợi ý nhẹ khi phát hiện KH chưa check-in hoặc có dấu hiệu xấu.</span>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:var(--s-12)">
    <div style="align-self:flex-end;max-width:80%;background:var(--accent-customer);color:#fff;padding:var(--s-12);border-radius:var(--radius-md);border-bottom-right-radius:4px">
      Chào Thủy, hôm nay em chưa check-in bữa trưa. Em cần hỗ trợ gì không?
    </div>
    <div style="align-self:flex-start;max-width:80%;background:var(--bg-subtle);padding:var(--s-12);border-radius:var(--radius-md);border-bottom-left-radius:4px;border:1px solid var(--border)">
      <div style="font-weight:600;margin-bottom:4px">HLV Thủy</div>
      Chào Hạnh, em nhớ bữa trưa nhé. Nếu ăn ngoài thì chụp ảnh cho chị phân tích.
    </div>
    <div style="align-self:flex-end;max-width:80%;background:var(--accent-customer);color:#fff;padding:var(--s-12);border-radius:var(--radius-md);border-bottom-right-radius:4px">
      Dạ em hiểu rồi ạ.
    </div>
  </div>
</div>
<div class="cta-bar" style="bottom:64px">
  <div class="flex-1" style="position:relative">
    <input placeholder="Nhắn tin..." style="height:44px;border-radius:var(--radius-md);border:1px solid var(--border);padding:0 48px 0 16px;width:100%">
    <span style="position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--accent-customer)">{icon('send')}</span>
  </div>
</div>
{bottom_nav('home', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-HLTH-05_chat.html'), 'w', encoding='utf-8').write(html('Chat — AnCare KH', body, has_nav=True))

# 5. Check-in
body = f'''
{appbar('Check-in hôm nay', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card">
    <h2>Chỉ số cơ thể</h2>
    <div class="table-wrap" style="margin-bottom:var(--s-12)">
      <table class="table">
        <thead><tr><th>Chỉ số</th><th>Giá trị</th><th>Đơn vị</th></tr></thead>
        <tbody>
          <tr><td>Cân nặng</td><td>55.2</td><td>kg</td></tr>
          <tr><td>Mỡ cơ thể</td><td>17.8</td><td>%</td></tr>
          <tr><td>Mỡ nội tạng</td><td>8</td><td>%</td></tr>
          <tr><td>Cơ bắp</td><td>52.5</td><td>kg</td></tr>
          <tr><td>Xương</td><td>2.8</td><td>kg</td></tr>
          <tr><td>Nước</td><td>58.1</td><td>%</td></tr>
          <tr><td>Tuổi sinh học</td><td>36</td><td>tuổi</td></tr>
          <tr><td>RMR</td><td>1280</td><td>kcal</td></tr>
        </tbody>
      </table>
    </div>
    <button class="btn ghost">Nhập lại chỉ số</button>
  </div>
  <div class="card">
    <h2>Thực đơn hôm nay</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('sun')}</span>
      <div class="flex-1"><div style="font-weight:600">Bữa sáng</div><div class="hint">320 kcal · Đạm 24g · Tinh bột 32g · Béo 11g</div></div>
      <button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{icon('camera', 'sm')}</button>
      <span style="color:var(--state-good)">{icon('check')}</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Bữa trưa</div><div class="hint">450 kcal · Đạm 30g · Tinh bột 40g · Béo 13g</div></div>
      <button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{icon('camera', 'sm')}</button>
      <span style="color:var(--text-muted)">{icon('check')}</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('sun')}</span>
      <div class="flex-1"><div style="font-weight:600">Bữa phụ</div><div class="hint">150 kcal · Đạm 11g · Tinh bột 15g · Béo 5g</div></div>
      <button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{icon('camera', 'sm')}</button>
      <span style="color:var(--text-muted)">{icon('check')}</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('moon')}</span>
      <div class="flex-1"><div style="font-weight:600">Bữa tối</div><div class="hint">390 kcal · Đạm 29g · Tinh bột 39g · Béo 13g</div></div>
      <button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{icon('camera', 'sm')}</button>
      <span style="color:var(--text-muted)">{icon('check')}</span>
    </div>
  </div>
  <div class="card">
    <h2>Hoạt động</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('water')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Uống nước</div>
        <div class="hint">8 cốc × 200ml = 1.6L</div>
      </div>
      <div class="flex items-center gap-8">
        <button class="btn secondary" style="height:32px;width:32px;padding:0;border-radius:var(--radius-md)">{icon('minus', 'sm')}</button>
        <span style="font-weight:700">8</span>
        <button class="btn secondary" style="height:32px;width:32px;padding:0;border-radius:var(--radius-md)">{icon('plus', 'sm')}</button>
      </div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('moon')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Giấc ngủ</div>
        <div class="hint">7 giờ · 23:00 → 06:00</div>
      </div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('run')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Vận động</div>
        <div class="hint">Pickleball 60 phút · ~360 kcal</div>
      </div>
      <button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Thêm</button>
    </div>
  </div>
  <div class="card">
    <h2>Kiến thức</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('book')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Bài 3 · Bột đường & năng lượng</div>
        <div class="hint">3 phút · 3 câu hỏi sau học</div>
      </div>
      <span style="color:var(--text-muted)">{icon('check')}</span>
    </div>
    <button class="btn primary customer block">{icon('book', 'sm')} Xem bài học</button>
  </div>
</div>
{cta('Hoàn thành check-in', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-HLTH-06_check_in.html'), 'w', encoding='utf-8').write(html('Check-in — AnCare KH', body))

# 6. Report
body = f'''
{appbar('Báo cáo', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="segmented">
    <button class="seg active">Tổng kết ngày</button>
    <button class="seg">Tiến trình</button>
    <button class="seg">Đề xuất</button>
  </div>
  <div class="focus-card customer" style="margin-bottom:var(--s-16)">
    <div class="label">Tổng kết 21:00</div>
    <div class="title" style="font-size:var(--text-xl)">Hôm nay bạn làm tốt! 👏</div>
  </div>
  <div class="card">
    <h2>Phân tích chuyên sâu</h2>
    <div class="card subtle">
      <div class="hint" style="line-height:1.7">Nước đạt 1.6L (tốt). Đạm đủ. Mỡ nội tạng giảm dần. Bữa trưa hơi thiếu rau.</div>
    </div>
  </div>
  <div class="card">
    <h2>Lý do ảnh hưởng</h2>
    <div class="card subtle">
      <div class="hint" style="line-height:1.7">Ngủ trễ hôm qua → mệt mỏi chiều. Uống đủ nước giúp trao đổi chất tốt.</div>
    </div>
  </div>
  <div class="card">
    <h2>Lời khuyên ngày mai</h2>
    <div class="card subtle">
      <div class="hint" style="line-height:1.7">• Ngủ trước 23h<br>• Thêm rau bữa trưa<br>• Vận động 30 phút</div>
    </div>
  </div>
  <div class="card" style="border-color:var(--accent-customer)">
    <h2 style="color:var(--accent-customer)">Đề xuất nâng cấp</h2>
    <div class="hint" style="margin-bottom:var(--s-12)">Gói Tối ưu hiện tại. Gợi ý thêm Omega-3 để hỗ trợ mỡ nội tạng.</div>
    <button class="btn ghost customer block">Xem gợi ý</button>
  </div>
  <button class="btn primary customer block" style="margin-bottom:var(--s-16)">{icon('share', 'sm')} Tạo Infographic nhật ký</button>
</div>
{bottom_nav('report', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-HLTH-07_bao_cao.html'), 'w', encoding='utf-8').write(html('Báo cáo — AnCare KH', body, has_nav=True))

# 7. Training
body = f'''
{appbar('Đào tạo', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="field" style="margin-bottom:var(--s-16)">
    <div style="position:relative">
      <span style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--text-muted)">{icon('search')}</span>
      <input type="text" placeholder="Tìm bài học..." style="padding-left:40px">
    </div>
  </div>
  <div style="font-size:var(--text-sm);font-weight:700;color:var(--accent-customer);text-transform:uppercase;margin-bottom:var(--s-12)">Kiến thức dinh dưỡng</div>
  <div class="card" style="padding:var(--s-12)">
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent-customer);color:#fff;display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">✓</div>
      <div class="flex-1"><div style="font-weight:600">Bài 1 · Nước & trao đổi chất</div><div class="hint">3 phút · đã hoàn thành</div></div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent-customer);color:#fff;display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">✓</div>
      <div class="flex-1"><div style="font-weight:600">Bài 2 · Đạm — cơ bắp</div><div class="hint">4 phút · đã hoàn thành</div></div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--bg-subtle);color:var(--text-muted);display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">3</div>
      <div class="flex-1"><div style="font-weight:600">Bài 3 · Bột đường & năng lượng</div><div class="hint">3 phút · 3 câu hỏi</div></div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--bg-subtle);color:var(--text-muted);display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">4</div>
      <div class="flex-1"><div style="font-weight:600">Bài 4 · Mỡ nội tạng & nguy cơ</div><div class="hint">5 phút</div></div>
      {icon('chevron-right')}
    </div>
  </div>
  <div style="font-size:var(--text-sm);font-weight:700;color:var(--accent-customer);text-transform:uppercase;margin:var(--s-24) 0 var(--s-12)">Thói quen sống khỏe</div>
  <div class="card" style="padding:var(--s-12)">
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--bg-subtle);color:var(--text-muted);display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">5</div>
      <div class="flex-1"><div style="font-weight:600">Bài 5 · Đồng hồ sinh học</div><div class="hint">4 phút</div></div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--bg-subtle);color:var(--text-muted);display:flex;align-items:center;justify-content:center;font-size:var(--text-sm);font-weight:700">6</div>
      <div class="flex-1"><div style="font-weight:600">Bài 6 · Ăn ngược & nhai kỹ</div><div class="hint">3 phút</div></div>
      {icon('chevron-right')}
    </div>
  </div>
</div>
{bottom_nav('learn', [('home', 'Trang chủ', 'home'), ('report', 'Báo cáo', 'chart'), ('learn', 'Đào tạo', 'book'), ('profile', 'Hồ sơ', 'user')])}
'''
open(os.path.join(out_dir, 'S-DEV-02_dao_tao.html'), 'w', encoding='utf-8').write(html('Đào tạo — AnCare KH', body, has_nav=True))

print('Batch KH generated: 7 files')
for f in ['S-HLTH-01_dong_ho_sinh_hoc.html','S-HLTH-02_trang_chu.html','S-HLTH-04_bua_an.html','S-HLTH-05_chat.html','S-HLTH-06_check_in.html','S-HLTH-07_bao_cao.html','S-DEV-02_dao_tao.html']:
    print('  ', f)
