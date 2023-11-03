if __name__ == '__main__':

    file = open("../fajlovi/users.txt", "r")

    content = file.readlines()

    for line in content:
        user_data = line.split("|")
        username = user_data[0]
        password = user_data[1]
        print("Korisničko ime:", username)
        print("Lozinka:", password)