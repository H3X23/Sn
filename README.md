# H3X Web Scraper & Analyzer  🔍


Bu Python aracı, hedef bir web sitesinin HTML içeriğini analiz ederek linkleri, yorum satırlarını, başlık hiyerarşisini, JavaScript kodlarını ve potansiyel hassas dosyaları ayıklamak için tasarlanmıştır.

## Özellikler

* **Link Taraması:** Sayfa içerisindeki tüm `<a>` etiketlerini ve hedef adreslerini listeler.
* **Yorum Ayıklama:** Geliştiriciler tarafından HTML içinde bırakılan `` satırlarını bulur.
* **Başlık Analizi:** SEO ve içerik yapısı için kritik olan `h1-h6` etiketlerini hiyerarşik olarak sunar.
* **JS Dedektörü:** Sayfada kullanılan dahili scriptleri ve harici `.js` dosyalarını ayırır.
* **Hassas Dosya Taraması:** `.php`, `.sql`, `.env`, `.bak` gibi riskli olabilecek dosya uzantılarını linkler içinde arar.

## Kurulum

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install requests beautifulsoup4


