import json
from Database.Models import models_by_name

class Table:
    def __init__(self, model):
        self.model = model
        self.rows = []
    def SelectById(self, id):
        for row in self.rows:
            if row[self.model.primary_key] == id:
                return row
        return None
    def Select(self, condition):
        for row in self.rows:
            if condition(row):
                return row
        return None
    def Insert(self, row):
        if self.SelectById(row[self.model.primary_key]) is not None:
            raise "Duplicate key"
        self.rows.append(row)

    def DeleteById(self, id):
        self.rows = [row for row in self.rows if row[self.model.primary_key] != id]

    def Delete(self, condition):
        self.rows = [row for row in self.rows if not condition(row)]

    def toJsonString(self):
        return json.dumps(self.toJsonObject())
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
