#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use File::Spec;
use File::Copy;
use File::Path qw(make_path remove_tree);
use File::Basename;

# Set output encoding to UTF-8
binmode(STDOUT, ":utf8");

my @FLOW = (
  { role => 'coach', name => 'AUTH-01_dang_nhap', title => 'Đăng nhập' },
  { role => 'coach', name => 'AUTH-02_shell', title => 'Trang chủ HLV' },
  { role => 'coach', name => 'LEAD-01_danh_sach', title => 'DS KH' },
  { role => 'coach', name => 'LEAD-02_tao_lead', title => 'Thêm mới KH' },
  { role => 'coach', name => 'CONS-02_chan_dung_kh', title => 'Chân dung KH' },
  { role => 'coach', name => 'CONS-03_tanita', title => 'Khảo sát Tanita' },
  { role => 'coach', name => 'CONS-04_phan_tich', title => 'Phân tích kết quả' },
  { role => 'coach', name => 'CONS-05_giai_phap', title => 'Xem lộ trình' },
  { role => 'coach', name => 'CONS-08_tao_tk', title => 'Tạo tài khoản' },
  { role => 'coach', name => 'CONS-07_bua_an', title => 'Xây dựng bữa ăn' },
  { role => 'coach', name => 'CARE-01_talking_point', title => 'Talking point' },
  { role => 'coach', name => 'CARE-03_dieu_chinh_bua_an', title => 'Điều chỉnh bữa ăn' },
  { role => 'coach', name => 'CARE-09_nhac_72h', title => 'Nhắc 72h' },
  { role => 'coach', name => 'DEV-01_microcourse', title => 'Micro-course' },
  { role => 'coach', name => 'CONS-09_ket_qua_kh', title => 'Kết quả của Hạnh' },
  { role => 'coach', name => 'CONS-10_bao_cao_kh', title => 'Báo cáo kết quả' },
  { role => 'coach', name => 'CONS-11_infographic', title => 'Tạo Infographic' },
  { role => 'customer', name => 'HLTH-02_trang_chu', title => 'Trang chủ KH' },
  { role => 'customer', name => 'HLTH-06_check_in', title => 'Check-in KH' },
  { role => 'customer', name => 'HLTH-04_bua_an', title => 'Ghi nhận bữa ăn' },
  { role => 'customer', name => 'DEV-02_dao_tao', title => 'Đào tạo KH' }
);

# Determine paths relative to this script
my $script_dir = dirname(File::Spec->rel2abs($0));
my $root_dir = File::Spec->catdir($script_dir, "..");
my $mockups_src_dir = File::Spec->catdir($root_dir, "docs", "03-mockups");
my $proto_dir = File::Spec->catdir($root_dir, "docs", "04-prototypes");
my $proto_mockups_dir = File::Spec->catdir($proto_dir, "03-mockups");

# Rebuild directories
make_path(File::Spec->catdir($proto_dir, "_assets"));
make_path(File::Spec->catdir($proto_dir, "coach"));
make_path(File::Spec->catdir($proto_dir, "customer"));

# Clean 03-mockups inside 04-prototypes
if (-d $proto_mockups_dir) {
    remove_tree($proto_mockups_dir);
}
make_path($proto_mockups_dir);
make_path(File::Spec->catdir($proto_mockups_dir, "_assets"));
make_path(File::Spec->catdir($proto_mockups_dir, "coach"));
make_path(File::Spec->catdir($proto_mockups_dir, "customer"));

# Copy subdirs from 03-mockups to 04-prototypes/03-mockups
sub copy_dir_files {
    my ($src, $dst, $ext) = @_;
    opendir(my $dh, $src) or die "Could not open $src: $!";
    while (my $entry = readdir($dh)) {
        next if $entry =~ /^\./;
        my $src_file = File::Spec->catfile($src, $entry);
        my $dst_file = File::Spec->catfile($dst, $entry);
        if (-f $src_file) {
            if (!defined $ext || $entry =~ /\.$ext$/) {
                copy($src_file, $dst_file) or die "Copy failed from $src_file to $dst_file: $!";
            }
        }
    }
    closedir($dh);
}

copy_dir_files(File::Spec->catdir($mockups_src_dir, "_assets"), File::Spec->catdir($proto_mockups_dir, "_assets"));
copy_dir_files(File::Spec->catdir($mockups_src_dir, "coach"), File::Spec->catdir($proto_mockups_dir, "coach"), "html");
copy_dir_files(File::Spec->catdir($mockups_src_dir, "customer"), File::Spec->catdir($proto_mockups_dir, "customer"), "html");

print "Copied 03-mockups files to 04-prototypes/03-mockups\n";

# Generate _proto-nav.css
my $css_path = File::Spec->catfile($proto_dir, "_assets", "_proto-nav.css");
open(my $fh, '>:utf8', $css_path) or die "Cannot write to $css_path: $!";
print $fh <<'CSS';
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');
.proto-nav{position:fixed;top:0;left:0;right:0;height:44px;background:#1f2933;color:#fff;display:flex;align-items:center;gap:8px;padding:0 16px;z-index:1000;font-size:12px;font-family:'Be Vietnam Pro',sans-serif;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.proto-nav .ttl{flex:1;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#f8fafc}
.proto-nav a{color:#9bb0c0;text-decoration:none;padding:6px 12px;border-radius:6px;font-size:12px;font-weight:500;transition:background .15s}
.proto-nav a:hover{background:#334155;color:#fff}
.proto-frame{margin-top:44px;border:none;width:100%;height:calc(100vh - 44px);display:block;background:#f8fafc}
CSS
close($fh);

# Generate wrapper HTMLs
for my $i (0 .. $#FLOW) {
    my $item = $FLOW[$i];
    my $role = $item->{role};
    my $name = $item->{name};
    my $title = $item->{title};
    
    my $prev = $i > 0 ? $FLOW[$i - 1] : undef;
    my $nxt = $i < $#FLOW ? $FLOW[$i + 1] : undef;
    
    my $prev_link = $prev ? "../$prev->{role}/$prev->{name}.html" : "#";
    my $prev_txt = $prev ? "‹ $prev->{title}" : "";
    my $next_link = $nxt ? "../$nxt->{role}/$nxt->{name}.html" : "#";
    my $next_txt = $nxt ? "$nxt->{title} ›" : "";
    
    my $html_path = File::Spec->catfile($proto_dir, $role, "$name.html");
    open(my $html_fh, '>:utf8', $html_path) or die "Cannot write to $html_path: $!";
    
    my $page_num = $i + 1;
    my $total_pages = scalar(@FLOW);
    
    print $html_fh <<"HTML";
<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>$title — AnCare Prototype</title>
<link rel="stylesheet" href="../_assets/_proto-nav.css">
</head><body>
<div class="proto-nav">
  <a href="../index.html">☰ Menu</a>
  <span class="ttl">$title · $page_num/$total_pages</span>
  <a href="$prev_link">$prev_txt</a>
  <a href="$next_link">$next_txt</a>
</div>
<iframe class="proto-frame" src="../03-mockups/$role/S-$name.html"></iframe>
</body></html>
HTML
    close($html_fh);
}

# Generate index.html
my $index_path = File::Spec->catfile($proto_dir, "index.html");
open(my $idx_fh, '>:utf8', $index_path) or die "Cannot write to $index_path: $!";

print $idx_fh <<'HTML';
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
HTML

# First 10 items
my $total = scalar(@FLOW);
for my $idx (0 .. 9) {
    my $item = $FLOW[$idx];
    my $num = $idx + 1;
    print $idx_fh "    <a class=\"card\" href=\"coach/$item->{name}.html\"><div class=\"id\">$num/$total</div><div class=\"nm\">$item->{title}</div><div class=\"tpl\">T1</div></a>\n";
}

print $idx_fh <<'HTML';
  </div>
</div>

<div class="flow">
  <h2>📋 Chăm sóc KH (HLV) <span class="badge">7 màn</span></h2>
  <div class="grid">
HTML

# Items 11 to 17
for my $idx (10 .. 16) {
    my $item = $FLOW[$idx];
    print $idx_fh "    <a class=\"card\" href=\"coach/$item->{name}.html\"><div class=\"id\">$item->{title}</div><div class=\"nm\">$item->{title}</div></a>\n";
}

print $idx_fh <<'HTML';
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
HTML

# Remaining items
for my $idx (17 .. $#FLOW) {
    my $item = $FLOW[$idx];
    print $idx_fh "    <a class=\"card kh\" href=\"$item->{role}/$item->{name}.html\"><div class=\"id\">$item->{title}</div><div class=\"nm\">$item->{title}</div></a>\n";
}

print $idx_fh <<'HTML';
  </div>
</div>

<div class="note">
  <strong>Cách xem:</strong> mở file này trong browser → click từng màn. Mỗi prototype mở mockup trong iframe + nav prototype (‹ › Menu).<br>
  <strong>Luồng đầy đủ HLV:</strong> Đăng nhập → Trang chủ → DS KH → Thêm mới KH → Chân dung → Tanita → Phân tích → Xem lộ trình → Tạo TK → Bữa ăn.<br>
  <strong>Tổng:</strong> 21 mockup + 21 prototype. Wireframe đã rebuild theo design system mới (không emoji, SVG Tabler, semantic tokens, 8dp spacing).
</div>
</div></body></html>
HTML

close($idx_fh);

print "Prototypes generated: " . scalar(@FLOW) . " wrappers + index.html\n";
