import json
from datetime import datetime


class Karta:

    def __init__(self, sifra, sifra_termina, oznaka_sedista, rezervisano, datum_prodaje, korisnicko_ime, ime_i_prezime):
        self.sifra = sifra
        self.sifra_termina = sifra_termina
        self.oznaka_sedista = oznaka_sedista
        self.rezervisano = rezervisano
        self.datum_prodaje = datum_prodaje
        self.korisnicko_ime = korisnicko_ime
        self.ime_i_prezime = ime_i_prezime

    def __getitem__(self, key):
        match key:
            case "sifra":
                return self.sifra
            case "sifra_termina":
                return self.sifra_termina
            case "oznaka_sedista":
                return self.oznaka_sedista
            case "rezervisano":
                return self.rezervisano
            case "datum_prodaje":
                return self.datum_prodaje
            case "korisnicko_ime":
                return self.korisnicko_ime
            case "ime_i_prezime":
                return self.ime_i_prezime
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key, value):
        match key:
            case "sifra":
                self.sifra = value
            case "sifra_termina":
                self.sifra_termina = value
            case "oznaka_sedista":
                self.oznaka_sedista = value
            case "rezervisano":
                self.rezervisano = value
            case "datum_prodaje":
                self.datum_prodaje = value
            case "korisnicko_ime":
                self.korisnicko_ime = value
            case "ime_i_prezime":
                self.ime_i_prezime = value
            case _:
                raise "Invalid key"
    
    def toJson(self):
        return json.dumps({
            "sifra": self.sifra,
            "sifra_termina": self.sifra_termina,
            "oznaka_sedista": self.oznaka_sedista,
            "rezervisano": self.rezervisano,
            "datum_prodaje": datetime.strftime(self.datum_prodaje, "%x"),
            "korisnicko_ime": self.korisnicko_ime,
            "ime_i_prezime": self.ime_i_prezime
        })
    
    @staticmethod
    def fromJson(str):
        v = json.loads(str)
        return Karta(
            v["sifra"],
            v["sifra_termina"],
            v["oznaka_sedista"],
            v["rezervisano"],
            datetime.strptime(v["datum_prodaje"], "%x"),
            v["korisnicko_ime"],
            v["ime_i_prezime"],
        )
