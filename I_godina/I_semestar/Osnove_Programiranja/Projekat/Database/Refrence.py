from Database.Models import Korisnik, Karta, Sala, Film, Projekcija, Termin

class Refrence:
    def __init__(self, model, source_key: str) -> None:
        self.model = model
        self.source_key = source_key
    
