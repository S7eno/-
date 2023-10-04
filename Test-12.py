import numpy as np

A = np.array([[1, 2, -1],
              [3, 4, 1],
              [5, 1, -3]])

b = np.array([-3, 1, -2])

solution = np.linalg.solve(A, b)

print("Розв'язок системи:")
print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
