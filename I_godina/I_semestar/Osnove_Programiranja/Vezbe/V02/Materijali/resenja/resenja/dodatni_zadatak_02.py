# napomena: Za rešavanje ovog zadatka potrebno je ovladati idejama i tehnikama koje za sada, prevazilaze gradivo ovog predmeta
# rešavanje ovog zadatka nije i neće biti potrebno za ispunjavanje ispitnih i predispitnih obaveza na ovom predmetu

# unose se granice
lower = eval(input("Unesite donju granicu:"))
upper = eval(input("Unesite gornju granicu:"))

# proveravamo da li su granice u dobrom poretku
if lower < upper:

    number_of_tries = 0
    while True:
        # biramo broj za predlog
        # ideja je da predložimo broj na sredini intervala jer na taj način odbacujemo polovinu potencijalnih pogodaka
        guess = (lower + upper)//2

        print("Da li je zadati broj", guess, "?")
        # povećavamo broj pokušaja
        number_of_tries += 1

        answer = input("Vaš odgovor:")

        if answer == ">":
            lower = guess + 1
        elif answer == "<":
            upper = guess - 1
        elif answer == "=":
            # ako broj nije ni manji ni veći od zadatog, onda je jednak
            print("Broj je pogođen.")
            # prekidamo petlju, igra je gotova
            break

        else:
            print("Unesite '<', '>' ili '='.")


    print("Broj pokušaja:", number_of_tries)

else:
    print("Navedene granice nisu u dobrom poretku.")