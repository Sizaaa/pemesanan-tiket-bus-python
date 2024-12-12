import sqlite3

def koneksi_db():
    db = sqlite3.connect("Booking_Bus.db")
    cursor = db.cursor()
    return db, cursor

def create_tables():
    db, cursor = koneksi_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        password VARCHAR(255),
        status_logged INTEGER DEFAULT 0 CHECK (status_logged IN (0, 1))
    )
    ''')
    # CATATAN BUAT YANG KEBAGIAN DATABASE, BUAT CURSOR EXECUTE SETELAH COMMENT INI !
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rute (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from TEXT,
        to TEXT,
        bill REAL,
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_id INTEGER,
        kapasitas INTEGER,
        plat_bus VARCHAR(20) UNIQUE NOT NULL,
        jenis VARCHAR(50),
        merek VARCHAR(50) UNIQUE NOT NULL,
        bahan_bakar VARCHAR(20),
        warna VARCHAR(30),
        fasilitas TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keberangkatan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_id INTEGER,
        rute_id INTEGER,
        waktu_awal DATETIME,
        waktu_akhir DATETIME,
        keterlambatan INTEGER DEFAULT 0,
        status VARCHAR(50) DEFAULT 'Dijadwalkan',
        FOREIGN KEY(bus_id) REFERENCES bus(id),
        FOREIGN KEY(rute_id) REFERENCES rute(id)
    )
    ''')
    
    db.commit()
create_tables()