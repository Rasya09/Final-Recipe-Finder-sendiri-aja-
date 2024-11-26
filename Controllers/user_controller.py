# untuk import bcrypt harus install terlebih dahulu
# pip install bcrypt
# jalankan perintah pada line 2
import bcrypt
import mysql

from setup_tables import connect_to_database


# Membuat password menjadi bcrypt
# bcryp merupakan fungsi hashing kata sandi untuk keamanan komputer (jadi passwordnya text unik)
def hash_password(password): # Fungsi untuk membuat hash dari password
    salt = bcrypt.gensalt()  # Membuat salt acak
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  # Menghash password
    return hashed_password

# Fungsi untuk mendaftarkan pengguna baru dengan pemilihan role Chef atau User.
def register_user(connection):
    cursor = connection.cursor()

    # Meminta input dari pengguna
    nama = input("Masukan Nama Anda: ")
    email = input("Masukan Email Anda: ")
    password = input("Masukan Password (minimal 8 karakter): ")

    # menapilkan pilihan role
    print("Pilih Role:")
    print("1: Koki")
    print("2: Pengguna")
    role_choices = input("Masukan pilihan (1/2): ")

    # Membuat fungsi untuk validasi inputan password dan role
    if len(password) < 8:
        print("Password harus minimal 8 karakter.")
        return
    if role_choices not in ["1","2"]:
        print("Pilihan role tidak valid. Tolong pilih 1 untuk menjadi Koki atau 2 Menjadi Pengguna")
        return

    # Menentukan role berdasarkan pilihan pengguna
    role = "chef" if role_choices == "1" else "user"

    # Hash password sebelum disimpan
    hashed_password = hash_password(password)

    # Periksa apakah nama sudah ada
    cursor.execute("SELECT nama_lengkap FROM users WHERE nama_lengkap = %s", (nama,))
    if cursor.fetchone():
        print("Nama Sudah digunakan. Silahkan pilih nama lain")

    # Menyimpan data ke Database
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        
        # Query SQL untuk memasukkan data pengguna
        query = "INSERT INTO users (nama_lengkap, password, role, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nama, hashed_password, role, email))
        
        # Commit perubahan ke database
        connection.commit()
        print(f"Registrasi berhasil! Selamat datang {nama} sebagai {role}.")
    
    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan: {err}")
    
    finally:
        # Menutup koneksi
        cursor.close()
        connection.close()

    print("Registrasi Berhasil!!, Silahkan Login")
