def f(x):
    return 4*x**4 - 4*x**3 + 2*x**2 - 3*x - 9

def df(x):
    return 16*x**3 - 12*x**2 + 4*x - 3

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    iter_count = 0
    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / df(x)
        iter_count += 1
    if iter_count == max_iter:
        raise Exception("Метод Ньютона не збігся")
    return x

initial_guess = 1.0  # Початкове наближення
root = newton_method(f, df, initial_guess)
print("Знайдений корінь:", root)
