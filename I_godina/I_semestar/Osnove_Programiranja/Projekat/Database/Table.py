import json
from Database.Models import models_by_name, Korisnik, Karta, Sala, Film, Projekcija, Termin
from Utils.GetPath import get_relative_path

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
    
    def SelectAll(self) -> list[Korisnik|Karta|Sala|Film|Projekcija|Termin]:
        return [row for row in self.rows]

    def Select(self, condition) -> list[Korisnik|Karta|Sala|Film|Projekcija|Termin]:
        return [row for row in self.rows if condition(row)]
    
    def Insert(self, row: Korisnik|Karta|Sala|Film|Projekcija|Termin) -> bool:
        if self.SelectById(row[self.model.primary_key]) is not None:
            return False
        self.rows.append(row)
        return True

    def DeleteById(self, id: str) -> int:
        old = len(self.rows)
        self.rows = [row for row in self.rows if row[self.model.primary_key] != id]
        new = len(self.rows)
        return old - new

    def Delete(self, condition) -> int:
        old = len(self.rows)
        self.rows = [row for row in self.rows if not condition(row)]
        new = len(self.rows)
        return old - new

    def DeleteAll(self) -> int:
        old = len(self.rows)
        self.rows = []
        return old
    
    # Upisuje tabelu u fajl
    def save(self) -> None:
        try:
            with open(get_relative_path(["Data", f"{self.model.name}.txt"]), "w", encoding="utf-8") as file:
                for row in self.rows:
                    file.write(f"{self.model.serialize(row)}\n")
        except Exception as e:
            print(f"Unable to write to the file {self.model.name}\nError: {e}")

    # Ucitava vrednosti iz fajla
    def load(self):
        try:
            with open(get_relative_path(["Data", f"{self.model.name}.txt"]), "r", encoding="utf-8") as file:
                for row in file.readlines():
                    self.Insert(self.model.deserialize(row[:-1]))
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
