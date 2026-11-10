from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_libri(self):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT l.*, b.nome as biblioteca_nome
                FROM libro l
                         JOIN biblioteca b ON l.id_biblioteca = b.id
                """
        cursor.execute(query)

        for row in cursor.fetchall():
            # Rimuove 'biblioteca_nome' dal dizionario row per non passarlo al costruttore
            nome_bib = row.pop('biblioteca_nome', None)

            # Crea l'oggetto Libro con i soli parametri nativi della tabella libro
            libro = Libro(**row)

            # Aggiunge dinamicamente l'attributo all'oggetto creato, così il Model può leggerlo
            libro.biblioteca_nome = nome_bib

            result.append(libro)

        cursor.close()
        conn.close()
        return result

    def get_all_generi(self):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        cursor = conn.cursor()
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere ASC"
        cursor.execute(query)

        for row in cursor.fetchall():
            result.append(row[0])

        cursor.close()
        conn.close()
        return result