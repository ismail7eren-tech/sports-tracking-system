⚡ Sporcu Performans Takip Sistemi | Athlete Performance Tracker

A modern, lightweight full-stack web application engineered for trainers, athletes, and fitness enthusiasts to systematically log workouts, track athletic progression, and manage athlete profiles with clean relational data models.

🇹🇷 Türkçe

🌟 Proje Hakkında

Sporcu Performans Takip Sistemi, sporcuların ve antrenörlerin günlük antrenman yüklerini, gelişim notlarını ve performans verilerini dijital ortamda düzenli bir şekilde kayıt altına almalarını sağlayan full-stack bir web uygulamasıdır.

Bu proje; ilişkisel veritabanı kısıtlamaları (Foreign Keys, Cascade Deletes), güvenli parametre yönetimi (SQLite3 parametreli sorguları) ve atletik/modern kullanıcı arayüzü (UI/UX) standartları gözetilerek baştan sona yeniden yapılandırılmıştır. Mimarinin geliştirilme ve refactor edilme süreçlerinde modern Yapay Zeka (AI) kodlama asistanlarından (Gemini AI, Cursor IDE) faydalanılmış; backend veri doğrulamaları, ergonomik form girdileri ve karanlık tema (Dark Mode) performans paneli ilkeleri insan odaklı yazılım disiplinleriyle projeye entegre edilmiştir.

✨ Temel Özellikler

👤 Sporcu Kaydı ve Profil Yönetimi: Sporcu adı, soyadı ve branşıyla (Powerlifting, Crossfit, Fitness vb.) hızlı ve güvenli profil oluşturma.

📝 Detaylı İlerleme ve Antrenman Günlüğü: Tarih, antrenman türü ve kaldırılan ağırlıklar/notlar ile sporcu bazlı gelişmiş performans günlüğü tutma.

🔗 İlişkisel Veri Bütünlüğü: FOREIGN KEY ve ON DELETE CASCADE kuralları ile veritabanı seviyesinde tutarlılık.

🎨 Atletik & Modern Dark UI: Koyu arduvaz ve amber/turuncu vurgu renkleriyle tasarlanmış, göz yormayan, mobil cihazlarla tam uyumlu esnek arayüz (CSS Grid & Flexbox).

⚡ Entegre Bildirim Sistemi (Flash Messages): Başarılı kayıt işlemlerinde veya eksik veri girişlerinde kullanıcıya anlık renk kodlu geri bildirimler.

🛠️ Teknolojik Altyapı

Backend: Python 3.x, Flask Framework

Veritabanı: SQLite3 (sqlite3.Row nesne eşlemesi ve Foreign Key desteği)

Frontend: HTML5 (Semantik etiketler), CSS3 (Modern Variables, Flexbox, Grid)

Yazılım Mimarisi: Clean Code & MVC Deseni

🇬🇧 English

🌟 About The Project

The Athlete Performance Tracker is a sleek, full-stack web application designed for coaches, personal trainers, and athletes to log daily training routines, track progress metrics, and manage athlete profiles within a structured relational database architecture.

Engineered with a focus on database integrity, query parameterization, and an athletic dark-themed interface design. Contemporary Artificial Intelligence (AI) coding assistants (Gemini AI, Cursor IDE) were utilized throughout the refactoring process to refine backend validation rules, eliminate memory leaks, and implement responsive CSS layouts.

✨ Key Features

👤 Athlete Onboarding: Fast and structured profile registration categorized by sports discipline (e.g., Powerlifting, Crossfit, Endurance).

📝 Performance & Workout Logs: Track individual workout routines, record metrics (weights, reps, sets), and attach qualitative progress notes by date.

🔗 Relational Data Integrity: Enforced FOREIGN KEY constraints with ON DELETE CASCADE logic ensuring database consistency.

🎨 Athletic Dark UI: Clean dark-mode dashboard styled with slate background tones and high-contrast amber/orange accents using CSS Grid & Flexbox.

⚡ Flash Notification Triggers: Instant feedback banners displaying real-time status alerts for validation errors or successful database commits.

🛠️ Technology Stack

Backend: Python 3.x, Flask Framework

Database: SQLite3 (Relational Schema with sqlite3.Row mapping)

Frontend: HTML5 (Semantic Structure), CSS3 (CSS Variables, Flexbox, Grid)

Architecture: Clean Code & MVC Pattern

⚙️ Kurulum ve Çalıştırma | Getting Started

1. Depoyu Klonlayın (Clone the Repository)

git clone https://github.com/kullanici-adin/spor-takip-sistemi.git
cd spor-takip-sistemi


2. Sanal Ortamı Oluşturun ve Çalıştırın (Virtual Environment)

# Windows
python -m venv venv
.\venv\Scripts\activate.bat

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


3. Gerekli Paketleri Yükleyin (Install Dependencies)

pip install flask


4. Uygulamayı Başlatın (Run the Application)

python app.py


Tarayıcınızdan http://127.0.0.1:5000 adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

"Disiplin, hedefler ile başarı arasındaki köprüdür. Her antrenmanı kaydedin, gelişiminizi izleyin."