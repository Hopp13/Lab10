import datetime
from dataclasses import dataclass


@dataclass
class Spedizione:
    id: int
    id_compagnia: int
    numero_tracking: str
    id_hub_origine: int
    id_hub_destinazione: int
    data_ritiro_programmata: datetime.datetime
    distanza: int
    data_consegna: datetime.datetime
    valore_merce: float

    def __eq__(self, other):
        return isinstance(other, Spedizione) and self.id == other.id

    def __str__(self):
        return f"{self.numero_tracking}"

    def __repr__(self):
        return f"{self.numero_tracking}"
