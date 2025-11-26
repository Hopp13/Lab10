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
        with connessione.cursor(dict = True) as cursor:
            query = "SELECT * FROM spedizione"
            cursor.excecute(query)
            edges_list = []
            for row in cursor:
                spedizione = Spedizione
                spedizione.id = row["id"]
                spedizione.id_compagnia = row["id_compagnia"]
                spedizione.numero_tracking = row["numero_tracking"]
                spedizione.id_hub_origine = row["id_hub_origine"]
                spedizione.id_hub_destinazione = row["id_hub_destinazione"]
                spedizione.data_ritiro_programmata = row["data_ritiro_programmata"]
                spedizione.distanza = row["distanza"]
                spedizione.data_consegna = row["data_consegna"]
                spedizione.valore_merce = row["valore_merce"]
                edges_list.append(spedizione)
        connessione.close()
        return edges_list

    @staticmethod
    def get_nodes():
        connessione = DBConnect.get_connection()
        with connessione.cursor(dict = True) as cursor:
            query = "SELECT * FROM hub"
            cursor.excecute(query)
            nodes_list = []
            for row in cursor:
                hub = Hub
                hub.id = row["row"]
                hub.codice = row["codice"]
                hub.nome = row["nome"]
                hub.citta = row["citta"]
                hub.stato = row["stato"]
                hub.latitudine = row["latitudine"]
                hub.longitudine = row["longitudine"]
                nodes_list.append(hub)
        connessione.close()
        return nodes_list