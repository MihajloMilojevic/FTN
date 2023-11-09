fajl = open("quiz.txt", "r", encoding="utf-8")
item = fajl.readline()
unos = None
print("Dobrodošli u kviz. Za izlazak unesite 'x'")
bodovi = 0
while unos not in ['x','X']:
    if item == '':
        print("Nema više pitanja.")
        break
    delovi = item.strip().split("|")
    pitanje = delovi[0]
    print(pitanje)
    tacan = -1
    for i in range(len(delovi[1:])):
        redni_broj = i+1
        odgovor = delovi[i+1]
        if odgovor[0] == '!':
            print(str(redni_broj)+ "." + odgovor[1:])
            tacan = i+1
        else:
            print(str(redni_broj) + "." + odgovor)
    if tacan == -1:
        print("Greška! Nijedan odgovor nije označen kao tačan. Aplikacija se prekida")
        break

    korisnicki_odgovor = eval(input("Vaš odgovor je: "))
    if korisnicki_odgovor == tacan:
        print("Odgovor je tačan")
        bodovi += 1
    else:
        print("Odgovor nije tačan. Tačan odgovor je pod", tacan, ".")
    item = fajl.readline()

    unos = input("Da li želite da nastavite sa kvizom?")

print("KRAJ. Osvojili ste", bodovi, "bodova.")
fajl.close()