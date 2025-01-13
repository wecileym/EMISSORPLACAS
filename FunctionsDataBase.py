import base64
import sqlite3

class DataBase():

    def fetch_images_from_db():
        # Conexão com o banco de dados
        conn = sqlite3.connect("seu_banco.db")
        cursor = conn.cursor()

        # Consulta para recuperar imagens
        cursor.execute("SELECT Image FROM sua_tabela LIMIT 30")
        rows = cursor.fetchall()
        conn.close()

        # Converte imagens binárias para formato base64
        images_base64 = [
            f"data:image/png;base64,{base64.b64encode(row[0]).decode()}" for row in rows
        ]
        return images_base64
