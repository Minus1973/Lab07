import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model


    def handle_umidita_media(self, e):
        #controllo i dati passati dal _view
        self._mese=self._view.dd_mese.value
        if self._mese is None:
            self._view.lst_result.controls.append(ft.Text(f"Selezionare un mese"))
            self._view.update_page()
            return

        #metto i dati nella lista
        lista_tmp = self._model.calcola_umidita_media(self._mese)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"L'umidità media nelle città è:"))
        for l in lista_tmp:
            self._view.lst_result.controls.append(ft.Text(f"{l[0]}  {l[1]}"))
        self._view.update_page()




