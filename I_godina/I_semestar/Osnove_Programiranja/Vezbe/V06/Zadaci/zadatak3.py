
def indeksTelesneMase(m, h):
    bmi = m / (h**2)
    if bmi < 18.5:
        return "pothranjenost"
    if bmi <= 25:
        return "idealna telesna tezina"
    if bmi <= 30:
        return "preterana telesna tezina"
    return "gojaznost"


def main():
    m = float(input("Unesi svoju težinu u kg: "))
    if m <= 0:
        return print("Negativna masa nije moguća, inače bi već imali worp letelice")
    h = float(input("Unesi svoju visinu u m: "))
    if h <= 0:
        return print("Unesi pravu visinu")
    print(indeksTelesneMase(m, h))
    

if __name__ == "__main__":
    main()