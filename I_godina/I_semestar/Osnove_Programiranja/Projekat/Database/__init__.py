from Database.Table import Table
import json


class Database:
    def __init__(self):
        self.korisnici = Table("Korisnik", "korisnicko_ime")
        self.sale = Table("Sala", "sifra")
        self.filmovi = Table("Film", "sifra")
        self.projekcije = Table("Projekcija", "sifra")
        self.termini = Table("Termin", "sifra")
        self.karte = Table("Karta", "sifra")

    def toJson(self):
        return json.dumps({
            "korisnici": self.korisnici.toJson(),
            "sale": self.sale.toJson(),
            "filmovi": self.filmovi.toJson(),
            "projekcije": self.projekcije.toJson(),
            "termini": self.termini.toJson(),
            "karte": self.karte.toJson()
        })
    
    @staticmethod
    def fromJson(str):
        v = json.loads(str)
        db = Database()
        db.korisnici = Table.fromJson(v["korisnici"])
        db.sale = Table.fromJson(v["sale"])
        db.filmovi = Table.fromJson(v["filmovi"])
        db.projekcije = Table.fromJson(v["projekcije"])
        db.termini = Table.fromJson(v["termini"])
        db.karte = Table.fromJson(v["karte"])
        return db

    def setup(self):
        file = open("data.json", "r")
        str = file.read()
        db = Database.fromJson(str)
        self.korisnici = db.korisnici
        self.sale = db.sale
        self.filmovi = db.filmovi
        self.projekcije = db.projekcije
        self.termini = db.termini
        self.karte = db.karte
        file.close()

    def save(self):
        file = open("data.json", "w")
        file.write(self.toJson())
        file.close()

