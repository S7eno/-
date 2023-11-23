import math

def f(x):
    return x**2 * math.cos(x)

def simpson_integral(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        coefficient = 4 if i % 2 == 1 else 2
        result += coefficient * f(x)

    result *= h / 3
    return result


a = 0.6
b = 1.4
n = 8


result = simpson_integral(a, b, n)


print("Значення інтегралу методом Сімпсона:", round(result, 4))
