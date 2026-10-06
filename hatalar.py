class Envanter_Sistemi(Exception):
    pass 
class UrunBulunamadiError(Envanter_Sistemi):
    pass
class UrunZatenVarError(Envanter_Sistemi):
    pass
class YetersizStokError(Envanter_Sistemi):
    pass 

if __name__ == '__main__' :
    try:
        raise UrunBulunamadiError('Webcem 4K bulunamadi')
    except UrunBulunamadiError as e :
        print('Yakalandi:' , e )

    try:
        raise UrunZatenVarError('Laptop - Lenovo IdeaPad 3 zaten  var')
    except UrunZatenVarError as e :
        print('Yakalndi:' , e)

    try:
        raise YetersizStokError('Stoktan fazla çikiş yapilmak isteniyor')
    except YetersizStokError as e :
        print('Yakalandi:' , e )