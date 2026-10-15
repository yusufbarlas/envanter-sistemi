import hatalar
from dataclasses import dataclass
from decimal import Decimal , ROUND_HALF_UP


@dataclass
class Urun:
    ad:str 
    stok:int
    fiyat:Decimal
    kategori:str

    def stok_giris(self , miktar):
        if miktar <= 0:
            raise hatalar.NegatifDegerError('Miktar 0 veya negatif değer olamaz...')
        else:
            self.stok += miktar 

    def stok_cikis(self , miktar):
        if miktar <= 0:
            raise hatalar.NegatifDegerError('Miktar 0 veya negatif değer olamaz...')
        elif miktar > self.stok:
            raise hatalar.YetersizStokError('Miktar stoktan fazla olamaz...')
        else:
            self.stok -= miktar

    def deger(self):
        price = self.fiyat * self.stok
        sonuc = Decimal(price).quantize(Decimal('0.01') , rounding=ROUND_HALF_UP)
        return sonuc


def urun_bul(envanter , ad):
    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    return envanter[ad]

def urun_ekle(envanter, ad, stok, fiyat, kategori):
    if ad in envanter:
        raise hatalar.UrunZatenVarError('Urun zaten var...')
    elif stok < 0 or fiyat < 0 :
        raise hatalar.NegatifDegerError('Stok veya Fiyat negatif değer alamaz...')
    else:
         envanter[ad] = Urun(ad ,  stok ,  fiyat ,  kategori)

def urun_sil(envanter , ad):
    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    del envanter[ad]

def toplam_deger(envanter):
    toplam = 0
    for ad , degerler in envanter.items():
        fiyatlar = degerler.deger()
        toplam += fiyatlar
    sonuc = Decimal(toplam).quantize(Decimal('0.01') , rounding=ROUND_HALF_UP)
    return sonuc

def listele(envanter):
    for ad, urun in envanter.items():
        print(f'{urun.ad} | Stok: {urun.stok} | Fiyat: {urun.fiyat} TL | Kategori: {urun.kategori}')
    print(f'Toplam ürün sayisi: {len(envanter)}')
   
    




    









































