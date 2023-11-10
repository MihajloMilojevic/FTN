from Database import Database
from datetime import datetime
import Database.Models as Models

def populateDatabase():
    db = Database()
    # Korisnici - menadzeri
    db.korisnici.Insert(Models.Korisnik("mihajlo", "Mihajlo123", "Mihajlo", "Milojevic", Models.Uloge.menadzer))

    # Korisnici - prodavci
    db.korisnici.Insert(Models.Korisnik("pepi", "Petar2004", "Petar", "Popovic", Models.Uloge.prodavac))
    db.korisnici.Insert(Models.Korisnik("prle", "kos2023", "Luka", "Prilincevic", Models.Uloge.prodavac))
    db.korisnici.Insert(Models.Korisnik("ljubogdan", "Boki951", "Bogdan", "Ljubinkovic", Models.Uloge.prodavac))

    # Korisnici - kupci
    db.korisnici.Insert(Models.Korisnik("lanmi", "hell0w0rld", "Milan", "Sazdov", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("laki", "hell0w0rld", "Lazar", "Sazdov", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("teo", "pmf2ftn", "Teodor", "Perucinic", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("madmax", "biznismen99", "Maksim", "Vasic", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("dance", "dance5", "Matija", "Dancetovic", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("sneza", "Nastja2021", "Snezana", "Milojcevic", Models.Uloge.kupac))

    # Sale
    db.sale.Insert(Models.Sala("S1", "Sala 1", 13, 10))
    db.sale.Insert(Models.Sala("S2", "Sala2", 13, 10))
    db.sale.Insert(Models.Sala("SV", "Velika sala", 20, 15))
    db.sale.Insert(Models.Sala("SR", "Rodjendanska", 6, 9))

    # Filmovi
    db.filmovi.Insert(Models.Film(
        "QNFTNGQX", # sifra
        "Iskupljenje u Shawshanku",  # naziv
        [Models.Zanrovi.drama],  # zanrovi
        142, #trajanje
        "Frank Darabont", #reziser
        ["Morgan Freeman", "Bob Gunton", "Tim Robbins"], # glavne uloge
        "SAD", # zemlja
        1994,  # godina
        "The Shawshank Redemption je prica o mladom coveku Andiju (Tim Robbins) bankaru kojem je smesteno ubistvo njegove zene i njenog ljubavnika. U zatvoru upoznaje Reda (Morgan Freeman) koji mu postaje prijatelj sa kojim provodi mnogo godina u zatvoru. Film prati njihove zivote iz oba ugla, iako naraciju u filmu radi Red, o zivotu Endija od trenutka kada je dosao u zatvor." # opis
        ))
    db.filmovi.Insert(Models.Film( 
        "LLC3M1AK",                         # sifra
        "Sindlerova lista" ,                         # naziv
        [Models.Zanrovi.biografski, Models.Zanrovi.drama, Models.Zanrovi.istorijski],           # zanrovi
        195,                           # trajanje
        "Steven Spielberg",                         # reziser
        ["Liam Neeson", "Ralph Fiennes", "Ben Kingsley"],                         # glavne uloge
        "SAD",                         # zemlja
        1993,                           # godina
        "Oskar sindler, biznismen, clan nacisticke stranke i nepopravljivi zenskaros, dolazi u Poljsku, okupiranu od strane nacista, u potrazi za ekonomskim prosperitetom. Zaposljava Jevreje u svojoj fabrici, kako bi proizvodili za Treci rajh. Posto je bio svedok stradanja Jevreja u krakovskom getu, ubrzo je uvidio zlo nacizma. Njegovi radnici dolaze pod teror nacistickog sadiste Amona Geta, posto su odvedeni u logor. Uz pomoc svog racunovodje Izaka Sterna, sindler pravi listu najpotrebnijih Jevreja. On podmicuje njemacke vlasti i samog Geta i uspeva da oslobodi vise od 1.000 Jevreja. Ovaj cuveni Spilbergov film je vizuelno veoma upecatljiv jer je radjen u crno-bijeloj tehnici. sokantan, tezak, emotivan i poucan, umetnicki i veoma realno odradjen film."                          # opis
        ))
    # db.filmovi.Insert(Models.Film(
    #     "",                         # sifra
    #     "",                         # naziv
    #     [Models.Zanrovi],           # zanrovi
    #     ,                           # trajanje
    #     "",                         # reziser
    #     [],                         # glavne uloge
    #     "",                         # zemlja
    #     ,                           # godina
    #     ""                          # opis
    #     ))
    # db.filmovi.Insert(Models.Film(
    #     "",                         # sifra
    #     "",                         # naziv
    #     [Models.Zanrovi],           # zanrovi
    #     ,                           # trajanje
    #     "",                         # reziser
    #     [],                         # glavne uloge
    #     "",                         # zemlja
    #     ,                           # godina
    #     ""                          # opis
    #     ))
    # db.filmovi.Insert(Models.Film(
    #     "",                         # sifra
    #     "",                         # naziv
    #     [Models.Zanrovi],           # zanrovi
    #     ,                           # trajanje
    #     "",                         # reziser
    #     [],                         # glavne uloge
    #     "",                         # zemlja
    #     ,                           # godina
    #     ""                          # opis
    #     ))
    # db.filmovi.Insert(Models.Film(
    #     "",                         # sifra
    #     "",                         # naziv
    #     [Models.Zanrovi],           # zanrovi
    #     ,                           # trajanje
    #     "",                         # reziser
    #     [],                         # glavne uloge
    #     "",                         # zemlja
    #     ,                           # godina
    #     ""                          # opis
    #     ))
    # db.filmovi.Insert(Models.Film(
    #     "",                         # sifra
    #     "",                         # naziv
    #     [Models.Zanrovi],           # zanrovi
    #     ,                           # trajanje
    #     "",                         # reziser
    #     [],                         # glavne uloge
    #     "",                         # zemlja
    #     ,                           # godina
    #     ""                          # opis
    #     ))
    
    # Projekcije
    db.projekcije.Insert(Models.Projekcija(
        "5378",                 # sifra
        "S1",                   # sifra sale
        "LLC3M1AK",             # sifra filma
        datetime.strptime("17:00:00", "%H:%M:%S"),       # vreme pocetka
        datetime.strptime("20:15:00", "%H:%M:%S"),       # vreme kraja
        [Models.Dani.ponedeljak, Models.Dani.utorak, Models.Dani.sreda],         # dani
        300.00
        ))
    db.projekcije.Insert(Models.Projekcija(
        "7620",                 # sifra
        "S1",                   # sifra sale
        "LLC3M1AK",             # sifra filma
        datetime.strptime("20:30:00", "%H:%M:%S"),       # vreme pocetka
        datetime.strptime("23:45:00", "%H:%M:%S"),       # vreme kraja
        [Models.Dani.ponedeljak, Models.Dani.utorak, Models.Dani.sreda],         # dani
        300.00
        ))
    
    # Termini
    db.termini.Insert(Models.Termin("5378AA", "5378", datetime.strptime("6.11.2023", "%d.%m.%Y")))
    db.termini.Insert(Models.Termin("5378BA", "5378", datetime.strptime("7.11.2023", "%d.%m.%Y")))
    db.termini.Insert(Models.Termin("5378CA", "5378", datetime.strptime("8.11.2023", "%d.%m.%Y")))

    # Karte
    db.karte.Insert(Models.Karta("EW2BTB0D6X", "5378AA", "1-A", True, None, "mihajlo", None, 0))
    db.karte.Insert(Models.Karta("ZVCM5CI42Z", "5378AA", "1-B", True, None, "mihajlo", None, 0))
    db.karte.Insert(Models.Karta("07BYLX0D5M", "5378AA", "2-C", False, datetime.strptime("1.11.2023", "%d.%m.%Y"), None, "Djordje Milojevic", 300))

    # SAVE
    db.save()
    # db.saveJson()

    print("Database population completed")