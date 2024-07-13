import numpy as np
import matplotlib.pyplot as plt



def fibonaci_metod(a, b, tol):
    # korak 1
    n = 1
    while ((b - a) / tol) > fibonaci_broj(n):
        n += 1
        
    # korak 2
    x1 = a + fibonaci_broj(n - 2) / fibonaci_broj(n) * (b - a)
    x2 = a + b - x1
    
    # korak 3 - iterativni postupak
    for i in range(2, n + 1):
        if func(x1) < func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1 

    if func(x1) < func(x2):
        xopt = x1
        fopt = func(xopt)
    else:
        xopt = x2
        fopt = func(x2)
        
    return xopt, fopt, n
                  

def fibonaci_broj(n):
    #1 1 2 3 5 8
    if n < 3:
        f = 1
    else:
        fp = 1
        fpp = 1
        for i in range(3, n+1):
            f = fp + fpp
            fpp = fp
            fp = f
    return f

def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f


##################################################
# TESTIRANJE
a = 0
b = 3
tol = 0.0001

[xopt, fopt, n] = fibonaci_metod(a, b, tol)
print(xopt, fopt, n)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])
    
p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, '*r', label = 'max[f(x)]', markersize = 15, markeredgewidth = 3)
plt.show()  



















