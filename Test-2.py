def f(x):
    return 4*x**3 + 2*x**2 - 3

a = -2
b = 2
tolerance = 0.0001

while (b - a) / 2 > tolerance:
    c = (a + b) / 2
    if f(c) == 0:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

root = (a + b) / 2
