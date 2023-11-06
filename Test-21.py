import numpy as np
from scipy.interpolate import approximate_taylor_polynomial
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-2*x) + x**2

x0 = 0.0

degree = 4

scale = 1.0

order = None

taylor_poly = approximate_taylor_polynomial(f, x0, degree, scale, order)

x_values = np.linspace(-1, 1, 400)
y_values = [taylor_poly(x) for x in x_values]
actual_values = [f(x) for x in x_values]

plt.plot(x_values, y_values, label='Taylor Polynomial')
plt.plot(x_values, actual_values, label='Actual Function')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor Polynomial vs. Actual Function')
plt.grid(True)
plt.show()
