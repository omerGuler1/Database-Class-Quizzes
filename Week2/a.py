import pandas as pd
import ace_tools as tools

# Proje takvimi ve iş paketleri tablosu
project_schedule = pd.DataFrame({
    "İş Paketi": [
        "Literatür Araştırması ve Veri Toplama",
        "Sistem Tasarımı ve Model Geliştirme",
        "Veri Entegrasyonu ve İşlenmesi",
        "Model Eğitimi ve Test Süreci",
        "Mobil ve Web Platform Geliştirme",
        "Sistem Entegrasyonu ve Optimizasyon",
        "Pilot Uygulama ve Testler",
        "Son Değerlendirme ve Raporlama",
        "Proje Tamamlama ve Yaygınlaştırma"
    ],
    "Alt Faaliyetler": [
        "Afet yönetimi ve yapay zeka uygulamalarına dair araştırma\nGereksinim analizi ve teknik dökümantasyon oluşturma",
        "Yapay zeka modelinin seçimi\nReinforcement learning algoritmalarının belirlenmesi\nMimari tasarım sürecinin tamamlanması",
        "AFAD ve diğer veri kaynaklarından veri entegrasyonu\nVatandaş bildirimleri için API geliştirilmesi\nVeri temizleme ve ön işleme süreçleri",
        "Makine öğrenmesi modellerinin eğitilmesi\nModel performansının değerlendirilmesi\nModelin fine-tuning işlemlerinin gerçekleştirilmesi",
        "Mobil uygulama ve web platformlarının geliştirilmesi\nKullanıcı arayüzü tasarımının tamamlanması\nGeri bildirim mekanizmalarının oluşturulması",
        "Yapay zeka modelinin sistemle entegre edilmesi\nÖnceliklendirme algoritmalarının test edilmesi\nKaynak yönetimi optimizasyonlarının uygulanması",
        "Gerçek verilerle pilot testlerin yapılması\nSaha ekiplerinden geri bildirim toplanması\nAlgoritma ve sistem performansının değerlendirilmesi",
        "Test sonuçlarının analiz edilmesi\nEksikliklerin giderilmesi ve sistem iyileştirmeleri\nSon kullanıcı testlerinin tamamlanması",
        "Projeyi yaygınlaştırmak için AFAD ve diğer yetkili kuruluşlarla iş birliği\nSistemin sürekli güncellenmesi için mekanizmaların oluşturulması\nSon raporun hazırlanması ve sunulması"
    ],
    "Başlangıç Tarihi": [
        "Mart 2025", "Nisan 2025", "Mayıs 2025", "Haziran 2025", "Temmuz 2025",
        "Ağustos 2025", "Eylül 2025", "Ekim 2025", "Kasım 2025"
    ],
    "Bitiş Tarihi": [
        "Nisan 2025", "Mayıs 2025", "Haziran 2025", "Temmuz 2025", "Ağustos 2025",
        "Eylül 2025", "Ekim 2025", "Kasım 2025", "Aralık 2025"
    ]
})

# Kullanıcıya tabloyu gösterme
tools.display_dataframe_to_user(name="Proje Takvimi ve İş Paketleri", dataframe=project_schedule)
