if __name__ == '__main__':

    #otvaramo dva fajla za čitanje i jedan za pisanje
    users = open("../fajlovi/users.txt", "r")
    accounts = open("../fajlovi/accounts.txt", "r")

    output_file = open("../fajlovi/statistics.txt", "w")

    #učitavamo prvu liniju iz svakog fajla
    user = users.readline()
    account = accounts.readline()

    #Ako učitamo praznu liniju, došli smo do kraja fajla
    #mogli smo pisati i while user:
    while user != "":
        username = user.split("|")[0]
        sum = 0
        counter = 0
        #elementi liste prices su pojedinačne cene ali u obliku stringa
        prices = account.split("|")
        for price in prices:
            #konvertujemo u broj
            sum += eval(price)
            counter += 1

        average = sum/counter

        #jednostavnije rešenje, bez zaokruživanja
        #string_to_write = username + "|" + str(sum) + "|" + str(average) + "\n"

        #rešenje sa zaokruživanjem na 2 decimale
        string_to_write = "{}|{:.2f}|{:.2f}\n".format(username, sum, average)
        output_file.write(string_to_write)

        #prelazimo na sledećeg korisnika ako postoji
        user = users.readline()
        # prelazimo na sledeći račun ako postoji
        account = accounts.readline()

    #zatvaranje fajlova
    users.close()
    accounts.close()
    output_file.close()