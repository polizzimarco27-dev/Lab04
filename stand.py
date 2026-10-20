class Stand: #Stand è la classe Padre
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.disponibile = True  # all'inizio ogni stand è libero
        self.espositore = None  # espositore a cui è assegnato (nessuno all'inizio)

    @property

    def prezzo(self):  # standard: prezzo = prezzo base
        return self.prezzo_base

    def __eq__(self, other):
        return self.codice == other.codice  # uguali se stesso codice

    def __lt__(self, other):
        return self.prezzo < other.prezzo  # serve a sorted() per ordinare per prezzo

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"{self.codice}: Standard | {self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - {stato}")  # .2f = 2 decimali


class StandPrese(Stand):  # eredita da Stand
    def __init__(self, codice, superficie, padiglione, prezzo_base, prese_extra):
        super().__init__(codice, superficie, padiglione, prezzo_base)  # dati in comune li fa Stand
        self.prese_extra = prese_extra

    @property
    def prezzo(self):  # +7% per ogni presa extra
        return self.prezzo_base * (1 + 0.07 * self.prese_extra)

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"{self.codice}: Prese Extra | {self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - "
                f"Prese aggiuntive: {self.prese_extra} - {stato}")


class StandPremium(Stand):  # eredita da Stand
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione  # Ingresso, Angolare, Vetrina

    @property
    def prezzo(self):  # +30% fisso
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"{self.codice}: Premium | {self.superficie} mq - "
                f"Padiglione {self.padiglione} - "
                f"Prezzo {self.prezzo:.2f}€ - "
                f"Posizione: {self.posizione} - {stato}")