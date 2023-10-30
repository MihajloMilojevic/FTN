# napomena: Za rešavanje ovog zadatka potrebno je ovladati idejama i tehnikama koje za sada, prevazilaze gradivo ovog predmeta
# rešavanje ovog zadatka nije i neće biti potrebno za ispunjavanje ispitnih i predispitnih obaveza na ovom predmetu
import random

# unose se granice
lower = eval(input("Unesite donju granicu:"))
higher = eval(input("Unesite gornju granicu:"))

# proveravamo da li su granice u dobrom poretku
if lower < higher:
    # biramo broj za pogađanje
    choosen_number = random.randint(lower, higher)

    # na početku inicijalizujemo pogodak na None
    guess = None
    number_of_tries = 0
    while True:

        guess = input("Vaš predlog:")

        if guess != "izlaz":

            # povećavamo broj pokušaja jedino ako korisnik nije odabrao da izađe
            number_of_tries += 1

            # pošto unos nije 'izlaz', pretvaramo ga u broj
            guess = eval(guess)

            # proveravamo da li je predlog u zadatom opsegu
            if lower <= guess <= higher:
                if guess < choosen_number:
                    print("Vaš pogodak je manji od zadatog broja")
                elif guess > choosen_number:
                    print("Vaš pogodak je veći od zadatog broja")
                else:
                    # ako broj nije ni manji ni veći od zadatog, onda je jednak
                    print("Bravo, pogodili ste zadati broj")
                    # prekidamo petlju, igra je gotova
                    break

            else:
                print("Unos nije u dozvoljenom opsegu, pokušajte ponovo.")
        else:
            # korisnik je uneo "izlaz"
            # ne povećavamo broj pogodaka
            # prekidamo petlju
            break

    print("Broj pokušaja:", number_of_tries)

else:
    print("Navedene granice nisu u dobrom poretku.")