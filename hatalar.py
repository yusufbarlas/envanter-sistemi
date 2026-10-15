class Envanter_Sistemi(Exception):
    pass 
class UrunBulunamadiError(Envanter_Sistemi):
    pass
class UrunZatenVarError(Envanter_Sistemi):
    pass
class YetersizStokError(Envanter_Sistemi):
    pass 
class NegatifDegerError(Envanter_Sistemi):
    pass

if __name__ == '__main__' :
   
    try:
        raise NegatifDegerError('Negatif değer saptandı , işlem başarısız')
    except Envanter_Sistemi as e :
        print('Yakalandı:' , e )

    