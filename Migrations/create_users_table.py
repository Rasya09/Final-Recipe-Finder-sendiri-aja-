# membuat fungsi untuk membuat table
def create_users_table(connection):
    cursor = connection.cursor() # Membuat objek cursor untuk menjalankan perintah SQL
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama_lengkap VARCHAR(55) NOT NULL,
        password VARCHAR(255) NOT NULL,
        role ENUM('admin','chef','user') NOT NULL,
        email VARCHAR(255) NOT NULL,
        Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor.execute(query) # Menjalankan perintah SQL / query yang sudah dibuat
    print("Table 'users' berhasil dibuat.")