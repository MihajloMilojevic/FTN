from Zadatak import Zadatak
import os


def clear():

    if os.name == "nt":         # Windows
        _ = os.system("cls")
    else:                       # Linux or Mac
        _ = os.system("clear")

def a(zadatak: Zadatak):
    clear()
    print("Podzatak a) - svi vrhovi za zadatu drzavu\n")
    drzava = input("Unesite drzavu za pretragu: ")
    rez = zadatak.podzatak_a(drzava)
    if(len(rez) == 0):
        print(f"Nema vrhova za drzavu {drzava}")
    else:
        print(f"\nVrhovi koji se nalaze u drzavi '{drzava}':")
        for vrh in rez:
            print(vrh)
    input("Pritisnte Enter za povratak")
    clear()

def b(zadatak: Zadatak):
    clear()
    print("\n\nPodzatak b) - svi vrhovi na granici 2 drzave cija je visina izmedju 7700m i 8100m\n")
    rez = zadatak.podzatak_b()
    if(len(rez) == 0):
        print(f"Nema vrhova na granici 2 drzave cija je visina izmedju 7700m i 8100m")
    else:
        print(f"\nVrhovi koji se nalaze na granici 2 drzave cija je visina izmedju 7700m i 8100m:")
        for vrh in rez:
            print(vrh)
    input("Pritisnte Enter za povratak")
    clear()

def main():
    zadatak = Zadatak()
    
    funcs = {
        "a": a,
        "b": b
    }
    
    while True:
        clear()
        print("X - Izlazak")
        print("A - Pretraga vrhova po drzavi")
        print("B - Prikaz vrhova na granici 2 drzave cija je visina izmedju 7700m i 8100m")

        opcija = input("\nOdaberite opciju: ")

        if opcija.lower() == "x":
            break
        if(opcija.lower() not in funcs):
            print("Neispravan unos")
            continue

        funcs[opcija.lower()](zadatak)
    
    clear()

if __name__ == "__main__":
    main()