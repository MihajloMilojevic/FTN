import copy
import os
import random
import unittest

from korisnici import korisnici
from test.test_utils import rand_str, rand_valid_user, gen_rand_valid_users


class KorisnikTest(unittest.TestCase):
    def setUp(self):
        self.pun_korisnik = rand_valid_user()
        self.opciona_polja = {
            "pasos": True, 
            "drzavljanstvo": True, 
            "pol": True
        }
        self.putanja = "test_korisnici.csv"

        if os.path.isfile(self.putanja):
            os.remove(self.putanja)

    def tearDown(self):
        if os.path.isfile(self.putanja):
            os.remove(self.putanja)

    def test_kreiraj_validnog_korisnika(self):
        svi_korisnici = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])
        self.assertIsNotNone(svi_korisnici, msg="Nije vraćena kolekcija korisnika")
        self.assertIn(self.pun_korisnik["korisnicko_ime"], svi_korisnici, msg="Korisnik nije u kolekciji")
        self.assertDictEqual(
            self.pun_korisnik, 
            svi_korisnici[self.pun_korisnik["korisnicko_ime"]], 
            msg="Korisnikove vrednosti nisu dobre"
        )

    def test_kreiraj_prazni(self):
        # Prodji kroz sve kljuceve, postavi jedan na None, pa pozovi funkciju
        for key in self.pun_korisnik:
            if key in self.opciona_polja:
                continue
            korisnik = copy.deepcopy(self.pun_korisnik)
            korisnik[key] = None
            rezultat = korisnici.kreiraj_korisnika(
                {},
                False,  # azuriraj
                korisnik["uloga"],
                None, # staro_korisnicko_ime
                korisnik["korisnicko_ime"],
                korisnik["lozinka"],
                korisnik["ime"],
                korisnik["prezime"],
                korisnik["email"],
                korisnik["pasos"],
                korisnik["drzavljanstvo"],
                korisnik["telefon"],
                korisnik["pol"])
            self.assertTrue(type(rezultat) is str, msg=f"Provera za nedostajucu vrednost: {key}")
            self.assertTrue(len(rezultat)>0, msg=f"Provera za nedostajucu vrednost: {key}")

    def test_kreiraj_postojece_korisnicko_ime(self):
        svi_korisnici = {
            self.pun_korisnik["korisnicko_ime"]: self.pun_korisnik
        }
        rezultat = korisnici.kreiraj_korisnika(
            svi_korisnici,
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])
        self.assertTrue(type(rezultat) is str, msg=f"Postojece korisnicko ime:")
        self.assertTrue(len(rezultat)>0, msg=f"Postojece korisnicko ime")

    def test_azuriraj_nepostojece_korisnicko_ime(self):
        rezultat = korisnici.kreiraj_korisnika(
            {},
            True,  # azuriraj
            self.pun_korisnik["uloga"],
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])
        self.assertTrue(type(rezultat) is str, msg=f"Nepostojece korisnicko ime pri azuriranju")
        self.assertTrue(len(rezultat)>0, msg=f"Nepostojece korisnicko ime pri azuriranju")

    def test_azuriraj_validnog_korisnika(self):
        korisnik = rand_valid_user()
        svi_korisnici = {
            korisnik["korisnicko_ime"]: copy.deepcopy(self.pun_korisnik) # Bez kopije se menja referenca
        }

        svi_korisnici = korisnici.kreiraj_korisnika(
            svi_korisnici,
            True, # azuriraj
            korisnik["uloga"],
            korisnik["korisnicko_ime"], # staro_korisnicko_ime
            korisnik["korisnicko_ime"],
            korisnik["lozinka"],
            korisnik["ime"],
            korisnik["prezime"],
            korisnik["email"],
            korisnik["pasos"],
            korisnik["drzavljanstvo"],
            korisnik["telefon"],
            korisnik["pol"])
        self.assertIsNotNone(svi_korisnici, msg="Nije vraćena kolekcija korisnika")
        self.assertIn(korisnik["korisnicko_ime"], svi_korisnici, msg="Korisnik nije u kolekciji")
        self.assertDictEqual(korisnik, svi_korisnici[korisnik["korisnicko_ime"]], msg="Korisnik nije dobro ažuriran")

    def test_email(self):
        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            "email_bez_at",
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])

        self.assertTrue(type(rezultat) is str, msg=f"Email provera bez @")
        self.assertTrue(len(rezultat)>0, msg=f"Email provera bez @")

        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            "email@email.vise.poddomena",
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])
        self.assertTrue(type(rezultat) is str, msg=f"Email provera sa @ ali sa više poddomena")
        self.assertTrue(len(rezultat)>0, msg=f"Email provera bez @")

    def test_pasos(self):
        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            "abcdefghi",
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])

        self.assertTrue(type(rezultat) is str, msg=f"Pasoš nebrojevni string")
        self.assertTrue(len(rezultat)>0, msg=f"Pasoš nebrojevni string")

        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            "123",
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])

        self.assertTrue(type(rezultat) is str, msg=f"Pasoš manje od 9 cifara")
        self.assertTrue(len(rezultat)>0, msg=f"Pasoš manje od 9 cifara")

        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            "111111111111",
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])

        self.assertTrue(type(rezultat) is str, msg=f"Pasoš više od 9 cifara")
        self.assertTrue(len(rezultat)>0, msg=f"Pasoš više od 9 cifara")

    def test_broj_telefona(self):
        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            self.pun_korisnik["uloga"],
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            "abcdefghi",
            self.pun_korisnik["pol"])
        self.assertTrue(type(rezultat) is str, msg="Broj telefona nije validan")
        self.assertTrue(len(rezultat)>0, msg=f"Broj telefona nije validan")

    def test_uloga(self):
        rezultat = korisnici.kreiraj_korisnika(
            {},
            False,  # azuriraj
            "nepoznata_uloga",
            None, # staro_korisnicko_ime
            self.pun_korisnik["korisnicko_ime"],
            self.pun_korisnik["lozinka"],
            self.pun_korisnik["ime"],
            self.pun_korisnik["prezime"],
            self.pun_korisnik["email"],
            self.pun_korisnik["pasos"],
            self.pun_korisnik["drzavljanstvo"],
            self.pun_korisnik["telefon"],
            self.pun_korisnik["pol"])
        self.assertTrue(type(rezultat) is str, msg=f"Uloga nije validna")
        self.assertTrue(len(rezultat)>0, msg=f"Uloga nije validna")

    def testiraj_korisnici_fajl(self):
        referentni_korisnici = {
            korisnik["korisnicko_ime"]: korisnik for korisnik in gen_rand_valid_users(10)
        }
        korisnici.sacuvaj_korisnike(self.putanja, "|", referentni_korisnici)

        ucitani_korisnici = korisnici.ucitaj_korisnike_iz_fajla(self.putanja, "|")
        self.assertIsNotNone(ucitani_korisnici, msg="Nisu učitani korisnici iz fajla")
        self.assertEqual(len(referentni_korisnici), len(ucitani_korisnici), msg="Dužine učitanih korisnika nisu jednake")
        for korisnicko_ime in ucitani_korisnici:
            ucitani_korisnik = ucitani_korisnici[korisnicko_ime]
            self.assertDictEqual(referentni_korisnici[korisnicko_ime], ucitani_korisnik, msg="Učitani korisnici se ne poklapaju")

    def testiraj_login(self):
        korisnicko_ime = self.pun_korisnik["korisnicko_ime"]
        lozinka = self.pun_korisnik["lozinka"]
        svi_korisnici = {
            korisnicko_ime: self.pun_korisnik
        }

        rezultat = korisnici.login(svi_korisnici, "mika", "mikic")

        self.assertTrue(type(rezultat) is str, msg=f"Login nepostojeći")
        self.assertTrue(len(rezultat)>0, msg=f"Login nepostojeći")

        rezultat = korisnici.login(svi_korisnici, korisnicko_ime, "321")

        self.assertTrue(type(rezultat) is str, msg=f"Login pogrešna lozinka")
        self.assertTrue(len(rezultat)>0, msg=f"Login pogrešna lozinka")

        pronadjeni_korisnik = korisnici.login(svi_korisnici, korisnicko_ime, lozinka)
        self.assertDictEqual(self.pun_korisnik, pronadjeni_korisnik, msg="Uspešan login")


if __name__ == '__main__':
    unittest.main()
