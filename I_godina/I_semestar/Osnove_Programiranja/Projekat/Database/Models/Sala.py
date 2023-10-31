import json


class Sala:

    primary_key = "sifra"
    name = "Sala"

    def __init__(self, sifra, naziv, broj_redova, broj_kolona):
        self.sifra = sifra
        self.naziv = naziv
        self.broj_redova = broj_redova
        self.broj_kolona = broj_kolona
        
    def __getitem__(self, key):
        match key:
            case "sifra":
                return self.sifra
            case "naziv":
                return  self.naziv
            case "broj_redova":
                return self.broj_redova
            case "broj_kolona":
                return self.broj_kolona
            case _:
                raise "Invalid key"
    def __setitem__(self, key, value):
        match key:
            case "sifra":
                self.sifra = value
            case "naziv":
                self.naziv = value
            case "broj_redova":
                self.broj_redova = value
            case "broj_kolona":
                self.broj_kolona = value
            case _:
                raise "Invalid key"
    def toJsonString(self):
        return json.dumps(self.toJsonObject())
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "naziv": self.naziv,
            "broj_redova": self.broj_redova,
            "broj_kolona": self.broj_kolona
        }
    
    @staticmethod
    def fromJsonString(str):
        return Sala.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        return Sala(
            obj["sifra"], 
            obj["naziv"], 
            obj["broj_redova"], 
            obj["broj_kolona"]
        )