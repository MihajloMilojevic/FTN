import json
from Constants import SEPARATOR
import Utils.Serialize as Serialize


class Sala:

    primary_key = "sifra"
    name = "Sala"

    def __init__(self, sifra: str, naziv: str, broj_redova: int, broj_kolona: int):
        self.sifra = sifra
        self.naziv = naziv
        self.broj_redova = broj_redova
        self.broj_kolona = broj_kolona 
    
    def __getitem__(self, key: str) -> str|int:
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
    
    def __setitem__(self, key: str, value: str|int) -> None:
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
    
    @staticmethod
    def serialize(obj: 'Sala') -> str:
        data = [
            Serialize.serialize_string(obj.sifra),
            Serialize.serialize_string(obj.name),
            Serialize.serialize_int(obj.broj_redova),
            Serialize.serialize_int(obj.broj_kolona)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Sala':
        data = str.split(SEPARATOR)
        return Sala(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_int(data[2]),
            Serialize.deserialize_int(data[3])
        )
    
    def toJsonString(self):
        return json.dumps(self.toJsonObject()) 
    
    def toJsonObject(self):
        return {
            "sifra": self.sifra,
            "naziv": self.naziv,
            "broj_redova": self.broj_redova,
            "broj_kolona": self.broj_kolona
        } 
    
    @staticmethod
    def fromJsonString(str):
        return Sala.fromJsonObject(json.loads(str))      
    
    @staticmethod
    def fromJsonObject(obj):
        return Sala(
            obj["sifra"], 
            obj["naziv"], 
            obj["broj_redova"], 
            obj["broj_kolona"]
        )
    