import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lin


def parabola(x1, x3, tol):
    x2 = (x1 + x3) / 2

    while True:
        A = np.array([[1, x1, x1 ** 2], [1, x2, x2 ** 2], [1, x3, x3 ** 2]])
        k = np.array([func(x1), func(x2), func(x3)])
        x = lin.solve(A, k)
        a = x[0]
        b = x[1]
        c = x[2]

        xopt = -b / (2 * c)

        if func(xopt) < func(x2):
            if xopt > x2:
                x1 = x2
            else:
                x3 = x2
            x2 = xopt
        else:
            if xopt > x2:
                x3 = xopt
            else:
                x1 = xopt
        if np.abs(np.dot([1, xopt, xopt ** 2], x) - func(xopt)) < tol:
            break

    return xopt


def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f


##################################################
# TESTIRANJE
a = 0
b = 2
tol = 0.001

xopt = parabola(a, b, tol)
print(xopt)

x = np.linspace(0, 4, 1000)
f = func(x)

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, func(xopt), '*r', label='max[f(x)]')
plt.show()
