import json
from Database.Models import models_by_name, Korisnik, Karta, Sala, Film, Projekcija, Termin
from Utils.GetPath import GetRelativePath

# Tip modela: Korisnik|Karta|Sala|Film|Projekcija|Termin 


class Table:

    def __init__(self, model: Korisnik|Karta|Sala|Film|Projekcija|Termin ):
        self.model = model
        self.rows = []

    def SelectById(self, id: str) -> Korisnik|Karta|Sala|Film|Projekcija|Termin|None:
        for row in self.rows:
            if row[self.model.primary_key] == id:
                return row
        return None
    
    def Select(self, condition) -> Korisnik|Karta|Sala|Film|Projekcija|Termin|None:
        return [row for row in self.rows if condition(row)]
    
    def Insert(self, row: Korisnik|Karta|Sala|Film|Projekcija|Termin) -> None:
        if self.SelectById(row[self.model.primary_key]) is not None:
            raise "Duplicate key"
        self.rows.append(row)

    def DeleteById(self, id: str) -> None:
        self.rows = [row for row in self.rows if row[self.model.primary_key] != id]

    def Delete(self, condition) -> None:
        self.rows = [row for row in self.rows if not condition(row)]
    
    # Upisuje tabelu u fajl
    def save(self) -> None:
        try:
            file = open(GetRelativePath(["Data", f"{self.model.name}.txt"]), "w")
            for row in self.rows:
                file.write(f"{self.model.serialize(row)}\n")
            file.close()
        except Exception as e:
            print(f"Unable to write to the file {self.model.name}\nError: {e}")

    # Ucitava vrednosti iz fajla
    def load(self):
        try:
            file = open(GetRelativePath(["Data", f"{self.model.name}.txt"]), "r")
            for row in file.readlines():
                self.Insert(self.model.deserialize(row[:-1]))
            file.close()
        except Exception as e:
            print(f"Unable to read from the file {self.model.name}\nError: {e}")

    def populatedObject(self, db):
        return {
            "model": self.model.name,
            "rows": [row.populatedObject(db) for row in self.rows]
        }

    def toJsonString(self, indent = 0):
        return json.dumps(self.toJsonObject(), indent=indent)
    
    def toJsonObject(self):
        return {
            "model": self.model.name,
            "rows": [row.toJsonObject() for row in self.rows]
        }
    
    @staticmethod
    def fromJsonString(str):
        return Table.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        table = Table(
           models_by_name[obj["model"]],
        )
        table.rows = [table.model.fromJsonObject(row) for row in obj["rows"]]
        return table
