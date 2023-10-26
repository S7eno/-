import numpy as np
import matplotlib.pyplot as plt


xi = np.array([1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390])
yi = np.array([4.2556, 4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706])


x_interpolate = np.array([1.361, 1.394, 1.346, 1.381, 1.342, 1.386])


n = len(xi)
coefficients = yi.copy()
for j in range(1, n):
    coefficients[j:] = (coefficients[j:] - coefficients[j - 1]) / (xi[j:] - xi[j - 1])

def newton_interpolation(x):
    result = coefficients[0]
    term = 1.0
    for j in range(1, n):
        term *= (x - xi[j - 1])
        result += coefficients[j] * term
    return result


y_interpolate = [newton_interpolation(x) for x in x_interpolate]

plt.scatter(xi, yi, label='Задані точки')
plt.plot(x_interpolate, y_interpolate, 'ro', label='Інтерполяційна функція')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
