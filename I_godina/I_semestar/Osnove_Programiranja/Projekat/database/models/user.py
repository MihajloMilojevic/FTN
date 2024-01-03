import json
from constants import SEPARATOR, LOYALTY_SUM
import utils.serialize as Serialize
from database.models import Ticket
from datetime import datetime



class User:

    primary_key = "username"
    name = "User"

    def __init__(self, username: str, password: str, name: str, surname: str, role: str):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role

    def __str__(self) -> str:
        return self.toJsonString()

    def __getitem__(self, key: str) -> str:
        match key:
            case "username":
                return self.username
            case "password":
                return self.password
            case "name":
                return self.name
            case "surname":
                return self.surname
            case "role":
                return self.role
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key: str, value: str) -> None:
        match key:
            case "username":
                self.username = value
            case "password":
                self.password = value
            case "name":
                self.name = value
            case "surname":
                self.surname = value
            case "role":
                self.role = value
            case _:
                raise "Invalid key"

    @staticmethod
    def serialize(obj: 'User') -> str:
        data = [
            Serialize.serialize_string(obj.username),
            Serialize.serialize_string(obj.password),
            Serialize.serialize_string(obj.name),
            Serialize.serialize_string(obj.surname),
            Serialize.serialize_string(obj.role)
        ]
        return SEPARATOR.join(data)
    
    @staticmethod
    def deserialize(str: str) -> 'User':
        data = str.split(SEPARATOR)
        return User(
            Serialize.deserialize_string(data[0]),
            Serialize.deserialize_string(data[1]),
            Serialize.deserialize_string(data[2]),
            Serialize.deserialize_string(data[3]),
            Serialize.deserialize_string(data[4])
        )
    
    def populatedObject(self, db):
        return self.toJsonObject()

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "role": self.role
        }
    
    @staticmethod
    def fromJsonString(json_string):
        return User.fromJsonObject(json.loads(json_string))
        
    @staticmethod
    def fromJsonObject(obj):
        return User(
            obj["username"],
            obj["password"],
            obj["name"],
            obj["surname"],
            obj["role"],
        )
    