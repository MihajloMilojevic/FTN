import numpy as np
import matplotlib.pyplot as plt
import math


def secica(x1, x2, tol):

    while True:
        x3 = x2 - dfunc(x2) * (x2 - x1) / (dfunc(x2) - dfunc(x1))
        if abs(x3 - x2) < tol:
            break
        x1 = x2
        x2 = x3

    return x3, func(x3)


def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f

def dfunc(x):
    f = -(4*x**3 - 15*x**2 - 4*x + 24)
    return f

#############################################
# TESTIRANJE
tol = 0.0001
init_guess1 = 0
init_guess2 = 3

xopt, fopt = secica(init_guess1, init_guess2, tol)
print(xopt, fopt)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(len(x)):
    f[i] = func(x[i])
    
p = plt.plot(x, f)
p = plt.plot(xopt, fopt, '*', label='max[f(x)]')
plt.show()  