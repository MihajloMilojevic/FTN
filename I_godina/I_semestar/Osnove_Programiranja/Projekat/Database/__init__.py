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

    def toJsonString(self):
        return json.dumps(self.toJsonObject())
    
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

    def setup(self):
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

    def save(self):
        file = open("data.json", "w")
        file.write(self.toJsonString())
        file.close()

