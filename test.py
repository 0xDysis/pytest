import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

x = np.linspace(-10, 10, 400)
y = f(x)

plt.plot(x, y)
plt.show()