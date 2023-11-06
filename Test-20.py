import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-2*x) + x**2


def taylor_approximation(x):
    return 1 - 2*x + 3*x**2 - 4*x**3

x = np.linspace(-2, 2, 400)  
y = f(x)
y_taylor = taylor_approximation(x)


plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = e^(-2x) + x^2', color='blue')
plt.plot(x, y_taylor, label='Тейлорське наближення', color='red', linestyle='--')
plt.legend()

error = np.abs(y - y_taylor)
plt.figure(figsize=(10, 3))
plt.plot(x, error, label='Похибка', color='green')
plt.legend()

plt.show()
