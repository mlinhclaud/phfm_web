#!/usr/bin/env python3
"""Tạo vendor/fonts/noto-serif-tc-600-subset.woff2 chỉ gồm 新 速 實 簡 (R4-05).
Cần: pip install fonttools brotli; npm pack @fontsource/noto-serif-tc (giải ra thư mục <pkg>).
Dùng: python3 tools/subset_hanzi.py <pkg>/files  (build không gọi mạng, chỉ commit file kết quả)."""
import sys, os, tempfile
from fontTools import subset, ttLib
from fontTools.merge import Merger

TEXT = '新速實簡'
SLICES = ['121', '122', '123']  # ba slice của @fontsource chứa 4 chữ trên (weight 600)
src = sys.argv[1]
out = os.path.join(os.path.dirname(__file__), '..', 'vendor', 'fonts', 'noto-serif-tc-600-subset.woff2')
parts = []
for n in SLICES:
    f = ttLib.TTFont(os.path.join(src, 'noto-serif-tc-%s-600-normal.woff2' % n))
    ss = subset.Subsetter(subset.Options(layout_features=[], name_IDs=[1, 2], notdef_outline=True, glyph_names=False))
    ss.populate(text=TEXT)
    ss.subset(f)
    p = os.path.join(tempfile.gettempdir(), '_hz_%s.ttf' % n)
    f.flavor = None
    f.save(p)
    parts.append(p)
m = Merger().merge(parts)
m.flavor = 'woff2'
m.save(out)
print(out, os.path.getsize(out), 'bytes')
cm = ttLib.TTFont(out).getBestCmap()
print({c: ord(c) in cm for c in TEXT})
