from decimal import Decimal, InvalidOperation
import veri
import islemler
import dosya_islemleri
import hatalar

ENVANTER_DOSYASI = 'envanter.json'


def listele(envanter):
    for ad, urun in envanter.items():
        print(f'{urun.ad} | Stok:{urun.stok} | Fiyat:{urun.fiyat} TL | Kategori:{urun.kategori}')
    print(f'Toplam ürün sayisi: {len(envanter)}')


def ana_menu():
    envanter = dosya_islemleri.envanter_yukle(ENVANTER_DOSYASI, veri.envanter)
    while True:
        try:
            kullanici_sorusu = int(input("Yapmak istediğiniz işlem numarasını girin. \n 1- Ürün Ekle: \n 2- Envanter Listesi: \n"
            " 3- Stok Girişi: \n"
            " 4- Stok Çıkışı: \n"
            " 5- Ürün Sil: \n"
            " 6- Toplam Stok Değeri: \n"
            " 7- Çıkış: "))

            if kullanici_sorusu == 1:
                ad = input("Ürün adi girin: ")
                stok = int(input("Stok adedi girin: "))
                fiyat = Decimal(input("Fiyat girin: "))
                kategori = input("Kategori girin: ")
                islemler.urun_ekle(envanter, ad, stok, fiyat, kategori)
                dosya_islemleri.envanter_kaydet(ENVANTER_DOSYASI, envanter)
                print("Ürün eklendi.")

            elif kullanici_sorusu == 2:
                print('Envanter Listesi')
                listele(envanter)

            elif kullanici_sorusu == 3:
                ad = input("Ürün adi girin: ")
                miktar = int(input('Stok miktarı girin: '))
                urun = islemler.urun_bul(envanter, ad)
                urun.stok_giris(miktar)
                dosya_islemleri.envanter_kaydet(ENVANTER_DOSYASI, envanter)
                print('Stok güncellendi.')

            elif kullanici_sorusu == 4:
                ad = input("Ürün adi girin: ")
                miktar = int(input('Stok miktarı girin: '))
                urun = islemler.urun_bul(envanter, ad)
                urun.stok_cikis(miktar)
                dosya_islemleri.envanter_kaydet(ENVANTER_DOSYASI, envanter)
                print('Stok çıkışı gerçekleşti.')

            elif kullanici_sorusu == 5:
                ad = input("Ürün adi girin: ")
                islemler.urun_sil(envanter, ad)
                dosya_islemleri.envanter_kaydet(ENVANTER_DOSYASI, envanter)
                print('Ürün silindi.')

            elif kullanici_sorusu == 6:
                toplam_sonuc = islemler.toplam_deger(envanter)
                print(f'Toplam envanter değeri: {toplam_sonuc:,.2f} TL')

            elif kullanici_sorusu == 7:
                print('Çıkış yapılıyor...')
                return

            else:
                print('Lütfen geçerli bir tercih numarası girin')

        except hatalar.EnvanterSistemiError as e:
            print('Hata:', e)
        except ValueError:
            print('Geçersiz değer: lütfen sayı girin')
        except InvalidOperation:
            print('Geçersiz fiyat: lütfen sayı girin')


if __name__ == "__main__":
    ana_menu()