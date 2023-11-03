#Na osnovu 2 dobijena stringa kreirati novi tako da bude sastavljen od prvog,
# srednjeg i poslednjeg karaktera jednog i drugog stringa naizmenično.
# Pretpostaviti da stringovi imaju neparan broj karaktera i da su dužine veće od 2.
# Primer:
# string1: Lampica
# string2: Kokos
# izlaz: LKpkas

if __name__ == '__main__':
    str1 = "Lampica"
    str2 = "Kokos"

    str1_middle_index = len(str1)//2
    str2_middle_index = len(str2)//2

    output = str1[0] + str2[0] + str1[str1_middle_index] + str2[str2_middle_index]
    output += str1[-1] + str2[-1]
    print(output)


