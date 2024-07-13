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

result = steepest_descent(gradf, x0=[0, 0], gamma = 0.1, tol=1e-4, iter=200)
print(result[-1])


# Treba znati ovaj kod

def plot_run(fun, run, x1span, x2span, labels=None, connect_the_dots=False):
    if not labels:
        labels = []
    for i in range(len(run)-len(labels)):
        labels.append(f"run {len(labels)+i}")
    colors = ["k", "r", "b", "g"]
    x1, x2 = np.meshgrid(x1span, x2span)
    Y = fun([x1, x2])
    plt.contour(x1, x2, Y, levels=10)
    for i, r in enumerate(run):
        x1 = [x[0, 0] for x in r]
        x2 = [x[1, 0] for x in r]
        plt.plot(x1, x2, f".{colors[i]}", label=labels[i])
        if connect_the_dots:
            plt.plot(x1, x2, f"--{colors[i]}")
    plt.axis("equal")
    plt.legend()

plot_run(f, [result],
         np.arange(-22, 12, 0.1), np.arange(-22, 12, 0.1),
         connect_the_dots=True, labels=["najbrzi pad"])

plt.show()

