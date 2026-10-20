from stand import Stand, StandPrese, StandPremium
from espositore import Espositore



class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._stand = {}  # dizionario codice -> oggetto Stand
        self._espositori = {}  # dizionario codice -> oggetto Espositore

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):  # getter
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):  # setter
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8") as file:  # se il file non c'è, open() dà FileNotFoundError
            stand = {}
            espositori = {}

            for riga in file:
                riga = riga.strip()  # tolgo \n e spazi
                if not riga:  # salto le righe vuote
                    continue

                campi = [c.strip() for c in riga.split(",")]  # divido la riga sulle virgole
                codice = campi[0]

                if codice.startswith("ST"):  # è uno stand
                    superficie = int(campi[1])
                    padiglione = int(campi[2])
                    prezzo_base = float(campi[3])

                    if len(campi) == 4:  # solo 4 campi -> Standard
                        stand[codice] = Stand(codice, superficie, padiglione, prezzo_base)
                    elif campi[4].isdigit():  # quinto campo è un numero -> prese extra
                        stand[codice] = StandPrese(codice, superficie, padiglione,
                                                   prezzo_base, int(campi[4]))
                    else:  # quinto campo è testo -> Premium
                        stand[codice] = StandPremium(codice, superficie, padiglione,
                                                     prezzo_base, campi[4])

                elif codice.startswith("ES"):  # è un espositore
                    espositori[codice] = Espositore(codice, campi[1], campi[2])

        self._stand = stand  # salvo solo a fine lettura
        self._espositori = espositori

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        stand = self._stand.get(codice_stand)  # get dà None se il codice non esiste
        espositore = self._espositori.get(codice_espositore)

        if stand is None:  # controllo che esistano
            raise ValueError(f"Stand {codice_stand} inesistente")
        if espositore is None:
            raise ValueError(f"Espositore {codice_espositore} inesistente")
        if not stand.disponibile:  # stand già preso
            raise ValueError(f"Stand {codice_stand} non disponibile")
        if espositore.stand is not None:  # espositore ha già uno stand
            raise ValueError(f"Espositore {codice_espositore} già associato "
                             f"allo stand {espositore.stand.codice}")

        stand.disponibile = False  # collego stand ed espositore
        stand.espositore = espositore
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self._espositori.values():
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self._stand.values())
