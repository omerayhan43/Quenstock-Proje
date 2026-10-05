# Büyüme Stratejisi (BISTTUM) — sadeleştirilmiş kriter metni

Kaynak: K10 (kriter 98258 / yayın 98346). Hesap mantığı, kapılar ve skor değişmedi.
Doğrulama: Python yorumlayıcıyla 168 site davranış modelinde eski = yeni (skor bit düzeyinde aynı).
Kesin kanıt: site testi, son sermaye 953.463.410.572 TL.

| Kutu | Eski ifade sayısı | Yeni |
|---|---|---|
| Temel | 13 | 8 |
| Sıralama | 26 | 18 |
| Teknik | 1 | 1 (değişmedi) |

## Temel
```
roe=OzsermayeKarlilikYillik();
karVerimi=NetKarYillik()/PD();
karlilik=roe>5 and (roe>=OzsermayeKarlilikYillik("",-1) or roe>=OzsermayeKarlilikYillik("",-4));
borc=FAVOKYillik()>0 and (NetBorc()/FAVOKYillik())<4;
ucuzluk=PDDD()<IF(roe>90,8+(roe-90)*0.07,8) and karVerimi>=0.025;
fiyatGucu=Getiri("s2a","TL")>Getiri("s2a","TL","XUTUM") and Getiri("s1a","TL")>-15;
balonFreni=Getiri("s12a","TL")<=300 or PDDD()<=8;
karlilik and borc and ucuzluk and fiyatGucu and balonFreni and HAOran()<60;
```

## Sıralama
```
favokBuyuyor=FAVOKBuyumeYillik()>Tufe(12) or (FAVOK("TL",0)>FAVOK("TL",-1) and FAVOK("TL",0)>FAVOK("TL",-4));
faaliyetBuyuyor=(BrutEFKBuyumeYillik()>Tufe(12) or (BrutEFK("TL",0)>BrutEFK("TL",-1) and BrutEFK("TL",0)>BrutEFK("TL",-4))) and (EFKBuyumeYillik()>Tufe(12) or (EFK("TL",0)>EFK("TL",-1) and EFK("TL",0)>EFK("TL",-4)));
oncelik=IF(Getiri("s2h","TL")>Getiri("s2h","TL","XUTUM")-10 and NetSatisBuyumeYillik()>Tufe(12) and (faaliyetBuyuyor or favokBuyuyor) and (EFK("TL",0)>=EFK("TL",-1) or EFK("TL",0)>=EFK("TL",-4)),1,0);
efkArtis=((EFK("TL",0)-EFK("TL",-4))/Abs(EFK("TL",-4)))/0.7;
favokArtis=((FAVOK("TL",0)-FAVOK("TL",-4))/Abs(FAVOK("TL",-4)))/0.6;
roeArtis=(OzsermayeKarlilikYillik()-OzsermayeKarlilikYillik("",-1))/2;
efkHizlanma=(EFKBuyumeYillik()-EFKBuyumeYillik("",-1))/10;
zirveOrani=Teknik.Indicator("C/HHV(H,252)","d");
puanEFK=IF(efkArtis == null, -1, efkArtis/(1+Abs(efkArtis)));
puanFAVOK=IF(favokArtis == null, -1, favokArtis/(1+Abs(favokArtis)));
puanROE=IF(roeArtis == null, -1, roeArtis/(1+Abs(roeArtis)));
puanHizlanma=IF(efkHizlanma == null, -1, efkHizlanma/(1+Abs(efkHizlanma)));
puanZirve=IF(zirveOrani == null, 0, ((zirveOrani-1)/0.0865)/(1+Abs((zirveOrani-1)/0.0865)));
ort75Orani=Teknik.Indicator("C/Mov(C,75,S)","d");
momOrani=Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d");
momentumPuani=IF(momOrani == null, 0, 8*IF(momOrani-1>1, 1, IF(momOrani-1<-1, -1, momOrani-1)));
karIvmesi=100+25*(puanEFK+puanFAVOK+puanROE+puanHizlanma+puanZirve)+IF(ort75Orani == null, 0, IF(ort75Orani>1.35, -15, 0))+momentumPuani;
oncelik*1000+karIvmesi;
```
Editör son satırı kabul etmezse son satır yerine: `SKOR=oncelik*1000+karIvmesi;` ve `SKOR;`

## Teknik (değişmedi)
```
C > Mov(C,200) and
C > Mov(C,75) and
Mov(C,20)>Mov(C,60) ;
```


Not (05/10): pdddTavan, zirveMesafe ve momFark ara satırları kullanıldıkları yere yedirildi (yalnız aritmetik; veri çağrısı artmadı). Bu ve roe değişikliği, sitenin değişkenleri yuvarlamadan sakladığı varsayımına dayanır; site testi (953.463.410.572 TL) bunu doğrular.
