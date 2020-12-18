import numpy as np
import matplotlib.pyplot as plt

plt.axhline(0, color='red')
plt.axvline(0, color='green')

x = np.arange(-5, 5.0, 0.01)
f = 3 * x + 6

plt.plot(x, f)
plt.show()
