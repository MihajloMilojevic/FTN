

def load(fname, delimiter):
    file = open(fname, "r")
    users = [line[:-1].split(delimiter) for line in file.readlines()]
    file.close()
    return users

def main():
    print("Program ucitava korisnike iz fajla")
    users = load("korisnici.txt", "|")
    print(users)



if __name__ == "__main__":
    main()