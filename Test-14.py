import math
x = 0.0
y = 0.0

epsilon = 0.001


while True:
    new_x = 1.3 - math.sin(y - 1)
    new_y = 0.8 + math.sin(new_x + 1)

    
    if abs(new_x - x) < epsilon and abs(new_y - y) < epsilon:
        break

    x = new_x
    y = new_y

print(f'Результат: x = {x}, y = {y}')

