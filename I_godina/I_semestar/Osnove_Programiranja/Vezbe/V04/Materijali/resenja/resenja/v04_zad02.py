if __name__ == '__main__':
    phrase = input("Unesite frazu:")
    words = phrase.split()

    acronym = ""
    for word in words:
        acronym += word[0]

    acronym = acronym.upper()

    print("Akronim za unetu frazu je", acronym)
