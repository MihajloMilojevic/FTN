# Izračunava prosek tri ocene
# Ilustruje unos vise podataka odjednom

if __name__ == '__main__':

    print("Izračunava prosek tri ocene.")

    score1, score2, score3 = eval(input("Unesite tri ocene razdvojene zarezom: "))
    average = (score1 + score2 + score3) / 3

    print("Prosečna ocena je:", average)
