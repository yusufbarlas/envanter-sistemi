import hatalar

def listele(envanter):
    for envtr in envanter.items():
        print(f'{envtr[0]} , {envtr[1]}')
    print(f'Toplam ürün sayisi: {len(envanter)}')

def urun_ekle(envanter, ad, stok, fiyat, kategori):
    if ad in envanter:
        raise hatalar.UrunZatenVarError('Urun zaten var...')
    if stok < 0  or fiyat < 0:
        raise ValueError('stok eksiiye düşemez...')
    
    envanter[ad] = {'stok': stok , 'fiyat' : fiyat , 'kategori' : kategori}


def stok_giris(envanter, ad, miktar):

    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    if miktar <= 0 :
        raise ValueError('Stok ve fiyat 0 dan küçük olamaz') 
    else :
        envanter[ad]['stok'] += miktar


def stok_cikis(envanter, ad, miktar):

    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    elif miktar <= 0 :
        raise ValueError('Miktar 0 veya eksi olamaz')
    elif miktar > envanter[ad]['stok']:
        raise hatalar.YetersizStokError('Stok yetersiz...')
    else:
        envanter[ad]['stok'] -= miktar

def urun_sil(envanter, ad):
    if ad not in envanter:
        raise hatalar.UrunBulunamadiError('Urun bulunamadi...')
    else:
        del envanter[ad]


def toplam_deger(envanter):
    toplam = 0 
    for satir in envanter:
        urun = envanter[satir]
        toplam += urun['fiyat'] * urun['stok']
    return toplam    


    
    
    