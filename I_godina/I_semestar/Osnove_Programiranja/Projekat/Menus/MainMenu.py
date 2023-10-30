from Utils.ClearConsole import  clear


def glavni():

    print("0. Izlazak iz aplikacije")
    print("1. Prijava na sistem")
    print("2. Registracija")
    print("4. Koristi kao neregistrovani korisnik")
    print("\n========================================\n")

    odabir = input("Odaberi opciju: ")
    try:
        opcija_num = int(odabir)
        if 0 <= opcija_num <= 4:
            return opcija_num
        raise
    except:
        return -1

def main_menu():
    while(True):
        op = glavni()
        if op >= 0:                      # valid input
            break
        # invalid input
        clear()
        print("Nevažeća opcija\n\n")