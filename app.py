import sqlite3
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "spor_takip_secret"
DB_NAME = "spor.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    # SQLite'ta ilişkisel veritabanı kurallarını (Foreign Key) aktif ediyoruz
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS sporcular (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                ad TEXT NOT NULL, 
                spor_dali TEXT NOT NULL
            )
        """)
        
        db.execute("""
            CREATE TABLE IF NOT EXISTS antrenmanlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                sporcu_id INTEGER NOT NULL, 
                ad TEXT NOT NULL, 
                detay TEXT,
                FOREIGN KEY (sporcu_id) REFERENCES sporcular (id) ON DELETE CASCADE
            )
        """)
        
        db.execute("""
            CREATE TABLE IF NOT EXISTS ilerlemeler (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                sporcu_id INTEGER NOT NULL, 
                tarih TEXT NOT NULL, 
                antrenman_ad TEXT NOT NULL, 
                aciklama TEXT,
                FOREIGN KEY (sporcu_id) REFERENCES sporcular (id) ON DELETE CASCADE
            )
        """)
        db.commit()

init_db()

@app.route("/")
def home():
    db = get_db()
    sporcular = db.execute("SELECT * FROM sporcular ORDER BY ad ASC").fetchall()
    
    ilerlemeler = db.execute("""
        SELECT i.*, s.ad as sporcu_ad 
        FROM ilerlemeler i 
        JOIN sporcular s ON i.sporcu_id = s.id 
        ORDER BY i.tarih DESC, i.id DESC
    """).fetchall()
    
    db.close()
    return render_template("index.html", sporcular=sporcular, ilerlemeler=ilerlemeler)

@app.route("/sporcu_ekle", methods=["POST"])
def sporcu_ekle():
    ad = request.form.get("ad", "").strip()
    dal = request.form.get("spor_dali", "").strip()
    
    if not ad or not dal:
        flash("Sporcu adı ve branşı zorunludur.", "error")
        return redirect("/")
        
    with get_db() as db:
        db.execute("INSERT INTO sporcular (ad, spor_dali) VALUES (?,?)", (ad, dal))
        db.commit()
        
    flash("Sporcu başarıyla kaydedildi!", "success")
    return redirect("/")

@app.route("/ilerleme_kaydet", methods=["POST"])
def ilerleme_kaydet():
    s_id = request.form.get("sporcu_id")
    tarih = request.form.get("tarih", "").strip()
    ant_ad = request.form.get("ant_ad", "").strip()
    notlar = request.form.get("aciklama", "").strip()
    
    if not s_id or not tarih or not ant_ad:
        flash("Sporcu, tarih ve antrenman adı alanları zorunludur.", "error")
        return redirect("/")
        
    with get_db() as db:
        db.execute(
            "INSERT INTO ilerlemeler (sporcu_id, tarih, antrenman_ad, aciklama) VALUES (?,?,?,?)", 
            (s_id, tarih, ant_ad, notlar)
        )
        db.commit()
        
    flash("İlerleme kaydı eklendi!", "success")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)