  // ---- B01 + B02: MỘT nguồn số cho mọi khối của trang quỹ ----
  // DEV: thay phần sinh chuỗi minh hoạ bên dưới bằng chuỗi NAV thật lấy từ CMS (mỗi ngày giao dịch 1 dòng: ngày, NAV/CCQ, chỉ số tham chiếu).
  //      PHFM_ASOF = ngày của dòng số liệu mới nhất, KHÔNG phải ngày người xem mở trang.
  //      Mọi con số (hero, bảng hiệu quả, biểu đồ, lịch sử NAV, danh sách quỹ) đều tính từ chuỗi này nên luôn khớp nhau.
  fundCalc(p) {
    if (!this._fc) this._fc = {};
    if (this._fc[p]) return this._fc[p];
    const D = window.PHFM_DATA, F = D.funds[p], ASOF = window.PHFM_ASOF;
    const A = (window.PHFM_ANCHORS || {})[p];
    const ds = []; { const dt = new Date(A.start + 'T00:00:00Z'), end = new Date(ASOF + 'T00:00:00Z'); while (dt <= end) { const wd = dt.getUTCDay(); if (wd && wd < 6) ds.push(dt.toISOString().slice(0, 10)); dt.setUTCDate(dt.getUTCDate() + 1); } }
    const N = ds.length, onOrBefore = d => { let i = N - 1; while (i > 0 && ds[i] > d) i--; return i; };
    const prevDay = d => { const x = new Date(d + 'T00:00:00Z'); x.setUTCDate(x.getUTCDate() - 1); return x.toISOString().slice(0, 10); };
    const iY = onOrBefore((+ASOF.slice(0, 4) - 1) + '-12-31'), iM = onOrBefore(prevDay(ASOF.slice(0, 8) + '01'));
    const mk = (seed, vol, t) => {
      let s = seed; const rnd = () => { s = (s * 9301 + 49297) % 233280; return s / 233280; };
      const r = [0]; for (let i = 1; i < N; i++) r.push((rnd() - .5) * 2 * vol);
      const L = x => Math.log(1 + x / 100), end = L(t.si);
      const anchors = [[0, 0]];
      if (t.ytd != null && iY > 0) anchors.push([iY, end - L(t.ytd)]);
      if (t.mtd != null && iM > iY) anchors.push([iM, end - L(t.mtd)]);
      if (t.day != null) anchors.push([N - 2, end - L(t.day)]);
      anchors.push([N - 1, end]);
      for (let k = 1; k < anchors.length; k++) { const [a, la] = anchors[k - 1], [b, lb] = anchors[k]; let sum = 0; for (let i = a + 1; i <= b; i++) sum += r[i]; const adj = ((lb - la) - sum) / (b - a); for (let i = a + 1; i <= b; i++) r[i] += adj; }
      const V = []; let acc = 0; for (let i = 0; i < N; i++) { acc += r[i]; V.push(Math.exp(acc)); } return V;
    };
    const V = [mk(A.seed[0], A.vol[0], A.fund), mk(A.seed[1], A.vol[1], A.bench)];
    const navEnd = parseFloat(F.nav.replace(/\./g, '').replace(',', '.')), vEnd = V[0][N - 1];
    const nav = V[0].map(v => navEnd * v / vEnd);
    const shiftDate = (m, y) => { const e = new Date(ASOF + 'T00:00:00Z'); if (y) e.setUTCFullYear(e.getUTCFullYear() - y); else e.setUTCMonth(e.getUTCMonth() - m); return e.toISOString().slice(0, 10); };
    const startIdx = d => { const i = ds.findIndex(x => x >= d); return i < 0 ? 0 : i; };
    // kỳ: [nhãn, ngày bắt đầu]; null = quỹ chưa đủ lịch sử cho kỳ này
    const per = {
      d1: N - 2, m1: shiftDate(1) >= ds[0] ? startIdx(shiftDate(1)) : null, m3: shiftDate(3) >= ds[0] ? startIdx(shiftDate(3)) : null,
      m6: shiftDate(6) >= ds[0] ? startIdx(shiftDate(6)) : null, ytd: iY > 0 ? iY : 0, y1: shiftDate(0, 1) >= ds[0] ? startIdx(shiftDate(0, 1)) : null,
      y3: shiftDate(0, 3) >= ds[0] ? startIdx(shiftDate(0, 3)) : null, si: 0, mtd: iM
    };
    const ret = (k, j) => per[k] == null ? null : (V[j][N - 1] / V[j][per[k]] - 1) * 100;
    // giá đóng cửa ETF = NAV × (1 + chênh lệch) ; chênh lệch minh hoạ cố định theo ngày
    const pdOf = i => ((((N - 1 - i) * 17 + 3) % 7) - 3) / 10;
    const out = { ds, V, nav, N, ret, per, pdOf, iY, asOf: ASOF };
    this._fc[p] = out; return out;
  }
  pct(v, dec, arrow) { if (v == null || isNaN(v)) return '—'; const a = Math.abs(v); const s = (v >= 0 ? '+' : '−') + this.fmt(a, dec) + '%'; return arrow ? (v >= 0 ? '▲ ' : '▼ ') + s : s; }
