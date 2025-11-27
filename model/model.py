from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()

        self.get_all_edges()
        self.get_all_nodes()

        nodes_list = []
        for node in self._nodes:
            node_id = node.id
            nodes_list.append(node_id)
        self.G.add_nodes_from(nodes_list)

        for node1 in list(self.G.nodes):
            for node2 in list(self.G.nodes):
                if node1 < node2:
                    valore_totale = 0
                    numero_edges = 0
                    for edge in self._edges:
                        node_a = edge.id_hub_origine
                        node_b = edge.id_hub_destinazione
                        peso = edge.valore_merce
                        if node_a == node1 and node_b == node2 or node_a == node2 and node_b == node1:
                            valore_totale += peso
                            numero_edges += 1
                    if not numero_edges == 0:
                        valore_medio = valore_totale / numero_edges
                        if valore_medio >= threshold:
                            self.G.add_edge(node1, node2, weight = valore_medio)

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        self._edges = DAO.get_edges()
        return self._edges

    def get_all_nodes(self):
        self._nodes = DAO.get_nodes()
        return self._nodes
