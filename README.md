🏋️ Sporcu Performans Takip Sistemi 
Bu proje; sporcuların antrenman programlarını kişiselleştirmek, gelişim süreçlerini dijital olarak kayıt altına almak ve performans raporlarını analiz etmek için geliştirilmiş Flask tabanlı bir yönetim panelidir.

Proje, özellikle veri ilişkileri (sporcu -> antrenman -> ilerleme) üzerine kurgulanmış bir veritabanı mimarisine sahiptir.

🚀 Öne Çıkan Özellikler
👤 Dinamik Sporcu Yönetimi
Sisteme farklı branşlardan sporcular eklenebilir. Her sporcu, veritabanında benzersiz bir kimlikle (ID) tutulur ve tüm gelişim süreci bu kimlik üzerinden takip edilir.

📈 Performans ve İlerleme Takibi
Kronolojik Raporlama: Sporcuların hangi tarihte, hangi antrenmanı yaptığı ve o günkü fiziksel durumu (açıklama/notlar) bir akış dahilinde listelenir.

Veri İlişkilendirme: SQL JOIN yapısı kullanılarak, karmaşık tablolar arası veri çekme işlemleri optimize edilmiştir.

Görsel Bildirimler: Kayıt başarılı olduğunda kullanıcıya anlık olarak yeşil onay mesajları (Flash Messages) gösterilir.

🎨 Modern Karanlık Tema (Dark Mode)
Spor salonu atmosferine uygun, kullanıcıyı yormayan ve odaklanmayı artıran profesyonel bir karanlık tema arayüzü ile tasarlanmıştır.

🛠️ Teknik Altyapı
Backend: Python 3.x ve Flask Mikro-Framework.

Veritabanı: SQLite3 kullanılarak ilişkisel veri modelleri (sporcular ve ilerlemeler) oluşturulmuştur.

Frontend: HTML5 ve CSS3 (Flexbox ve Shadow efektleri) kullanılarak responsive bir deneyim sunulmuştur.

Template Engine: Dinamik içerik yönetimi için Jinja2 tercih edilmiştir.


Çalıtştırma Komutu
py app.py
