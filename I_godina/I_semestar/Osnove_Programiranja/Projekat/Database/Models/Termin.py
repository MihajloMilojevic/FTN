import json
from datetime import datetime


class Termin:

    primary_key = "sifra"
    name = "Termin"

    def __init__(self, sifra, sifra_projekcije, datum_odrzavanja):
        self.sifra = sifra
        self.sifra_projekcije = sifra_projekcije
        self.datum_odrzavanja = datum_odrzavanja

    def __getitem__(self, key):
        match key:
            case "sifra":
                return self.sifra
            case "sifra_projekcije":
                return self.sifra_projekcije
            case "datum_odrzavanja":
                return self.datum_odrzavanja
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key, value):
        match key:
            case "sifra":
                self.sifra = value
            case "sifra_projekcije":
                self.sifra_projekcije = value
            case "datum_odrzavanja":
                self.datum_odrzavanja = value
            case _:
                raise "Invalid key"
            
    def toJsonString(self):
        return json.dumps(self.toJsonObject())
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "sifra_projekcije": self.sifra_projekcije,
            "datum_odrzavanja": datetime.strftime(self.datum_odrzavanja, "%x")
        }
    
    @staticmethod
    def fromJsonString(str):
        return Termin.fromJsonObject(json.loads(str))
    
    @staticmethod
    def fromJsonObject(obj):
        return Termin(
            obj["sifra"], 
            obj["sifra_projekcije"], 
            datetime.strptime(obj["datum_odrzavanja"], "%x")
        )