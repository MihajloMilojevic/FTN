import json
from pymongo import MongoClient

client = MongoClient("mongodb://134.209.250.243:27017/")
db = client['sv57-2023']
collection = db['collection']

with open("sample1.json", "r") as file:
    data = json.load(file)

collection.insert_many(data)