
def dadilja(pocetak: str, kraj: str):
    pp = pocetak.split(":")
    p_sat = int(pp[0])
    p_min = int(pp[1])
    p = p_sat * 60 + p_min
    kk = kraj.split(":")
    k_sat = int(kk[0])
    k_min = int(kk[1])
    k = k_sat * 60 + k_min
    devet = 21*60
    cena = (max(devet - p, 0) + min(k-devet, 0))/60.0 * 150 + max(k - devet, 0) / 60.0 * 100
    return f"zarada dadilje je {round(cena)} din"


def main():
    pocetak = input("Unesi vreme pocetka u formatu 'hh:mm' = ")
    kraj = input("Unesi vreme kraja u formatu 'hh:mm' = ")
    print(dadilja(pocetak, kraj))


if __name__ == "__main__":
    main()