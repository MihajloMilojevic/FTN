import numpy as np
import matplotlib.pyplot as plt
import math


# Njutn - Rapsonov metod
def newton_raphson(x1, tol):

    while True:
        x2 = x1 - dfunc(x1)/ddfunc(x1)
        if abs(x2 - x1) < tol:
            break
        x1 = x2

    return x2, func(x2)

def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f

def dfunc(x):
    f = -(4*x**3 - 15*x**2 - 4*x + 24)
    return f

def ddfunc(x):
    f = -(12*x**2 - 30*x - 4)
    return f

###############################################
# TESTIRANJE ALGORITMA
tol = 0.0001
init_guess = 1
xopt, fopt = newton_raphson(init_guess, tol)
print(xopt, fopt)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])
    
p = plt.plot(x, f)
p = plt.plot(xopt, fopt, '*', label = 'max[f(x)]')
plt.show()    
