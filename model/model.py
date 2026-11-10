from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        tutti_i_libri = self._libro_dao.get_all_libri()
        libri_filtrati = []

        for libro in tutti_i_libri:
            # Verifica filtro biblioteca (se presente e non "Nessun filtro")
            if biblioteca and biblioteca != "Nessun filtro" and libro.biblioteca_nome != biblioteca:
                continue
            # Verifica filtro genere (se presente e non "Nessun filtro")
            if genere and genere != "Nessun filtro" and libro.genere != genere:
                continue

            libri_filtrati.append(libro)

        return libri_filtrati
    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        return self._libro_dao.get_all_generi()
    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        return self._biblioteca_dao.get_all_biblioteche()
