from Controllers.user_controller import register_user
from setup_tables import connect_to_database

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1: Registrasi")
        print("2: Login")
        print("3: Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\n=== Registrasi Pengguna ===")
            connection = connect_to_database()
            register_user(connection)
        elif pilihan == "2":
            print("\n=== Fitur Login (Belum diimplementasikan) ===")
            # Fitur login akan ditambahkan di sini nanti
        elif pilihan == "3":
            print("Keluar dari aplikasi.")
            break  # Keluar dari loop dan menutup aplikasi
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
