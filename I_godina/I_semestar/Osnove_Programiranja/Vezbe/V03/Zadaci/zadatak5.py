import math

def main():
    print("Program racuna povrsinu i zapreminu svere")
    poluprecnik = int(input("Unesite poluprecnik sfere: "))
    if(poluprecnik <= 0):
        print("Poluprecnik mora biti pozitivan realan broj!!!")
        return
    povrsina = 4 * math.pi * (poluprecnik ** 2)
    zapremina = 4 / 3 * math.pi * (poluprecnik ** 3)

    print(f"Sfera sa poluprecnikom R = {poluprecnik} ima povrsinu P = {povrsina} i zapreminu V = {zapremina}")


if __name__ == "__main__":
    main()