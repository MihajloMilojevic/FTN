from Database import Database
import Database.Models as Models

def populateDatabase():
    db = Database()
    # Korisnici - menadzeri
    db.korisnici.Insert(Models.Korisnik("mihajlo", "Mihajlo123", "Mihajlo", "Milojević", Models.Uloge.menadzer))

    # Korisnici - prodavci
    db.korisnici.Insert(Models.Korisnik("pepi", "Petar2004", "Petar", "Popović", Models.Uloge.prodavac))
    db.korisnici.Insert(Models.Korisnik("prle", "kos2023", "Luka", "Prilinčević", Models.Uloge.prodavac))
    db.korisnici.Insert(Models.Korisnik("ljubogdan", "Boki951", "Bogdan", "Ljubinković", Models.Uloge.prodavac))

    # Korisnici - kupci
    db.korisnici.Insert(Models.Korisnik("lanmi", "hell0w0rld", "Milan", "Sazdov", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("laki", "hell0w0rld", "Lazar", "Sazdov", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("teo", "pmf2ftn", "Teodor", "Peručinić", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("madmax", "biznismen99", "Maksim", "Vasić", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("dance", "dance5", "Matija", "Dančetović", Models.Uloge.kupac))
    db.korisnici.Insert(Models.Korisnik("sneza", "Nastja2021", "Snežana", "Milojčević", Models.Uloge.kupac))

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
        "The Shawshank Redemption je priča o mladom čoveku Andiju (Tim Robbins) bankaru kojem je smešteno ubistvo njegove žene i njenog ljubavnika. U zatvoru upoznaje Reda (Morgan Freeman) koji mu postaje prijatelj sa kojim provodi mnogo godina u zatvoru. Film prati njihove živote iz oba ugla, iako naraciju u filmu radi Red, o životu Endija od trenutka kada je došao u zatvor." # opis
        ))
    db.filmovi.Insert(Models.Film( 
        "LLC3M1AK",                         # sifra
        "Šindlerova lista",                         # naziv
        [Models.Zanrovi.biografski, Models.Zanrovi.drama, Models.Zanrovi.istorijski],           # zanrovi
        195,                           # trajanje
        "Steven Spielberg",                         # reziser
        ["Liam Neeson", "Ralph Fiennes", "Ben Kingsley"],                         # glavne uloge
        "SAD",                         # zemlja
        1993,                           # godina
        "Oskar Šindler, biznismen, član nacističke stranke i nepopravljivi ženskaroš, dolazi u Poljsku, okupiranu od strane nacista, u potrazi za ekonomskim prosperitetom. Zapošljava Jevreje u svojoj fabrici, kako bi proizvodili za Treći rajh. Pošto je bio svedok stradanja Jevreja u krakovskom getu, ubrzo je uvidio zlo nacizma. Njegovi radnici dolaze pod teror nacističkog sadiste Amona Geta, pošto su odvedeni u logor. Uz pomoć svog računovođe Izaka Sterna, Šindler pravi listu najpotrebnijih Jevreja. On podmićuje njemačke vlasti i samog Geta i uspeva da oslobodi više od 1.000 Jevreja. Ovaj čuveni Spilbergov film je vizuelno veoma upečatljiv jer je rađen u crno-bijeloj tehnici. Šokantan, težak, emotivan i poučan, umetnički i veoma realno odrađen film."                          # opis
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
