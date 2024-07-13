import numpy as np
import matplotlib.pyplot as plt


def fibonaci_metod(a, b, tol):
    # korak 1
    n = 1
    while ((b - a) / tol) > fib(n):
        n += 1
        
    # korak 2
    x1 = a + fib(n - 2) / fib(n) * (b - a)
    x2 = a + b - x1
    
    # korak 3 - iterativni postupak
    for i in range(1, n+1):
        if func(x1) < func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

    return x1 if func(x1) < func(x2) else x2


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f


##################################################
# TESTIRANJE
a = 0
b = 3
tol = 0.0001

xopt = fibonaci_metod(a, b, tol)
print(xopt)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(len(x)):
    f[i] = func(x[i])
    
plt.plot(x, f)
plt.plot(xopt, func(xopt), '*r',)
plt.show()  



















