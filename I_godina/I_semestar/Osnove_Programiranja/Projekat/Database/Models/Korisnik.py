import json


class Korisnik:

    primary_key = "korisnicko_ime"
    name = "Korisnik"

    def __init__(self, korisnicko_ime, lozinka, ime, prezime, uloga):
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.ime = ime
        self.prezime = prezime
        self.uloga = uloga

    def __getitem__(self, key):
        match key:
            case "korisnicko_ime":
                return self.korisnicko_ime
            case "lozinka":
                return self.lozinka
            case "ime":
                return self.ime
            case "prezime":
                return self.prezime
            case "uloga":
                return self.uloga
            case _:
                raise "Invalid key"
        
    def __setitem__(self, key, value):
        match key:
            case "korisnicko_ime":
                self.korisnicko_ime = value
            case "lozinka":
                self.lozinka = value
            case "ime":
                self.ime = value
            case "prezime":
                self.prezime = value
            case "uloga":
                self.uloga = value
            case _:
                raise "Invalid key"
            
    def toJsonString(self):
        return json.dumps(self.toJsonObject())
    
    def toJsonObject(self):
        return {
            "korisnicko_ime": self.korisnicko_ime,
            "lozinka": self.lozinka,
            "ime": self.ime,
            "prezime": self.prezime,
            "uloga": self.uloga
        }
    
    @staticmethod
    def fromJsonString(str):
        return Korisnik.fromJsonObject(json.loads(str))
        
    @staticmethod
    def fromJsonObject(obj):
        return Korisnik(
            obj["korisnicko_ime"],
            obj["lozinka"],
            obj["ime"],
            obj["prezime"],
            obj["uloga"],
        )