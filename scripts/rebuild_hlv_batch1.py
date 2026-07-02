import os

ICONS = {
    'arrow-left': '<path d="M5 12h14M12 5l-7 7 7 7"/>',
    'info': '<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="8.01"/><line x1="12" y1="12" x2="12" y2="16"/>',
    'chevron-left': '<path d="M15 6l-6 6 6 6"/>',
    'chevron-right': '<path d="M9 6l6 6-6 6"/>',
    'search': '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/>',
    'bell': '<path d="M10 5a2 2 0 0 1 4 0 7 7 0 0 1 4 6v3a4 4 0 0 0 1 2H5a4 4 0 0 0 1-2v-3a7 7 0 0 1 4-6M9 17v1a3 3 0 0 0 6 0v-1"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'user': '<path d="M12 12a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM5 20a7 7 0 0 1 14 0"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM20 21v-2a4 4 0 0 0-3-3.87"/>',
    'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'home': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'chart': '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'camera': '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    'check': '<polyline points="20 6 9 17 4 12"/>',
    'scan': '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/>',
    'scale': '<path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L2.5 7.5"/>',
    'filter': '<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>',
    'more': '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>',
    'mail': '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'eye': '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    'alert': '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'help': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'clipboard': '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    'utensils': '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>',
    'trending-up': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    'trending-down': '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
    'water': '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
    'moon': '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
    'run': '<path d="M4 15l3-3 2 2 2.5-3L14 12l2-2 3 4-3 2-1-1-2 3-4-2z"/><circle cx="17" cy="4" r="2"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.3 12.3 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.3 12.3 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    'thumb-up': '<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'heart': '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    'award': '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
}

def icon(name, size='md'):
    if name not in ICONS:
        return '<svg viewBox="0 0 24 24" class="icon"/>'
    cls = {'sm': 'icon-sm', 'md': 'icon', 'lg': 'icon-lg'}.get(size, 'icon')
    return f'<svg class="{cls}" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def appbar(title, back=False, info=False):
    b = f'<span class="back">{icon("chevron-left")}</span>' if back else '<span class="back" style="opacity:0">' + icon('chevron-left') + '</span>'
    i = f'<span class="info">{icon("info")}</span>' if info else '<span class="info" style="opacity:0">' + icon('info') + '</span>'
    return f'<div class="appbar">{b}<h1>{title}</h1>{i}</div>'

def progress_dots(step, total=4):
    dots = ''
    for i in range(total):
        cls = 'active' if i == step - 1 else ('done' if i < step - 1 else '')
        dots += f'<span class="dot {cls}"></span>'
    return f'<div class="progress-dots">{dots}</div>'

def bottom_nav(active, items):
    out = '<div class="bottom-nav">'
    for name, label, iname in items:
        cls = 'nav-item active' if active == name else 'nav-item'
        out += f'<div class="{cls}"><span class="icon">{icon(iname)}</span><span>{label}</span></div>'
    return out + '</div>'

def cta(primary, secondary=None, icon_name=None):
    s = f'<button class="btn secondary">{secondary}</button>' if secondary else ''
    ic = icon(icon_name) if icon_name else ''
    return f'<div class="cta-bar">{s}<button class="btn primary">{ic}{primary}</button></div>'

def html(title, body, has_nav=False, nav_active=None, nav_items=None, cta_html=None, extra_head=''):
    default_nav = [('home', 'Trang chủ', 'home'), ('team', 'Team', 'users'), ('chat', 'Chat', 'chat'), ('coach', 'HLV', 'award'), ('profile', 'Hồ sơ', 'user')]
    nav = bottom_nav(nav_active, nav_items or default_nav) if has_nav else ''
    cta = cta_html or ''
    return f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../_assets/_tokens.css"><link rel="stylesheet" href="../_assets/_base.css">
{extra_head}
</head><body><div class="screen">{body}{nav}{cta}</div></body></html>'''

out_dir = '/Users/cuongpt/Workspaces/ancare-enhancement/docs/03-mockups/coach'
os.makedirs(out_dir, exist_ok=True)

# 1. Login
login_body = f'''
<div class="appbar" style="background:transparent;border:none"><span class="back" style="opacity:0">{icon('chevron-left')}</span><h1></h1><span class="info" style="opacity:0">{icon('info')}</span></div>
<div class="content no-nav" style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:0">
  <div style="width:72px;height:72px;border-radius:var(--radius-lg);background:linear-gradient(135deg,var(--accent),var(--accent-hover));display:flex;align-items:center;justify-content:center;color:#fff;margin-bottom:var(--s-24)">
    {icon('heart', 'lg')}
  </div>
  <h2 style="margin:0 0 4px;font-size:var(--text-2xl)">AN Care</h2>
  <p style="color:var(--text-muted);margin:0 0 var(--s-32)">Sống khỏe mỗi ngày</p>
  <div class="card" style="width:100%;margin-bottom:0">
    <div class="field">
      <label>Số điện thoại hoặc Email</label>
      <input type="text" placeholder="Nhập số điện thoại hoặc email">
    </div>
    <div class="field">
      <label>Mật khẩu</label>
      <div style="position:relative">
        <input type="password" placeholder="Nhập mật khẩu">
        <span style="position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--text-muted)">{icon('eye')}</span>
      </div>
    </div>
    <button class="btn primary block" style="margin:var(--s-8) 0">Đăng nhập</button>
    <div class="flex justify-between" style="margin-top:var(--s-12)">
      <a href="#" style="font-size:var(--text-sm);color:var(--text-muted);text-decoration:none">Quên mật khẩu?</a>
      <a href="#" style="font-size:var(--text-sm);color:var(--accent);text-decoration:none;font-weight:600">Đăng ký</a>
    </div>
  </div>
  <div class="hint text-center" style="margin-top:var(--s-16)">Face ID sẽ tự động kích hoạt khi có sẵn</div>
</div>
'''
open(os.path.join(out_dir, 'S-AUTH-01_dang_nhap.html'), 'w', encoding='utf-8').write(html('Đăng nhập — AnCare', login_body, cta_html=None))

# 2. HLV Dashboard
nav_items = [('home', 'Trang chủ', 'home'), ('team', 'Team', 'users'), ('chat', 'Chat', 'chat'), ('coach', 'HLV', 'award'), ('profile', 'Hồ sơ', 'user')]
body = f'''
{appbar('Trang chủ', info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">Xin chào, Thủy</div>
    <div class="title" style="font-size:var(--text-lg)">Chào buổi sáng! ☀️</div>
  </div>
  <div class="card" style="margin-bottom:var(--s-16)">
    <h2 style="font-size:var(--text-base)">KPI hôm nay</h2>
    <div class="flex justify-between" style="gap:var(--s-12)">
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-2xl);font-weight:700;color:var(--accent)">0</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Khách hàng</div>
      </div>
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-2xl);font-weight:700;color:var(--accent)">0₫</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Doanh thu</div>
      </div>
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-2xl);font-weight:700;color:var(--accent)">0</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Nhà PP</div>
      </div>
    </div>
  </div>
  <div class="card" style="margin-bottom:var(--s-16)">
    <h2 style="font-size:var(--text-base)">Công việc hôm nay</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12);border:1px solid var(--border);border-radius:var(--radius-md);margin-bottom:var(--s-12)">
      <span style="color:var(--accent)">{icon('scan')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Nhắc cập nhật chỉ số Tanita</div>
        <div class="hint">3 khách hàng cần cập nhật</div>
      </div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12);border:1px solid var(--border);border-radius:var(--radius-md)">
      <span style="color:var(--accent)">{icon('chat')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Chăm sóc hội viên</div>
        <div class="hint">2 KH có nguy cơ bỏ cuộc</div>
      </div>
      {icon('chevron-right')}
    </div>
  </div>
</div>
{bottom_nav('home', nav_items)}
'''
open(os.path.join(out_dir, 'S-AUTH-02_shell.html'), 'w', encoding='utf-8').write(html('Trang chủ HLV — AnCare', body, has_nav=True))

# 3. Team list
body = f'''
{appbar('Team', info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="segmented">
    <button class="seg">KH tiềm năng</button>
    <button class="seg active">KH của tôi</button>
  </div>
  <div class="card" style="margin-bottom:var(--s-16)">
    <div class="flex items-center gap-12" style="margin-bottom:var(--s-12)">
      <div class="flex-1" style="position:relative">
        <span style="position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--text-muted)">{icon('search')}</span>
        <input type="text" placeholder="Tìm theo tên, SĐT..." style="padding-left:40px">
      </div>
      <button class="pill" style="height:40px">{icon('filter')} Lọc</button>
    </div>
    <div class="flex justify-between" style="margin-bottom:var(--s-12)">
      <div style="text-align:center;flex:1;padding:var(--s-12);background:var(--state-good-bg);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--state-good)">3</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Tích cực</div>
      </div>
      <div style="text-align:center;flex:1;padding:var(--s-12);background:var(--state-warn-bg);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--state-warn)">1</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Có nguy cơ</div>
      </div>
      <div style="text-align:center;flex:1;padding:var(--s-12);background:var(--state-alert-bg);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--state-alert)">1</div>
        <div style="font-size:var(--text-xs);color:var(--text-muted)">Kém quan tâm</div>
      </div>
    </div>
  </div>
  <div class="card" style="padding:var(--s-12)">
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:44px;height:44px;border-radius:var(--radius-full);background:var(--accent-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent);font-weight:700">H</div>
      <div class="flex-1">
        <div style="font-weight:600">Hạnh</div>
        <div class="hint">Cơ-Nước-Mỡ · 8 ngày còn lại</div>
      </div>
      <span class="chip good">Tích cực</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:44px;height:44px;border-radius:var(--radius-full);background:var(--state-warn-bg);display:flex;align-items:center;justify-content:center;color:var(--state-warn);font-weight:700">M</div>
      <div class="flex-1">
        <div style="font-weight:600">Mipt01</div>
        <div class="hint">Bữa ăn lành mạnh · 12 ngày còn lại</div>
      </div>
      <span class="chip warn">Có nguy cơ</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div style="width:44px;height:44px;border-radius:var(--radius-full);background:var(--state-alert-bg);display:flex;align-items:center;justify-content:center;color:var(--state-alert);font-weight:700">T</div>
      <div class="flex-1">
        <div style="font-weight:600">Testkhtn02</div>
        <div class="hint">Chưa mua gói</div>
      </div>
      <span class="chip alert">Kém quan tâm</span>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <div style="width:44px;height:44px;border-radius:var(--radius-full);background:var(--accent-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent);font-weight:700">C</div>
      <div class="flex-1">
        <div style="font-weight:600">Cường</div>
        <div class="hint">Dinh dưỡng tế bào · 45 ngày còn lại</div>
      </div>
      <span class="chip good">Tích cực</span>
    </div>
  </div>
</div>
{bottom_nav('team', nav_items)}
<button class="fab">{icon('plus')}</button>
'''
open(os.path.join(out_dir, 'S-LEAD-01_danh_sach.html'), 'w', encoding='utf-8').write(html('Team — AnCare', body, has_nav=True))

# 4+5. Lead creation / portrait (same content, different context)
portrait_body = lambda with_dots: f'''
{appbar('Thêm mới KH' if not with_dots else 'Chân dung KH', back=True, info=True)}
{progress_dots(2 if with_dots else 0, 4) if with_dots else ''}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card">
    <h2>Thông tin cơ bản</h2>
    <div class="field"><label>Họ và tên KH <span style="color:var(--state-alert)">*</span></label><input placeholder="Họ và tên"></div>
    <div class="flex gap-12">
      <div class="field flex-1"><label>Số điện thoại</label><input placeholder="SĐT"></div>
      <div class="field flex-1"><label>Email</label><input placeholder="Email"></div>
    </div>
    <div class="flex gap-12">
      <div class="field flex-1"><label>Ngày sinh</label><input placeholder="dd/mm/yyyy"></div>
      <div class="field flex-1"><label>Giới tính</label><input placeholder="Nam"></div>
    </div>
    <div class="flex gap-12">
      <div class="field flex-1"><label>Chiều cao (cm)</label><input placeholder="170"></div>
      <div class="field flex-1"><label>Cân nặng (kg)</label><input placeholder="64.8"></div>
    </div>
    <div class="field"><label>Người mời</label><input placeholder="Thủy (HLV)" value="Thủy (HLV)"></div>
  </div>
  <div class="card">
    <h2>Chân dung Khách hàng</h2>
    <div class="card subtle" style="margin-bottom:var(--s-12)">
      <div style="font-size:var(--text-sm);line-height:1.7;color:var(--text-secondary)">
        <strong>1.</strong> Mệt mỏi/dễ cảm? &nbsp;<strong>2.</strong> Đau đầu, đau lưng, đau mỏi? &nbsp;<strong>3.</strong> Có tiểu đường, huyết áp, tim mạch, khớp? &nbsp;<strong>4.</strong> Công việc/gia đình có áp lực? &nbsp;<strong>5.</strong> Giấc ngủ tốt không? &nbsp;<strong>6.</strong> Hay đói hoặc thèm ăn? &nbsp;<strong>7.</strong> Thường ăn đồ chế biến sẵn? &nbsp;<strong>8.</strong> Có nghĩ thức ăn ảnh hưởng sức khỏe? &nbsp;<strong>9.</strong> Có thường bỏ bữa sáng? &nbsp;<strong>10.</strong> Mỗi ngày uống khoảng bao nhiêu cốc nước? &nbsp;<strong>11.</strong> Có tập thể dục không? &nbsp;<strong>12.</strong> Bác sĩ có khuyên giảm cân hoặc giảm cholesterol? &nbsp;<strong>13.</strong> Muốn giảm cân hoặc giảm vòng bụng? &nbsp;<strong>14.</strong> Muốn tăng cân? &nbsp;<strong>15.</strong> Có hút thuốc hoặc tiếp xúc khói thuốc? &nbsp;<strong>16.</strong> Có thường uống rượu, bia hoặc cà phê? &nbsp;<strong>17.</strong> Mục tiêu chính khi kiểm tra sức khỏe là gì?
      </div>
    </div>
    <div class="field"><label>Trả lời (HLV nhập gộp)</label><textarea placeholder="Tóm tắt câu trả lời của KH, tập trung kết quả mong muốn..."></textarea></div>
  </div>
</div>
{cta('Lưu → Khảo sát Tanita' if with_dots else 'Lưu KH', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-LEAD-02_tao_lead.html'), 'w', encoding='utf-8').write(html('Thêm mới KH — AnCare', portrait_body(False)))
open(os.path.join(out_dir, 'S-CONS-02_chan_dung_kh.html'), 'w', encoding='utf-8').write(html('Chân dung KH — AnCare', portrait_body(True)))

# 6. Tanita
body = f'''
{appbar('Khảo sát Tanita', back=True, info=True)}
{progress_dots(3, 4)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card">
    <h2>Nhập nhanh từ ảnh</h2>
    <div class="flex gap-12">
      <button class="btn secondary flex-1" style="height:48px">{icon('camera')} Chụp ảnh</button>
      <button class="btn secondary flex-1" style="height:48px">{icon('search')} Chọn ảnh</button>
    </div>
    <div class="hint" style="margin-top:var(--s-12)">OCR tự nhận chỉ số từ màn hình cân Tanita. HLV kiểm tra & sửa.</div>
  </div>
  <div class="card">
    <h2>Hoặc nhập tay</h2>
    <div class="field"><label>Cân nặng (kg)</label><input value="64.8"></div>
    <div class="field"><label>Tỷ lệ mỡ cơ thể (%)</label><input value="18.9"></div>
    <div class="field"><label>Khối lượng xương (kg)</label><input value="2.8"></div>
    <div class="field"><label>Tỷ lệ nước (%)</label><input value="57.7"></div>
    <div class="field"><label>Khối lượng cơ (kg)</label><input value="52.0"></div>
    <div class="field"><label>Vóc dáng</label><input value="Bình thường"></div>
    <div class="field"><label>Tuổi sinh học</label><input value="37"></div>
    <div class="field"><label>Năng lượng nghỉ ngơi (kcal)</label><input value="1276"></div>
    <div class="field"><label>Tỷ lệ mỡ nội tạng (1-50)</label><input value="10"></div>
  </div>
</div>
{cta('Tạo bản tư vấn', icon_name='scan')}
'''
open(os.path.join(out_dir, 'S-CONS-03_tanita.html'), 'w', encoding='utf-8').write(html('Khảo sát Tanita — AnCare', body))

# 7. Analysis
body = f'''
{appbar('Phân tích kết quả', back=True, info=True)}
{progress_dots(4, 4)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="table-wrap">
    <table class="table">
      <thead><tr><th>Chỉ số</th><th>Hiện tại</th><th>Cần ±</th><th>Tiêu chuẩn</th><th>Đánh giá</th></tr></thead>
      <tbody>
        <tr class="good"><td>Cân nặng</td><td>64.8 kg</td><td>−2.8</td><td>62</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Khối lượng cơ</td><td>52.0 kg</td><td>+0</td><td>≥38%</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Khối lượng xương</td><td>2.8 kg</td><td>+0</td><td>2.5-3.5</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Tỷ lệ nước</td><td>57.7%</td><td>+0</td><td>&gt;50%</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="warn"><td>Tỷ lệ mỡ</td><td>18.9%</td><td>−1.4%</td><td>17.5%</td><td><span class="chip warn">Thừa 1.4%</span></td></tr>
        <tr class="alert"><td>Mỡ nội tạng</td><td>10</td><td>−3</td><td>1-7</td><td><span class="chip alert">Nguy hiểm</span></td></tr>
        <tr class="good"><td>Vóc dáng</td><td>Bình thường</td><td>—</td><td>—</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Tuổi sinh học</td><td>37</td><td>—</td><td>≤42</td><td><span class="chip good">Trẻ 5t</span></td></tr>
        <tr class="good"><td>RMR</td><td>1276</td><td>—</td><td>—</td><td><span class="chip good">Tốt</span></td></tr>
      </tbody>
    </table>
  </div>
  <div class="hint text-center" style="margin-bottom:var(--s-16)">Bấm từng dòng để xem ý nghĩa chỉ số & rủi ro bệnh lý</div>
  <div class="card">
    <h2>Chốt mục tiêu</h2>
    <div class="pills" style="margin-bottom:var(--s-12)">
      <span class="pill active">{icon('check', 'sm')} Giảm cân</span>
      <span class="pill">Tăng cân</span>
      <span class="pill">Giữ cân</span>
    </div>
    <div class="focus-card" style="margin-bottom:0">
      <div class="label">Chương trình đề xuất</div>
      <div class="title" style="font-size:var(--text-xl)">Cân bằng Cơ — Nước — Mỡ</div>
    </div>
  </div>
  <div class="card subtle">
    <div class="flex items-center gap-12">
      <span style="color:var(--state-warn)">{icon('alert')}</span>
      <span class="hint" style="margin:0">Không có gì là thần dược; để có kết quả cần kiến thức dinh dưỡng, kỷ luật bản thân, hiểu nguyên lý để không phụ thuộc vào HLV hoặc sản phẩm.</span>
    </div>
  </div>
</div>
{cta('Xem lộ trình', secondary='Đóng', icon_name='chevron-right')}
'''
open(os.path.join(out_dir, 'S-CONS-04_phan_tich.html'), 'w', encoding='utf-8').write(html('Phân tích kết quả — AnCare', body))

# 8. Program plan
body = f'''
{appbar('Xem lộ trình', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">Chương trình Cơ — Nước — Mỡ</div>
    <div class="title" style="font-size:var(--text-xl)">Giảm đúng mỡ thừa · giữ cơ + nước</div>
  </div>
  <div class="card">
    <h2>Lợi ích</h2>
    <div style="display:flex;flex-direction:column;gap:var(--s-8)">
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Giảm đúng mỡ thừa, không mất cơ</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Cân bằng nước & điện giải</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Khỏe mạnh từ bên trong</span></div>
    </div>
  </div>
  <div class="card">
    <h2>Kết quả dự kiến</h2>
    <div class="flex gap-12">
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--accent)">−3 kg</div>
        <div class="hint">mỡ</div>
      </div>
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--accent)">52 kg</div>
        <div class="hint">giữ cơ</div>
      </div>
      <div class="flex-1" style="text-align:center;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
        <div style="font-size:var(--text-xl);font-weight:700;color:var(--accent)">&gt;55%</div>
        <div class="hint">nước</div>
      </div>
    </div>
  </div>
  <div class="card">
    <h2>Lộ trình 3 tháng <span class="chip accent">mặc định</span></h2>
    <div style="display:flex;flex-direction:column;gap:var(--s-12)">
      <div class="flex gap-12">
        <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">1</div>
        <div class="flex-1">
          <div style="font-weight:700">Tháng 1</div>
          <div class="hint">Điều chỉnh cân nặng, trang bị kiến thức cơ bản thay đổi tư duy dinh dưỡng & thể chất.</div>
        </div>
      </div>
      <div class="flex gap-12">
        <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">2</div>
        <div class="flex-1">
          <div style="font-weight:700">Tháng 2</div>
          <div class="hint">Tăng cơ, tăng cường sức khỏe, điều chỉnh các thói quen không lành mạnh.</div>
        </div>
      </div>
      <div class="flex gap-12">
        <div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">3</div>
        <div class="flex-1">
          <div style="font-weight:700">Tháng 3</div>
          <div class="hint">Tối ưu hóa vóc dáng, trẻ hóa, duy trì năng lượng, xây dựng thói quen lành mạnh bền vững.</div>
        </div>
      </div>
    </div>
  </div>
  <div class="card">
    <h2>Gói sản phẩm đi kèm</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1">
        <div style="font-weight:600">F1 — Bữa ăn lành mạnh</div>
        <div class="hint">Thay bữa, kiểm soát cân nặng</div>
      </div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('scale')}</span>
      <div class="flex-1">
        <div style="font-weight:600">PPP — Bột Protein</div>
        <div class="hint">Bổ sung đạm, hỗ trợ cơ</div>
      </div>
      {icon('chevron-right')}
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent)">{icon('heart')}</span>
      <div class="flex-1">
        <div style="font-weight:600">Omega-3 Herbalifeline</div>
        <div class="hint">Hỗ trợ tim mạch</div>
      </div>
      {icon('chevron-right')}
    </div>
  </div>
  <div class="card subtle">
    <div class="flex items-center gap-12">
      <span style="color:var(--state-warn)">{icon('alert')}</span>
      <span class="hint" style="margin:0">Giá sản phẩm HLV giải thích bên ngoài app. Không có gì là thần dược.</span>
    </div>
  </div>
</div>
{cta('Tạo tài khoản', secondary='Đóng', icon_name='chevron-right')}
'''
open(os.path.join(out_dir, 'S-CONS-05_giai_phap.html'), 'w', encoding='utf-8').write(html('Xem lộ trình — AnCare', body))

print('Batch 1 generated: 8 files')
for f in ['S-AUTH-01_dang_nhap.html','S-AUTH-02_shell.html','S-LEAD-01_danh_sach.html','S-LEAD-02_tao_lead.html','S-CONS-02_chan_dung_kh.html','S-CONS-03_tanita.html','S-CONS-04_phan_tich.html','S-CONS-05_giai_phap.html']:
    print('  ', f)
