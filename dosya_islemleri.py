import json 
from dataclasses import dataclass , asdict
from decimal import Decimal , ROUND_HALF_UP
import islemler

def envanter_kaydet(dosya_adi , envanter):
    szlk = {}
   
    for ad , urun in envanter.items():
            urun_sozlugu = asdict(urun)
            del urun_sozlugu['ad']
            urun_sozlugu['fiyat'] = str(urun.fiyat)
            szlk[ad] = urun_sozlugu
    with open (dosya_adi , 'w' , encoding='utf-8') as f:
        json.dump(szlk , f , ensure_ascii=False , indent=4)


def envanter_yukle(dosya_adi, baslangic_verisi):

    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            ham = json.load(f)                      # 1. dosyayı oku
    except FileNotFoundError:
        ham = baslangic_verisi      
    szlk = {}
    for ad , sözlük in ham.items():
          fiyat = str(sözlük['fiyat'])
          prices = Decimal(fiyat).quantize(Decimal('0.01') , rounding= ROUND_HALF_UP)
          szlk[ad] = islemler.Urun(ad , sözlük['stok'] , prices , sözlük['kategori'])
    envanter_kaydet(dosya_adi, szlk)
    return  szlk 


     

    
    
