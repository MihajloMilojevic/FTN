import json
from datetime import datetime
from Constants import SEPARATOR
import Utils.Serialize as Serialize
from Database.Refrence import Refrence
import Database.Models as Models


class Karta:
    
    primary_key = "sifra"
    name = "Karta"

    def __init__(self, sifra: str, sifra_termina: str, oznaka_sedista: str, rezervisano: bool, 
                 datum_prodaje: datetime, korisnicko_ime: str|None, ime_i_prezime: str|None, prodajna_cena: float):
        self.sifra = sifra
        self.sifra_termina = sifra_termina
        self.oznaka_sedista = oznaka_sedista
        self.rezervisano = rezervisano
        self.datum_prodaje = datum_prodaje
        self.korisnicko_ime = korisnicko_ime
        self.ime_i_prezime = ime_i_prezime
        self.prodajna_cena = prodajna_cena
        self.termin = Refrence(self, Models.Termin, "sifra_termina")
        self.korisnik = Refrence(self, Models.Korisnik, "korisnicko_ime")

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str|bool|float|datetime|None:
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
            case "prodajna_cena":
                return self.prodajna_cena
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str|bool|float|datetime|None) -> None:
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
            case "prodajna_cena":
                self.prodajna_cena = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Karta') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.sifra_termina),
            Serialize.serialize_string(obj.oznaka_sedista),
            Serialize.serialize_bool(obj.rezervisano),
            Serialize.serialize_date(obj.datum_prodaje),
            Serialize.serialize_string(obj.korisnicko_ime),
            Serialize.serialize_string(obj.ime_i_prezime),
            Serialize.serialize_float(obj.prodajna_cena)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Karta':
        data = str.split(SEPARATOR)
        return Karta(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_string(data[2]),
            Serialize.deserialize_bool(data[3]),
            Serialize.deserialize_date(data[4]),
            Serialize.deserialize_string(data[5]),
            Serialize.deserialize_string(data[6]),
            Serialize.deserialize_float(data[7])
        )
    
    def populatedObject(self, db):
        obj = self.toJsonObject()
        obj["termin"] = self.termin.get(db)
        obj["korisnik"] = self.korisnik.get(db)
        return obj

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "sifra_termina": self.sifra_termina,
            "oznaka_sedista": self.oznaka_sedista,
            "rezervisano": self.rezervisano,
            "datum_prodaje": datetime.strftime(self.datum_prodaje, "%x") if self.datum_prodaje is not None else None,
            "korisnicko_ime": self.korisnicko_ime,
            "ime_i_prezime": self.ime_i_prezime
        }
    
    @staticmethod
    def fromJson(str):
        return Karta.fromJsonObject(json.loads(str))
    
    @staticmethod
    def fromJsonObject(obj):
        return Karta(
            obj["sifra"],
            obj["sifra_termina"],
            obj["oznaka_sedista"],
            obj["rezervisano"],
            datetime.strptime(obj["datum_prodaje"], "%x"),
            obj["korisnicko_ime"],
            obj["ime_i_prezime"],
        )
