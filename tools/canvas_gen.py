# Sinh artboard .dc.html cho canvas "Website PHFM - Teal Vanguard · Trang con" từ bản build (mid.html).
# Mỗi trang con = 1 artboard: giữ header + nhánh của trang đó + footer, dữ liệu + logic thật, ảnh = asset đã upload.
import re, json, os, sys, html
# Chạy: python3 tools/canvas_gen.py  -> build/canvas/project/*.dc.html + canvas.json (đăng lên canvas Trang con từ Cowork).
# Ảnh trên canvas là asset đã upload: specs/canvas/blobs.txt (tên file -> id), specs/canvas/manifest.json (khoá -> tên file).
# Ảnh mới chưa có trong blobs.txt: upload lên canvas trước (Cowork, Artifact asset) rồi thêm dòng vào blobs.txt.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from patches import apply_all
mid = apply_all(open(os.path.join(ROOT, 'src', 'src_o8.html'), encoding='utf-8').read())
OUT = os.path.join(ROOT, 'build', 'canvas')
CV = os.path.join(ROOT, 'specs', 'canvas')
man = json.load(open(CV + '/manifest.json'))
blob = dict(l.split() for l in open(CV + '/blobs.txt') if l.strip())
B = lambda fn: '/_blob/' + blob[fn]

# ---- template
a = mid.find('id="dc-tpl"'); a = mid.find('>', a) + 1
T = mid[a:mid.find('</script>', a)]
for k, fn in man.items():
    if k.startswith('T.'):
        pass
svgs = re.findall(r'src="(data:image/svg\+xml;base64,[^"]+)"', T)
for n, u in enumerate(svgs):
    T = T.replace('src="%s"' % u, 'src="%s"' % B(man['T.%d' % n]), 1)
assert 'data:image' not in T.replace('[src*="data:image"]', '')

# ---- css ngoài template (trừ font nhúng)
a2 = mid.find('id="dc-tpl"'); e2 = mid.find('</script>', a2)
css = []
for m in re.finditer(r'<style[^>]*>', mid):
    if a2 < m.start() < e2: continue
    z = mid.find('</style>', m.end()); c = mid[m.end():z]
    if '@font-face' in c[:200]: continue
    css.append(c)
EXTRA = ('\n/* canvas: bỏ hiệu ứng hiện dần để mọi khối luôn hiển thị khi chỉnh */\n'
         '.cr{opacity:1!important;transform:none!important;transition:none!important}\n'
         + '\n'.join(css))
HEAD_LINK = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap">'

# ---- tách nhánh trang
def blocks(t):
    """các khối <sc-if value="{{ is.X }}" ...> ... </sc-if> cấp ngoài cùng"""
    out = []
    for m in re.finditer(r'<sc-if value="\{\{ is\.(\w+) \}\}"[^>]*>', t):
        if any(s <= m.start() < e for _, s, e in out): continue
        depth, i = 1, m.end()
        while depth:
            o = t.find('<sc-if', i); c = t.find('</sc-if>', i)
            if o != -1 and o < c: depth += 1; i = o + 6
            else: depth -= 1; i = c + 8
        out.append((m.group(1), m.start(), i))
    return out
BL = blocks(T)
GROUP = {'phvsf': 'fund', 'vnshine': 'fund', 'member': 'service', 'portfolio': 'service', 'advisory': 'service',
         'guidePhvsf': 'guide', 'guideVnshine': 'guide', 'terms': 'legal', 'privacy': 'legal'}
def tpl_for(page):
    g = GROUP.get(page, page)
    keep = [b for b in BL if b[0] == g]
    assert len(keep) == 1, (page, [b[0] for b in BL])
    t = T
    for name, s, e in sorted(BL, key=lambda b: -b[1]):
        if name != g: t = t[:s] + t[e:]
    return t

# ---- script
def script_body(sel):
    i = mid.find(sel); st = mid.rfind('<script>', 0, i) + 8; return mid[st:mid.find('</script>', i)]
DATA = script_body('window.PHFM_B=b;')
ANCH = script_body('PHFM_ASOF')
k = mid.find('data-dc-script data-props='); ks = mid.find('>', k) + 1
LOGIC = mid[ks:mid.find('</script>', ks)]
props = json.loads(html.unescape(re.search(r'data-props="([^"]*)"', mid[k-40:ks]).group(1)))
IMAP = {k[2:]: B(fn) for k, fn in man.items() if k.startswith('I.')}
CMAP = {k[2:]: B(fn) for k, fn in man.items() if k.startswith('C.')}

def script_for(page, h):
    pr = dict(props); pr['$preview'] = {'width': 1440, 'height': h}
    stub = ('(function(){var R={lang:"vi",page:%s};'
            'window.__phfmRoute=function(){return {lang:R.lang,page:R.page}};'
            'window.__phfmSetHash=function(l,p){if(l&&l!==R.lang){R.lang=l;try{window.dispatchEvent(new Event("hashchange"))}catch(e){}}};'
            'window.__phfmTitle=function(){};window.__phfmToast=function(){};'
            'window.PHFM_ZH=window.PHFM_ZH||{};'
            'window.__I=%s;window.__ICONS=%s;})();\n') % (json.dumps(page), json.dumps(IMAP), json.dumps(CMAP))
    body = stub + ANCH + '\n' + DATA + '\n' + LOGIC
    assert '</script' not in body
    dp = json.dumps(pr, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
    return "<script type=\"text/x-dc\" data-dc-script data-props='%s'>\n%s\n</script>" % (dp, body)

TITLES = {'about': 'Về chúng tôi', 'funds': 'Danh sách quỹ', 'phvsf': 'Quỹ mở PHVSF', 'vnshine': 'PHFM VNSHINE ETF',
          'member': 'Quỹ thành viên', 'portfolio': 'Quản lý danh mục', 'advisory': 'Tư vấn đầu tư', 'ir': 'Công bố thông tin',
          'news': 'Góc nhìn & Tin tức', 'academy': 'Học viện Đầu tư', 'guidePhvsf': 'Hướng dẫn đầu tư PHVSF',
          'guideVnshine': 'Hướng dẫn đầu tư VNSHINE', 'faq': 'Câu hỏi thường gặp', 'glossary': 'Thuật ngữ đầu tư',
          'careers': 'Tuyển dụng', 'contact': 'Liên hệ', 'forms': 'Biểu mẫu', 'terms': 'Điều khoản sử dụng', 'privacy': 'Chính sách bảo mật'}
FILE = {p: (p[0].upper() + p[1:]) + '.dc.html' for p in TITLES}
FILE['about'] = 'Main.dc.html'

def artboard(page, h):
    t = tpl_for(page)
    hel_end = t.find('</helmet>')
    t = t[:hel_end] + HEAD_LINK + '\n<style>' + EXTRA + '</style>\n' + t[hel_end:]
    t = t.replace('<title>PHFM · Phu Hung Fund Management</title>', '<title>%s · PHFM</title>' % TITLES[page], 1)
    return ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<title>%s · PHFM</title>\n'
            '<script src="./support.js"></script>\n<script src="%s"></script>\n</head>\n<body>\n<x-dc>\n%s\n</x-dc>\n%s\n</body>\n</html>\n'
            % (TITLES[page], B('ds_bundle.js'), t.strip('\n'), script_for(page, h)))

if __name__ == '__main__':
    H = json.load(open(CV + '/heights.json'))
    os.makedirs(OUT + '/project', exist_ok=True)
    ROWS = [['about', 'funds', 'phvsf', 'vnshine', 'member', 'portfolio', 'advisory'],
            ['ir', 'news', 'academy', 'guidePhvsf', 'guideVnshine', 'faq', 'glossary'],
            ['careers', 'contact', 'forms', 'terms', 'privacy']]
    RT = ['Giới thiệu · Sản phẩm & Dịch vụ', 'Công bố thông tin · Tin tức · Học viện', 'Tuyển dụng · Liên hệ · Biểu mẫu · Pháp lý']
    boards, order, notes, y = {}, [], {}, 0
    for r, row in enumerate(ROWS):
        notes['r%d' % r] = {'x': 0, 'y': y - 300, 'text': RT[r], 'kind': 'title1', 'maxW': len(row) * 1520 - 80}
        for c, p in enumerate(row):
            h = H.get(p, 3000)
            f = FILE[p]
            boards[f] = {'x': c * 1520, 'y': y, 'w': 1440, 'h': h, 'title': TITLES[p] + ' · Tiếng Việt · Desktop', 'expand': 'fill', 'is_interactive': True}
            order.append(f)
            src = artboard(p, h)
            open(OUT + '/project/' + f, 'w', encoding='utf-8').write(src)
        y += max(H.get(p, 3000) for p in row) + 420
    order.remove('Main.dc.html'); order.insert(0, 'Main.dc.html')
    notes['n0'] = {'x': -620, 'y': 0, 'w': 520, 'fill': 'teal', 'size': 'm',
                   'text': 'Trang chủ nằm ở canvas "Website PHFM - Teal Vanguard".\n\nỞ đây: 19 trang con, bản tiếng Việt, desktop 1440px.\n\nSửa trực tiếp bố cục, khoảng cách, màu, cỡ chữ, ảnh. Chữ lấy từ dữ liệu (tên quỹ, đoạn mô tả, số liệu) sửa ở artifact "Nội dung website PHFM".\n\nSửa xong nhắn Claude: "đưa thay đổi canvas trang con vào web".'}
    idx = {'v': 3, 'createdOnFiles': {'v': 1, 'at': '2026-10-29T16:40:00Z'}, 'title': 'Website PHFM - Teal Vanguard · Trang con',
           'launch': {'view': 'canvas'}, 'pages': [], 'boards': boards, 'order': order, 'notes': notes, 'designSystems': []}
    json.dump(idx, open(OUT + '/project/canvas.json', 'w'), ensure_ascii=False, indent=1)
    for f in order: print(f, os.path.getsize(OUT + '/project/' + f) // 1024, 'KB')
