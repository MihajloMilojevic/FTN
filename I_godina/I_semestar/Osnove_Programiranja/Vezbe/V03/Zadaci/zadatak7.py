def main():
    MASA_VODNIKA = 1.0079
    MASA_UGLJENIKA = 12.011
    print("Program molekularnu masu uglovodnoika")
    brojUgljenika = int(input("Unesite broj atoma uglenjika: "))
    if(brojUgljenika < 0):
        print("Atom ne moze imati negativan broj atoma")
        return
    brojVodonika = int(input("Unesite broj atoma vodonika: "))
    if (brojVodonika < 0):
        print("Atom ne moze imati negativan broj atoma")
        return
    masa = brojVodonika * MASA_VODNIKA + brojUgljenika * MASA_UGLJENIKA
    formula = ""
    if (brojUgljenika > 0):
        formula = formula + f"C{brojUgljenika}"
    if (brojVodonika > 0):
        formula = formula + f"H{brojVodonika}"

    print(f"Molekularna masa {formula} je {masa}")


if __name__ == "__main__":
    main()