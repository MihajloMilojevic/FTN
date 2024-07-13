import numpy as np
import matplotlib.pyplot as plt
import math


def sjecica(x1, x0, tol):
    x_pre = x0
    x_ppre = math.inf
    x_novo = x1
    iteracije = 0

    while(abs(x_novo - x_pre) > tol):
        iteracije += 1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre)*(x_pre - x_ppre)/(dfunc(x_pre) - dfunc(x_ppre))
        
    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iteracije     


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

[xopt, fopt, iteracije] = sjecica(init_guess1, init_guess2, tol)
print(xopt, fopt, iteracije)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])
    
p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'or', label = 'max[f(x)]', markersize = 15, markeredgewidth = 3)
plt.show()  