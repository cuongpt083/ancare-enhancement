import os
ICONS={'chevron-left':'<path d="M15 6l-6 6 6 6"/>','chevron-right':'<path d="M9 6l6 6-6 6"/>','info':'<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="8.01"/><line x1="12" y1="12" x2="12" y2="16"/>','bell':'<path d="M10 5a2 2 0 0 1 4 0 7 7 0 0 1 4 6v3a4 4 0 0 0 1 2H5a4 4 0 0 0 1-2v-3a7 7 0 0 1 4-6M9 17v1a3 3 0 0 0 6 0v-1"/>','user':'<path d="M12 12a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM5 20a7 7 0 0 1 14 0"/>','home':'<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>','chart':'<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>','book':'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>','check':'<polyline points="20 6 9 17 4 12"/>','camera':'<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>','utensils':'<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>','water':'<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>','moon':'<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>','run':'<path d="M4 15l3-3 2 2 2.5-3L14 12l2-2 3 4-3 2-1-1-2 3-4-2z"/><circle cx="17" cy="4" r="2"/>','sun':'<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>','trending-up':'<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>','trending-down':'<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>','scale':'<path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L2.5 7.5"/>','heart':'<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>','clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>','plus':'<path d="M12 5v14M5 12h14"/>','minus':'<path d="M5 12h14"/>','image':'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>','alert':'<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>','target':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>','activity':'<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'}
def ic(n,s='md'):
 c={'sm':'icon-sm','md':'icon','lg':'icon-lg'}.get(s,'icon')
 return f'<svg class="{c}" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(n,"")}</svg>'
def appbar(t,back=True,info=True):
 b=f'<span class="back">{ic("chevron-left")}</span>' if back else '<span class="back" style="opacity:0">'+ic('chevron-left')+'</span>'
 i=f'<span class="info">{ic("info")}</span>' if info else '<span class="info" style="opacity:0">'+ic('info')+'</span>'
 return f'<div class="appbar">{b}<h1>{t}</h1>{i}</div>'
def cta(p,s=None,pn=None):
 ss=f'<button class="btn secondary">{s}</button>' if s else ''
 pi=ic(pn) if pn else ''
 return f'<div class="cta-bar">{ss}<button class="btn primary customer">{pi}{p}</button></div>'
def bnav(active):
 items=[('home','Trang chủ','home'),('report','Báo cáo','chart'),('learn','Đào tạo','book'),('profile','Hồ sơ','user')]
 out='<div class="bottom-nav">'
 for n,l,inm in items:
  cls='nav-item active' if active==n else 'nav-item'
  out+=f'<div class="{cls}"><span class="icon">{ic(inm)}</span><span>{l}</span></div>'
 return out+'</div>'
def page(t,body,extra=''):
 return f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link rel="stylesheet" href="../_assets/_tokens.css"><link rel="stylesheet" href="../_assets/_base.css">
<style>:root{{--accent:var(--accent-customer);--accent-hover:var(--accent-customer-hover)}}</style>{extra}</head><body><div class="screen">{body}</div></body></html>'''
D='/Users/cuongpt/Workspaces/ancare-enhancement/docs/03-mockups/customer'

# === HLTH-02: check-in 5 mục mới, bảng 4 cột mới, line-chart 3 ngày, mục tiêu, phân tích chuyên sâu ===
body=f'''
<div class="appbar" style="border:none;background:linear-gradient(135deg,var(--accent-customer),var(--accent-customer-hover));color:#fff">
  <span class="back" style="opacity:0">{ic('chevron-left')}</span>
  <div class="flex-1 flex items-center gap-12">
    <div style="width:44px;height:44px;border-radius:var(--radius-full);background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;border:2px solid rgba(255,255,255,.4)">{ic('user')}</div>
    <div><div style="font-weight:700;font-size:var(--text-lg)">Xin chào, Hạnh</div><div style="font-size:var(--text-sm);opacity:.9">Cơ-Nước-Mỡ · Tối ưu · còn 8 ngày</div></div>
  </div>
  <span class="info" style="color:#fff">{ic('bell')}</span>
</div>
<div class="content" style="padding-top:var(--s-12)">
  <div class="card" style="border-color:var(--accent-customer);background:linear-gradient(135deg,#f0fdfa,#e6f7f5)">
    <div class="flex justify-between items-center" style="margin-bottom:var(--s-12)"><h2 style="margin:0">Check-in hôm nay</h2><a href="S-HLTH-06_check_in.html" style="font-size:var(--text-sm);color:var(--accent-customer);font-weight:600;text-decoration:none">Mở Check-in →</a></div>
    <div class="hint" style="margin-bottom:var(--s-8)">1/5 mục đã ghi</div>
    <div class="flex" style="gap:var(--s-8);overflow-x:auto;padding-bottom:var(--s-8)">
      <div class="pill" style="border-color:var(--accent-customer);background:var(--accent-customer);color:#fff;height:36px">{ic('check','sm')} Ăn</div>
      <div class="pill" style="height:36px">Uống</div>
      <div class="pill" style="height:36px">Ngủ</div>
      <div class="pill" style="height:36px">Vận động</div>
      <div class="pill" style="height:36px">Học TKP</div>
    </div>
  </div>
  <div class="card"><h2>Đồng hồ sinh học 24h</h2>
    <div style="display:flex;justify-content:space-around;padding:var(--s-12) 0">
      <div style="text-align:center"><div style="width:56px;height:56px;border-radius:var(--radius-full);background:var(--state-good-bg);display:flex;align-items:center;justify-content:center;margin:0 auto var(--s-4)"><span style="color:var(--state-good);font-weight:700;font-size:var(--text-lg)">7</span></div><div class="hint">Dinh dưỡng</div></div>
      <div style="text-align:center"><div style="width:56px;height:56px;border-radius:var(--radius-full);background:var(--state-warn-bg);display:flex;align-items:center;justify-content:center;margin:0 auto var(--s-4)"><span style="color:var(--state-warn);font-weight:700;font-size:var(--text-lg)">5</span></div><div class="hint">Vận động</div></div>
      <div style="text-align:center"><div style="width:56px;height:56px;border-radius:var(--radius-full);background:var(--state-alert-bg);display:flex;align-items:center;justify-content:center;margin:0 auto var(--s-4)"><span style="color:var(--state-alert);font-weight:700;font-size:var(--text-lg)">3</span></div><div class="hint">TKP</div></div>
    </div>
  </div>
  <div class="card"><h2>Mục tiêu của bạn</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <span style="color:var(--accent-customer)">{ic('target')}</span>
      <div class="flex-1"><div style="font-weight:600">Giảm cân · 62 kg</div><div class="hint">Ngày 3/90 buổi trải nghiệm</div></div>
      <div style="text-align:right"><div style="font-weight:700;color:var(--accent-customer)">55.2 kg</div><div class="hint">hiện tại</div></div>
    </div>
  </div>
  <div class="card"><h2>Chỉ số cơ thể</h2>
    <div class="table-wrap" style="margin-bottom:0"><table class="table">
      <thead><tr><th>Chỉ số</th><th>Tiêu chuẩn</th><th>Mục tiêu</th><th>Hiện tại</th><th>Đánh giá</th></tr></thead><tbody>
        <tr class="good"><td>Cân nặng</td><td>62</td><td>62</td><td>55.2</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Khối lượng cơ</td><td>≥38%</td><td>52</td><td>52.5</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Khối lượng xương</td><td>2.5-3.5</td><td>2.8</td><td>2.8</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Tỷ lệ nước</td><td>&gt;50%</td><td>55</td><td>58.1</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="warn"><td>Tỷ lệ mỡ</td><td>17.5%</td><td>17.5</td><td>17.8</td><td><span class="chip warn">Thừa 0.3%</span></td></tr>
        <tr class="good"><td>Mỡ nội tạng</td><td>1-7</td><td>7</td><td>8</td><td><span class="chip warn">Cần cải thiện</span></td></tr>
        <tr class="good"><td>Vóc dáng</td><td>—</td><td>—</td><td>BT</td><td><span class="chip good">Tốt</span></td></tr>
        <tr class="good"><td>Tuổi sinh học</td><td>≤42</td><td>42</td><td>36</td><td><span class="chip good">Trẻ 6t</span></td></tr>
        <tr class="good"><td>RMR</td><td>—</td><td>—</td><td>1280</td><td><span class="chip good">Tốt</span></td></tr>
      </tbody>
    </table></div>
  </div>
  <div class="card"><h2>Tiến trình 3 ngày gần nhất</h2>
    <div style="height:80px;padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)">
      <svg viewBox="0 0 300 60" width="100%" height="60" preserveAspectRatio="none"><polyline points="0,40 100,28 200,18 300,10" fill="none" stroke="var(--accent-customer)" stroke-width="2.5" stroke-linejoin="round"/><polyline points="0,40 100,28 200,18 300,10 300,60 0,60" fill="rgba(20,158,110,.12)" stroke="none"/><text x="5" y="55" font-size="9" fill="var(--text-muted)">30/6</text><text x="100" y="55" font-size="9" fill="var(--text-muted)">01/7</text><text x="200" y="55" font-size="9" fill="var(--text-muted)">02/7</text></svg>
    </div>
  </div>
  <div class="card"><h2>Phân tích chuyên sâu & lời khuyên</h2>
    <div style="display:flex;flex-direction:column;gap:var(--s-12)">
      <div class="card subtle" style="margin:0"><div style="font-weight:600;margin-bottom:var(--s-4)">Đánh giá tiến trình chuyển hóa</div><div class="hint" style="line-height:1.6">Cân nặng giảm tốt (55.2 kg). Mỡ nội tạng còn 8 (cần ≤7). Bữa trưa lệch giờ gây tăng đường huyết chiều. Ngủ trễ ảnh hưởng trao đổi chất.</div></div>
      <div class="card subtle" style="margin:0"><div style="font-weight:600;margin-bottom:var(--s-4)">Giải pháp</div><div class="hint" style="line-height:1.6">• Tăng đạm bữa trưa (thêm ức gà 50g)<br>• Tối ưu nước: 2.5L/ngày (dung môi chuyển hóa)<br>• Giải pháp mỡ nội tạng: Omega-3 + vận động 30 phút</div></div>
    </div>
  </div>
</div>
{bnav('home')}'''
open(f'{D}/S-HLTH-02_trang_chu.html','w',encoding='utf-8').write(page('Trang chủ — AnCare KH',body))
print('HLTH-02 OK')

# === HLTH-06: Chạm để cập nhật, con số kỳ diệu, 6 bữa, AI chi tiết ===
body=f'''
{appbar('Check-in hôm nay')}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card"><h2>Chỉ số cơ thể</h2>
    <div class="table-wrap" style="margin-bottom:var(--s-12)"><table class="table">
      <thead><tr><th>Chỉ số</th><th>Giá trị</th><th>Đơn vị</th></tr></thead><tbody>
        <tr><td>Cân nặng</td><td>55.2</td><td>kg</td></tr><tr><td>Mỡ cơ thể</td><td>17.8</td><td>%</td></tr><tr><td>Mỡ nội tạng</td><td>8</td><td>%</td></tr><tr><td>Cơ bắp</td><td>52.5</td><td>kg</td></tr><tr><td>Xương</td><td>2.8</td><td>kg</td></tr><tr><td>Nước</td><td>58.1</td><td>%</td></tr><tr><td>Tuổi sinh học</td><td>36</td><td>tuổi</td></tr><tr><td>RMR</td><td>1280</td><td>kcal</td></tr>
      </tbody>
    </table></div>
    <button class="btn ghost" style="width:100%">Chạm để cập nhật chỉ số</button>
  </div>
  <div class="card" style="border-color:var(--accent-customer)"><h2 style="color:var(--accent-customer)">Con số kỳ diệu</h2>
    <div class="flex items-center justify-between">
      <div><div style="font-size:var(--text-2xl);font-weight:700;color:var(--accent-customer)">1.359</div><div class="hint">kcal/ngày</div></div>
      <span style="color:var(--accent-customer)">{ic('target','lg')}</span>
    </div>
  </div>
  <div class="card"><h2>Gợi ý bữa ăn hôm nay</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('sun')}</span><div class="flex-1"><div style="font-weight:600">Bữa sáng · 320 kcal</div><div class="hint">Đạm 24g · Bột 32g · Béo 11g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--state-good)">{ic('check')}</span></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Ăn nhẹ buổi sáng · 150 kcal</div><div class="hint">Đạm 11g · Bột 15g · Béo 5g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--text-muted)">{ic('check')}</span></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Bữa trưa · 450 kcal</div><div class="hint">Đạm 30g · Bột 40g · Béo 13g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--text-muted)">{ic('check')}</span></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('sun')}</span><div class="flex-1"><div style="font-weight:600">Ăn nhẹ buổi chiều · 150 kcal</div><div class="hint">Đạm 11g · Bột 15g · Béo 5g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--text-muted)">{ic('check')}</span></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('moon')}</span><div class="flex-1"><div style="font-weight:600">Bữa tối · 390 kcal</div><div class="hint">Đạm 29g · Bột 39g · Béo 13g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--text-muted)">{ic('check')}</span></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0"><span style="color:var(--accent-customer)">{ic('moon')}</span><div class="flex-1"><div style="font-weight:600">Ăn nhẹ buổi tối · 100 kcal</div><div class="hint">Đạm 7g · Bột 10g · Béo 3g</div></div><button class="pill" style="height:32px;border-color:var(--accent-customer);color:var(--accent-customer)">{ic('camera','sm')}</button><span style="color:var(--text-muted)">{ic('check')}</span></div>
  </div>
  <div class="card" style="border-color:var(--accent-customer)"><h2 style="color:var(--accent-customer)">AI đánh giá bữa sáng</h2>
    <div style="display:flex;gap:var(--s-12);margin-bottom:var(--s-12)"><div style="width:64px;height:64px;border-radius:var(--radius-md);background:var(--bg-subtle);display:flex;align-items:center;justify-content:center;color:var(--accent-customer)">{ic('image')}</div><div class="flex-1"><div class="hint">Năng lượng · Đường bột · Đạm · Chất béo tốt</div></div></div>
    <div class="table-wrap" style="margin-bottom:var(--s-12)"><table class="table">
      <thead><tr><th>Thành phần</th><th>AI ước tính</th><th>Tiêu chuẩn</th><th>Đánh giá</th></tr></thead><tbody>
        <tr class="good"><td>Năng lượng</td><td>310 kcal</td><td>320</td><td><span class="chip good">Đạt</span></td></tr>
        <tr class="warn"><td>Đạm</td><td>18g</td><td>24g</td><td><span class="chip warn">Thiếu 6g</span></td></tr>
        <tr class="good"><td>Đường bột</td><td>35g</td><td>32g</td><td><span class="chip warn">Thừa 3g</span></td></tr>
        <tr class="good"><td>Chất béo tốt</td><td>10g</td><td>11g</td><td><span class="chip good">Đạt</span></td></tr>
      </tbody>
    </table></div>
    <div class="card subtle" style="margin:0"><div class="hint">Nhận xét: Bữa sáng thiếu đạm, nên thêm 1 quả trứng hoặc 1 muỗng PPP.</div></div>
  </div>
  <div class="card"><h2>Hoạt động dinh dưỡng & thể chất</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('water')}</span><div class="flex-1"><div style="font-weight:600">Uống nước</div><div class="hint">8 cốc × 200ml = 1.6L</div></div><div class="flex items-center gap-8"><button class="btn secondary" style="height:32px;width:32px;padding:0">{ic('minus','sm')}</button><span style="font-weight:700">8</span><button class="btn secondary" style="height:32px;width:32px;padding:0">{ic('plus','sm')}</button></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('moon')}</span><div class="flex-1"><div style="font-weight:600">Giấc ngủ</div><div class="hint">7 giờ · 23:00 → 06:00</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0"><span style="color:var(--accent-customer)">{ic('run')}</span><div class="flex-1"><div style="font-weight:600">Vận động</div><div class="hint">Pickleball 60 phút · ~360 kcal</div></div><button class="pill" style="border-color:var(--accent-customer);color:var(--accent-customer)">+ Thêm</button></div>
  </div>
  <div class="card"><h2>Kiến thức TKP</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent-customer)">{ic('book')}</span><div class="flex-1"><div style="font-weight:600">Bài 3 · Bột đường & năng lượng</div><div class="hint">3 phút · 3 câu hỏi sau học</div></div></div>
    <button class="btn primary customer block">{ic('book','sm')} Xem bài học</button>
  </div>
</div>
{cta('Hoàn thành check-in',pn='check')}'''
open(f'{D}/S-HLTH-06_check_in.html','w',encoding='utf-8').write(page('Check-in — AnCare KH',body))
print('HLTH-06 OK')
print('KH batch done: 2 files')
