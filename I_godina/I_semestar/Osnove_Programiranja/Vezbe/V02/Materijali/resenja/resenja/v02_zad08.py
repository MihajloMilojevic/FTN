# futval.py
# Izračunava buduće stanje oročenog novca za zadati broj godina

if __name__ == '__main__':

    print("Ovaj program izračunava stanje štednog racuna")

    year = eval(input("Unesite broj godina na koji želite da oročite štednju: "))
    principal = eval(input("Unesite početni ulog: "))
    apr = eval(input("Unesite godišnju kamatu: "))
    inflation = eval(input("Unesite inflaciju: "))

    for i in range(year):
        principal = principal * (1 + apr)
        principal = principal / (1 + inflation)

    print("Stanje nakon", year," godina:", principal)
