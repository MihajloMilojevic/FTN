def main():
    BRZINA = 340

    print("Program racuna udaljenost posmatraca od munje")
    vreme = int(input("Unesite vreme koje je proteklo od kada ste videli munju do trenutka kada ste je culi: "))
    if(vreme < 0):
        print("Vreme ne moze biti negativno")
        return
    if(vreme == 0):
        print("RIP lupio Vas grom :)")
        return

    udaljenost = BRZINA * vreme

    print(f"Grom je udario {udaljenost} metara od Vas")


if __name__ == "__main__":
    main()