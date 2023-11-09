if __name__ == '__main__':
    input_file = open("../fajlovi/neformatiraniTekst.txt", "r")
    output_file = open("../fajlovi/formatiranTekst.txt", "w")

    text = input_file.read()

    #izbacivanje suvišnih razmaka rešavamo zamenom dvostukog razmaka jednostrukim
    #postupak ponavljamo sve dok ne ponestane dvostrukih razmaka
    while True:
        new_text = text.replace("  ", " ")
        if len(new_text) == len(text):
            break
        text = new_text

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

        sentences = paragraph.split(".")
        for i in range(len(sentences)):
            sentences[i] = sentences[i].capitalize()

        paragraph = ". ".join(sentences)
        output_file.write("     " + paragraph + "\n")

    input_file.close()
    output_file.close()

