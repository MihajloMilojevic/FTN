# quadratic.py
# Racuna realne korene kvadratne jednacine
# Ilustruje upotrebu paketa math
# Napomena: program ce puci ako nema realnih korena

import math

print("Izracunavanje korena kvadratne jednacine")
print()

a, b, c = eval(input("Unesite koeficijente (a, b, c): "))

discRoot = math.sqrt(b * b - 4 * a * c)
root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a)

print()
print("Resenja su:", root1, root2)
