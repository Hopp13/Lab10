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

                self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hub: {num_nodes}"))
                self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {num_edges}"))

                for edge in self._model.G.edges:
                    for node in self._model.get_all_nodes():
                        if edge[0] == node.id:
                            node1 = node
                        if edge[1] == node.id:
                            node2 = node
                        peso = self._model.G.get_edge_data(edge[0], edge[1])["weight"]

                    text = ft.Text(f"[{node1} <-> {node2}] ----- Guadagno medio: € {peso}")
                    self._view.lista_visualizzazione.controls.append(text)

        self._view.update()
