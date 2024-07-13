import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def adagrad(gradf, x0, gamma, epsilon, n):
    x0 = np.array(x0).reshape(len(x0), 1)
    g0 = np.zeros(x0.shape)
    x = []
    for k in range(n):
        g = gradf(x0)
        g0 = g0 + np.multiply(g, g)
        # np.ones(g0.shape) ovo je u sustini samo [1
        #                                          1]
        v = gamma * g * np.ones(g0.shape) / np.sqrt(g0 + epsilon)
        x0 = x0 - v
        x.append(x0)
        if np.linalg.norm(g) < epsilon:
            break
    return x


# y = x1^2 + x1x2 + 0.5x2^2 + x1 + 10x2
# ova funkcija mi treba samo za crtanje
def f(x):
    x1 = x[0]
    x2 = x[1]
    y = x1 ** 2 + x1 * x2 + 0.5 * x2 ** 2 + x1 + 10 * x2
    return y


# gradijent je vektor parcijalnih izvoda
# parcijalni po x1, p1 =  je 2x1 + x2 + 1
# parcijalni po x2, p2 =  je x1 + x2 + 10
# g = [x1, x2]^T
def gradf(x):
    x = np.array(x).reshape((len(x), 1))
    x1 = x[0]
    x2 = x[1]
    parc1 = 2 * x1 + x2 + 1
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


# ovo je glup primer i funkcija za ovaj metod ali je cisto dat zbog implementacije
result_adagrad = adagrad(gradf, x0=[0, 0], gamma=5, epsilon=1e-6, n=75)
print(result_adagrad[-1])

plot_run(f, result_adagrad, np.arange(-22, 12, 0.1), np.arange(-22, 12, 0.1), label="ADAGRAD")