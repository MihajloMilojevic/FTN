def main():
    string = input("Unesi string: ")
    cifre = "".join([c for c in string if c.isdigit()])
    mala = "".join([c for c in string if c.islower()])

    print(f"Samo cifre: {cifre}")
    print(f"Samo mala slova: {mala}")
 
if __name__ == "__main__":
    main()