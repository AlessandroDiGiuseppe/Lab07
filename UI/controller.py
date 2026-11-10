import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdowns(self):
        self._view.dd_biblioteca.options = [ft.dropdown.Option("Nessun filtro")]
        self._view.dd_genere.options = [ft.dropdown.Option("Nessun filtro")]

        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

        self._view.dd_biblioteca.value = "Nessun filtro"
        self._view.dd_genere.value = "Nessun filtro"
    # CALLBACKS DROPDOWN
    # TODO
    def handle_biblioteca_changed(self, e):
        self.biblioteca_selezionata = e.control.value

    def handle_genere_changed(self, e):
        self.genere_selezionato = e.control.value
    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        self._view.lv_libri.controls.clear()

        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio selezionati.")
            self._view.update()
            return

        for libro in libri:
            testo_libro = f"📚 {libro.titolo} ({libro.genere}) - Presso: {libro.biblioteca_nome}"
            self._view.lv_libri.controls.append(ft.Text(value=testo_libro, size=16))

        self._view.update()