import json
from Constants import SEPARATOR
import Utils.Serialize as Serialize


class Hall:

    primary_key = "sifra"
    name = "Hall"

    def __init__(self, sifra: str, naziv: str, broj_redova: int, broj_sedista: int):
        self.sifra = sifra
        self.naziv = naziv
        self.broj_redova = broj_redova
        self.broj_sedista = broj_sedista 

    def __str__(self) -> str:
        return self.toJsonString()
    
    def __getitem__(self, key: str) -> str|int:
        match key:
            case "sifra":
                return self.sifra
            case "naziv":
                return  self.naziv
            case "broj_redova":
                return self.broj_redova
            case "broj_sedista":
                return self.broj_sedista
            case _:
                raise "Invalid key"
    
    def __setitem__(self, key: str, value: str|int) -> None:
        match key:
            case "sifra":
                self.sifra = value
            case "naziv":
                self.naziv = value
            case "broj_redova":
                self.broj_redova = value
            case "broj_sedista":
                self.broj_sedista = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Hall') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.naziv),
            Serialize.serialize_int(obj.broj_redova),
            Serialize.serialize_int(obj.broj_sedista)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Hall':
        data = str.split(SEPARATOR)
        return Hall(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_int(data[2]),
            Serialize.deserialize_int(data[3])
        )
    
    def populatedObject(self, db):
        print("Hall: ", self.toJsonObject())
        return self.toJsonObject()
    
    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent) 
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "naziv": self.naziv,
            "broj_redova": self.broj_redova,
            "broj_sedista": self.broj_sedista
        } 
    
    @staticmethod
    def fromJsonString(str):
        return Hall.fromJsonObject(json.loads(str))      
    
    @staticmethod
    def fromJsonObject(obj):
        return Hall(
            obj["sifra"], 
            obj["naziv"], 
            obj["broj_redova"], 
            obj["broj_sedista"]
        )
    