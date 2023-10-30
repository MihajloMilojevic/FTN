# futval.py
# Izracunava buduce stanje orocenog novca
# za rok od 10 godina

print("Ovaj program izracunava stanje stednog racuna")
print("nakon isteka roka od n godina.")

principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))
god = eval(input("Unesite broj godina za racunanje: "))
inf = eval(input("Unesite inflaciju: "))

for i in range(god):
    principal = principal * (1 + apr)
    principal = principal / (1 + inf)

print(f"Stanje nakon {god} godina: {round(principal, 2)}")
