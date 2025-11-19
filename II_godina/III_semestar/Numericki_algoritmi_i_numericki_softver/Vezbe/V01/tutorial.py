import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3], dtype=np.float64)
x = np.array([[1, 2], [3, 4]], dtype=np.float64)

print(np.multiply(x, x))

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y, "r+")
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.plot(x, x, "g-")
plt.plot(x, np.cos(x), "b-")
plt.show()