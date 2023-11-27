import json
from Constants import SEPARATOR
import Utils.Serialize as Serialize


class Hall:

    primary_key = "id"
    name = "Hall"

    def __init__(self, id: str, name: str, row_count: int, seats_per_row: int):
        self.id = id
        self.name = name
        self.row_count = row_count
        self.seats_per_row = seats_per_row 

    def __str__(self) -> str:
        return self.toJsonString()
    
    def __getitem__(self, key: str) -> str|int:
        match key:
            case "id":
                return self.id
            case "name":
                return  self.name
            case "row_count":
                return self.row_count
            case "seats_per_row":
                return self.seats_per_row
            case _:
                raise "Invalid key"
    
    def __setitem__(self, key: str, value: str|int) -> None:
        match key:
            case "id":
                self.id = value
            case "name":
                self.name = value
            case "row_count":
                self.row_count = value
            case "seats_per_row":
                self.seats_per_row = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Hall') -> str:
        data = [
            Serialize.serialize_string(obj.id),
            Serialize.serialize_string(obj.name),
            Serialize.serialize_int(obj.row_count),
            Serialize.serialize_int(obj.seats_per_row)
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
            "id": self.id,
            "name": self.name,
            "row_count": self.row_count,
            "seats_per_row": self.seats_per_row
        } 
    
    @staticmethod
    def fromJsonString(str):
        return Hall.fromJsonObject(json.loads(str))      
    
    @staticmethod
    def fromJsonObject(obj):
        return Hall(
            obj["id"], 
            obj["name"], 
            obj["row_count"], 
            obj["seats_per_row"]
        )
    