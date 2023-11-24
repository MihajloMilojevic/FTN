import json
from Constants import SEPARATOR
from datetime import datetime
from Database.Refrence import Refrence
from Database.Models.Projection import Projection
import Utils.Serialize as Serialize


class Showtime:

    primary_key = "sifra"
    name = "Showtime"
    refrences = [
    ]

    def __init__(self, sifra: str, sifra_projekcije: str, datum_odrzavanja: datetime):
        self.sifra = sifra
        self.sifra_projekcije = sifra_projekcije
        self.datum_odrzavanja = datum_odrzavanja
        self.projekcija = Refrence(self, Projection, "sifra_projekcije")

    def __str__(self) -> str:
        return self.toJsonString()
    
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
    def serialize(obj: 'Showtime') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.sifra_projekcije),
            Serialize.serialize_date(obj.datum_odrzavanja)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Showtime':
        data = str.split(SEPARATOR)
        return Showtime(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_date(data[2])
        )
    
    def populatedObject(self, db):
        obj = self.toJsonObject()
        obj["projekcija"] = self.projekcija.get(db)
        return obj

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "sifra_projekcije": self.sifra_projekcije,
            "datum_odrzavanja": datetime.strftime(self.datum_odrzavanja, "%x")
        } 
    
    @staticmethod
    def fromJsonString(str):
        return Showtime.fromJsonObject(json.loads(str))
    
    @staticmethod
    def fromJsonObject(obj):
        return Showtime(
            obj["sifra"], 
            obj["sifra_projekcije"], 
            datetime.strptime(obj["datum_odrzavanja"], "%x")
        )