from setup_tables import connect_to_database
from Controllers.user_controller import UserController

def main_menu():
    connection = connect_to_database()
    controller = UserController(connection)

    while True:
        print("\n===== MAIN MENU =====")
        print("1: Registrasi")
        print("2: Login")
        print("3: Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\n=== Registrasi Pengguna ===")
            controller.register_user()
        elif pilihan == "2":
            print("\n=== Silahkan Login ===")
            controller.login_user()
        elif pilihan == "3":
            print("Keluar dari aplikasi.")
            break  # Keluar dari loop dan menutup aplikasi
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
