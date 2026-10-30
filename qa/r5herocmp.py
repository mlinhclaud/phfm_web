"""So bảng cỡ chữ hero giữa bản main và bản PR: python3 qa/r5herocmp.py hero-main.json hero-pr.json [md]
In các dòng khác nhau (font-size, line-height, letter-spacing, font-weight, word-spacing, text-align). Có tham số 'md' thì in bảng markdown main | PR."""
import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
md = len(sys.argv) > 3 and sys.argv[3] == 'md'
diff = 0; n = 0; rows = []
for x, y in zip(a, b):
    assert (x['page'], x['W'], x['lang']) == (y['page'], y['W'], y['lang'])
    ix = {i['role']: i for i in x['items']}; iy = {i['role']: i for i in y['items']}
    for role in sorted(set(ix) | set(iy)):
        p, q = ix.get(role), iy.get(role); n += 1
        if not p or not q:
            print('THIẾU', x['page'], x['lang'], x['W'], role, bool(p), bool(q)); diff += 1; continue
        d = [k for k in ('fs', 'lh', 'ls', 'fw', 'ws', 'ta') if p[k] != q[k]]
        if d:
            diff += 1; print('KHÁC', x['page'], x['lang'], x['W'], role, p['text'][:18], {k: (p[k], q[k]) for k in d})
        rows.append((x['W'], x['page'], role, p, q, not d))
print('so sánh', n, 'dòng, khác', diff)
if md:
    print('| Rộng | Trang | Phần tử | main: cỡ / dòng / giãn chữ / đậm | PR: cỡ / dòng / giãn chữ / đậm | Trùng |')
    print('|---|---|---|---|---|---|')
    f = lambda i: '%s / %s / %s / %s' % (i['fs'], i['lh'], i['ls'], i['fw'])
    for W, pg, role, p, q, ok in rows:
        print('| %s | %s | %s | %s | %s | %s |' % (W, pg, role, f(p), f(q), 'có' if ok else '**không**'))
