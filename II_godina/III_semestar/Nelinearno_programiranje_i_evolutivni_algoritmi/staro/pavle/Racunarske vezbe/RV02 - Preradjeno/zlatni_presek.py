import numpy as np
import matplotlib.pyplot as plt
import math


def zlatni_presek(a, b, tol):
    c = (3 - math.sqrt(5)) / 2
    # korak 1 - x1 i x2
    x1 = a + c * (b - a)
    x2 = a + b - x1

    # korak 2 - iterativni postupak
    while (b - a) > tol:
        if func(x1) <= func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x1
        else:
            a = x1
            x1 = x2
            x2 = a + b - x2

    xopt = x1 if func(x1) < func(x2) else x2
    fopt = func(xopt)

    return xopt, fopt


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


##################################################
# TESTIRANJE
a = 0
b = 3
tol = 0.0001

xopt, fopt = zlatni_presek(a, b, tol)
print(xopt, fopt)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f)
p = plt.plot(xopt, fopt, '*r', label='max[f(x)]')
plt.show()
