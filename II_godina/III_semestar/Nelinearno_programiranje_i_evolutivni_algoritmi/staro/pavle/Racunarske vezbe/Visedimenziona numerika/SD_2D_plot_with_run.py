import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def steepest_descent(gradf, x0, gamma, tol, iter):
    x = [] # ako mi bude potrebno crtanje
    x0 = np.array(x0).reshape((len(x0), 1))
    for i in range(iter):
        grad = gradf(x0)
        x0 = x0 - gamma*gradf(x0)
        x.append(x0)
        if np.linalg.norm(grad) < tol:
            break
    return x

# y = x1^2 + x1x2 + 0.5x2^2 + x1 + 10x2
# ova funkcija mi treba samo za crtanje
def f(x):
    x1 = x[0]
    x2 = x[1]
    y = x1**2 + x1*x2 + 0.5*x2**2 + x1 + 10*x2
    return y

# gradijent je vektor parcijalnih izvoda
# parcijalni po x1, p1 =  je 2x1 + x2 + 1
# parcijalni po x2, p2 =  je x1 + x2 + 10
# g = [x1, x2]^T
def gradf(x):
    x = np.array(x).reshape((len(x), 1))
    x1 = x[0]
    x2 = x[1]
    parc1 = 2*x1 + x2 + 1
    parc2 = x1 + x2 + 10
    grad = np.array([parc1, parc2]).reshape((2, 1))
    return grad


def plot_run(fun, run, x1span, x2span, label):
    x1, x2 = np.meshgrid(x1span, x2span)
    Y = fun([x1, x2])
    plt.contour(x1, x2, Y, levels=10)
    x1 = [x[0, 0] for x in run]
    x2 = [x[1, 0] for x in run]
    plt.plot(x1, x2, ".", label=label)

    plt.axis("equal")
    plt.legend()
    plt.show()


result = steepest_descent(gradf, x0=[0, 0], gamma = 0.1, tol=1e-4, iter=200)
print(result[-1])
plot_run(f, result, np.arange(-22, 12, 0.1), np.arange(-22, 12, 0.1), label=["Najbrzi pad"])