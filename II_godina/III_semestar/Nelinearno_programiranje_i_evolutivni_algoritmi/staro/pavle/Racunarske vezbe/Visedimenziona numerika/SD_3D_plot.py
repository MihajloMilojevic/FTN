import numpy as np
import matplotlib.pyplot as plt


def steepest_descent(gradf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)
    for k in range(N):
        g = gradf(x)
        x = x - gamma * g
        if np.linalg.norm(g) < epsilon:
            break
    return x


# f = x1^2 + x1x2 + 0.5x2^2 + x1 + 10x2
def func(x):
    f = x[0] * x[0] + x[0] * x[1] + 0.5 * x[1] * x[1] + x[0] + 10 * x[1]
    return f


def gradf(x):
    df = np.zeros((2, 1))
    df[0] = 2 * x[0] + x[1] + 1
    df[1] = x[0] + x[1] + 10
    return df


x0 = [0, 0]
gamma = 0.1
epsilon = 0.001
N = 200
xopt = steepest_descent(gradf, x0, gamma, epsilon, N)
fopt = func(xopt)
print("Funkcija ima minimum fopt = ", fopt, "u tacki: ", xopt, ".\n")

x = np.arange(-25, 15, 0.1)
y = np.arange(-25, 15, 0.1)
xx, yy = np.meshgrid(x, y)
zz = func([xx, yy])

ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, zz)
ax.scatter(xopt[0], xopt[1], fopt, c='r', marker='o')
plt.show()
