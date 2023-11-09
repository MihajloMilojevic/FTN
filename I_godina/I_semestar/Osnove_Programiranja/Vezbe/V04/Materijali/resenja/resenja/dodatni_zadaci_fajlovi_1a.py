if __name__ == '__main__':
    fajl = open("../fajlovi/names.txt", "r")
    name = input("Unesite ime: ")
    lines = fajl.readlines()
    counter = 0
    for line in lines:
        line = line.replace("\n", "")
        if name == line:
            counter += 1

    print("Ime", name, "se ponavlja", counter, "puta.")
    fajl.close()