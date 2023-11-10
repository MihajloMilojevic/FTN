import math

def izbaci_duplikate(niz: list[str]) -> bool:
    return " ".join(list(set(niz)))

def main():
    print("Program izbacuje reci duplikate")

    print(izbaci_duplikate(input("Unesi reci razdvojene razmakom: ").split(" ")))


if __name__ == "__main__":
    main()