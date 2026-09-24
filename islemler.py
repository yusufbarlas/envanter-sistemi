def listele(envanter):
    for envtr in envanter.items():
        print(f'{envtr[0]} , {envtr[1]}')
    print(f'Toplam ürün sayisi: {len(envanter)}')

def urun_ekle(envanter, ad, stok, fiyat, kategori):
    envanter[ad] = {'stok': stok , 'fiyat' : fiyat , 'kategori' : kategori}
    