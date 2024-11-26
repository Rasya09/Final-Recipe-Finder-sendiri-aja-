import mysql.connector
from Migrations.create_users_table import create_users_table

def connect_to_database():
    """
    Menghubungkan ke database 'RecipeFinder'.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="RecipeFinder",  # Pastikan database ini sudah dibuat
    )

if __name__ == "__main__":
    # Koneksi ke database
    db_connection = connect_to_database()
    print("Terhubung ke database 'RecipeFinder'.")

    # Membuat tabel 'users'
    create_users_table(db_connection)
