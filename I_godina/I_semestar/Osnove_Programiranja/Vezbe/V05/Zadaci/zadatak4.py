

def load(fname, delimiter):
    file = open(fname, "r")
    users = [line[:-1].split(delimiter) for line in file.readlines()]
    file.close()
    return users

def save(fname, delimiter, username, password):
    file = open(fname, "a")
    file.write(f"{username}{delimiter}{password}\n")
    file.close()
    return load(fname, delimiter)

def main():
    print("Program registruje novog korisnika")
    username = input("Unesi korisničko ime: ")
    password = input("Unesi lozinku: ")

    users = save("korisnici.txt", "|", username, password)
    print(users)


if __name__ == "__main__":
    main()