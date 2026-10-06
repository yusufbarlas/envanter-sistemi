import json 

def envanter_kaydet(dosya_adi, envanter):
    with open(dosya_adi , 'w' , encoding='utf-8') as f :
        json.dump(envanter , f , ensure_ascii=False , indent=4)



def envanter_yukle(dosya_adi, baslangic_verisi):
    try:
        with open (dosya_adi , 'r' , encoding='utf-8') as f:
            return  json.load(f)
    except FileNotFoundError:
        envanter_kaydet(dosya_adi , baslangic_verisi)
        return baslangic_verisi


if __name__ == "__main__":
    import veri

    envanter = envanter_yukle("envanter.json", veri.envanter)
    print("Ürün sayısı:", len(envanter))

    envanter["Test Ürün"] = {"stok": 1, "fiyat": 10.0, "kategori": "Deneme"}
    envanter_kaydet("envanter.json", envanter)

    tekrar = envanter_yukle("envanter.json", veri.envanter)
    print("Ürün sayısı:", len(tekrar))
    print("Test Ürün var mı:", "Test Ürün" in tekrar)


