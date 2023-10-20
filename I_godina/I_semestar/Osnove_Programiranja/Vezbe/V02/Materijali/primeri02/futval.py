# futval.py
# Izracunava buduce stanje orocenog novca
# za rok od 10 godina

print("Ovaj program izracunava stanje stednog racuna")
print("nakon isteka roka od 10 godina.")

principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))

for i in range(10):
    principal = principal * (1 + apr)

print("Stanje nakon 10 godina:", principal)
