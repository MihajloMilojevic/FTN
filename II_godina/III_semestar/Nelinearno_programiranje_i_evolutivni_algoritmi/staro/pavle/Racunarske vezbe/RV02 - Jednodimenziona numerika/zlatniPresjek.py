import numpy as np
import matplotlib.pyplot as plt
import math

def zlatniPresjek(a, b, tol):
    
    c = (3 - math.sqrt(5)) / 2
    # korak 1 - x1 i x2
    x1 = a + c * (b - a)
    x2 = a + b - x1
    n = 1
    
    # korak 2 - iterativni postupak
    while (b - a) > tol:
        n += 1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c * (b - a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c * (b - a)
            x2 = a + b - x1
            
    if func(x1) < func(x2):
        xopt = x1
        fopt = func(x1)
    else:
        xopt = x2
        fopt = func(x2)
        
    return xopt, fopt, n               



def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f

##################################################
# TESTIRANJE
a = 0
b = 3
tol = 0.0001

[xopt, fopt, n] = zlatniPresjek(a, b, tol)
print(xopt, fopt, n)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])
    
p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, '*r', label = 'max[f(x)]', markersize = 15, markeredgewidth = 3)
plt.show()  

