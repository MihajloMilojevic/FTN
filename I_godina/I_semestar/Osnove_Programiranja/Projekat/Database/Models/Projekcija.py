import json
from datetime import datetime


class Projekcija:
    def __init__(self, sifra, sifra_sale, sifra_filma, vreme_pocetka, vreme_kraja, dani, cena):
        self.sifra = sifra
        self.sifra_sale = sifra_sale
        self.sifra_filma = sifra_filma
        self.vreme_pocetka = vreme_pocetka
        self.vreme_kraja = vreme_kraja
        self.dani = dani
        self.cena = cena
    
    def __getitem__(self, key):
        match key:
            case "sifra":
                return self.sifra
            case "sifra_filma":
                return self.sifra_filma
            case "sifra_sale":
                return self.sifra_sale
            case "vreme_pocetka":
                return self.vreme_pocetka
            case "vreme_kraja":
                return self.vreme_kraja
            case "dani":
                return self.dani
            case "cena":
                return self.cena
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key, value):
        match key:
            case "sifra":
                self.sifra = value
            case "sifra_filma":
                self.sifra_filma = value
            case "sifra_sale":
                self.sifra_sale = value
            case "vreme_pocetka":
                self.vreme_pocetka = value
            case "vreme_kraja":
                self.vreme_kraja = value
            case "dani":
                self.dani = value
            case "cena":
                self.cena = value
            case _:
                raise "Invalid key"
    def toJson(self):
        return json.dumps({
            "sifra": self.sifra,
            "sifra_sale": self.sifra_sale,
            "sifra_filma": self.sifra_filma,
            "vreme_pocetka": datetime.strftime(self.vreme_pocetka, "%X"),
            "vreme_kraja": datetime.strftime(self.vreme_kraja, "%X"),
            "dani": self.dani,
            "cena": self.cena
        })

    @staticmethod
    def fromJson(str):
        v = json.loads(str)
        return Projekcija(
            v["sifra"],
            v["sifra_sale"],
            v["sifra_filma"],
            datetime.strptime(v["vreme_pocetka"], "%X"),
            datetime.strptime(v["vreme_kraja"], "%X"),
            v["dani"],
            v["cena"],
        )