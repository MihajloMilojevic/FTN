def main():
    with open("korisnici.txt", "r") as file:
        for line in file.readlines():
            list = line.split("|")
            print(f"Unesi korisničko ime: {list[0]}")
            print(f"Unesi lozinku: {list[1]}")
        
if __name__ == "__main__":
    main()