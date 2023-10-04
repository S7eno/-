import numpy as np

matrix = np.array([[1, 2, 3],
                   [-1, 2, 1],
                   [1, 3, 2]])

determinant = np.linalg.det(matrix)
print(determinant)
