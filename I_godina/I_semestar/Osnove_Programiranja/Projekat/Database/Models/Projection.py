import json
from Constants import SEPARATOR
from datetime import datetime
import Utils.Serialize as Serialize
from Database.Refrence import Refrence
import Database.Models as Models

class Projection:

    primary_key = "id"
    name = "Projection"

    def __init__(self, id: str, hall_id: str, film_id: str, starting_time: datetime, ending_time: datetime, days: list[str], price: float):
        self.id = id
        self.hall_id = hall_id
        self.film_id = film_id
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.days = days
        self.price = price
        self.hall = Refrence(self, Models.Hall, "hall_id")
        self.film = Refrence(self, Models.Film, "film_id")

    def __str__(self) -> str:
        return self.toJsonString()
    
    def __getitem__(self, key: str) -> str|datetime|float|list[str]:
        match key:
            case "id":
                return self.id
            case "film_id":
                return self.film_id
            case "hall_id":
                return self.hall_id
            case "starting_time":
                return self.starting_time
            case "ending_time":
                return self.ending_time
            case "days":
                return self.days
            case "price":
                return self.price
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str|datetime|float|list[str]) -> None:
        match key:
            case "id":
                self.id = value
            case "film_id":
                self.film_id = value
            case "hall_id":
                self.hall_id = value
            case "starting_time":
                self.starting_time = value
            case "ending_time":
                self.ending_time = value
            case "days":
                self.days = value
            case "price":
                self.price = value
            case _:
                raise "Invalid key"

    @staticmethod
    def serialize(obj: 'Projection') -> str:
        data = [
            Serialize.serialize_string(obj.id),
            Serialize.serialize_string(obj.hall_id),
            Serialize.serialize_string(obj.film_id),
            Serialize.serialize_time(obj.starting_time),
            Serialize.serialize_time(obj.ending_time),
            Serialize.serialize_list(obj.days),
            Serialize.serialize_float(obj.price)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Projection':
        data = str.split(SEPARATOR)
        return Projection(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_string(data[2]),
            Serialize.deserialize_time(data[3]),
            Serialize.deserialize_time(data[4]),
            Serialize.deserialize_list(data[5]),
            Serialize.deserialize_float(data[6])
        )

    def populatedObject(self, db):
        obj = self.toJsonObject()
        obj.update()
        obj["sala"] = self.hall.get(db)
        obj["film"] = self.film.get(db)
        print("Projection - Hall: ", obj["sala"])
        return obj
    
    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "id": self.id,
            "hall_id": self.hall_id,
            "film_id": self.film_id,
            "starting_time": datetime.strftime(self.starting_time, "%X"),
            "ending_time": datetime.strftime(self.ending_time, "%X"),
            "days": self.days,
            "price": self.price
        }

    @staticmethod
    def fromJsonString(str):
        return Projection.toJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        return Projection(
            obj["id"],
            obj["hall_id"],
            obj["film_id"],
            datetime.strptime(obj["starting_time"], "%X"),
            datetime.strptime(obj["ending_time"], "%X"),
            obj["days"],
            obj["price"],
        )