
def najveci_el(niz: list[float]) -> float:
    max = niz[0]
    for el in niz:
        if el > max:
            max = el
    return max

def najmanji_el(niz: list[float]) -> float:
    min = niz[0]
    for el in niz:
        if el < min:
            min = el
    return min

def suma_el(niz: list[float]) -> float:
    s = 0
    for el in niz:
        s += el
    return s

def sr_vr_el(niz: list[float]) -> float:
    return suma_el(niz) / len(niz)

def karakteristike_niza(niz: list[float]) -> None:
    print(f"Najveci element niza je {round(najveci_el(niz), 2)}")
    print(f"Najmanji element niza je {round(najmanji_el(niz), 2)}")
    print(f"Suma elemenata niza je {round(suma_el(niz), 2)}")
    print(f"Srednja vrednost elemenata niza je {round(sr_vr_el(niz), 2)}")

def main():
    print("Program odredjuje karakteristike niza")
    n = int(input("Unesi broj elemenata niza: "))
    while(n < 1):
        print("Unesite validan broj elemenata: ")
        n = float(input("Unesi broj elemenata niza: "))
    niz = []
    for i in range(n):
        niz.append(float(input(f"niz[{i}] = ")))
    
    karakteristike_niza(niz)



if __name__ == "__main__":
    main()