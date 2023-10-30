# futval.py
# Izračunava buduće stanje oročenog novca za zadati broj godina

if __name__ == '__main__':

    print("Ovaj program izračunava stanje štednog racuna")

    year = eval(input("Unesite broj godina na koji želite da oročite štednju: "))
    principal = eval(input("Unesite početni ulog: "))
    apr = eval(input("Unesite godišnju kamatu: "))

    for i in range(year):
        principal = principal * (1 + apr)

    print("Stanje nakon", year," godina:", principal)
