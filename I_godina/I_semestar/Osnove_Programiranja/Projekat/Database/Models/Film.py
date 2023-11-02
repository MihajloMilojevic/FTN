import json
from Constants import SEPARATOR
import Utils.Serialize as Serialize

class Film:

    primary_key = "sifra"
    name = "Film"
    
    def __init__(self, sifra: str, naziv: str, zanrovi: list[str], trajanje: int, reziser: str, glavne_uloge: list[str],
                 zemlja_porekla: str, godina_proizvodnje: int, opis: str):
        self.sifra = sifra
        self.naziv = naziv
        self.zanrovi = zanrovi
        self.trajanje = trajanje
        self.reziser = reziser
        self.glavne_uloge = glavne_uloge
        self.zemlja_porekla = zemlja_porekla
        self.godina_proizvodnje = godina_proizvodnje
        self.opis = opis

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str|int|list[str]:
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
        
    def __setitem__(self, key: str, value: str|int|list[str]) -> None:
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
    
    @staticmethod
    def serialize(obj: 'Film') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.naziv),
            Serialize.serialize_list(obj.zanrovi),
            Serialize.serialize_int(obj.trajanje),
            Serialize.serialize_string(obj.reziser),
            Serialize.serialize_list(obj.glavne_uloge),
            Serialize.serialize_string(obj.zemlja_porekla),
            Serialize.serialize_int(obj.godina_proizvodnje),
            Serialize.serialize_string(obj.opis)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Film':
        data = str.split(SEPARATOR)
        return Film(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_list(data[2]),
            Serialize.deserialize_int(data[3]),
            Serialize.deserialize_string(data[4]),
            Serialize.deserialize_list(data[5]),
            Serialize.deserialize_string(data[6]),
            Serialize.deserialize_int(data[7]),
            Serialize.deserialize_string(data[8])
        )
    
    def populatedObject(self, db):
        return self.toJsonObject()
    
    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "naziv": self.naziv,
            "zanrovi": self.zanrovi,
            "trajanje": self.trajanje,
            "reziser": self.reziser,
            "glavne_uloge": self.glavne_uloge,
            "zemlja_porekla": self.zemlja_porekla,
            "godina_proizvodnje": self.godina_proizvodnje,
            "opis": self.opis
        }
    
    @staticmethod
    def fromJsonString(str):
        return Film.fromJsonObject(json.loads(str))

    @staticmethod
    def fromJsonObject(obj):
        return Film(
            obj["sifra"], 
            obj["naziv"], 
            obj["zanrovi"], 
            obj["trajanje"], 
            obj["reziser"],
            obj["glavne_uloge"], 
            obj["zemlja_porekla"], 
            obj["godina_proizvodnje"], 
            obj["opis"]
        )
    