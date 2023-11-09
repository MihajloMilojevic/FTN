def main():
    username = input("Unesi korisničko ime: ")
    password = input("Unesi lozinku: ")

    with open("korisnici.txt", "a") as file:
        file.write(f"{username}|{password}\n")
        print("Uspešno registrovan")

if __name__ == "__main__":
    main()