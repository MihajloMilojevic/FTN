if __name__ == '__main__':
    fajl = open("../fajlovi/names.txt", "r")
    # Koristimo isti indeks da smestimo podatak o imenu i broju pojavljivanja zadatog imena
    # Npr. na indeksu 5 u listi names se nalazi ime "Jagoda" a na istom tom indeksu
    # u listi times se nalazi broj pojavljivanja imena "Jagoda"
    names = []
    times = []
    lines = fajl.readlines()
    fajl.close()

    for line in lines:
        line = line.replace("\n", "")
        # found koristimo kao indikator da li je ime već registrovano
        found = False
        for name_index in range(len(names)):
            # Ukoliko je ime već registrovano, uvećavamo broj ponavljanja za 1
            if names[name_index] == line:
                times[name_index] += 1
                found = True

        # Ako nismo pronašli ime među postojećim imenima, dodajemo
        if not found:
            names.append(line)
            times.append(1)

    # Sada u listama imamo broj pojavljivanja svakog od imena
    # implementiramo algoritam maksimuma
    # pored privremene maksimalne vrednosti beležimo i poziciju na kojoj smo taj element našli
    max_value = times[0]
    max_index = 0

    for index in range(len(names)):
        if times[index] > max_value:
            max_value = times[index]
            max_index = index

    print("Ime", names[max_index], "se ponavlja", max_value, "puta.")