# -*- coding: utf-8 -*-
"""Deger (BISTTUM) ORIJINAL vs ADAY: cok modelli rastgele karsilastirma. Kullanim: python3 dfuzz.py [aday_onek] [n]"""
import math, random, struct, sys, os, time
from multiprocessing import Pool
from ddil import parse, compile_prog, Model, Hata

D = os.path.dirname(os.path.abspath(__file__))
ONEK = sys.argv[1] if len(sys.argv) > 1 else 'aday'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
def oku(f): return open(os.path.join(D, f), encoding='utf-8').read()
AST = {(s, k): parse(oku('%s_%s.txt' % (s, k))) for s, k in [('orig', 'temel'), ('orig', 'siralama'), (ONEK, 'temel'), (ONEK, 'siralama')]}
ALANLAR = set()
for a in AST.values(): compile_prog(a, Model(), ALANLAR)
ALANLAR = sorted(ALANLAR)

ESIK = [-100.0, 300.0, -15.0, 5.0, 90.0, 4.0, 1.35, -10.0, 0.0, 0.22, 50.0, 40.0, 8.0, 1.5, 0.7, 0.70, 0.5, 15.0, 3.0, 2.0, 0.15, 0.08, 30.0, 1.0, -1.0, 9.0, 7.0, 60.0,
        0.036716, 0.050129, 0.082663, 0.128810, 0.192415, 0.298789, 0.401334, 0.802668]
KNOT_INV = [1.0]
def aralik(ad):
    if ad.startswith(('NetKarYillik', 'FAVOK(', 'FAVOKYillik', 'NetIsletmeSermayesi', 'NetBorc', 'EFK(', 'BrutEFK(')): return 'buyuk'
    if ad.startswith('PD('): return 'pozbuyuk'
    if ad.startswith(('ToplamBorc', 'Aktifler(')): return 'pozbuyuk'
    if ad.startswith('SermayeArtisBedelliTarihi') or ad == 'AnalizTarih': return 'tarih'
    if ad.startswith(('Kapanis', 'Mov(')): return 'fiyat'
    return 'oran'
ORAN = {'AktifKarlilikYillik': (-50, 50), 'CariOran': (0, 5), 'BrutKarMarji': (-50, 80), 'AktifDevirHizi': (0, 3),
        'FDFAVOK': (-5, 30), 'Getiri': (-80, 500), 'FK': (-50, 120), 'NetSatisBuyumeYillik': (-100, 300),
        'Teknik.Indicator(C/LLV': (0.9, 4), 'Teknik.Indicator(C/HHV': (0.2, 1.05), 'PDDD': (-2, 20), 'HAOran': (0, 100),
        'PDNakitAkis': (-30, 60), 'Teknik.Indicator(': (0.3, 2.5), 'OzsermayeKarlilikYillik': (-100, 200), 'Tufe': (0, 90), 'EFKBuyumeYillik': (-300, 600), 'FAVOKBuyumeYillik': (-200, 400), 'BrutEFKBuyumeYillik': (-200, 400), 'HAOran': (0, 100)}
def deger(r, ad, d):
    x = r.random()
    if x < 0.12: return None
    if x < 0.16: return 0.0
    tur = aralik(ad)
    if tur == 'buyuk':
        v = 10 ** r.uniform(3, 11); return -v if r.random() < 0.3 else v
    if tur == 'pozbuyuk':
        return 10 ** r.uniform(3, 11) * (1 if r.random() < 0.97 else -1)
    if tur == 'tarih':
        return float(r.randint(0, 8000))
    if tur == 'fiyat':
        return 10 ** r.uniform(-1, 3)
    if x < 0.30:
        if ad.startswith('PDNakitAkis'): return r.choice(KNOT_INV + [0.0, -1.0, 1.0])
        return r.choice(ESIK)
    for k, (lo, hi) in ORAN.items():
        if ad.startswith(k):
            v = r.uniform(lo, hi); return round(v, 2) if r.random() < 0.4 else v
    return r.uniform(-100, 100)
EKSTREM = [1e300, -1e300, 5e-324, -5e-324, 1e-300, float('inf'), float('-inf')]
def hisse(r, ekstrem):
    d = {a: deger(r, a, None) for a in ALANLAR}
    # cifti esitle (s3, s5, s6, s7, s8 esitlikleri)
    for a in ALANLAR:
        if '-4' in a and r.random() < 0.1:
            b = a.replace('null,-4.0', '').replace('-4.0', '').replace('(,', '(').replace(',)', ')')
            if b in d: d[a] = d[b]
    if r.random() < 0.15:  # gecmeye egilim: F-skor maddeleri saglansin
        for a in ALANLAR:
            if a.endswith('(null,-4.0)') or a.endswith('(-4.0)'):
                b = a.split('(')[0] + '()'
                if b in d and d[b] is not None and r.random() < 0.85:
                    d[a] = d[b] - abs(r.uniform(0.01, 5)) if not a.startswith('ToplamBorc') else d[b] * 2
    if ekstrem:
        for a in ALANLAR:
            if r.random() < 0.05: d[a] = r.choice(EKSTREM)
    return d
def bits(v):
    if v is None: return 'null'
    if v is True or v is False: return str(v)
    if isinstance(v, float) and v != v: return 'nan'
    return struct.pack('>d', float(v)).hex()
def calis(f, d):
    try: return bits(f(d))
    except Hata: return 'HATA'
    except ZeroDivisionError: return 'HATA'
ATAMA = ['yok', 'nan2null', 'sonsuz2null', 'null2sifir', 'float32', 'yuvarla6']
MODELLER = [(nl, bl, mt, at) for nl in ('G3', 'YAY') for bl in ('null', 'ieee', 'hata') for mt in ('kisa', 'hevesli') for at in ATAMA]
def is_(arg):
    m, tohum, n, ekstrem = arg
    M = Model(*m); r = random.Random(tohum)
    F = {k: compile_prog(a, M) for k, a in AST.items()}
    st = {'temel': 0, 'skor': 0, 'gecen': 0, 'ornek': None}
    for _ in range(n):
        d = hisse(r, ekstrem)
        to, ta = calis(F[('orig', 'temel')], d), calis(F[(ONEK, 'temel')], d)
        so, sa = calis(F[('orig', 'siralama')], d), calis(F[(ONEK, 'siralama')], d)
        if to == 'True': st['gecen'] += 1
        if to != ta: st['temel'] += 1; st['ornek'] = st['ornek'] or ('temel', to, ta, {k: v for k, v in d.items() if v is not None})
        if to == 'True' and so != sa: st['skor'] += 1; st['ornek'] = st['ornek'] or ('skor', so, sa, {k: v for k, v in d.items() if v is not None})
    return m, st
if __name__ == '__main__':
    t0 = time.time()
    for etiket, ekstrem, n in (('normal', False, N), ('ekstrem', True, N // 4)):
        isler = [(m, 7000 + i * 13 + p, n // 4, ekstrem) for i, m in enumerate(MODELLER) for p in range(4)]
        with Pool(os.cpu_count()) as pool: sonuc = pool.map(is_, isler)
        top = {}
        for m, st in sonuc:
            t = top.setdefault(m, {'temel': 0, 'skor': 0, 'gecen': 0, 'ornek': None})
            for k in ('temel', 'skor', 'gecen'): t[k] += st[k]
            t['ornek'] = t['ornek'] or st['ornek']
        print('== %s: %d model x %d hisse [%.0fs]' % (etiket, len(MODELLER), n, time.time() - t0))
        for at in ATAMA:
            sel = {m: t for m, t in top.items() if m[3] == at}
            print('   atama=%-11s temelFark=%d skorFark=%d (temel gecen ort %d)' % (at, sum(t['temel'] for t in sel.values()), sum(t['skor'] for t in sel.values()), sum(t['gecen'] for t in sel.values()) // len(sel)))
        for m, t in top.items():
            if (t['temel'] or t['skor']) and m[3] in ('yok',):
                print('   !!', m, t['temel'], t['skor'], str(t['ornek'])[:600])
