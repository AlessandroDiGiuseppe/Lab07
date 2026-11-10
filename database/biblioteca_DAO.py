from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_biblioteche(self):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca ORDER BY nome ASC"
        cursor.execute(query)

        for row in cursor.fetchall():
            result.append(Biblioteca(**row))

        cursor.close()
        conn.close()
        return result