if __name__ == '__main__':
    input_file = open("../fajlovi/neformatiraniTekst.txt", "r")
    output_file = open("../fajlovi/formatiranTekst.txt", "w")

    text = input_file.read()

    #izbacivanje suvišnih razmaka rešavamo zamenom dvostukog razmaka jednostrukim
    #postupak ponavljamo sve dok ne ponestane dvostrukih razmaka
    # while True:
    #     new_text = text.replace("  ", " ")
    #     if len(new_text) == len(text):
    #         break
    #     text = new_text

    # izbacivanje suvišnih razmaka vršimo tako što isečemo string po razmacima.
    # Na mestima gde ima više razmaka dobili bismo prazne stringove
    # npr. "abc  cd e".split(" ") -> ["abc", "", "cd", "e"]
    # kada spojimo ove stringove razmakom dobijamo "abc cd e"
    text = " ".join(text.split(" "))
    lines = text.split("\n")

    #naslov
    caption = lines[0]
    #sva slova naslova se smanjuju, a zatim se prvo slovo svake reči povećava
    caption = caption.lower().title()

    #centriramo naslov na 100 karaktera
    caption = caption.center(100)

    #dodajemo ispravljen naslov na konačan tekst
    output_file.write(caption+"\n")

    #pristupamo paragrafima od indeksa 1 pa naviše (jer je paragraf na indeksu 0 naslov)
    for paragraph in lines[1:]:
        found_end = False

        #start_index određuje poziciju prvog slova u paragrafu
        start_index = 0

        #ignorišemo razmak ako postoji na početku paragrafa
        if paragraph[start_index] == " ":
            start_index += 1

        fixed_paragraph = "     "
        fixed_paragraph += paragraph[start_index].upper()
        start_index += 1

        #ako je u pitanju slovo, znak , ili znak ; prepisujemo ga na izlaz
        #ako smo pronašli znak koji određuje kraj rečenice (. ili ! ili ?) to beležimo pomoću indikatora found_end
        #ukoliko smo kod prethodnog karaktera pronašli znak za kraj rečenice, treba ubaciti razmak i pretvoriti sledeće
        #slovo u veliko
        for character in paragraph[start_index:]:
            if found_end:
                if character != " ":
                    fixed_paragraph += " " + character.upper()
                    found_end = False
                continue

            if character in ".?!":
                found_end = True

            fixed_paragraph += character

        output_file.write(fixed_paragraph + "\n")

    input_file.close()
    output_file.close()

