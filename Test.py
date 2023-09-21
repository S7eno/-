def f(x):
    return 4*x**3 + 2*x**2 - 3

a = -2
b = 2
tolerance = 0.0001

while abs(b - a) > tolerance:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    a = b
    b = c

root = (a + b) / 2
                                                                                        
print(root)