from Menus.MainMenu import main_menu
from Database.Models import Sala, Korisnik, Uloge
from datetime import datetime
import json
from Database import Database
from Database.initialDB import populateDatabase

def main():
    main_menu()

if __name__ == '__main__':
    populateDatabase()
    # main()
    # k = Sala("aaa", "Sala 1", 2, 3)
    # str = k.toJson()
    # s = Sala.fromJson(str)
    # print(s.toJson())
    # d = datetime.now()
    # djson = datetime.strptime(json.loads(json.dumps(datetime.strftime(d, "%x"))),"%x")
    # print(djson)
    # print(json.dumps({"list": ["a", "b", 1, 3, [9, 8, 7]]}))
    # db = Database()
    # db.load()
    # k = Korisnik("mihajlo", "Mihajlo123", "Mihajlo", "Milojevic", Uloge.menadzer)
    # db.korisnici.Insert(k)
    # print(json.dumps(db.toJsonObject(), indent=2))
    # def con(kor):
    #     return kor.uloga == Uloge.menadzer
    # print(db.korisnici.Select(con).ime)
    # db.saveJson()
    # db.save()
    # print(db.toJsonString())

