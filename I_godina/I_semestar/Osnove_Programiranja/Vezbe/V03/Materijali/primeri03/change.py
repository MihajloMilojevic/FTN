# change.py
# Izracunava iznos u gvozdenim novcicima dolara

print("Brojac kusura")
print()
print("Unesite kolicinu svakog od novcica.")
quarters = eval(input("Quarters: "))
dimes = eval(input("Dimes: "))
nickels = eval(input("Nickels: "))
pennies = eval(input("Pennies: "))
total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
print()
print("Ukupna vrednost novcica je", total)

