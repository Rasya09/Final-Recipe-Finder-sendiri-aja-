class UserView:
    @staticmethod
    def get_user_input():
        nama = input("Masukan Nama Anda: ")
        email = input("Masukan Email Anda: ")
        password = input("Masukan Password (minimal 8 karakter): ")
        return nama, email, password
    
    @staticmethod
    def get_role_choices():
        print("Pilih Role:")
        print("1: Koki")
        print("2: Pengguna")
        role_choices = input("Masukan pilihan (1/2): ")
        return role_choices
    
    @staticmethod
    def show_message(message):
        print(message)