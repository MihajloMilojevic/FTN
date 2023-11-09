if __name__ == '__main__':

    username = input("Unesite ime:")
    password = input("Unesite lozinku:")

    file = open("../fajlovi/users.txt", "a")
    file.write(username+"|"+password+"\n")
    file.close()