import math


def rectangle_method(func, a, b, p):
    h = (b - a) / p
    result = 0
    for i in range(p):
        result += func(a + i * h)
    result *= h
    return result


def func1(x):
    return 1 / math.sqrt(x + 2.5)

def func2(x):
    return 2.2 / math.sqrt(x + 2.5)


a1, b1 = 2.2, 4.6
a2, b2 = 1.6, 3.2
p = 10

result1 = rectangle_method(func1, a1, b1, p)
result2 = rectangle_method(func2, a2, b2, p)

print(f"Значення першого інтегралу: {result1:.6f}")
print(f"Значення другого інтегралу: {result2:.6f}")
