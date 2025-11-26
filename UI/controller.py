import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        try:
            threshold = int(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert("Inserisci un valore valido per il costo minimo")
        else:
            if threshold < 0:
                self._view.show_alert("Inserisci un valore valido per il costo minimo")
            else:
                self._view.lista_visualizzazione.clean()

                self._model.costruisci_grafo(threshold)
                num_edges = self._model.get_num_edges()
                num_nodes = self._model.get_num_nodes()

                self._view.lista_visualizzazione.append(ft.Text(f"Numero di Hub: {num_nodes}"))
                self._view.lista_visualizzazione.append(ft.Text(f"Numero di Tratte: {num_edges}"))

