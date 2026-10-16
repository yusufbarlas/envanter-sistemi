import json
from dataclasses import asdict
from decimal import Decimal
import islemler


def envanter_kaydet(dosya_adi, envanter):
    """Envanteri JSON dosyasına kaydeder.

    Parametreler:
        dosya_adi (str): Yazılacak dosyanın adı.
        envanter (dict): {ad: Urun} sözlüğü.

    Döndürür:
        None. Ad sadece anahtarda tutulur, fiyat metin olarak yazılır.
    """
    kayit_verisi = {}
    for ad, urun in envanter.items():
        urun_bilgisi = asdict(urun)
        del urun_bilgisi['ad']
        urun_bilgisi['fiyat'] = str(urun.fiyat)
        kayit_verisi[ad] = urun_bilgisi

    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(kayit_verisi, f, ensure_ascii=False, indent=4)


def envanter_yukle(dosya_adi, baslangic_verisi):
    """JSON dosyasından envanteri yükler.

    

    Parametreler:
        dosya_adi (str): Okunacak dosyanın adı.
        baslangic_verisi (dict): Dosya yoksa kullanılacak
            {ad: {stok, fiyat, kategori}} sözlüğü.

    Döndürür:
        dict: {ad: Urun} sözlüğü.
    """
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            ham_veri = json.load(f)
    except FileNotFoundError:
        ham_veri = baslangic_verisi

    envanter = {}
    for ad, urun_bilgisi in ham_veri.items():
        fiyat = islemler.tutar_yuvarla(Decimal(str(urun_bilgisi['fiyat'])))
        envanter[ad] = islemler.Urun(
            ad, urun_bilgisi['stok'], fiyat, urun_bilgisi['kategori']
        )

   
    return envanter