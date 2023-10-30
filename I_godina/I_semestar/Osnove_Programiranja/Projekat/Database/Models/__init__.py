from Database.Models.Enums import Uloge, Zanrovi, Dani
from Database.Models.Film import Film
from Database.Models.Karta import Karta
from Database.Models.Korisnik import Korisnik
from Database.Models.Projekcija import Projekcija
from Database.Models.Sala import Sala
from Database.Models.Termin import Termin

models_by_name = {
    "Uloge": Uloge,
    "Zanrovi": Zanrovi,
    "Dani": Dani,
    "Film": Film,
    "Karta": Karta,
    "Korisnik": Korisnik,
    "Projekcija": Projekcija,
    "Sala": Sala,
    "Termin": Termin
}