import json
from datetime import datetime
from constants import SEPARATOR
import utils.serialize as Serialize
from database.refrence import Refrence
import database.models as Models


class Ticket:
    
    primary_key = "id"
    name = "Ticket"

    def __init__(self, id: str, showtime_id: str, seat_tag: str, reserved: bool, 
                 sale_date: datetime, username: str|None, full_name: str|None, sold_price: float):
        self.id = id
        self.showtime_id = showtime_id
        self.seat_tag = seat_tag
        self.reserved = reserved
        self.sale_date = sale_date
        self.username = username
        self.full_name = full_name
        self.sold_price = sold_price
        self.showtime = Refrence(self, Models.Showtime, "showtime_id")
        self.user = Refrence(self, Models.User, "username")

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str|bool|float|datetime|None:
        match key:
            case "id":
                return self.id
            case "showtime_id":
                return self.showtime_id
            case "seat_tag":
                return self.seat_tag
            case "reserved":
                return self.reserved
            case "sale_date":
                return self.sale_date
            case "username":
                return self.username
            case "full_name":
                return self.full_name
            case "sold_price":
                return self.sold_price
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str|bool|float|datetime|None) -> None:
        match key:
            case "id":
                self.id = value
            case "showtime_id":
                self.showtime_id = value
            case "seat_tag":
                self.seat_tag = value
            case "reserved":
                self.reserved = value
            case "sale_date":
                self.sale_date = value
            case "username":
                self.username = value
            case "full_name":
                self.full_name = value
            case "sold_price":
                self.sold_price = value
            case _:
                raise "Invalid key"
    
    @staticmethod
    def serialize(obj: 'Ticket') -> str:
        data = [
            Serialize.serialize_string(obj.id),
            Serialize.serialize_string(obj.showtime_id),
            Serialize.serialize_string(obj.seat_tag),
            Serialize.serialize_bool(obj.reserved),
            Serialize.serialize_date(obj.sale_date),
            Serialize.serialize_string(obj.username),
            Serialize.serialize_string(obj.full_name),
            Serialize.serialize_float(obj.sold_price)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'Ticket':
        data = str.split(SEPARATOR)
        return Ticket(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_string(data[2]),
            Serialize.deserialize_bool(data[3]),
            Serialize.deserialize_date(data[4]),
            Serialize.deserialize_string(data[5]),
            Serialize.deserialize_string(data[6]),
            Serialize.deserialize_float(data[7])
        )
    
    def populatedObject(self, db):
        obj = self.toJsonObject()
        obj["showtime"] = self.showtime.get(db)
        obj["user"] = self.user.get(db)
        return obj

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "id": self.id,
            "showtime_id": self.showtime_id,
            "seat_tag": self.seat_tag,
            "reserved": self.reserved,
            "sale_date": datetime.strftime(self.sale_date, "%x") if self.sale_date is not None else None,
            "username": self.username,
            "full_name": self.full_name
        }
    
    @staticmethod
    def fromJson(str):
        return Ticket.fromJsonObject(json.loads(str))
    
    @staticmethod
    def fromJsonObject(obj):
        return Ticket(
            obj["id"],
            obj["showtime_id"],
            obj["seat_tag"],
            obj["reserved"],
            datetime.strptime(obj["sale_date"], "%x"),
            obj["username"],
            obj["full_name"],
        )
