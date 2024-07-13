import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math


def ackley(x):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(x)):
        sum1 += x[i]**2.0
        sum2 += math.cos(2.0*math.pi*x[i])
    total = -20.0*math.exp(-0.2*math.sqrt(sum1/len(x)))-math.exp(sum2/len(x))+20.0+math.e
    return total

x1v = np.arange(-6, 6, 0.01)
x2v = np.arange(-6, 6, 0.01)
x1, x2 = np.meshgrid(x1v, x2v)
f = np.zeros((len(x1),len(x2)))

for i in range(0,len(x1),1):
    for j in range(0,len(x1),1):
        f[i,j]=ackley((x1[i,j], x2[i,j]))

fig = plt.figure()
ax = fig.gca(projection='3d')
p1 = ax.plot_surface(x1, x2, f)
plt.show()