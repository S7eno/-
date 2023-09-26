def f(x):
    return 4*x**4 - 4*x**3 + 2*x**2 - 3*x - 9

def df(x):
    return 16*x**3 - 12*x**2 + 4*x - 3

def newton_method(initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    for i in range(max_iter):
        f_value = f(x)
        if abs(f_value) < tol:
            return x
        x = x - f_value / df(x)
    raise ValueError("Метод Ньютона не сходився")

newton_root = newton_method(0.5)
print(f"За допомогою комбінованого методу: x = {newton_root}")
