"""Bảng chiều cao hero (khối đầu của <main> hoặc .nm-ghero) giữa ba bản: python3 qa/r6herotable.py gốc.json main.json pr.json
Đầu vào là kết quả qa/r6geo.js (VI)."""
import json, sys
a, b, c = [json.load(open(f)) for f in sys.argv[1:4]]
key = lambda x: (x['page'], x['W'])
A = {key(x): x for x in a}; B = {key(x): x for x in b}; C = {key(x): x for x in c}
def hero(x):
    for bl in x['blocks']:
        if 'nm-ghero' in bl['cls']: return bl['h']
    for bl in x['blocks']:
        if bl['cls'] in ('nm-sbar', 'nm-gnav'): continue
        return bl['h']
print('| Rộng | Trang | Gốc 3131e7e | main | PR |')
print('|---|---|---|---|---|')
for W in (1440, 1024, 390):
    for pg in ('about', 'phvsf', 'vnshine', 'member', 'portfolio', 'advisory', 'academy', 'careers', 'guidePhvsf', 'guideVnshine'):
        k = (pg, W)
        if k in A and k in B and k in C:
            print('| %d | %s | %s | %s | %s |' % (W, pg, round(hero(A[k])), round(hero(B[k])), round(hero(C[k]))))
