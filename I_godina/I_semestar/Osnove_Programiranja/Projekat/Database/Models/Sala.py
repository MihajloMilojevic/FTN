import json


class Sala:
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
    def toJson(self):
        return json.dumps({
            "sifra": self.sifra,
            "naziv": self.naziv,
            "broj_redova": self.broj_redova,
            "broj_kolona": self.broj_kolona
        })
    
    @staticmethod
    def fromJson(str):
        value = json.loads(str)
        return Sala(
            value["sifra"], 
            value["naziv"], 
            value["broj_redova"], 
            value["broj_kolona"]
        )