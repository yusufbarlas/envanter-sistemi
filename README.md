# Envanter Sistemi

Terminal üzerinden çalışan, basit bir stok/envanter takip programı. Ürün ekleme, stok giriş/çıkışı, ürün silme ve toplam envanter değerini hesaplama işlemlerini yapar. Veriler `envanter.json` dosyasında saklanır.

## Dosyalar

- **ana.py** — Programın giriş noktası. Kullanıcıya menü gösterir, seçimlere göre diğer modülleri çağırır ve hataları yakalar.
- **veri.py** — Programın ilk çalıştırmasında kullanılacak örnek/başlangıç envanter verisi.
- **dosya_islemleri.py** — Envanteri JSON dosyasından okuma ve JSON dosyasına kaydetme fonksiyonlarını içerir.
- **islemler.py** — Ürün ekleme, stok girişi/çıkışı, ürün silme ve toplam envanter değerini hesaplama gibi iş mantığı fonksiyonlarını içerir.
- **hatalar.py** — Envanter sistemine özel hata (exception) sınıflarını tanımlar (örnek: ürün bulunamadı, ürün zaten var, yetersiz stok).
- **envanter.json** — Programın çalışma zamanında oluşturduğu/güncellediği veri dosyası. Depoya dahil edilmez (`.gitignore` içinde).

## Nasıl Çalıştırılır

```
python ana.py
```

Program açıldığında ekrana gelen menüden işlem numarasını girerek devam edebilirsiniz:

1. Ürün Ekle
2. Envanter Listesi
3. Stok Girişi
4. Stok Çıkışı
5. Ürün Sil
6. Toplam Stok Değeri
7. Çıkış
