def main():
    CENA_PO_KG = 105
    CENA_DOSTAVE_PO_KG = 18
    CENA_FIKSNIH_TROSKOVA = 15

    print("Program racuna cenu dostave odredjene kolicine kafe")
    kg = int(input("Unesite broj kilograma za dostavu: "))
    if(kg <= 0):
        print("Morate poruciti bar malo kafe")
        return
    cena = CENA_PO_KG * kg + CENA_DOSTAVE_PO_KG * kg + CENA_FIKSNIH_TROSKOVA

    print(f"Cena vase porudbine za {round(kg, 2)}kg kafe je {round(cena, 2)}dinara")


if __name__ == "__main__":
    main()