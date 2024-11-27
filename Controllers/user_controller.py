import mysql
from Models.user_model import UserModel
from Views.user_view import UserView
from setup_tables import connect_to_database

class UserController:
    def __init__(self, connection):
        self.model = UserModel(connection)
        self.view = UserView()

    # Fungsi untuk mendaftarkan pengguna baru dengan pemilihan role Chef atau User.
    def register_user(self):
        nama, email, password = self.view.get_user_input()

        if not self.model.validate_password(password):
            self.view.show_message("Password harus minimal 8 karakter.")
            return
        
        # Periksa apakah nama sudah ada mengambil dari model
        if self.model.check_user_exists(nama):
            self.view.show_message("Nama sudah digunakan. Silahkan gunakan nama lain.")
            return
        
        # Pilih role
        role_choice = self.view.get_role_choices()
        role = self.model.get_role_from_choice(role_choice)
        if role is None:
            self.view.show_message("Pilihan role tidak valid.")
            return
        
        # Hash password
        hashed_password = self.model.hash_password(password)

        # Simpan data yang baru diinput oleh user pengguna
        self.model.create_user(nama, email, hashed_password, role)
        self.view.show_message(f"Registrasi berhasil!!. Selamat datang {nama} sebagai {role}")