from random import randint

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()[].,:;!#$%&@"

def main():
    duzina = int(input("Unesi duzinu lozinke: "))
    niz = []
    for _ in range(duzina):
        niz.append(chars[randint(0, len(chars)-1)])
    lozinka = "".join(niz)
    print(lozinka)
 
if __name__ == "__main__":
    main()