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

x_points = [-3.5, -3, -0.5, 2]


results = [lagrange_interpolation(x_values, y_values, x) for x in x_points]

for i, x in enumerate(x_points):
    print(f"f({x}) ≈ {results[i]:.4f}")
