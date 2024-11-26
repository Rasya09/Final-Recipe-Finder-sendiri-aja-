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

if __name__ == "__main__": # Tujuan: Memastikan script hanya dijalankan sebagai file utama.
    conn = connect_to_database()
    print("Terhubung ke database")
    