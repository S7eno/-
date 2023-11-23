import math

def function(x):
    return 2.2 / math.sqrt(3 * x**2 + 1)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = (function(a) + function(b)) / 2.0

    for i in range(1, n):
        result += function(a + i * h)

    result *= h
    return result

a = 1.4
b = 2.2
n = 10000  

result = trapezoidal_rule(a, b, n)
print(f"Значення інтегралу методом трапецій: {result:.5f}")
