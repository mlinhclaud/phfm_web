# Vòng 3 (29/10): góp ý của Rin sau bản Teal đầu tiên.
import re
from patches import rep, part


# ---------------------------------------------------------------- ảnh mới + logo đối tác (chạy trước p_images)
def p_r3img(s):
    # hero trang VNSHINE ETF: ảnh riêng, không dùng chung với trang hướng dẫn
    s = rep(s, "heroImg:'@@IMG:vn_city@@',price", "heroImg:'@@IMG:r3_vns_hero@@',price")
    # hero Tư vấn đầu tư: tách khỏi ảnh 224 đang dùng ở thẻ Tuyển dụng 02
    s = rep(s, "advisory:{img:'@@IMG:pk_I06@@'", "advisory:{img:'@@IMG:r3_adv_hero@@'")
    # ảnh bìa 2 bài nền kem
    s = rep(s, "{img:'@@IMG:nw_msci@@'", "{img:'@@IMG:r3_nw_msci@@'")
    s = rep(s, "{img:'@@IMG:nw_rot@@'", "{img:'@@IMG:r3_nw_rot@@'")
    # logo đối tác: bỏ link ngoài, dùng file trong D:\AI\PHFM\Partner
    for dm, key in [('bidv.com.vn', 'p_bidv'), ('ey.com', 'p_ey'), ('vndirect.com.vn', 'p_vnd'), ('finhay.com.vn', 'p_finhay'),
                    ('masvn.com', 'p_mirae'), ('hsc.com.vn', 'p_hsc'), ('vietcap.com.vn', 'p_vietcap')]:
        s, n = re.subn(r"(dm:'%s',src:)'https?://[^']+'" % re.escape(dm), r"\1'@@IMG:%s@@'" % key, s)
        assert n == 1, dm
    s = rep(s, "[/HSC|Thành phố Hồ Chí Minh|Ho Chi Minh City Securities|胡志明/,'HSC'],[/Mirae/,'Mirae Asset'],[/Vietcap/,'Vietcap'],[/Finhay/,'Finhay']",
            "[/HSC|Thành phố Hồ Chí Minh|Ho Chi Minh City Securities|胡志明/,'@@IMG:p_hsc@@'],[/Mirae/,'@@IMG:p_mirae@@'],[/Vietcap/,'@@IMG:p_vietcap@@'],[/Finhay/,'@@IMG:p_finhay@@']")
    return s


# ---------------------------------------------------------------- chữ: PHVSF, VNSHINE Index
def p_r3text(s):
    s = rep(s, "heroRows:[{n:b('Quỹ','Fund'),v:[1.8,4.6,42.4]}", "heroRows:[{n:'PHVSF',v:[1.8,4.6,42.4]}")
    s = rep(s, "cols:['FUEPHVNS',b('Chỉ số tham chiếu','Reference index')],", "cols:['FUEPHVNS','VNSHINE Index'],")
    return s


# ---------------------------------------------------------------- ban điều hành: bấm cả thẻ để xem
def p_r3people(s):
    s = rep(s, '\n              <div style="flex:none;font-size:14px;font-weight:700;color:var(--gold-ink)">{{ d.ui.learnMore }} +</div>', '')
    s = rep(s, '<div data-keepgrid class="nm-mgr" onClick="{{ m.open }}"',
            '<div data-keepgrid class="nm-mgr" role="button" tabindex="0" aria-haspopup="dialog" onClick="{{ m.open }}"')
    # Về chúng tôi: thẻ lãnh đạo mở hộp thông tin khi bấm (xử lý trong site.js)
    s = rep(s, '<div style="background:var(--white);border:1px solid var(--sand);border-radius:16px;padding:36px 34px 40px">',
            '<div class="ld-card" role="button" tabindex="0" aria-haspopup="dialog" style="background:var(--white);border:1px solid var(--sand);border-radius:16px;padding:36px 34px 40px;cursor:pointer">')
    s = rep(s, '<details style="margin:16px 0 0"><summary style="cursor:pointer;font-size:14px;font-weight:700;color:var(--gold-ink)">{{ d.ui.learnMore }} +</summary><p style="font-size:16px;line-height:27px;color:var(--muted);margin:12px 0 0;text-wrap:pretty">{{ p.bio }}</p></details>',
            '<p class="ld-bio" hidden>{{ p.bio }}</p>')
    return s


# ---------------------------------------------------------------- khối "Quỹ phù hợp", ô chênh lệch giá/NAV
FIT_OLD = '''          <div style="margin-top:56px;background:var(--white);border:1px solid var(--sand);border-radius:16px;padding:36px 40px">
            <div style="font-size:20px;line-height:28px;font-weight:700;color:var(--ink)">{{ f.fitTitle }}</div>
            <div style="display:grid;grid-template-columns:{{ f.fitCols }};gap:24px 40px;margin-top:24px">
              <sc-for list="{{ f.fitL }}" as="fi" hint-placeholder-count="3">
                <div style="display:grid;grid-template-columns:24px minmax(0,1fr);gap:12px;align-items:start">
                  <svg viewBox="0 0 24 24" style="width:22px;height:22px;margin-top:3px"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="#C0962D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                  <div style="font-size:16px;line-height:26px;color:var(--ink);text-wrap:pretty">{{ fi.t }}</div>
                </div>
              </sc-for>
            </div>
          </div>'''
FIT_NEW = '''          <div class="fit" data-keepgrid>
            <div class="fit-h"><i class="fit-bar"></i><div class="fit-t">{{ f.fitTitle }}</div></div>
            <div class="fit-l">
              <sc-for list="{{ f.fitL }}" as="fi" hint-placeholder-count="5">
                <div class="fit-i"><span class="fit-c"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg></span><span class="fit-x">{{ fi.t }}</span></div>
              </sc-for>
            </div>
          </div>'''

def p_r3blocks(s):
    s = rep(s, FIT_OLD, FIT_NEW)
    s = rep(s, '<div style="padding:24px 28px;background:var(--gold-soft)"><div style="font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-ink)">{{ d.fundUi.pd }}</div><div style="font-size:30px;font-weight:700;color:{{ f.trading.pdColor }};margin-top:8px">{{ f.trading.pd }}</div></div>',
            '<div class="pd-cell"><div class="pd-l">{{ d.fundUi.pd }}</div><div class="pd-v">{{ f.trading.pd }}</div></div>')
    # hero trang quỹ: nền teal đậm theo trang chủ
    s = rep(s, '<section style="min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));display:grid;align-content:center;box-sizing:border-box;position:relative;overflow:hidden;background:var(--cream)', '<section class="fh" style="min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));display:grid;align-content:center;box-sizing:border-box;position:relative;overflow:hidden;background:var(--cream)')
    # hero các trang con khác (dịch vụ, học viện, tuyển dụng): nền teal đậm
    for old in ['<section style="min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));display:grid;align-content:center;box-sizing:border-box;background:var(--ivory);position:relative;overflow:hidden">',
                '<section style="min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));display:grid;align-content:center;box-sizing:border-box;position:relative;background:var(--ivory);overflow:hidden;border-bottom:1px solid var(--sand)">',
                '<section style="min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));display:grid;align-content:center;box-sizing:border-box;background:var(--ivory)">']:
        s = rep(s, old, old.replace('<section ', '<section class="dh" '))
    return s


# ---------------------------------------------------------------- tài liệu quỹ: lọc loại, chọn nhiều, tải
def p_r3docs(s):
    m = re.search(r'          <div data-keepgrid class="nm-dfl"[^\n]*\n', s)
    line = m.group(0)
    yr = re.search(r'<label.*</label>', line).group(0)
    ty = (yr.replace('{{ d.ir.year }}', '{{ f.fdTypeL }}').replace('{{ f.docYrSel }}', '{{ f.docSel }}')
            .replace('{{ f.docYrOpts }}', '{{ f.docOpts }}').replace('{{ f.docYr }}', '{{ f.docVal }}'))
    assert ty.count('f.docVal') == 2 and 'f.docOpts' in ty
    new = ('          <div data-keepgrid class="nm-dfl fd-f">' + ty + yr + '</div>\n'
           '          <div class="fd-bar"><span class="fd-n">{{ f.docCount }} {{ d.ir.docsN }} · {{ f.fdN }} {{ d.ir.selN }}</span>'
           '<button type="button" class="fd-dl" onClick="{{ f.fdDl }}" disabled="{{ f.fdNone }}"><svg viewBox="0 0 24 24"><path d="M12 4v11m0 0l-4.5-4.5M12 15l4.5-4.5M5 19h14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>{{ f.fdLabel }}</button></div>\n')
    s = s.replace(line, new, 1)
    BOX = ('<span onClick="{{ %s }}" role="checkbox" class="fd-cb"><sc-if value="{{ %s }}"><i class="fd-box on">✓</i></sc-if>'
           '<sc-if value="{{ %s }}" hint-placeholder-val="{{ true }}"><i class="fd-box"></i></sc-if></span>')
    s = rep(s, '''          <div style="margin-top:28px;background:var(--white);border:1px solid var(--sand)">
            <sc-for list="{{ f.docs }}" as="doc" hint-placeholder-count="6">
              <div data-keepgrid class="nm-docr" style="display:grid;grid-template-columns:56px minmax(0,1fr) 160px 100px 100px;gap:16px;align-items:center;padding:20px 24px;border-bottom:1px solid var(--sand)">
''', '''          <div class="fd-list" style="margin-top:16px;background:var(--white);border:1px solid var(--sand)">
            <div class="fd-head" data-keepgrid>''' + BOX % ('f.fdToggleAll', 'f.fdAllSel', 'f.fdNotAll') + '''<span>{{ f.fdAllL }}</span></div>
            <sc-for list="{{ f.docs }}" as="doc" hint-placeholder-count="6">
              <div data-keepgrid class="nm-docr fd-r" style="display:grid;grid-template-columns:28px 52px minmax(0,1fr) 180px 100px 44px;gap:16px;align-items:center;padding:20px 24px;border-bottom:1px solid var(--sand)">
                ''' + BOX % ('doc.toggle', 'doc.sel', 'doc.unsel') + '\n')
    # logic
    s = rep(s, "const docOpts = F.docCats.map((label, i) => ({ v: String(i), label }))",
            "const docOpts = F.docCats.map((label, i) => ({ v: String(i), label })).filter(o => o.v === '0' || F.docs.some(x => x.c === +o.v))")
    s = rep(s, "const docs = F.docs.filter(x => (docYr === 'all' || String(x.date).slice(-4) === docYr)).map(x => ({ ...x, cat: F.docCats[x.c], isNew: this.isNew(x.date) }));",
            "const fdS = S.fdSel || {}, fdK = x => F.code + '|' + x.t + '|' + x.date;\n"
            "      const docs = F.docs.filter(x => (docYr === 'all' || String(x.date).slice(-4) === docYr) && (!S.docCat || x.c === S.docCat)).map(x => { const k = fdK(x), on = !!fdS[k]; return { ...x, cat: F.docCats[x.c], isNew: this.isNew(x.date), sel: on, unsel: !on, toggle: () => this.setState(st => { const n = { ...(st.fdSel || {}) }; if (n[k]) delete n[k]; else n[k] = 1; return { fdSel: n }; }) }; });\n"
            "      const fdN = docs.filter(x => x.sel).length, fdAll = docs.length > 0 && fdN === docs.length, fdVi = l === 'vi';\n"
            "      const fdX = { fdN, fdNone: fdN === 0, fdAllSel: fdAll, fdNotAll: !fdAll, fdTypeL: fdVi ? 'Loại tài liệu' : 'Document type', fdAllL: fdAll ? (fdVi ? 'Bỏ chọn tất cả' : 'Clear selection') : (fdVi ? 'Chọn tất cả' : 'Select all'),\n"
            "        fdLabel: (fdVi ? 'Tải tài liệu đã chọn' : 'Download selected') + (fdN ? ' (' + fdN + ')' : ''),\n"
            "        fdToggleAll: () => this.setState(st => { const n = { ...(st.fdSel || {}) }; docs.forEach(x => { const k = fdK(x); if (fdAll) delete n[k]; else n[k] = 1; }); return { fdSel: n }; }),\n"
            "        fdDl: () => { if (fdN && window.__phfmToast) window.__phfmToast(fdVi ? 'Tài liệu đang được cập nhật. Vui lòng quay lại sau.' : 'This document is being updated. Please check back later.'); } };")
    s = rep(s, "docEmpty: docs.length === 0, docs,", "docEmpty: docs.length === 0, docs, ...fdX,")
    # đổi trang hoặc đổi quỹ thì bỏ chọn
    s = rep(s, "docCat: 0, docYr: 'all',", "docCat: 0, docYr: 'all', fdSel: {},")
    return s


# ---------------------------------------------------------------- script + css vòng 3
def p_r3assets(s):
    s = rep(s, '</helmet>', '<style>' + part('r3.css') + '</style></helmet>')
    i = s.rfind('</body>')
    s = s[:i] + part('tools.html') + '\n' + s[i:]
    return s


# ---------------------------------------------------------------- chữ Rin sửa ở artifact "Nội dung website PHFM"
def p_r3edits(s):
    import json, os
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'edits.json')
    E = json.load(open(f, encoding='utf-8')) if os.path.exists(f) else []
    i = s.find('window.PHFM_B=b;'); e = s.find('</script>', i)
    js = ('\n/* nội dung đã sửa (artifact Nội dung website PHFM) */\n(function(E){var D=window.PHFM_DATA;E.forEach(function(x){'
          'var k=x.p.split("."),o=D;for(var j=0;j<k.length-1;j++){if(o==null)return;o=o[k[j]]}if(o==null)return;var l=k[k.length-1],v=o[l];'
          'if(v&&v.__b){if(x.vi!=null)v.vi=x.vi;if(x.en!=null)v.en=x.en}else if(typeof v==="string"&&x.vi!=null)o[l]=x.vi})})('
          + json.dumps(E, ensure_ascii=False).replace('</', '<\\/') + ');\n')
    return s[:e] + js + s[e:]


PRE = [p_r3img]                      # chạy ngay sau p_imgmap
POST = [p_r3edits, p_r3text, p_r3people, p_r3blocks, p_r3docs, p_r3assets]
