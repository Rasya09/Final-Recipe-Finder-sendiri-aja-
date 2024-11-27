# untuk import bcrypt harus install terlebih dahulu
# pip install bcrypt
# jalankan perintah pada line 2
import bcrypt
import mysql.connector

class UserModel:
    def __init__(self, connection):
        self.connection = connection # Menghubungkan ke database

    def create_user(self, nama, email, hashed_password, role):
        cursor = self.connection.cursor() # Membuka cursor untuk query sql
        try:
            query = "INSERT INTO users (nama_lengkap, password, role, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nama, email, hashed_password, role))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    # Fungsi untuk Periksa apakah nama sudah ada
    def check_user_exists(self, nama):
        cursor = self.connection.cursor()
        cursor.execute("SELECT nama_lengkap FROM users WHERE nama_lengkap = %s", (nama,))
        result = cursor.fetchone()
        cursor.close()
        return result is not None
    
    # Membuat password menjadi bcrypt
    # bcryp merupakan fungsi hashing kata sandi untuk keamanan komputer (jadi passwordnya text unik)
    def hash_password(password): # Fungsi untuk membuat hash dari password
        salt = bcrypt.gensalt()  # Membuat salt acak
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  # Menghash password
        return hashed_password
    
    # Membuat fungsi untuk validasi inputan password
    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True
    
    # Menentukan role berdasarkan pilihan pengguna
    def get_role_from_choice(self, role_choice):
        if role_choice == "1":
            return "chef"
        elif role_choice == "2":
            return "user"
        else:
            return None
        
    # Mengubah karakter password menjadi Hash password sebelum disimpan
    def hash_password(self, password): # Fungsi untuk membuat hash dari password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password