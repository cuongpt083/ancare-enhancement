import os

# Icons (same as batch1, abbreviated)
ICONS = {
    'chevron-left': '<path d="M15 6l-6 6 6 6"/>', 'chevron-right': '<path d="M9 6l6 6-6 6"/>',
    'info': '<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="8.01"/><line x1="12" y1="12" x2="12" y2="16"/>',
    'check': '<polyline points="20 6 9 17 4 12"/>', 'camera': '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    'utensils': '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>',
    'scale': '<path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L2.5 7.5"/>',
    'water': '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
    'alert': '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'help': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'clipboard': '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    'message': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'bell': '<path d="M10 5a2 2 0 0 1 4 0 7 7 0 0 1 4 6v3a4 4 0 0 0 1 2H5a4 4 0 0 0 1-2v-3a7 7 0 0 1 4-6M9 17v1a3 3 0 0 0 6 0v-1"/>',
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.3 12.3 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.3 12.3 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM20 21v-2a4 4 0 0 0-3-3.87"/>',
    'home': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'award': '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
    'user': '<path d="M12 12a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM5 20a7 7 0 0 1 14 0"/>',
    'chart': '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'moon': '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
    'sun': '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>',
    'trending-up': '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    'trending-down': '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
    'run': '<path d="M4 15l3-3 2 2 2.5-3L14 12l2-2 3 4-3 2-1-1-2 3-4-2z"/><circle cx="17" cy="4" r="2"/>',
    'thumb-up': '<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>',
    'heart': '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
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

# 9. Close package
body = f'''
{appbar('Chốt gói', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">Chương trình Cơ — Nước — Mỡ</div>
    <div class="title" style="font-size:var(--text-xl)">Gói Tối ưu · 3 tháng</div>
  </div>
  <div class="card">
    <h2>SP đi kèm</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{icon('utensils')}</span><div class="flex-1"><div style="font-weight:600">F1 · Bữa ăn lành mạnh</div><div class="hint">2 muỗng/bữa</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{icon('scale')}</span><div class="flex-1"><div style="font-weight:600">PPP · Bột Protein</div><div class="hint">1 muỗng/bữa</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{icon('heart')}</span><div class="flex-1"><div style="font-weight:600">Herbalifeline · Omega-3</div><div class="hint">2 viên/ngày</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0"><span style="color:var(--accent)">{icon('water')}</span><div class="flex-1"><div style="font-weight:600">Lô Hội Thảo Mộc</div><div class="hint">3 muỗng/ngày</div></div></div>
  </div>
  <div class="card">
    <h2>Cam kết</h2>
    <div style="display:flex;flex-direction:column;gap:var(--s-8)">
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Theo đúng thực đơn & nước mỗi ngày</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Check-in đầy đủ trên app</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--state-good)">{icon('check')}</span><span>Chủ động hỏi HLV khi gặp khó</span></div>
    </div>
  </div>
  <div class="card subtle">
    <div class="flex items-center gap-12">
      <span style="color:var(--state-warn)">{icon('alert')}</span>
      <span class="hint" style="margin:0">KH đã đọc & hiểu: không thần dược, cần kiến thức + kỷ luật + hiểu nguyên lý.</span>
    </div>
  </div>
</div>
{cta('Tạo tài khoản', secondary='Đóng về DS KH', icon_name='chevron-right')}
'''
open(os.path.join(out_dir, 'S-CONS-06_chot_goi.html'), 'w', encoding='utf-8').write(html('Chốt gói — AnCare', body))

# 10. Create account modal-like screen
body = f'''
{appbar('Tạo tài khoản KH', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">Thông tin đăng nhập</div>
    <div class="title" style="font-size:var(--text-xl)">Phạm Hạnh</div>
  </div>
  <div class="card">
    <div class="field"><label>Tài khoản</label><input value="097xxxxxxx"></div>
    <div class="field"><label>Mật khẩu</label><input value="AnCare@2026" type="text"></div>
    <div class="field"><label>Xác nhận mật khẩu</label><input value="AnCare@2026" type="text"></div>
    <div class="hint" style="margin-bottom:var(--s-12)">Mật khẩu ngẫu nhiên, HLV có thể chỉnh sửa.</div>
    <div class="flex items-center gap-12" style="padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <span style="color:var(--accent)">{icon('mail')}</span>
      <span class="hint" style="margin:0">Gửi email/SMS chứa tài khoản & mật khẩu cho KH</span>
    </div>
  </div>
</div>
{cta('Tạo tài khoản', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-CONS-08_tao_tk.html'), 'w', encoding='utf-8').write(html('Tạo tài khoản KH — AnCare', body))

# 11. Meal plan
body = f'''
{appbar('Gợi ý bữa ăn', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card">
    <h2>Mục tiêu</h2>
    <div class="flex gap-12">
      <div class="field flex-1" style="margin-bottom:0"><label>Calo/ngày</label><div class="flex items-center gap-12"><button class="btn secondary" style="height:36px;width:36px;padding:0;border-radius:var(--radius-md)">−</button><input value="1359" style="text-align:center"><button class="btn secondary" style="height:36px;width:36px;padding:0;border-radius:var(--radius-md)">+</button></div></div>
      <div class="field flex-1" style="margin-bottom:0"><label>Số bữa</label><div class="flex items-center gap-12"><button class="btn secondary" style="height:36px;width:36px;padding:0;border-radius:var(--radius-md)">−</button><input value="4" style="text-align:center"><button class="btn secondary" style="height:36px;width:36px;padding:0;border-radius:var(--radius-md)">+</button></div></div>
    </div>
    <button class="btn primary block" style="margin-top:var(--s-16)">{icon('utensils', 'sm')} Tạo gợi ý bữa ăn</button>
  </div>
  <div class="card">
    <h2>Cấu trúc bữa ăn</h2>
    <div class="flex justify-between" style="margin-bottom:var(--s-12)">
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">30%</div><div class="hint">Đạm</div></div>
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">40%</div><div class="hint">Tinh bột</div></div>
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">30%</div><div class="hint">Chất béo</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <span style="color:var(--accent)">{icon('water')}</span>
      <div><div style="font-weight:600">Nước khuyến nghị</div><div class="hint">2.5L (8 cốc 200ml)</div></div>
    </div>
  </div>
  <div class="card">
    <h2>Bữa sáng · 320 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">F1 + PPP</div><div class="hint">2 muỗng F1 + 1 muỗng PPP + 250ml nước</div></div>
      <div style="text-align:right"><div style="font-weight:700">160 kcal</div><div class="hint">18g đạm</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Trứng luộc</div><div class="hint">2 quả</div></div>
      <div style="text-align:right"><div style="font-weight:700">120 kcal</div><div class="hint">12g đạm</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Rau xào</div><div class="hint">1 đĩa nhỏ</div></div>
      <div style="text-align:right"><div style="font-weight:700">40 kcal</div><div class="hint">2g chất béo</div></div>
    </div>
  </div>
  <div class="card">
    <h2>Bữa trưa · 450 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Cơm lứt</div><div class="hint">1/2 bát</div></div>
      <div style="text-align:right"><div style="font-weight:700">150 kcal</div><div class="hint">Tinh bột</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Ức gà áp chảo</div><div class="hint">150g</div></div>
      <div style="text-align:right"><div style="font-weight:700">250 kcal</div><div class="hint">30g đạm</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0">
      <span style="color:var(--accent)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Canh rau</div><div class="hint">1 bát</div></div>
      <div style="text-align:right"><div style="font-weight:700">50 kcal</div><div class="hint">Rau/xơ</div></div>
    </div>
  </div>
  <div class="card subtle">
    <div class="hint">Lưu ý: Ăn ngược (đạm → rau → tinh bột), nhai kỹ, ăn chậm.</div>
  </div>
</div>
{cta('Hoàn thành', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-CONS-07_bua_an.html'), 'w', encoding='utf-8').write(html('Gợi ý bữa ăn — AnCare', body))

# 12. Talking point
body = f'''
{appbar('Talking point', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">KH tiềm năng</div>
    <div class="title" style="font-size:var(--text-xl)">Testkhtn01</div>
  </div>
  <div class="card">
    <h2>Bối cảnh & cảm xúc</h2>
    <div class="card subtle" style="margin-bottom:0">
      <div class="hint">Đang "ấm". Vừa xem video 21 ngày. Cần đề cập tiến độ trước đó, tránh gây áp lực.</div>
    </div>
  </div>
  <div class="card">
    <h2>Điểm chạm hôm nay</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('check')}</span>
      <div class="flex-1"><div style="font-weight:600">Hỏi thăm kết quả uống nước 2 ngày qua</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('check')}</span>
      <div class="flex-1"><div style="font-weight:600">Gợi ý đặt lịch Tanita miễn phí</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent)">{icon('check')}</span>
      <div class="flex-1"><div style="font-weight:600">Chia sẻ case study giảm 5kg của HLV</div></div>
    </div>
  </div>
  <div class="card">
    <h2>Tránh</h2>
    <div class="card subtle" style="margin-bottom:0">
      <div class="hint">Không đề cập giá trước khi KH hiểu rõ giá trị. Không nhắn quá 2 tin liên tiếp.</div>
    </div>
  </div>
</div>
{cta('Đã gọi điện xong', icon_name='phone')}
'''
open(os.path.join(out_dir, 'S-CARE-01_talking_point.html'), 'w', encoding='utf-8').write(html('Talking point — AnCare', body))

# 13. Adjust meal
body = f'''
{appbar('Điều chỉnh bữa ăn', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card customer" style="margin-bottom:var(--s-16)">
    <div class="label">Phạm Hạnh</div>
    <div class="title" style="font-size:var(--text-xl)">Bữa tối · 390 kcal</div>
  </div>
  <div class="card">
    <h2>Thay đổi món</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div class="flex-1">
        <div style="font-weight:600">Cá hấp</div>
        <div class="hint">150g · 200 kcal · 25g đạm</div>
      </div>
      <button class="btn ghost">Thay</button>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <div class="flex-1">
        <div style="font-weight:600">Cơm lứt</div>
        <div class="hint">1/2 bát · 130 kcal</div>
      </div>
      <button class="btn ghost">Thay</button>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <div class="flex-1">
        <div style="font-weight:600">Rau luộc</div>
        <div class="hint">1 đĩa · 60 kcal</div>
      </div>
      <button class="btn ghost">Thay</button>
    </div>
  </div>
  <div class="card">
    <h2>Gợi ý thay thế</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent-customer)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Ức gà luộc</div><div class="hint">150g · 220 kcal · 28g đạm</div></div>
      <button class="pill active" style="border-color:var(--accent-customer);background:var(--accent-customer);color:#fff">Chọn</button>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent-customer)">{icon('utensils')}</span>
      <div class="flex-1"><div style="font-weight:600">Đậu phụ rim</div><div class="hint">150g · 180 kcal · 15g đạm</div></div>
      <button class="pill">Chọn</button>
    </div>
  </div>
</div>
{cta('Lưu thay đổi', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-CARE-03_dieu_chinh_bua_an.html'), 'w', encoding='utf-8').write(html('Điều chỉnh bữa ăn — AnCare', body))

# 14. 72h reminder
body = f'''
{appbar('Nhắc 72h', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">KH kém quan tâm</div>
    <div class="title" style="font-size:var(--text-xl)">Testkhtn02 · 72h không check-in</div>
  </div>
  <div class="card">
    <h2>Mẫu tin nhắn gợi ý</h2>
    <div class="card subtle" style="margin-bottom:var(--s-12)">
      <div class="hint" style="line-height:1.7">"Chào Hạnh, mình thấy bạn 3 ngày nay chưa check-in. Có khó khăn gì trong việc uống nước hoặc bữa ăn không? Mình sẵn sàng hỗ trợ nhé."</div>
    </div>
    <button class="btn secondary block" style="margin-bottom:var(--s-12)">{icon('message', 'sm')} Sao chép nội dung</button>
    <div class="hint">Tùy chỉnh theo phong cách HLV, gửi qua Zalo/SMS.</div>
  </div>
  <div class="card">
    <h2>Bước tiếp đề xuất</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('phone')}</span>
      <div class="flex-1"><div style="font-weight:600">Gọi điện 2-1</div><div class="hint">Ưu tiên cao nhất</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)">
      <span style="color:var(--accent)">{icon('message')}</span>
      <div class="flex-1"><div style="font-weight:600">Nhắn Zalo</div><div class="hint">Nếu KH không nghe máy</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0">
      <span style="color:var(--accent)">{icon('calendar')}</span>
      <div class="flex-1"><div style="font-weight:600">Hẹn gặp trực tiếp</div><div class="hint">Nếu 24h vẫn chưa phản hồi</div></div>
    </div>
  </div>
</div>
{cta('Đã nhắn', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-CARE-09_nhac_72h.html'), 'w', encoding='utf-8').write(html('Nhắc 72h — AnCare', body))

# 15. Microcourse
body = f'''
{appbar('Micro-course', back=True, info=True)}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)">
    <div class="label">Bài học 3 phút</div>
    <div class="title" style="font-size:var(--text-xl)">Nước & trao đổi chất</div>
  </div>
  <div class="card" style="padding:0;overflow:hidden">
    <div style="height:180px;background:linear-gradient(135deg,var(--accent),var(--accent-hover));display:flex;align-items:center;justify-content:center;color:#fff">
      <div style="text-align:center">{icon('water', 'lg')}<div style="margin-top:var(--s-12);font-weight:700">▶ Phát video</div></div>
    </div>
  </div>
  <div class="card">
    <h2>Nội dung chính</h2>
    <div class="card subtle">
      <div class="hint" style="line-height:1.7">1. Vai trò của nước trong trao đổi chất.<br>2. Dấu hiệu cơ thể thiếu nước.<br>3. Công thức uống nước cá nhân hóa.</div>
    </div>
  </div>
  <div class="card">
    <h2>3 câu kiểm tra</h2>
    <div class="field" style="margin-bottom:var(--s-12)"><label>Điều gì xảy ra khi thiếu nước?</label><textarea style="min-height:60px"></textarea></div>
    <div class="field" style="margin-bottom:var(--s-12)"><label>Bạn sẽ áp dụng như thế nào?</label><textarea style="min-height:60px"></textarea></div>
    <div class="field"><label>Bạn sẽ chia sẻ với ai?</label><textarea style="min-height:60px"></textarea></div>
  </div>
</div>
{cta('Gửi kết quả', icon_name='check')}
'''
open(os.path.join(out_dir, 'S-DEV-01_microcourse.html'), 'w', encoding='utf-8').write(html('Micro-course — AnCare', body))

print('Batch 2 generated: 7 files')
for f in ['S-CONS-06_chot_goi.html','S-CONS-08_tao_tk.html','S-CONS-07_bua_an.html','S-CARE-01_talking_point.html','S-CARE-03_dieu_chinh_bua_an.html','S-CARE-09_nhac_72h.html','S-DEV-01_microcourse.html']:
    print('  ', f)
