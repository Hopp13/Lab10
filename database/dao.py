from database.DB_connect import DBConnect
from model.spedizione import Spedizione
from model.hub import Hub


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def get_edges():
        connessione = DBConnect.get_connection()
        with connessione.cursor(dictionary = True) as cursor:
            query = "SELECT * FROM spedizione"
            cursor.execute(query)
            edges_list = []
            for row in cursor:
                spedizione = Spedizione(row["id"],
                                        row["id_compagnia"],
                                        row["numero_tracking"],
                                        row["id_hub_origine"],
                                        row["id_hub_destinazione"],
                                        row["data_ritiro_programmata"],
                                        row["distanza"],
                                        row["data_consegna"],
                                        row["valore_merce"])
                edges_list.append(spedizione)
        connessione.close()
        return edges_list

    @staticmethod
    def get_nodes():
        connessione = DBConnect.get_connection()
        with connessione.cursor(dictionary = True) as cursor:
            query = "SELECT * FROM hub"
            cursor.execute(query)
            nodes_list = []
            for row in cursor:
                hub = Hub(int(row["id"]),
                          row["codice"],
                          row["nome"],
                          row["citta"],
                          row["stato"],
                          float(row["latitudine"]),
                          float(row["longitudine"]))
                nodes_list.append(hub)
        connessione.close()
        return nodes_list
