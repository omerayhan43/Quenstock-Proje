# -*- coding: utf-8 -*-
"""ORIJINAL ve ADAY Buyume (BISTTUM) formullerini cok sayida anlam modelinde karsilastirir."""
import math, os, random, struct, sys, json, time, itertools
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dil import parse, compile_prog, Model, Hata, ALANLAR

D = os.path.dirname(os.path.abspath(__file__))
def oku(f):
    return open(os.path.join(D, f), encoding='utf-8').read()

KUTULAR = ['temel', 'siralama', 'teknik']
AST = {(s, k): parse(oku('%s_%s.txt' % (s, k))) for s in ('orig', 'aday') for k in KUTULAR}

# ---------------- rastgele hisse uretici ----------------
NORMAL = {
    'ROE0': (-100, 200), 'ROE1': (-100, 200), 'ROE4': (-100, 200),
    'PDDD': (-2, 20), 'G2a': (-80, 300), 'G2aX': (-30, 60), 'G1a': (-60, 100), 'HA': (0, 100),
    'G12a': (-80, 800), 'G2h': (-40, 80), 'G2hX': (-20, 40), 'SATISB': (-100, 300), 'TUFE': (0, 90),
    'FAVOKB': (-200, 400), 'BRUTB': (-200, 400), 'EFKB': (-300, 600), 'EFKB1': (-300, 600),
    'Z': (0.2, 1.05), 'R75': (0.5, 2.0), 'M6': (0.1, 3.5),
}
BUYUK = {'FAVOKY', 'NETBORC', 'NKY', 'PD', 'F0', 'F1', 'F4', 'B0', 'B1', 'B4', 'E0', 'E1', 'E4'}
FIYAT = {'C', 'MA200', 'MA75', 'MA20', 'MA60'}
OZEL = {
    'ROE0': [5.0, 90.0, 5.000000000000001, 4.999999999999999, 90.00000000000001, 100.0, 120.0, -5.0],
    'ROE1': [5.0, 90.0], 'ROE4': [5.0, 90.0],
    'PDDD': [8.0, 7.999999999999999, 8.000000000000002, 8.7, 10.1, 0.0],
    'G1a': [-15.0, -15.000000000000002, -14.999999999999998],
    'G12a': [300.0, 300.00000000000006],
    'HA': [60.0, 59.99999999999999],
    'R75': [1.35, 1.3500000000000003, 1.3499999999999999],
    'M6': [2.0, 0.0, 1.0, 2.0000000000000004, 1.9999999999999998, 4.440892098500626e-16],
    'Z': [1.0, 0.0, 0.9135, 1.0000000000000002],
    'TUFE': [12.0, 50.0], 'G2hX': [10.0, 0.0], 'G2h': [0.0, -10.0],
    'PD': [40.0, 1e9], 'NKY': [1.0, 2.5e7],
}
EKSTREM = [1e300, -1e300, 1.7976931348623157e308, -1.7976931348623157e308, 5e-324, -5e-324,
           1e-300, -1e-300, 1e15, -1e15, 2.2250738585072014e-308]
GENEL_OZEL = [1.0, -1.0, 0.5, 100.0, 2.0, 10.0, 0.1, 0.7, 0.6, 0.0865]

def normal(r, f):
    if f in BUYUK:
        v = 10 ** r.uniform(0, 11)
        if r.random() < 0.3: v = -v
        if r.random() < 0.3: v = float(round(v))
        return v
    if f in FIYAT:
        return 10 ** r.uniform(-1, 3)
    lo, hi = NORMAL[f]
    v = r.uniform(lo, hi)
    if r.random() < 0.3: v = round(v, 2)
    return v

GECER = {  # Temel/Teknik/oncelik'i gecmeye egilimli araliklar
    'ROE0': (5, 150), 'ROE1': (-20, 120), 'ROE4': (-20, 120), 'PDDD': (0.1, 9), 'G2a': (5, 60), 'G2aX': (-10, 20),
    'G1a': (-16, 40), 'HA': (10, 65), 'G12a': (0, 320), 'G2h': (-5, 30), 'G2hX': (-5, 15), 'SATISB': (20, 150),
    'TUFE': (20, 70), 'FAVOKB': (10, 200), 'BRUTB': (10, 200), 'EFKB': (10, 200), 'EFKB1': (0, 150),
    'Z': (0.7, 1.0), 'R75': (0.9, 1.5), 'M6': (0.6, 2.5)}

def gecer_deger(r, f, d):
    if f == 'FAVOKY': return 10 ** r.uniform(6, 10)
    if f == 'NETBORC': return r.uniform(-2, 4.2) * (d.get('FAVOKY') or 1e8)
    if f == 'PD': return 10 ** r.uniform(8, 11)
    if f == 'NKY': return r.uniform(0.0, 0.2) * (d.get('PD') or 1e9)
    if f in BUYUK:
        return 10 ** r.uniform(6, 10) * (1 if r.random() < 0.85 else -1)
    if f in FIYAT:
        return 10 ** r.uniform(0, 3)
    lo, hi = GECER[f]
    v = r.uniform(lo, hi)
    return round(v, 2) if r.random() < 0.4 else v

def hisse(r, sonsuz=False):
    pnull = r.uniform(0.10, 0.30)
    egilim = r.random() < 0.5
    d = {}
    for f in ALANLAR:
        x = r.random()
        if x < pnull:
            d[f] = None; continue
        if egilim and r.random() < 0.75:
            d[f] = gecer_deger(r, f, d); continue
        y = r.random()
        if y < 0.06:
            d[f] = -0.0 if r.random() < 0.3 else 0.0
        elif y < 0.24:
            d[f] = r.choice(OZEL.get(f, GENEL_OZEL) + GENEL_OZEL[:3])
        elif y < 0.28:
            d[f] = r.choice(EKSTREM)
        elif sonsuz and y < 0.30:
            d[f] = r.choice([float('inf'), float('-inf'), float('nan')])
        else:
            d[f] = normal(r, f)
    # esitlik / esik iliskileri
    def p(q=0.12):
        return r.random() < q
    if p(): d['ROE1'] = d['ROE0']
    if p(): d['ROE4'] = d['ROE0']
    if p() and d['ROE0'] is not None and d['ROE0'] > 90:
        d['PDDD'] = 8 + (d['ROE0'] - 90) * 0.07
    if p():
        if d['FAVOKY'] is not None: d['NETBORC'] = 4 * d['FAVOKY']
    if p():
        if r.random() < 0.5: d['NKY'], d['PD'] = 1.0, 40.0
        elif d['PD'] is not None: d['NKY'] = 0.025 * d['PD']
    if p(): d['G2aX'] = d['G2a']
    if p() and d['G2h'] is not None: d['G2hX'] = d['G2h'] + 10
    for a in ('SATISB', 'FAVOKB', 'BRUTB', 'EFKB'):
        if p(0.08): d[a] = d['TUFE']
    for x0, x1, x4 in (('F0', 'F1', 'F4'), ('B0', 'B1', 'B4'), ('E0', 'E1', 'E4')):
        if p(): d[x1] = d[x0]
        if p(): d[x4] = d[x0]
    if p(): d['EFKB1'] = d['EFKB']
    if p(0.08): d['E4'] = r.choice([0.0, -0.0])
    if p(0.08): d['F4'] = r.choice([0.0, -0.0])
    if p(0.05): d['PD'] = 0.0
    if p(0.05): d['FAVOKY'] = 0.0
    if p(): d['MA200'] = d['C']
    if p(): d['MA75'] = d['C']
    if p(): d['MA60'] = d['MA20']
    return d

# ---------------- karsilastirma ----------------
def bits(v):
    if v is None: return 'NULL'
    if v is True or v is False: return 'BOOL:%s' % v
    if v != v: return 'NaN'
    return struct.pack('>d', v).hex()

def calistir(f, d):
    try:
        return f(d)
    except Hata as e:
        return 'HATA'

def gecti(v):
    return v is True

def esit_skor(a, b):
    if a == 'HATA' or b == 'HATA':
        return a == b
    return bits(a) == bits(b)

def derle(M, kaynak='orig'):
    return {k: compile_prog(AST[(kaynak, k)], M) for k in KUTULAR}

# ---------------- en kucuk ornek ----------------
def uyumsuz(fo, fa, d):
    out = []
    for k in KUTULAR:
        a = calistir(fo[k], d); b = calistir(fa[k], d)
        if k == 'siralama':
            if not esit_skor(a, b): out.append(k)
        else:
            if gecti(a) != gecti(b): out.append(k)
    return out

def _rank(v):
    if v is None: return 0
    if v == 0.0: return 1
    if v == 1.0: return 2
    return 3

def kucult(fo, fa, d):
    """Alanlari sirayla daha 'basit' degere (null < 0 < 1 < diger) cekerek uyumsuzlugu koruyan en kucuk ornegi bul."""
    d = dict(d)
    hedef = set(uyumsuz(fo, fa, d))
    degisti = True
    while degisti:
        degisti = False
        for f in ALANLAR:
            for aday in (None, 0.0, 1.0):
                if _rank(aday) >= _rank(d[f]):
                    continue
                e = dict(d); e[f] = aday
                if set(uyumsuz(fo, fa, e)) & hedef:
                    d = e; degisti = True; break
    return d

def is_parcasi(arg):
    mad, seed, n, sonsuz = arg
    M = Model(*mad)
    fo, fa = derle(M, 'orig'), derle(M, 'aday')
    r = random.Random(seed)
    st = {'n': 0, 'temel_fark': 0, 'teknik_fark': 0, 'skor_fark': 0,
          'temel_gecen': 0, 'temel_kalan': 0, 'temel_hata_vs_false': 0, 'temel_hata_ikisi': 0,
          'teknik_gecen': 0, 'skor_hata_ikisi': 0, 'skor_nan_ikisi': 0, 'skor_null_ikisi': 0,
          'skor_1000plus': 0, 'ornekler': []}
    for i in range(n):
        d = hisse(r, sonsuz)
        st['n'] += 1
        to, ta = calistir(fo['temel'], d), calistir(fa['temel'], d)
        if gecti(to) != gecti(ta):
            st['temel_fark'] += 1
            if len(st['ornekler']) < 3: st['ornekler'].append(('temel', d, repr(to), repr(ta)))
        else:
            st['temel_gecen' if gecti(to) else 'temel_kalan'] += 1
            if (to == 'HATA') != (ta == 'HATA'): st['temel_hata_vs_false'] += 1
            elif to == 'HATA': st['temel_hata_ikisi'] += 1
        ko, ka = calistir(fo['teknik'], d), calistir(fa['teknik'], d)
        if gecti(ko) != gecti(ka):
            st['teknik_fark'] += 1
        elif gecti(ko):
            st['teknik_gecen'] += 1
        so, sa = calistir(fo['siralama'], d), calistir(fa['siralama'], d)
        if not esit_skor(so, sa):
            st['skor_fark'] += 1
            if len(st['ornekler']) < 3: st['ornekler'].append(('siralama', d, repr(so), repr(sa)))
        else:
            if so == 'HATA': st['skor_hata_ikisi'] += 1
            elif so is None: st['skor_null_ikisi'] += 1
            elif so != so: st['skor_nan_ikisi'] += 1
            elif so >= 1000: st['skor_1000plus'] += 1
    return mad, st

def birlestir(parcalar):
    top = {}
    for mad, st in parcalar:
        t = top.setdefault(mad, {'ornekler': []})
        for k, v in st.items():
            if k == 'ornekler': t['ornekler'] += v
            else: t[k] = t.get(k, 0) + v
    return top

TEMEL_MODELLER = [(nl, bl, mt, 'yok') for nl in ('G3', 'YAY') for bl in ('null', 'ieee', 'hata') for mt in ('hevesli', 'kisa')]
EK_MODELLER = [(nl, bl, mt, at) for nl in ('G3', 'YAY') for bl in ('null', 'ieee', 'hata') for mt in ('hevesli', 'kisa')
               for at in ('nan2null', 'sonsuz2null', 'null2sifir')]

def main():
    N = int(os.environ.get('N', '200000'))
    PARCA = 8
    t0 = time.time()
    rapor = {}
    for etiket, modeller, sonsuz in (('ana', TEMEL_MODELLER, False), ('ek_atama', EK_MODELLER, False),
                                     ('stres_inf_nan_girdi', TEMEL_MODELLER + EK_MODELLER, True)):
        n = N if etiket != 'stres_inf_nan_girdi' else max(N // 4, 20000)
        isler = []
        for mi, mad in enumerate(modeller):
            for p in range(PARCA):
                isler.append((mad, hash((etiket, mi, p)) & 0xffffffff if False else (mi * 1000 + p + (7 if sonsuz else 0) * 100000 + (3 if etiket == 'ek_atama' else 0) * 10000000), n // PARCA, sonsuz))
        with Pool(os.cpu_count()) as pool:
            sonuc = birlestir(pool.map(is_parcasi, isler))
        rapor[etiket] = sonuc
        print('==== %s (her modelde %d hisse) [%.0fs]' % (etiket, n, time.time() - t0), flush=True)
        for mad, st in sonuc.items():
            print('%-34s temelFark=%d teknikFark=%d skorFark=%d | temelGecen=%d temelKalan=%d (HATA<->false=%d, ikisiHATA=%d) teknikGecen=%d skor1000+=%d skorHATA=%d skorNaN=%d skorNull=%d' % (
                '/'.join(mad), st['temel_fark'], st['teknik_fark'], st['skor_fark'], st['temel_gecen'], st['temel_kalan'],
                st['temel_hata_vs_false'], st['temel_hata_ikisi'], st['teknik_gecen'], st['skor_1000plus'],
                st['skor_hata_ikisi'], st['skor_nan_ikisi'], st['skor_null_ikisi']), flush=True)
    json.dump({e: {'/'.join(m): {k: v for k, v in st.items() if k != 'ornekler'} for m, st in s.items()} for e, s in rapor.items()},
              open(os.path.join(D, 'sonuc_ozet.json'), 'w'), indent=1)
    # en kucuk ornekler
    print('\n==== UYUMSUZLUK ORNEKLERI (kucultulmus) ====', flush=True)
    for etiket, sonuc in rapor.items():
        for mad, st in sonuc.items():
            for kutu, d, a, b in st['ornekler'][:1]:
                M = Model(*mad)
                fo, fa = derle(M, 'orig'), derle(M, 'aday')
                k = kucult(fo, fa, d)
                izo, iza = {}, {}
                try: so = fo['siralama'](k, izo)
                except Hata: so = 'HATA'
                try: sa = fa['siralama'](k, iza)
                except Hata: sa = 'HATA'
                print('\n[%s] %s kutu=%s' % (etiket, '/'.join(mad), kutu))
                print('  kucuk ornek (null olmayan alanlar; digerleri null):',
                      {f: v for f, v in k.items() if v is not None})
                print('  orig sonuc:', repr(so), ' aday sonuc:', repr(sa))
                print('  orig iz:', {x: izo[x] for x in ('xE', 'xF', 'pE', 'pF', 'pR', 'pI', 'pZ', 'karIvmesi', 'SKOR', 'tam') if x in izo})
                print('  aday iz:', {x: iza[x] for x in ('efkArtis', 'favokArtis', 'puanToplami', 'oncelik') if x in iza})
                izo, iza = {}, {}
                try: to = fo['temel'](k, izo)
                except Hata: to = 'HATA'
                try: ta = fa['temel'](k, iza)
                except Hata: ta = 'HATA'
                print('  TEMEL orig:', repr(to), {x: izo.get(x) for x in ('a', 'b', 'd', 'epv', 'ucuz')}, ' aday:', repr(ta), {x: iza.get(x) for x in ('karlilik', 'borc', 'ucuzluk')}, flush=True)
    json.dump({e: {'/'.join(m): {k: v for k, v in st.items() if k != 'ornekler'} for m, st in s.items()} for e, s in rapor.items()},
              open(os.path.join(D, 'sonuc_ozet.json'), 'w'), indent=1)
    print('\nToplam sure %.0fs' % (time.time() - t0))

if __name__ == '__main__':
    main()
