from pymongo import MongoClient

# U connection_string treba da kopirate adresu za vas Atlas cluster
connection_string = "mongodb+srv://maximaksimovic7:<password>@cluster0.usmjvhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "test"
collection_name = "programeri"

# Povezivanje sa vasim Atlas klasterom
client = MongoClient(connection_string)
# Odabir jedne od baze podataka unutar klastera
db = client[database_name]
# Odabir jedne od kolekcija unutar baze
collection = db[collection_name]

records = collection.find({"skills": {"$all": ["Python", "MongoDB"]}})
for record in records:
    print(record)

records = collection.aggregate([
  { "$unwind": "$skills" },
  { "$group": { "_id": "$skills", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } }
])
for record in records:
    print(record)
