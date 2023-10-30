import json

class Film:
    def __init__(self, sifra, naziv, zanrovi, trajanje, reziser, glavne_uloge,
                 zemlja_porekla, godina_proizvodnje, opis):
        self.sifra = sifra
        self.naziv = naziv,
        self.zanrovi = zanrovi,
        self.trajanje = trajanje
        self.reziser = reziser
        self.glavne_uloge = glavne_uloge
        self.zemlja_porekla = zemlja_porekla
        self.godina_proizvodnje = godina_proizvodnje
        self.opis = opis

    def __getitem__(self, key):
        match key:
            case "sifra":
                return self.sifra
            case "naziv":
                return self.naziv
            case "zanrovi":
                return self.zanrovi
            case "trajanje":
                return self.trajanje
            case "reziser":
                return self.reziser
            case "glavne_uloge":
                return self.glavne_uloge
            case "zemlja_porekla":
                return self.zemlja_porekla
            case "godina_proizvodnje":
                return self.godina_proizvodnje
            case "opis":
                return self.opis
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key, value):
        match key:
            case "sifra":
                self.sifra = value
            case "naziv":
                self.naziv = value
            case "zanrovi":
                self.zanrovi = value
            case "trajanje":
                self.trajanje = value
            case "reziser":
                self.reziser = value
            case "glavne_uloge":
                self.glavne_uloge = value
            case "zemlja_porekla":
                self.zemlja_porekla = value
            case "godina_proizvodnje":
                self.godina_proizvodnje = value
            case "opis":
                self.opis = value
            case _:
                raise "Invalid key"
    
    def toJson(self):
        return json.dumps({
            "sifra": self.sifra,
            "naziv": self.naziv,
            "zanrovi": self.zanrovi,
            "trajanje": self.trajanje,
            "reziser": self.reziser,
            "glavne_uloge": self.glavne_uloge,
            "zemlja_porekla": self.zemlja_porekla,
            "godina_proizvodnje": self.godina_proizvodnje,
            "opis": self.opis
        })

    @staticmethod
    def fromJson(str):
        val = json.loads(str)
        return Film(
            val["sifra"], 
            val["naziv"], 
            val["zanrovi"], 
            val["trajanje"], 
            val["reziser"],
            val["glavne_uloge"], 
            val["zemlja_porekla"], 
            val["godina_proizvodnje"], 
            val["opis"]
        )
    