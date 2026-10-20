class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice  # es. ES1
        self.nome = nome
        self.cognome = cognome
        self.stand = None  # stand assegnato, all'inizio nessuno

    def __eq__(self, other):
        return self.codice == other.codice  # uguali se stesso codice

    def __str__(self):
        if self.stand is None:  # nessuno stand assegnato
            return f"{self.codice}: {self.nome} {self.cognome} - Nessuno stand assegnato"
        return f"{self.codice}: {self.nome} {self.cognome} - Stand assegnato: {self.stand.codice}"
