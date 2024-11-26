import mysql.connector

# def connect_to_database ini adalah fungsi untuk membuat koneksi ke database MySQL
def connect_to_database(): 
    return mysql.connector.connect(
        host="localhost", #ini host yang ada di database (ini yang defaultnya)
        user="root", #ini user yang ada di database (ini yang defaultnya)
        password="", #ini password yang ada di database (ini yang defaultnya)
    )
# Penyesuaian: Sesuaikan host, user, dan password sesuai konfigurasi MySQL Anda.
# Output: Mengembalikan objek koneksi ke database.
# Tujuan: Membuat koneksi ke server MySQL

# Fungsi untuk membuat database jika belum ada
def create_database(connection):
    cursor = connection.cursor() # Gunakan cursor() untuk menjalankan perintah SQL.
    cursor.execute("SHOW DATABASES") #Query ini digunakan untuk mendapatkan daftar semua database yang ada di server MySQL.
    database = [db[0] for db in cursor.fetchall()] # Ambil daftar nama database

    if "recipefinder" in database:
        print("Database 'recipefinder' Sudah ada.")
    # jika recipe_finder ada dalam daftar database ("recipe_finder" in databases), maka cetak pesan bahwa database sudah ada.
    else:
        cursor.execute("CREATE DATABASE recipefinder")
        print("Database 'recipefinder' berhasil dibuat.")
    # jika tidak ada, maka buat database menggunakan query CREATE DATABASE.

    # Set database aktif
    connection.database = "recipefinder" # Setelah memastikan database sudah ada, atur database aktif untuk koneksi dengan connection.database = "recipe_finder".
    return connection
# Tujuan: Membuat database bernama recipe_finder jika belum ada.
# Parameter: connection adalah objek koneksi ke MySQL.

if __name__ == "__main__": # Tujuan: Memastikan script hanya dijalankan sebagai file utama.
    conn = connect_to_database()
    conn = create_database(conn) # Panggil fungsi create_database untuk mempersiapkan database.
    print("Terhubung ke database")
    