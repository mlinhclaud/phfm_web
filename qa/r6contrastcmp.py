"""So kết quả qa/r5contrast.js giữa hai bản: python3 qa/r6contrastcmp.py main.json pr.json
In các chữ không đạt ở bản PR mà bản main đạt (hoặc không có), và số lượng chung."""
import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
key = lambda r: (r['page'], r['lang'], r['W'], r['text'][:20])
A = {key(r): r for r in a}; B = {key(r): r for r in b}
badA = {k for k, r in A.items() if not r['pass']}; badB = {k for k, r in B.items() if not r['pass']}
print('main: %d/%d không đạt; PR: %d/%d không đạt' % (len(badA), len(A), len(badB), len(B)))
print('Không đạt ở PR, main đạt hoặc không đo được:')
for k in sorted(badB - badA):
    r = B[k]; print(' ', k, r['color'], '%spx' % r['fs'], 'min', r['min'], 'med', r['med'], '| main:', A[k]['min'] if k in A else '-')
print('Không đạt ở main, đạt ở PR:', len(badA - badB))
