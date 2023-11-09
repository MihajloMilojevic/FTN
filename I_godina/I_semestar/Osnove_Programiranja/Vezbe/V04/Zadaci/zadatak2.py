def main():
    fraza = input("Unesi frazu: ")
    rez = "".join([rec.upper()[0] for rec in fraza.split()])
    print(f"Akronim je: {rez}")

if __name__ == "__main__":
    main()