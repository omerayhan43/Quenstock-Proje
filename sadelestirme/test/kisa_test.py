# -*- coding: utf-8 -*-
"""SAGLAM oneriyi (benim_temel.txt + kisa_siralama.txt) tum modellerde ORIJINAL ile karsilastir."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multiprocessing import Pool
import fuzz
from fuzz import is_parcasi, birlestir, oku, TEMEL_MODELLER, EK_MODELLER
from dil import parse
fuzz.AST[('aday', 'temel')] = parse(oku('benim_temel.txt'))
fuzz.AST[('aday', 'siralama')] = parse(oku('kisa_siralama.txt'))
SAKLAMA = [(nl, bl, mt, at) for nl in ('G3', 'YAY') for bl in ('null', 'ieee', 'hata') for mt in ('hevesli', 'kisa')
           for at in ('float32', 'yuvarla4', 'yuvarla6')]
if __name__ == '__main__':
    t0 = time.time()
    for etiket, modeller, sonsuz, n in (('ana', TEMEL_MODELLER, False, 200000), ('ek_atama', EK_MODELLER, False, 200000),
                                        ('ek_saklama', SAKLAMA, False, 200000), ('stres_inf_nan', TEMEL_MODELLER + EK_MODELLER + SAKLAMA, True, 50000)):
        isler = [(m, 90000000 + len(etiket) * 100000 + i * 100 + p, n // 8, sonsuz) for i, m in enumerate(modeller) for p in range(8)]
        with Pool(os.cpu_count()) as pool:
            sonuc = birlestir(pool.map(is_parcasi, isler))
        top = sum(st['temel_fark'] + st['teknik_fark'] + st['skor_fark'] for st in sonuc.values())
        print('== %s: %d model x %d hisse, toplam uyumsuzluk = %d [%.0fs]' % (etiket, len(modeller), n, top, time.time() - t0), flush=True)
        for mad, st in sonuc.items():
            if st['temel_fark'] + st['teknik_fark'] + st['skor_fark']:
                print('   %-32s temelFark=%d skorFark=%d ornek=%s' % ('/'.join(mad), st['temel_fark'], st['skor_fark'],
                      {k: v for k, v in st['ornekler'][0][1].items() if v is not None}), flush=True)
