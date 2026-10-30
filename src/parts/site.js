<script>
/* Hành vi chung cho toàn site (chạy ngoài template):
   - chặn link href="#" làm mất đường dẫn trang (A01)
   - nút tải tài liệu chưa có file: hiện thông báo thay vì nhảy trang (A05); nút có data-dl cũng được tính (R6-03, dùng cho bản 中文 chưa khớp chữ "Tải về"/"Download")
   - tìm kiếm trong site (A06) */
(function () {
  var L = function () { return (document.documentElement.lang || 'vi').slice(0, 2) === 'vi' ? 'vi' : 'en'; };
  var TX = {
    vi: { doc: 'Tài liệu đang được cập nhật. Vui lòng quay lại sau.', ph: 'Tìm trang, bài viết, thuật ngữ, câu hỏi…', none: 'Không tìm thấy kết quả phù hợp.', close: 'Đóng tìm kiếm',
          g: { page: 'Trang', news: 'Bài viết', faq: 'Câu hỏi thường gặp', gloss: 'Thuật ngữ', form: 'Biểu mẫu', ir: 'Công bố thông tin', job: 'Tuyển dụng' } },
    en: { doc: 'This document is being updated. Please check back later.', ph: 'Search pages, articles, terms, questions…', none: 'No matching results.', close: 'Close search',
          g: { page: 'Page', news: 'Article', faq: 'FAQ', gloss: 'Glossary', form: 'Form', ir: 'Disclosure', job: 'Careers' } }
  };
  // ---------- thông báo nhỏ ----------
  var toastEl, toastT;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'phfm-toast'; toastEl.setAttribute('role', 'status'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(function () { toastEl.classList.remove('on'); }, 2800);
  }
  window.__phfmToast = toast;
  var DL = /^(tải về|tải xuống|download)(\s|$|↓|\()|csv\/excel|\(pcf\)/i;
  document.addEventListener('click', function (e) {
    var t = e.target; if (!t || !t.closest) return;
    var lab = t.closest('[aria-label="Tải xuống"],[aria-label="Download"],[title="Tải xuống"],[title="Download"]');
    var el = t.closest('a,button,[role="button"]');
    var txt = el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : '';
    if (lab || (el && el.hasAttribute('data-dl')) || (el && DL.test(txt) && !/app store|google play/i.test(txt))) {
      e.preventDefault(); e.stopPropagation(); toast(TX[L()].doc); return;
    }
    var a = t.closest('a[href="#"]'); if (a) e.preventDefault();
  }, true);

  // ---------- tìm kiếm ----------
  var nrm = function (x) { return String(x || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/gi, 'd').toLowerCase(); };
  var tx = function (x, l) { return x && x.__b ? (x[l] || x.vi) : (x || ''); };
  var TITLES = {
    home: ['Trang chủ', 'Home'], about: ['Về chúng tôi', 'About us'], funds: ['Danh sách quỹ', 'Fund list'], phvsf: ['Quỹ mở PHVSF – Quỹ Đầu tư Chọn lọc Phú Hưng Việt Nam', 'PHVSF Open-ended Fund'],
    vnshine: ['PHFM VNSHINE ETF – Chiến lược Lợi suất Cổ đông', 'PHFM VNSHINE ETF – Shareholder Yield'], member: ['Quỹ thành viên', 'Member funds'], portfolio: ['Quản lý danh mục', 'Portfolio management'],
    advisory: ['Tư vấn đầu tư', 'Investment advisory'], ir: ['Công bố thông tin', 'Information disclosure'], news: ['Góc nhìn & Tin tức', 'Insights & News'], academy: ['Học viện Đầu tư', 'Investment Academy'],
    careers: ['Tuyển dụng', 'Careers'], contact: ['Liên hệ', 'Contact'], guidePhvsf: ['Hướng dẫn đầu tư quỹ mở PHVSF', 'How to invest in PHVSF'], guideVnshine: ['Hướng dẫn đầu tư PHFM VNSHINE ETF', 'How to invest in PHFM VNSHINE ETF'],
    faq: ['Câu hỏi thường gặp', 'FAQ'], glossary: ['Thuật ngữ đầu tư', 'Glossary'], forms: ['Biểu mẫu', 'Forms'], terms: ['Điều khoản sử dụng', 'Terms of use'], privacy: ['Chính sách bảo mật', 'Privacy policy']
  };
  function index(l) {
    var D = window.PHFM_DATA || {}, out = [], k = l === 'vi' ? 0 : 1, add = function (g, t, page, sub) { if (t) out.push({ g: g, t: t, p: page, s: sub || '', n: nrm(t + ' ' + (sub || '')) }); };
    Object.keys(TITLES).forEach(function (p) { add('page', TITLES[p][k], p); });
    var N = D.news || {}; [].concat(N.insights || [], N.news || []).forEach(function (x) { add('news', tx(x.t, l), 'news', x.date); });
    var A = D.academy || {}; (A.faqFull || []).forEach(function (x) { add('faq', tx(x.q, l), 'faq'); }); (A.glossFull || []).forEach(function (x) { var dd = tx(x.d, l); add('gloss', tx(x.t, l), 'glossary', dd.length > 96 ? dd.slice(0, 94).replace(/\s+\S*$/, '') + '…' : dd); });
    ((D.forms || {}).groups || []).forEach(function (g) { (g.items || []).forEach(function (x) { add('form', tx(x.t, l), 'forms', tx(g.g, l)); }); });
    ((D.ir || {}).items || []).forEach(function (x) { add('ir', tx(x.t, l), 'ir', x.date); });
    ((D.careers || {}).jobs || []).forEach(function (x) { add('job', tx(x.t, l), 'careers'); });
    return out;
  }
  var ov, inp, list, idxL, IDX;
  function build() {
    ov = document.createElement('div'); ov.className = 'phfm-search'; ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true');
    ov.innerHTML = '<div class="ps-box"><div class="ps-row"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0B6274" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input type="search" class="ps-in" autocomplete="off"><button type="button" class="ps-x">×</button></div><div class="ps-list" role="listbox"></div></div>';
    document.body.appendChild(ov); inp = ov.querySelector('.ps-in'); list = ov.querySelector('.ps-list');
    ov.addEventListener('click', function (e) { if (e.target === ov || e.target.closest('.ps-x')) close(); var it = e.target.closest('.ps-it'); if (it) { go(it.getAttribute('data-p')); } });
    inp.addEventListener('input', render);
    inp.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); if (e.key === 'Enter') { var f = list.querySelector('.ps-it'); if (f) go(f.getAttribute('data-p')); } });
  }
  function go(p) { var l = (window.__phfmRoute ? window.__phfmRoute().lang : 'vi'); close(); window.__phfmSetHash(l, p); window.scrollTo(0, 0); }
  function render() {
    var l = L(); if (idxL !== l) { IDX = index(l); idxL = l; }
    var q = nrm(inp.value).trim(), T = TX[l];
    if (!q) { list.innerHTML = ''; return; }
    var words = q.split(/\s+/), hits = IDX.filter(function (x) { return words.every(function (w) { return x.n.indexOf(w) >= 0; }); }).slice(0, 12);
    list.innerHTML = hits.length ? hits.map(function (h) { return '<button type="button" class="ps-it" data-p="' + h.p + '"><span class="ps-g">' + T.g[h.g] + '</span><span class="ps-t"></span><span class="ps-s"></span></button>'; }).join('') : '<div class="ps-none">' + T.none + '</div>';
    [].forEach.call(list.querySelectorAll('.ps-it'), function (b, i) { b.querySelector('.ps-t').textContent = hits[i].t; b.querySelector('.ps-s').textContent = hits[i].s; });
  }
  function open(q) {
    if (!ov) build(); var T = TX[L()]; inp.placeholder = T.ph; ov.querySelector('.ps-x').setAttribute('aria-label', T.close);
    ov.classList.add('on'); inp.value = q || ''; render(); setTimeout(function () { inp.focus(); }, 30);
  }
  function close() { if (ov) ov.classList.remove('on'); }
  window.__phfmSearch = open;
  document.addEventListener('keydown', function (e) {
    var t = e.target; if (e.key === 'Enter' && t && t.matches && t.matches('.tb-search input')) { e.preventDefault(); open(t.value); t.value = ''; }
  });
  document.addEventListener('click', function (e) {
    var t = e.target; if (!t || !t.closest) return;
    var b = t.closest('.th-burg button'); if (b && b === b.parentElement.firstElementChild) { e.preventDefault(); open(''); }
  });
  document.addEventListener('focusin', function (e) { var t = e.target; if (t && t.matches && t.matches('.tb-search input')) { t.blur(); open(''); } });

  // ---------- Ban lãnh đạo (Về chúng tôi): bấm cả thẻ để xem thông tin ----------
  var lm;
  function ldOpen(card) {
    if (!lm) {
      lm = document.createElement('div'); lm.className = 'ld-modal'; lm.innerHTML = '<div class="ld-box" role="dialog" aria-modal="true"><button type="button" class="ld-x">×</button><div class="ld-top"><div class="ld-ini"></div><div><div class="ld-n"></div><div class="ld-r"></div></div></div><div class="ld-edu"></div><p class="ld-p"></p></div>';
      document.body.appendChild(lm);
      lm.addEventListener('click', function (e) { if (e.target === lm || e.target.closest('.ld-x')) ldClose(); });
    }
    var kids = card.children, q = function (s) { return lm.querySelector(s); };
    q('.ld-ini').textContent = (kids[0] && kids[0].textContent || '').trim();
    q('.ld-n').textContent = (kids[1] && kids[1].textContent || '').trim();
    q('.ld-r').textContent = (kids[2] && kids[2].textContent || '').trim();
    var edu = card.querySelector('.ld-bio') ? card.querySelector('.ld-bio').previousElementSibling : null;
    q('.ld-edu').innerHTML = ''; if (edu && edu !== kids[2]) [].forEach.call(edu.children, function (c) { var d = document.createElement('div'); d.textContent = c.textContent.trim(); if (d.textContent) q('.ld-edu').appendChild(d); });
    q('.ld-p').textContent = (card.querySelector('.ld-bio') || {}).textContent || '';
    q('.ld-x').setAttribute('aria-label', L() === 'vi' ? 'Đóng' : 'Close');
    lm.classList.add('on'); document.documentElement.style.overflow = 'hidden'; q('.ld-x').focus(); lm.__from = card;
  }
  function ldClose() { if (!lm) return; lm.classList.remove('on'); document.documentElement.style.overflow = ''; if (lm.__from) lm.__from.focus(); }
  document.addEventListener('click', function (e) { var c = e.target.closest && e.target.closest('.ld-card'); if (c) ldOpen(c); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') ldClose();
    var t = e.target; if ((e.key === 'Enter' || e.key === ' ') && t && t.matches && t.matches('.ld-card,.nm-mgr')) { e.preventDefault(); t.click(); }
  });
})();
</script>
