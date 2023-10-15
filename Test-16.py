import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

x_values = [-4, -2, 0, 3]
y_values = [-18, 8, -6, 3]

x_range = np.linspace(min(x_values), max(x_values), 400)
y_range = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

x_points = [-3.5, -3, -0.5, 2]
y_points = [lagrange_interpolation(x_values, y_values, x) for x in x_points]

plt.figure(figsize=(8, 6))
plt.plot(x_range, y_range, label='Ln(x)')
plt.scatter(x_points, y_points, color='red', label='Обчислені точки')
plt.scatter(x_values, y_values, color='blue', label='Задані точки')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Графік інтерполяційної функції Ln(x)')
plt.show()
