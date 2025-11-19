from pymongo import MongoClient

client = MongoClient("mongodb://134.209.250.243:27017/")
db = client['sv57-2023']
collection = db['collection']

records = collection.find({})
print("Rezultati nakon praznog upita:")
print("----------------------------")
for record in records:
    print(record)

records = collection.find({"from":{"$in": ["Subotica","Novi Sad"]}})
print("Ljudi iz Novog Sada ili Subotice")
print("----------------------------")
for record in records:
    print(record)

records = collection.aggregate([
    {
        "$match": {
            "from":"Subotica"
        }
    },
    {
        "$count" :"ukupan broj"
    }
])
print("Ukupn broj ljudi iz Subotice")
print("----------------------------")
for record in records:
    print(record)
