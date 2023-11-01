from typing import Any
from Database.Table import Table
import Database.Models as Models
import json

class Database:

    def __init__(self):
        self.korisnici = Table(Models.Korisnik)
        self.sale = Table(Models.Sala)
        self.filmovi = Table(Models.Film)
        self.projekcije = Table(Models.Projekcija)
        self.termini = Table(Models.Termin)
        self.karte = Table(Models.Karta)

    def __getitem__(self, key: str) -> Table:
        match key:
            case Models.Korisnik.name:
                return self.korisnici
            case Models.Karta.name:
                return self.karte
            case Models.Sala.name:
                return self.sale
            case Models.Film.name:
                return self.filmovi
            case Models.Projekcija.name:
                return self.projekcije
            case Models.Termin.name:
                return self.termini
            case _:
                raise "Invalid key"

    def load(self):
        self.korisnici.load()
        self.sale.load()
        self.filmovi.load()
        self.projekcije.load()
        self.termini.load()
        self.karte.load()

    def save(self):
        self.korisnici.save()
        self.sale.save()
        self.filmovi.save()
        self.projekcije.save()
        self.termini.save()
        self.karte.save()

    def populatedObject(self):
        return {
            "korisnici": self.korisnici.populatedObject(self),
            "sale": self.sale.populatedObject(self),
            "filmovi": self.filmovi.populatedObject(self),
            "projekcije": self.projekcije.populatedObject(self),
            "termini": self.termini.populatedObject(self),
            "karte": self.karte.populatedObject(self)
        }

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "korisnici": self.korisnici.toJsonObject(),
            "sale": self.sale.toJsonObject(),
            "filmovi": self.filmovi.toJsonObject(),
            "projekcije": self.projekcije.toJsonObject(),
            "termini": self.termini.toJsonObject(),
            "karte": self.karte.toJsonObject()
        }
    
    @staticmethod
    def fromJsonString(str):
        return Database.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        db = Database()
        db.korisnici = Table.fromJsonObject(obj["korisnici"])
        db.sale = Table.fromJsonObject(obj["sale"])
        db.filmovi = Table.fromJsonObject(obj["filmovi"])
        db.projekcije = Table.fromJsonObject(obj["projekcije"])
        db.termini = Table.fromJsonObject(obj["termini"])
        db.karte = Table.fromJsonObject(obj["karte"])
        return db

    def setupJson(self):
        file = open("data.json", "r")
        str = file.read()
        db = Database.fromJsonString(str)
        self.korisnici = db.korisnici
        self.sale = db.sale
        self.filmovi = db.filmovi
        self.projekcije = db.projekcije
        self.termini = db.termini
        self.karte = db.karte
        file.close()

    def saveJson(self):
        file = open("data.json", "w")
        file.write(self.toJsonString())
        file.close()

