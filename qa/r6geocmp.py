"""So hình học hai build (kết quả của qa/r6geo.js): python3 qa/r6geocmp.py ref.json pr.json [tol=2] [chi-tiet]
Khối cấp 1: so top, cao, padding, margin. Chữ: so toạ độ tương đối khối chứa (dx, dy), rộng, cao, cỡ chữ, line-height, giãn chữ.
Khớp chữ theo khoá (id khối | thẻ | 36 ký tự đầu | lần xuất hiện). In số khác theo trang và loại."""
import json, sys, collections
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
tol = float(sys.argv[3]) if len(sys.argv) > 3 else 2
detail = len(sys.argv) > 4
summary = []
for x, y in zip(a, b):
    assert (x['page'], x['W'], x['lang']) == (y['page'], y['W'], y['lang'])
    tag = '%s %s %s' % (x['page'], x['lang'], x['W'])
    bad = collections.OrderedDict()
    def add(kind, msg):
        bad.setdefault(kind, []).append(msg)
    # khối cấp 1: ghép theo id, hoặc theo thứ tự khi không có id
    bx, by = x['blocks'], y['blocks']
    if len(bx) != len(by):
        add('số khối', '%d vs %d' % (len(bx), len(by)))
    for p, q in zip(bx, by):
        nm = p['id'] or p['cls'] or 'b%d' % p['i']
        if (p['id'] or '') != (q['id'] or '') and p['id'] and q['id']:
            add('khối lệch id', '%s vs %s' % (p['id'], q['id']))
        for k in ('y', 'h'):
            if abs(p[k] - q[k]) > tol: add('khối ' + k, '%s %s: %s -> %s' % (nm, k, p[k], q[k]))
        if abs(p['w'] - q['w']) > tol: add('khối w', '%s: %s -> %s' % (nm, p['w'], q['w']))
        if any(abs(m - n) > tol for m, n in zip(p['pad'], q['pad'])): add('khối padding', '%s: %s -> %s' % (nm, p['pad'], q['pad']))
        if any(abs(m - n) > tol for m, n in zip(p['mar'], q['mar'])): add('khối margin', '%s: %s -> %s' % (nm, p['mar'], q['mar']))
        pi, qi = p.get('inner'), q.get('inner')
        if pi and qi:
            for k in ('y', 'h', 'w'):
                if abs(pi[k] - qi[k]) > tol: add('khung trong ' + k, '%s %s: %s -> %s' % (nm, k, pi[k], qi[k]))
            if any(abs(m - n) > tol for m, n in zip(pi['pad'], qi['pad'])): add('khung trong padding', '%s: %s -> %s' % (nm, pi['pad'], qi['pad']))
    # chữ
    tx = {t['k']: t for t in x['texts']}; ty = {t['k']: t for t in y['texts']}
    miss = [k for k in tx if k not in ty]; extra = [k for k in ty if k not in tx]
    if miss: add('chữ thiếu ở PR', '%d: %s' % (len(miss), '; '.join(m[:50] for m in miss[:3])))
    if extra: add('chữ thừa ở PR', '%d: %s' % (len(extra), '; '.join(m[:50] for m in extra[:3])))
    for k, p in tx.items():
        q = ty.get(k)
        if not q: continue
        if abs(p['fs'] - q['fs']) > 0.5: add('cỡ chữ', '%s: %s -> %s' % (k[:60], p['fs'], q['fs']))
        if p['lh'] != q['lh'] and (isinstance(p['lh'], str) or isinstance(q['lh'], str) or abs(p['lh'] - q['lh']) > 0.5): add('line-height', '%s: %s -> %s' % (k[:60], p['lh'], q['lh']))
        if abs(p['ls'] - q['ls']) > 0.05: add('giãn chữ', '%s: %s -> %s' % (k[:60], p['ls'], q['ls']))
        for kk, nm2 in (('dx', 'chữ x'), ('dy', 'chữ y'), ('w', 'chữ rộng'), ('h', 'chữ cao')):
            if abs(p[kk] - q[kk]) > tol: add(nm2, '%s: %s -> %s' % (k[:60], p[kk], q[kk]))
    def renum(lst):  # đánh số lại ảnh theo thứ tự trong khối (chỉ ảnh đang hiện), vì chỉ số thô tính cả ảnh ẩn
        c = {}; o = {}
        for t in lst:
            b = t['k'].split('|')[0]; c[b] = c.get(b, -1) + 1; o['%s|img|%d' % (b, c[b])] = t
        return o
    ix = renum(x['imgs']); iy = renum(y['imgs'])
    for k, p in ix.items():
        q = iy.get(k)
        if not q: add('ảnh thiếu', k); continue
        for kk in ('dx', 'dy', 'w', 'h'):
            if abs(p[kk] - q[kk]) > tol: add('ảnh ' + kk, '%s: %s -> %s' % (k, p[kk], q[kk]))
    if abs(x['h'] - y['h']) > tol: add('cao trang', '%s -> %s' % (x['h'], y['h']))
    summary.append((tag, bad))
    n = sum(len(v) for v in bad.values())
    print('%-22s %s' % (tag, 'OK' if not n else '%d lệch: ' % n + ', '.join('%s %d' % (k, len(v)) for k, v in bad.items())))
    if detail and n:
        for k, v in bad.items():
            for m in v[:8]: print('      ', k, '|', m)
tot = sum(sum(len(v) for v in bad.values()) for _, bad in summary)
print('Tổng lệch:', tot, 'trên', len(summary), 'lượt trang')
