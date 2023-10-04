import numpy as np

N = 5  
M = 4  

matrix = np.random.rand(N, M)

print("Матриця A:")
print(matrix)

mean_row = np.mean(matrix, axis=1)
mean_column = np.mean(matrix, axis=0)

print("Середні значення рядків:")
print(mean_row)

print("Середні значення стовпців:")
print(mean_column)
