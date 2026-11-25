import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala

OGGI = date(2026, 11, 2)
MARTEDI = date(2026, 11, 3)


class TestSegnalazioneOrari(unittest.TestCase):
    def test_prenotazioni_contigue_sono_ammissibili(self):
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", MARTEDI, "09:00", "10:00", "Rossi", 10)
        seconda = Prenotazione("A2", MARTEDI, "10:00", "11:00", "Bianchi", 10)

        agenda.prenota(prima, oggi=OGGI)
        identificativo = agenda.prenota(seconda, oggi=OGGI)

        self.assertEqual(identificativo, 2)


class TestSegnalazioneCapienza(unittest.TestCase):
    def test_sala_accetta_la_capienza_massima(self):
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))
        prenotazione = Prenotazione("R1", MARTEDI, "09:00", "10:00", "Rossi", 10)

        identificativo = agenda.prenota(prenotazione, oggi=OGGI)

        self.assertEqual(identificativo, 1)


if __name__ == "__main__":
    unittest.main()
