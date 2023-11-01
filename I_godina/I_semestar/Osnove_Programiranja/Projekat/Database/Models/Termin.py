import json
from Constants import SEPARATOR
from datetime import datetime
from Database.Refrence import Refrence
from Database.Models.Projekcija import Projekcija
import Utils.Serialize as Serialize


class Termin:

    primary_key = "sifra"
    name = "Termin"
    refrences = [
        Refrence(Projekcija, "sifra_projekcije")
    ]

    def __init__(self, sifra: str, sifra_projekcije: str, datum_odrzavanja: datetime):
        self.sifra = sifra
        self.sifra_projekcije = sifra_projekcije
        self.datum_odrzavanja = datum_odrzavanja
    
    def __getitem__(self, key: str) -> str|datetime:
        match key:
            case "sifra":
                return self.sifra
            case "sifra_projekcije":
                return self.sifra_projekcije
            case "datum_odrzavanja":
                return self.datum_odrzavanja
            case _:
                raise "Invalid key"   
    
    def __setitem__(self, key: str, value: str|datetime) -> None:
        match key:
            case "sifra":
                self.sifra = value
            case "sifra_projekcije":
                self.sifra_projekcije = value
            case "datum_odrzavanja":
                self.datum_odrzavanja = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Termin') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.sifra_projekcije),
            Serialize.serialize_date(obj.datum_odrzavanja)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Termin':
        data = str.split(SEPARATOR)
        return Termin(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_date(data[2])
        )
    
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