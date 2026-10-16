class EnvanterSistemiError(Exception):
    """üst kategori"""
     

class UrunBulunamadiError(EnvanterSistemiError):
    """Urun yoksa devreye girer."""
    

class UrunZatenVarError(EnvanterSistemiError):
    """ Urun varsa devreye girer."""
    

class YetersizStokError(EnvanterSistemiError):
    """Stok çıkışında miktar > stok anında hata verir"""
    

class NegatifDegerError(EnvanterSistemiError):
    """stok yada fiyat negatifse devreye girer"""
    

if __name__ == '__main__':
   
    try:
        raise NegatifDegerError('Negatif değer saptandı, işlem başarısız')
    except EnvanterSistemiError as e:
        print('Yakalandı:', e)

    