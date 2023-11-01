
class Refrence:
    def __init__(self, parent, model, source_key: str) -> None:
        self.parent = parent
        self.model = model
        self.source_key = source_key

    def get(self, db):
        # print(self.model.name)
        table = db[self.model.name]
        id = self.parent[self.source_key]
        res = table.SelectById(id)
        print("Table: ", table.toJsonString(2))
        print("Id: ", id)
        print("Select: ", res.toJsonString(2) if res is not None else "Null")
        return res

    
