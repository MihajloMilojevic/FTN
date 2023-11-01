from Menus.MainMenu import main_menu
import Database.Models as Models
from datetime import datetime
import json
from Database import Database
from Database.initialDB import populateDatabase

def main():
    main_menu()

if __name__ == '__main__':
    db = Database()
    db.load()
    # print(json.dumps(db.populatedObject(), indent=2))
    # print(db.populatedObject())
    obj = db.populatedObject()
    print(obj["projekcije"]["rows"][0]["sala"])
    print(obj)
    # print(db.projekcije.SelectById("5378").sala.get(db))


