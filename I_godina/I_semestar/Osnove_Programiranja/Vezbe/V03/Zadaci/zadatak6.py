import math

def main():
    print("Program racuna cenu pice po kvadratnom centimetru")
    poluprecnik = int(input("Unesite poluprecnik pice u cm: "))
    if(poluprecnik <= 0):
        print("Poluprecnik mora biti pozitivan realan broj!!!")
        return
    cena = int(input("Unesite cenu pice: "))
    if(cena <= 0):
        print("Cena mora biti veca od 0!!!")
        return
    povrsina = math.pi * (poluprecnik ** 2)
    cenaPoKvadratu = cena / povrsina
    print(f"Za picu poluprecnika {poluprecnik}cm koja kosta {cena} dinara, cena jednog kvadratnog centimetra pice je {round(cenaPoKvadratu, 2)} dinara")


if __name__ == "__main__":
    main()