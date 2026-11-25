import unittest
from datetime import date, timedelta

from prenotazioni import (
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)

OGGI = date(2026, 11, 2)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A1", "Aula Magna", 20))

    def test_aggiungi_sala_rifiuta_codice_duplicato(self):
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(Sala("A1", "Altra aula", 10))

    def test_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("Z9")

    def test_prenota_rifiuta_data_passata(self):
        richiesta = Prenotazione("A1", date(2026, 10, 30), "09:00", "10:00", "Rossi", 1)

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=OGGI)

    def test_prenota_rifiuta_domenica(self):
        richiesta = Prenotazione("A1", date(2026, 11, 8), "09:00", "10:00", "Rossi", 1)

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=OGGI)

    def test_prenota_rifiuta_data_oltre_orizzonte(self):
        richiesta = Prenotazione(
            "A1", OGGI + timedelta(days=61), "09:00", "10:00", "Rossi", 1
        )

        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=OGGI)

    def test_prenota_accetta_oggi(self):
        richiesta = Prenotazione("A1", OGGI, "09:00", "10:00", "Rossi", 1)

        self.assertEqual(self.agenda.prenota(richiesta, oggi=OGGI), 1)

    def test_prenotazione_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(99)

    def test_cancella_prenotazione_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(99)


if __name__ == "__main__":
    unittest.main()
