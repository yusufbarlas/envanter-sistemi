import hatalar
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP



def tutar_yuvarla(tutar):
    return Decimal(tutar).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


@dataclass
class Urun:
    ad: str 
    stok: int
    fiyat: Decimal
    kategori: str


    def stok_giris(self, miktar):
        """ Urunlere miktar bazinda stok girişi."""

        if miktar <= 0:
            raise hatalar.NegatifDegerError('Miktar 0 veya negatif değer olamaz...')
        else:
            self.stok += miktar 

    
    def stok_cikis(self, miktar):
        """ Urunlerden miktar bazinda stok çikişi."""

        if miktar <= 0:
            raise hatalar.NegatifDegerError('Miktar 0 veya negatif değer olamaz...')
        elif miktar > self.stok:
            raise hatalar.YetersizStokError('Miktar stoktan fazla olamaz...')
        else:
            self.stok -= miktar

    
    def deger(self):
        """Urun toplam değeri , (fiyat * stok) =>  sayi döner (decimal)"""

        toplam_urun_degeri = self.fiyat * self.stok
        sonuc = tutar_yuvarla(toplam_urun_degeri)
        return sonuc


def urun_bul(envanter, ad):
    """ Envanterden urun bulma. 
    parametre: envanter (sözlük içinde nesne) , ad (sözlüğün anahtar değeri).
    dönen anahtarin değeri .
    """

    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    return envanter[ad]

def urun_ekle(envanter, ad, stok, fiyat, kategori):
    """Envantere urun ekleme.
        parametre envanter (dict) , (ad, stok, fiyat, kategori) => nesne parametreleri
    """

    if ad in envanter:
        raise hatalar.UrunZatenVarError('Urun zaten var...')
    elif stok < 0 or fiyat < 0:
        raise hatalar.NegatifDegerError('Stok veya Fiyat negatif değer alamaz...')
    else:
         envanter[ad] = Urun(ad, stok, fiyat, kategori)

def urun_sil(envanter, ad):
    """Envanterden urun silme.
       parametre envanter (dict) {anahtar(ad): Urun(.........)}
       ad , verilen anahtar ismi silinir.
    """

    urun_bul(envanter , ad)
    del envanter[ad]

def toplam_deger(envanter):
    """Envanterdeki her ürünün, fiyat * stok (Urun.deger()) hesaplar , dönen decimal.
        parametre envanter (dict) => {ad:Urun(......)} => Urun nesnesi => urun
    """

    toplam_urun_degeri = 0
    for ad, urun in envanter.items():
        urun_deger = urun.deger()
        toplam_urun_degeri += urun_deger
    sonuc = tutar_yuvarla(toplam_urun_degeri)
    return sonuc


    




    









































