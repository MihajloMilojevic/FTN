# futval.py
# Izracunava buduce stanje orocenog novca
# za rok od 10 godina

print("Ovaj program izracunava stanje stednog racuna")
print("nakon isteka roka od n godina.")

principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))
god = eval(input("Unesite broj godina za racunanje: "))

for i in range(god):
    principal = principal * (1 + apr)

print(f"Stanje nakon {god} godina: {round(principal, 2)}")
