import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) * np.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x) * cos(x)')
plt.title('Plot of sin(x) * cos(x)')
plt.grid()
plt.show()
