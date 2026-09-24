envanter = {
    "Laptop - Lenovo IdeaPad 3": {"stok": 12, "fiyat": 24999.90, "kategori": "Bilgisayar"},
    "Kablosuz Mouse": {"stok": 85, "fiyat": 189.90, "kategori": "Aksesuar"},
    "Mekanik Klavye": {"stok": 40, "fiyat": 749.50, "kategori": "Aksesuar"},
    "24 inç Monitör": {"stok": 18, "fiyat": 3899.00, "kategori": "Bilgisayar"},
    "USB-C Şarj Kablosu": {"stok": 200, "fiyat": 79.90, "kategori": "Aksesuar"},
    "Kablosuz Kulaklık": {"stok": 55, "fiyat": 899.00, "kategori": "Ses"},
    "Webcam HD": {"stok": 30, "fiyat": 649.90, "kategori": "Aksesuar"},
    "Harici SSD 1TB": {"stok": 25, "fiyat": 1899.00, "kategori": "Depolama"},
    "Bluetooth Hoparlör": {"stok": 45, "fiyat": 549.90, "kategori": "Ses"},
    "Laptop Çantası": {"stok": 60, "fiyat": 399.00, "kategori": "Aksesuar"},
    "Ofis Sandalyesi": {"stok": 15, "fiyat": 2499.00, "kategori": "Mobilya"},
    "Yazıcı - Mürekkep Tanklı": {"stok": 10, "fiyat": 6999.00, "kategori": "Ofis Ekipmanı"},
    "Yazıcı Kartuşu Seti": {"stok": 70, "fiyat": 449.90, "kategori": "Ofis Ekipmanı"},
    "Powerbank 20000mAh": {"stok": 90, "fiyat": 599.90, "kategori": "Aksesuar"},
    "USB Hub 4 Port": {"stok": 110, "fiyat": 149.90, "kategori": "Aksesuar"},
}


## envanteri dict' te komple gez .items()

envanter_içerik = {urun_adi : ürün_bilgileri for urun_adi , ürün_bilgileri in envanter.items()}
print(envanter_içerik)
print("---------Envanter--------")
for envtr in envanter.items():
    print(f"{envtr[0]} : {envtr[1]}")
print(f"Toplam ürün sayisi: {len(envanter)}")

yeni_ürün_adi = input('Ürün adi: ')
stok_miktari = int(input('Stok Miktari: '))
fiyat = float(input('Fiyat: '))
kategori = input('Kategori: ')

envanter[yeni_ürün_adi] = {'stok': stok_miktari , 'fiyat': fiyat , 'kategori': kategori }

print('-----Güncellenmiş Envanter ------')
for envtr in envanter.items():
    print(f"{envtr[0]} : {envtr[1]}")
print(f"Toplam ürün sayisi: {len(envanter)}")

