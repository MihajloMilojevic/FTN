from typing import Any
from Database.Table import Table
import Database.Models as Models
import json

class Database:

    def __init__(self):
        self.users = Table(Models.User)
        self.halls = Table(Models.Hall)
        self.films = Table(Models.Film)
        self.projections = Table(Models.Projection)
        self.showtimes = Table(Models.Showtime)
        self.tickets = Table(Models.Ticket)

    def __getitem__(self, key: str) -> Table:
        match key:
            case Models.User.name:
                return self.users
            case Models.Ticket.name:
                return self.tickets
            case Models.Hall.name:
                return self.halls
            case Models.Film.name:
                return self.films
            case Models.Projection.name:
                return self.projections
            case Models.Showtime.name:
                return self.showtimes
            case _:
                raise "Invalid key"

    def load(self):
        self.users.load()
        self.halls.load()
        self.films.load()
        self.projections.load()
        self.showtimes.load()
        self.tickets.load()

    def save(self):
        self.users.save()
        self.halls.save()
        self.films.save()
        self.projections.save()
        self.showtimes.save()
        self.tickets.save()

    def populatedObject(self):
        return {
            "users": self.users.populatedObject(self),
            "halls": self.halls.populatedObject(self),
            "films": self.films.populatedObject(self),
            "projections": self.projections.populatedObject(self),
            "showtimes": self.showtimes.populatedObject(self),
            "tickets": self.tickets.populatedObject(self)
        }

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "users": self.users.toJsonObject(),
            "halls": self.halls.toJsonObject(),
            "films": self.films.toJsonObject(),
            "projections": self.projections.toJsonObject(),
            "showtimes": self.showtimes.toJsonObject(),
            "tickets": self.tickets.toJsonObject()
        }
    
    @staticmethod
    def fromJsonString(str):
        return Database.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        db = Database()
        db.users = Table.fromJsonObject(obj["users"])
        db.halls = Table.fromJsonObject(obj["halls"])
        db.films = Table.fromJsonObject(obj["films"])
        db.projections = Table.fromJsonObject(obj["projections"])
        db.showtimes = Table.fromJsonObject(obj["showtimes"])
        db.tickets = Table.fromJsonObject(obj["tickets"])
        return db

    def setupJson(self):
        with open("data.json", "r", encoding="utf-8") as file:
            str = file.read()
            db = Database.fromJsonString(str)
            self.users = db.users
            self.halls = db.halls
            self.films = db.films
            self.projections = db.projections
            self.showtimes = db.showtimes
            self.tickets = db.tickets

    def saveJson(self):
        with open("data.json", "w", encoding="utf-8") as file:
            file.write(self.toJsonString())

