# factorial.py
# Racunanje faktorijela
# Ilustruje petlju sa akumulatorom

n = eval(input("Unesite ceo broj: "))
fact = 1
for factor in range(n, 1, -1):
    fact = fact * factor
print("Faktorijel od", n, "je", fact)
