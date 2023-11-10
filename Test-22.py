import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

xi = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
yi = np.exp(-xi) + xi**2

def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

params_linear, covariance_linear = curve_fit(linear_func, xi, yi)
a_linear, b_linear = params_linear

params_quadratic, covariance_quadratic = curve_fit(quadratic_func, xi, yi)
a_quadratic, b_quadratic, c_quadratic = params_quadratic

x_linear = np.linspace(0, 1, 100)
y_linear = linear_func(x_linear, a_linear, b_linear)

x_quadratic = np.linspace(0, 1, 100)
y_quadratic = quadratic_func(x_quadratic, a_quadratic, b_quadratic, c_quadratic)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(xi, yi, label='Точки', color='r')
plt.plot(x_linear, y_linear, label='Наближення прямою', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Наближення прямою')

plt.subplot(1, 2, 2)
plt.scatter(xi, yi, label='Точки', color='r')
plt.plot(x_quadratic, y_quadratic, label='Наближення параболою', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Наближення параболою')

plt.tight_layout()
plt.show()
