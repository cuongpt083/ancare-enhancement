import os
ICONS={'chevron-left':'<path d="M15 6l-6 6 6 6"/>','chevron-right':'<path d="M9 6l6 6-6 6"/>','info':'<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="8.01"/><line x1="12" y1="12" x2="12" y2="16"/>','check':'<polyline points="20 6 9 17 4 12"/>','camera':'<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>','utensils':'<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>','scale':'<path d="M12 2a10 10 0 1 0 10 10H12V2z"/><path d="M12 2a10 10 0 0 1 10 10"/><path d="M12 12L2.5 7.5"/>','water':'<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>','alert':'<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>','heart':'<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>','book':'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>','image':'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>','user':'<path d="M12 12a4 4 0 1 0 0-8 4 4 0 1 0 0 8zM5 20a7 7 0 0 1 14 0"/>','mail':'<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>','map-pin':'<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>','clock':'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'}
def ic(n,s='md'):
 c={'sm':'icon-sm','md':'icon','lg':'icon-lg'}.get(s,'icon')
 return f'<svg class="{c}" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(n,"")}</svg>'
def appbar(t,back=True,info=True):
 b=f'<span class="back">{ic("chevron-left")}</span>' if back else '<span class="back" style="opacity:0">'+ic('chevron-left')+'</span>'
 i=f'<span class="info">{ic("info")}</span>' if info else '<span class="info" style="opacity:0">'+ic('info')+'</span>'
 return f'<div class="appbar">{b}<h1>{t}</h1>{i}</div>'
def dots(step,total=4):
 return ''.join(f'<span class="dot {"active" if i==step-1 else ("done" if i<step-1 else "")}"></span>' for i in range(total))
def cta(p,s=None,pn=None):
 ss=f'<button class="btn secondary">{s}</button>' if s else ''
 pi=ic(pn) if pn else ''
 return f'<div class="cta-bar">{ss}<button class="btn primary">{pi}{p}</button></div>'
def page(t,body,extra=''):
 return f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link rel="stylesheet" href="../_assets/_tokens.css"><link rel="stylesheet" href="../_assets/_base.css">{extra}</head><body><div class="screen">{body}</div></body></html>'''
D='/Users/cuongpt/Workspaces/ancare-enhancement/docs/03-mockups/coach'

# === CONS-02 + LEAD-02: 16 new questions, remove cân nặng, add địa chỉ + SĐT người mời ===
QUESTIONS='''<strong>1.</strong> Bạn muốn chúng tôi giúp bạn điều gì về sức khỏe? &nbsp;<strong>2.</strong> Lâu nay có đi khám bác sĩ không? &nbsp;<strong>3.</strong> Bác sĩ có khuyên giảm cân hoặc giảm mỡ máu? &nbsp;<strong>4.</strong> Thường ăn gì vào bữa sáng? &nbsp;<strong>5.</strong> Mệt mỏi/dễ cảm? &nbsp;<strong>6.</strong> Đau đầu, đau lưng, đau mỏi? &nbsp;<strong>7.</strong> Có tiểu đường, huyết áp, tim mạch, khớp? &nbsp;<strong>8.</strong> Công việc/gia đình có áp lực? &nbsp;<strong>9.</strong> Giấc ngủ tốt không? &nbsp;<strong>10.</strong> Hay đói hoặc thèm ăn? &nbsp;<strong>11.</strong> Thường ăn đồ chế biến sẵn? &nbsp;<strong>12.</strong> Có nghĩ thức ăn ảnh hưởng sức khỏe? &nbsp;<strong>13.</strong> Mỗi ngày uống khoảng bao nhiêu cốc nước? &nbsp;<strong>14.</strong> Có tập thể dục không? &nbsp;<strong>15.</strong> Có hút thuốc hoặc tiếp xúc khói thuốc? &nbsp;<strong>16.</strong> Có thường uống rượu, bia hoặc cà phê?'''
def portrait_body(with_dots):
 return f'''
{appbar('Chân dung KH' if with_dots else 'Thêm mới KH')}
{f'<div class="progress-dots">{dots(2)}</div>' if with_dots else ''}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card"><h2>Thông tin cơ bản</h2>
    <div class="field"><label>Người mời</label><input value="Thủy (HLV)"></div>
    <div class="field"><label>SĐT người mời</label><input placeholder="SĐT (tùy chọn)"></div>
    <div class="field"><label>Họ và tên KH <span style="color:var(--state-alert)">*</span></label><input placeholder="Họ và tên"></div>
    <div class="flex gap-12"><div class="field flex-1"><label>Số điện thoại</label><input placeholder="SĐT"></div><div class="field flex-1"><label>Email</label><input placeholder="Email"></div></div>
    <div class="flex gap-12"><div class="field flex-1"><label>Ngày sinh</label><input placeholder="dd/mm/yyyy"></div><div class="field flex-1"><label>Giới tính</label><input value="Nam"></div></div>
    <div class="flex gap-12"><div class="field flex-1"><label>Chiều cao (cm)</label><input placeholder="170"></div><div class="field flex-1"><label>Địa chỉ</label><input placeholder="Địa chỉ"></div></div>
  </div>
  <div class="card"><h2>Chân dung Khách hàng</h2>
    <div class="card subtle" style="margin-bottom:var(--s-12)"><div style="font-size:var(--text-sm);line-height:1.7;color:var(--text-secondary)">{QUESTIONS}</div></div>
    <div class="field"><label>Trả lời (HLV nhập gộp)</label><textarea placeholder="Tóm tắt câu trả lời, tập trung kết quả KH mong muốn..."></textarea></div>
  </div>
</div>
{cta('Lưu → Khảo sát Tanita' if with_dots else 'Lưu KH',pn='check')}'''
open(f'{D}/S-CONS-02_chan_dung_kh.html','w',encoding='utf-8').write(page('Chân dung KH — AnCare',portrait_body(True)))
open(f'{D}/S-LEAD-02_tao_lead.html','w',encoding='utf-8').write(page('Thêm mới KH — AnCare',portrait_body(False)))
print('CONS-02 + LEAD-02 OK')

# === CONS-04: remove Cần± column (3 cols: Hiện tại, Tiêu chuẩn, Đánh giá) ===
body=f'''
{appbar('Phân tích kết quả')}
<div class="progress-dots">{dots(4)}</div>
<div class="content" style="padding-top:var(--s-12)">
  <div class="table-wrap"><table class="table">
    <thead><tr><th>Chỉ số</th><th>Hiện tại</th><th>Tiêu chuẩn</th><th>Đánh giá</th></tr></thead><tbody>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Cân nặng <span style="color:var(--accent);font-size:var(--text-xs);font-weight:600">(quan trọng)</span></td><td>64.8 kg</td><td>62</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Cân nặng cho biết tổng khối lượng cơ thể, cơ sở tính BMI, nhu cầu calo và nước.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Thừa cân kéo dài tăng nguy cơ tim mạch, tiểu đường type 2, thoái hóa khớp.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Khối lượng cơ <span style="color:var(--accent);font-size:var(--text-xs);font-weight:600">(quan trọng)</span></td><td>52.0 kg</td><td>≥38%</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Cơ bắp giúp đốt cháy năng lượng, ổn định đường huyết, hỗ trợ khớp.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Mất cơ (sarcopenia) giảm trao đổi chất, dễ tích mỡ, tăng nguy cơ ngã/gãy xương.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Tỷ lệ nước <span style="color:var(--accent);font-size:var(--text-xs);font-weight:600">(quan trọng)</span></td><td>57.7%</td><td>&gt;50%</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Nước tham gia trao đổi chất, vận chuyển dinh dưỡng, điều hòa nhiệt.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Thiếu nước làm máu đặc, tăng huyết áp, táo bón, mệt mỏi, ảnh hưởng thận.</td></tr></table></div></td></tr>
      <tr class="warn clickable" onclick="toggleRow(this)"><td>Tỷ lệ mỡ <span style="color:var(--accent);font-size:var(--text-xs);font-weight:600">(quan trọng)</span></td><td>18.9%</td><td>17.5%</td><td><span class="chip warn">Thừa 1.4%</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Tỷ lệ mỡ cơ thể quan trọng hơn cân nặng đơn thuần.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Mỡ thừa tăng nguy cơ tim mạch, tiểu đường, huyết áp, gan nhiễm mỡ.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Tuổi sinh học <span style="color:var(--accent);font-size:var(--text-xs);font-weight:600">(quan trọng)</span></td><td>37</td><td>≤42</td><td><span class="chip good">Trẻ 5t</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Tuổi sinh học phản ánh mức lão hóa thực tế dựa trên cơ/mỡ/nước.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Cao hơn tuổi thật = cơ thể lão hóa nhanh do thói quen không lành mạnh.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Khối lượng xương</td><td>2.8 kg</td><td>2.5-3.5</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Đánh giá khối lượng xương, liên quan sức mạnh và loãng xương.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Xương thấp tăng nguy cơ loãng xương, gãy xương, đặc biệt phụ nữ mãn kinh.</td></tr></table></div></td></tr>
      <tr class="alert clickable" onclick="toggleRow(this)"><td>Mỡ nội tạng</td><td>10</td><td>1-7</td><td><span class="chip alert">Nguy hiểm</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Mỡ nội tạng bao quanh cơ quan ổ bụng, không sờ thấy nhưng nguy hiểm nhất.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Nguyên nhân chính gây tiểu đường, tim mạch, huyết áp, gan nhiễm mỡ, đột quỵ.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>Vóc dáng</td><td>Bình thường</td><td>—</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Đánh giá tỷ lệ cơ/mỡ so với chiều cao.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>Vóc dáng kém thường đi kèm mỡ nội tạng cao hoặc mất cơ.</td></tr></table></div></td></tr>
      <tr class="good clickable" onclick="toggleRow(this)"><td>RMR</td><td>1276</td><td>—</td><td><span class="chip good">Tốt</span></td></tr>
      <tr class="detail"><td colspan="4"><div class="detail-inner"><table class="detail-table"><tr><th>Ý nghĩa</th><td>Resting Metabolic Rate: calo cần khi nghỉ ngơi.</td></tr><tr><th>Nguy cơ bệnh lý</th><td>RMR thấp do mất cơ giảm khả năng đốt mỡ, dễ tăng cân lại.</td></tr></table></div></td></tr>
    </tbody></table></div>
  <div class="hint text-center" style="margin-bottom:var(--s-16)">Bấm từng dòng để xem ý nghĩa chỉ số & rủi ro bệnh lý</div>
  <div class="card"><h2>Chốt mục tiêu</h2>
    <div class="pills" style="margin-bottom:var(--s-12)"><span class="pill active">{ic('check','sm')} Giảm cân</span><span class="pill">Tăng cân</span><span class="pill">Giữ cân</span></div>
    <div class="focus-card" style="margin-bottom:0"><div class="label">Chương trình đề xuất</div><div class="title" style="font-size:var(--text-xl)">Cân bằng Cơ — Nước — Mỡ</div></div>
  </div>
  <div class="card subtle"><div class="flex items-center gap-12"><span style="color:var(--state-warn)">{ic('alert')}</span><span class="hint" style="margin:0">Không có gì là thần dược; để có kết quả cần kiến thức dinh dưỡng, kỷ luật bản thân, hiểu nguyên lý để không phụ thuộc vào HLV hoặc sản phẩm.</span></div></div>
</div>
{cta('Xem lộ trình',s='Đóng',pn='chevron-right')}'''
extra='<style>.table tr.clickable{cursor:pointer}.table tr.clickable:hover td{background:var(--bg-subtle)}.table tr.detail td{padding:0;background:var(--bg-subtle)}.table .detail-inner{display:none;padding:var(--s-12)}.table tr.expanded+.detail td .detail-inner{display:block}.table tr.expanded td{background:var(--accent-subtle)}.detail-table{width:100%;border-collapse:collapse;font-size:var(--text-sm)}.detail-table th{text-align:left;color:var(--text-muted);font-weight:600;padding:6px 0;background:transparent}.detail-table td{text-align:left;padding:6px 0;border:none;background:transparent}</style><script>function toggleRow(r){r.classList.toggle("expanded")}</script>'
open(f'{D}/S-CONS-04_phan_tich.html','w',encoding='utf-8').write(page('Phân tích kết quả — AnCare',body,extra))
print('CONS-04 OK')

# === CONS-05: 5 lợi ích, 5 kết quả, 1/2/3 tháng chọn, gói dịch vụ sử dụng ===
body=f'''
{appbar('Xem lộ trình')}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)"><div class="label">Chương trình Cơ — Nước — Mỡ</div><div class="title" style="font-size:var(--text-xl)">Giảm đúng mỡ thừa · giữ cơ + nước</div></div>
  <div class="card"><h2>Lợi ích chương trình</h2><div style="display:flex;flex-direction:column;gap:var(--s-8)">
    <div class="flex items-center gap-12"><span style="color:var(--state-good)">{ic('check')}</span><span>Làm sạch hệ tiêu hoá; giảm mỡ xấu</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--state-good)">{ic('check')}</span><span>Chuyển giao 21 chủ đề DD & chuyên đề chuyên sâu</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--state-good)">{ic('check')}</span><span>Biết cách chăm sóc da đúng cách</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--state-good)">{ic('check')}</span><span>HLV chăm sóc 1-1 và giao lưu hội viên</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--state-good)">{ic('check')}</span><span>App chăm sóc sức khoẻ chuyên nghiệp, đồng hành hàng ngày</span></div>
  </div></div>
  <div class="card"><h2>Kết quả đạt được</h2><div style="display:flex;flex-direction:column;gap:var(--s-8)">
    <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('check')}</span><span>Thay đổi thói quen</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('check')}</span><span>Tăng cường sức khoẻ</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('check')}</span><span>Tăng cơ, giảm mỡ xấu</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('check')}</span><span>Làn da tươi trẻ</span></div>
    <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('check')}</span><span>Có kiến thức chăm sóc sức khoẻ trọn đời</span></div>
  </div></div>
  <div class="card"><h2>Lộ trình</h2>
    <div class="pills" style="margin-bottom:var(--s-12)"><span class="pill">1 tháng</span><span class="pill">2 tháng</span><span class="pill active">3 tháng (Tốt nhất)</span></div>
    <div style="display:flex;flex-direction:column;gap:var(--s-12)">
      <div class="flex gap-12"><div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">1</div><div class="flex-1"><div style="font-weight:700">Tháng 1</div><div class="hint">Điều chỉnh cân nặng, trang bị kiến thức cơ bản thay đổi tư duy dinh dưỡng & thể chất.</div></div></div>
      <div class="flex gap-12"><div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">2</div><div class="flex-1"><div style="font-weight:700">Tháng 2</div><div class="hint">Tăng cơ, tăng cường sức khỏe, điều chỉnh các thói quen không lành mạnh.</div></div></div>
      <div class="flex gap-12"><div style="width:32px;height:32px;border-radius:var(--radius-full);background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">3</div><div class="flex-1"><div style="font-weight:700">Tháng 3</div><div class="hint">Tối ưu hóa vóc dáng, trẻ hóa, duy trì năng lượng, xây dựng thói quen lành mạnh bền vững.</div></div></div>
    </div>
  </div>
  <div class="card"><h2>Gói dịch vụ sử dụng</h2>
    <div class="flex justify-between" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span class="hint">Gói</span><span style="font-weight:600">Cơ-Nước-Mỡ · Tối ưu</span></div>
    <div class="flex justify-between" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span class="hint">Thời gian</span><span style="font-weight:600">3 tháng</span></div>
    <div class="flex justify-between" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span class="hint">Ngày bắt đầu</span><span style="font-weight:600">02/07/2026</span></div>
    <div class="flex justify-between" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span class="hint">Ngày kết thúc</span><span style="font-weight:600">02/10/2026</span></div>
    <div class="flex justify-between" style="padding:var(--s-8) 0"><span class="hint">Số buổi</span><span style="font-weight:600">90 buổi</span></div>
  </div>
  <div class="card"><h2>Gói sản phẩm đi kèm</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">F1 — Bữa ăn lành mạnh</div><div class="hint">Thay bữa, kiểm soát cân nặng</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('scale')}</span><div class="flex-1"><div style="font-weight:600">PPP — Bột Protein</div><div class="hint">Bổ sung đạm, hỗ trợ cơ</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-12) 0"><span style="color:var(--accent)">{ic('heart')}</span><div class="flex-1"><div style="font-weight:600">Omega-3 Herbalifeline</div><div class="hint">Hỗ trợ tim mạch</div></div></div>
  </div>
  <div class="card subtle"><div class="flex items-center gap-12"><span style="color:var(--state-warn)">{ic('alert')}</span><span class="hint" style="margin:0">Giá sản phẩm HLV giải thích bên ngoài app. Không có gì là thần dược.</span></div></div>
</div>
{cta('Tạo tài khoản',s='Đóng',pn='chevron-right')}'''
open(f'{D}/S-CONS-05_giai_phap.html','w',encoding='utf-8').write(page('Xem lộ trình — AnCare',body))
print('CONS-05 OK')

# === CONS-07: bỏ card mục tiêu, thêm giờ ăn, CTA đổi, thời gian sinh hoạt ===
body=f'''
{appbar('Gợi ý bữa ăn')}
<div class="content" style="padding-top:var(--s-12)">
  <div class="card"><h2>Cấu trúc bữa ăn</h2>
    <div class="flex justify-between" style="margin-bottom:var(--s-12)">
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">30%</div><div class="hint">Đạm</div></div>
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">40%</div><div class="hint">Tinh bột</div></div>
      <div class="flex-1" style="text-align:center"><div style="font-weight:700;color:var(--accent)">30%</div><div class="hint">Chất béo tốt</div></div>
    </div>
    <div class="flex items-center gap-12" style="padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)"><span style="color:var(--accent)">{ic('water')}</span><div><div style="font-weight:600">Nước khuyến nghị</div><div class="hint">2.5L (8 cốc 200ml)</div></div></div>
  </div>
  <div class="card"><h2>Bữa sáng · 07:00 · 320 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">F1 + PPP <span class="chip accent">đạm</span></div><div class="hint">2 muỗng F1 + 1 muỗng PPP + 250ml</div></div><div style="text-align:right"><div style="font-weight:700">160 kcal</div><div class="hint">18g đạm</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Trứng luộc <span class="chip accent">đạm</span></div><div class="hint">2 quả</div></div><div style="text-align:right"><div style="font-weight:700">120 kcal</div><div class="hint">12g đạm</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Rau xào <span class="chip neutral">rau</span></div><div class="hint">1 đĩa nhỏ</div></div><div style="text-align:right"><div style="font-weight:700">40 kcal</div><div class="hint">2g béo</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-top:1px solid var(--border)"><span style="color:var(--text-muted)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Trái cây</div><div class="hint">món ăn kèm</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-top:1px solid var(--border)"><span style="color:var(--accent)">{ic('scale')}</span><div class="flex-1"><div style="font-weight:600">PPP <span class="chip good">TPCN</span></div><div class="hint">thực phẩm bổ sung</div></div></div>
    <div class="card subtle" style="margin-top:var(--s-8);margin-bottom:0"><div class="hint">Lưu ý: Ăn ngược (đạm → rau → tinh bột), nhai kỹ, ăn chậm.</div></div>
  </div>
  <div class="card"><h2>Bữa trưa · 11:30 · 450 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Cơm lứt <span class="chip neutral">bột</span></div><div class="hint">1/2 bát</div></div><div style="text-align:right"><div style="font-weight:700">150 kcal</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Ức gà áp chảo <span class="chip accent">đạm</span></div><div class="hint">150g</div></div><div style="text-align:right"><div style="font-weight:700">250 kcal</div><div class="hint">30g đạm</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Canh rau <span class="chip neutral">rau</span></div><div class="hint">1 bát</div></div><div style="text-align:right"><div style="font-weight:700">50 kcal</div></div></div>
  </div>
  <div class="card"><h2>Bữa phụ · 16:00 · 150 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Trái cây ít ngọt</div><div class="hint">ổi/táo</div></div><div style="text-align:right"><div style="font-weight:700">150 kcal</div></div></div>
  </div>
  <div class="card"><h2>Bữa tối · 18:30 · 390 kcal</h2>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Cơm lứt <span class="chip neutral">bột</span></div><div class="hint">1/2 bát</div></div><div style="text-align:right"><div style="font-weight:700">130 kcal</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0;border-bottom:1px solid var(--border)"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Cá hấp <span class="chip accent">đạm</span></div><div class="hint">150g</div></div><div style="text-align:right"><div style="font-weight:700">200 kcal</div><div class="hint">25g đạm</div></div></div>
    <div class="flex items-center gap-12" style="padding:var(--s-8) 0"><span style="color:var(--accent)">{ic('utensils')}</span><div class="flex-1"><div style="font-weight:600">Rau luộc <span class="chip neutral">rau</span></div><div class="hint">1 đĩa</div></div><div style="text-align:right"><div style="font-weight:700">60 kcal</div></div></div>
  </div>
  <div class="card"><h2>Khuyến nghị thời gian & sinh hoạt</h2>
    <div style="display:flex;flex-direction:column;gap:var(--s-8)">
      <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('clock')}</span><span>07:00-07:30 Ăn sáng · 11:30-13:00 Ăn trưa · 16:00-17:00 Bữa phụ · 18:00-19:00 Ăn tối</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('water')}</span><span>Lượng nước: 2.5L (8 cốc)</span></div>
      <div class="flex items-center gap-12"><span style="color:var(--accent)">{ic('book')}</span><span>Giờ ngủ: 22:30 · Vận động: 30 phút/ngày</span></div>
    </div>
  </div>
</div>
{cta('Lưu & về xem chi tiết KH',pn='check')}'''
open(f'{D}/S-CONS-07_bua_an.html','w',encoding='utf-8').write(page('Gợi ý bữa ăn — AnCare',body))
print('CONS-07 OK')

# === CONS-08: mật khẩu=1, bỏ xác nhận, mục tiêu cải thiện bảng, số bữa, 3 ảnh ===
body=f'''
{appbar('Tạo tài khoản KH')}
<div class="content" style="padding-top:var(--s-12)">
  <div class="focus-card" style="margin-bottom:var(--s-16)"><div class="label">Thông tin đăng nhập</div><div class="title" style="font-size:var(--text-xl)">Phạm Hạnh</div></div>
  <div class="card"><h2>Thông tin tài khoản</h2>
    <div class="field"><label>Tài khoản</label><input value="097xxxxxxx"></div>
    <div class="field"><label>Mật khẩu</label><input value="1"></div>
    <div class="hint" style="margin-bottom:var(--s-12)">Mật khẩu mặc định = 1, HLV có thể chỉnh sửa.</div>
    <div class="flex items-center gap-12" style="padding:var(--s-12);background:var(--bg-subtle);border-radius:var(--radius-md)"><span style="color:var(--accent)">{ic('mail')}</span><span class="hint" style="margin:0">Gửi email chứa tài khoản & mật khẩu cho KH</span></div>
  </div>
  <div class="card"><h2>Mục tiêu cải thiện</h2>
    <div class="table-wrap" style="margin-bottom:var(--s-12)"><table class="table">
      <thead><tr><th>Chỉ số</th><th>Hiện tại</th><th>Tiêu chuẩn</th><th>Đánh giá</th><th>Mục tiêu</th></tr></thead><tbody>
        <tr class="good"><td>Cân nặng</td><td>64.8</td><td>62</td><td><span class="chip good">Tốt</span></td><td><input value="62" style="width:56px;height:32px;text-align:center;border:1px solid var(--border);border-radius:var(--radius-sm)"></td></tr>
        <tr class="warn"><td>Tỷ lệ mỡ</td><td>18.9%</td><td>17.5%</td><td><span class="chip warn">Thừa 1.4%</span></td><td><input value="17.5" style="width:56px;height:32px;text-align:center;border:1px solid var(--border);border-radius:var(--radius-sm)"></td></tr>
        <tr class="alert"><td>Mỡ nội tạng</td><td>10</td><td>1-7</td><td><span class="chip alert">Nguy hiểm</span></td><td><input value="7" style="width:56px;height:32px;text-align:center;border:1px solid var(--border);border-radius:var(--radius-sm)"></td></tr>
        <tr class="good"><td>Cơ</td><td>52</td><td>≥38%</td><td><span class="chip good">Tốt</span></td><td><input value="52" style="width:56px;height:32px;text-align:center;border:1px solid var(--border);border-radius:var(--radius-sm)"></td></tr>
      </tbody>
    </table></div>
    <div class="hint" style="margin-bottom:var(--s-8)">Mục tiêu mặc định = tiêu chuẩn, HLV có thể sửa.</div>
  </div>
  <div class="card"><h2>Số bữa ăn/ngày</h2>
    <div class="pills"><span class="pill">3 bữa</span><span class="pill active">4 bữa</span><span class="pill">5 bữa</span></div>
  </div>
  <div class="card"><h2>Ảnh check-in ban đầu</h2>
    <div class="hint" style="margin-bottom:var(--s-12)">Lưu vào nhật ký ngày tạo TK, dùng làm ảnh gốc so tiến độ.</div>
    <div class="flex gap-12">
      <div style="flex:1;text-align:center;padding:var(--s-16);border:2px dashed var(--border);border-radius:var(--radius-md);cursor:pointer"><div style="color:var(--accent)">{ic('image')}</div><div class="hint" style="margin-top:var(--s-4)">Chân dung</div></div>
      <div style="flex:1;text-align:center;padding:var(--s-16);border:2px dashed var(--border);border-radius:var(--radius-md);cursor:pointer"><div style="color:var(--accent)">{ic('image')}</div><div class="hint" style="margin-top:var(--s-4)">Toàn thân</div></div>
      <div style="flex:1;text-align:center;padding:var(--s-16);border:2px dashed var(--border);border-radius:var(--radius-md);cursor:pointer"><div style="color:var(--accent)">{ic('image')}</div><div class="hint" style="margin-top:var(--s-4)">Vòng eo</div></div>
    </div>
  </div>
</div>
{cta('Tạo tài khoản',pn='check')}'''
open(f'{D}/S-CONS-08_tao_tk.html','w',encoding='utf-8').write(page('Tạo tài khoản KH — AnCare',body))
print('CONS-08 OK')
print('HLV batch done: 5 files')
