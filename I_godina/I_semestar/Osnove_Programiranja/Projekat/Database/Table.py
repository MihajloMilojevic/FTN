import json
from Database.Models import models_by_name

class Table:
    def __init__(self, name, primary_key):
        self.name = name
        self.primary_key = primary_key
        self.rows = []
    def SelectById(self, id):
        for row in self.rows:
            if row[self.primary_key] == id:
                return row
        return None
    def Select(self, condition):
        for row in self.rows:
            if condition(row):
                return row
        return None
    def Insert(self, row):
        if self.SelectById(row[self.primary_key]) is not None:
            raise "Duplicate key"
        self.rows.append(row)

    def DeleteById(self, id):
        self.rows = [row for row in self.rows if row[self.primary_key] != id]

    def Delete(self, condition):
        self.rows = [row for row in self.rows if not condition(row)]

    def toJson(self):
        return json.dumps({
            "name": self.name,
            "primary_key": self.primary_key,
            "rows": [row.toJson() for row in self.rows]
        })
    @staticmethod
    def fromJson(str):
        v = json.loads(str)
        table = Table(
            v["name"],
            v["primary_key"]
        )
        table.rows = [models_by_name[table.name].fromJson(row) for row in v["rows"]]
        return table

