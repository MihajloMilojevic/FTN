import json
from constants import SEPARATOR
import utils.serialize as Serialize
from datetime import datetime
from database.refrence import Refrence
from database.models.projection import Projection


class Showtime:

    primary_key = "id"
    name = "Showtime"

    def __init__(self, id: str, projection_id: str, date: datetime):
        self.id = id
        self.projection_id = projection_id
        self.date = date
        self.projection = Refrence(self, Projection, "projection_id")

    def __str__(self) -> str:
        return self.toJsonString()
    
    def __getitem__(self, key: str) -> str|datetime:
        match key:
            case "id":
                return self.id
            case "projection_id":
                return self.projection_id
            case "date":
                return self.date
            case _:
                raise "Invalid key"   
    
    def __setitem__(self, key: str, value: str|datetime) -> None:
        match key:
            case "id":
                self.id = value
            case "projection_id":
                self.projection_id = value
            case "date":
                self.date = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Showtime') -> str:
        data = [
            Serialize.serialize_string(obj.id),
            Serialize.serialize_string(obj.projection_id),
            Serialize.serialize_date(obj.date)
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
        obj["projection"] = self.projection.get(db)
        return obj

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "id": self.id,
            "projection_id": self.projection_id,
            "date": datetime.strftime(self.date, "%x")
        } 
    
    @staticmethod
    def fromJsonString(json_string):
        return Showtime.fromJsonObject(json.loads(json_string))
    
    @staticmethod
    def fromJsonObject(obj):
        return Showtime(
            obj["id"], 
            obj["projection_id"], 
            datetime.strptime(obj["date"], "%x")
        )