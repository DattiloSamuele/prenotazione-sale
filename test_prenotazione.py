import unittest
from datetime import date

from prenotazioni import Prenotazione

MARTEDI = date(2026, 11, 3)


class TestPrenotazione(unittest.TestCase):
    def test_costruttore_rifiuta_orari_non_ammessi(self):
        casi = [
            ("09:15", "10:00"),
            ("07:30", "09:00"),
            ("19:30", "20:30"),
            ("10:00", "10:00"),
        ]
        for inizio, fine in casi:
            with self.subTest(inizio=inizio, fine=fine):
                with self.assertRaises(ValueError):
                    Prenotazione("A1", MARTEDI, inizio, fine, "Rossi", 1)

    def test_costruttore_rifiuta_giorno_non_date(self):
        with self.assertRaises(TypeError):
            Prenotazione("A1", "2026-11-03", "09:00", "10:00", "Rossi", 1)

    def test_durata_minuti_restituisce_durata_corretta(self):
        prenotazione = Prenotazione("A1", MARTEDI, "09:00", "10:30", "Rossi", 1)

        self.assertEqual(prenotazione.durata_minuti(), 90)


if __name__ == "__main__":
    unittest.main()
