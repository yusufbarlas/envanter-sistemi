import veri
import islemler

def ana_menu():
 while True:
    kullanici_sorusu = int(input("Yapmak istediğiniz işlem numarasını girin. \n 1- Ürün Ekle \n 2- Envanter Listesi \n 3- Çıkış"))

    if kullanici_sorusu == 1:
          ad = input("Ürün adi girin: ")
          stok = int(input("Stok adedi girin: "))
          fiyat = float(input("Fiyat girin: "))
          kategori = input("Kategori girin: ")
          islemler.urun_ekle(veri.envanter, ad, stok, fiyat, kategori)
          print("Ürün eklendi.")

    elif kullanici_sorusu == 2:
         islemler.listele(veri.envanter)
         print('Envanter Listesi')

    else:
        print('Çıkış yapılıyor...')
        return


if __name__ == "__main__":
    ana_menu()
     
        
            
              
            
