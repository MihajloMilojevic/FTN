import json
from Constants import SEPARATOR
import Utils.Serialize as Serialize

class Film:

    primary_key = "id"
    name = "Film"
    
    def __init__(self, id: str, name: str, genres: list[str], duration: int, director: str, main_roles: list[str],
                 country: str, year: int, description: str):
        self.id = id
        self.name = name
        self.genres = genres
        self.duration = duration
        self.director = director
        self.main_roles = main_roles
        self.country = country
        self.year = year
        self.description = description

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str|int|list[str]:
        match key:
            case "id":
                return self.id
            case "name":
                return self.name
            case "genres":
                return self.genres
            case "duration":
                return self.duration
            case "director":
                return self.director
            case "main_roles":
                return self.main_roles
            case "country":
                return self.country
            case "year":
                return self.year
            case "description":
                return self.description
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str|int|list[str]) -> None:
        match key:
            case "id":
                self.id = value
            case "name":
                self.name = value
            case "genres":
                self.genres = value
            case "duration":
                self.duration = value
            case "director":
                self.director = value
            case "main_roles":
                self.main_roles = value
            case "country":
                self.country = value
            case "year":
                self.year = value
            case "description":
                self.description = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Film') -> str:
        data = [
            Serialize.serialize_string(obj.id),
            Serialize.serialize_string(obj.name),
            Serialize.serialize_list(obj.genres),
            Serialize.serialize_int(obj.duration),
            Serialize.serialize_string(obj.director),
            Serialize.serialize_list(obj.main_roles),
            Serialize.serialize_string(obj.country),
            Serialize.serialize_int(obj.year),
            Serialize.serialize_string(obj.description)
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
            "id": self.id,
            "name": self.name,
            "genres": self.genres,
            "duration": self.duration,
            "director": self.director,
            "main_roles": self.main_roles,
            "country": self.country,
            "year": self.year,
            "description": self.description
        }
    
    @staticmethod
    def fromJsonString(str):
        return Film.fromJsonObject(json.loads(str))

    @staticmethod
    def fromJsonObject(obj):
        return Film(
            obj["id"], 
            obj["name"], 
            obj["genres"], 
            obj["duration"], 
            obj["director"],
            obj["main_roles"], 
            obj["country"], 
            obj["year"], 
            obj["description"]
        )
    