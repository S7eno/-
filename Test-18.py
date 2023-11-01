import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x = np.array([1.1, 1.4, 1.9, 2.5, 2.7])
y = np.array([2.9, 3.64, 4.55, 2.57, 0.24])


cs = CubicSpline(x, y)


x_new = np.linspace(1.1, 2.7, 100)
y_new = cs(x_new)


plt.figure()
plt.scatter(x, y, c='b', label='Табличні дані')
plt.plot(x_new, y_new, 'r', label='Кубічний сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.title('Кубічний сплайн для табличних даних')
plt.grid(True)
plt.show()
