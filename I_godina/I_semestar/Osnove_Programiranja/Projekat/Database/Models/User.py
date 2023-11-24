import json
import Utils.Serialize as Serialize
from Constants import SEPARATOR, LOYALTY_SUM
from Database.Models import Ticket
from datetime import datetime



class User:

    primary_key = "korisnicko_ime"
    name = "User"

    def __init__(self, korisnicko_ime: str, lozinka: str, ime: str, prezime: str, uloga: str):
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.ime = ime
        self.prezime = prezime
        self.uloga = uloga

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str:
        match key:
            case "korisnicko_ime":
                return self.korisnicko_ime
            case "lozinka":
                return self.lozinka
            case "ime":
                return self.ime
            case "prezime":
                return self.prezime
            case "uloga":
                return self.uloga
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str) -> None:
        match key:
            case "korisnicko_ime":
                self.korisnicko_ime = value
            case "lozinka":
                self.lozinka = value
            case "ime":
                self.ime = value
            case "prezime":
                self.prezime = value
            case "uloga":
                self.uloga = value
            case _:
                raise "Invalid key"

    @staticmethod
    def serialize(obj: 'User') -> str:
        data = [
            Serialize.serialize_string(obj.korisnicko_ime),
            Serialize.serialize_string(obj.lozinka),
            Serialize.serialize_string(obj.ime),
            Serialize.serialize_string(obj.prezime),
            Serialize.serialize_string(obj.uloga)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'User':
        data = str.split(SEPARATOR)
        return User(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_string(data[2]),
            Serialize.deserialize_string(data[3]),
            Serialize.deserialize_string(data[4])
        )
    
    def populatedObject(self, db):
        return self.toJsonObject()

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "korisnicko_ime": self.korisnicko_ime,
            "lozinka": self.lozinka,
            "ime": self.ime,
            "prezime": self.prezime,
            "uloga": self.uloga
        }
    
    @staticmethod
    def fromJsonString(str):
        return User.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        return User(
            obj["korisnicko_ime"],
            obj["lozinka"],
            obj["ime"],
            obj["prezime"],
            obj["uloga"],
        )
    
    def check_loyalty(self, db) -> bool:
        def check(karta: Ticket) -> bool:
            if karta.datum_prodaje is None:
                return False
            if karta.korisnicko_ime is None:
                return False
            if karta.korisnicko_ime != self.korisnicko_ime:
                return False
            today = datetime.now()
            last_year = today.replace(year=today.year-1)
            if karta.datum_prodaje < last_year:
                return False
            return True
        karte = db.karte.Select(check)
        total_value = sum([karta.prodajna_cena for karta in karte])
        return total_value >= LOYALTY_SUM
