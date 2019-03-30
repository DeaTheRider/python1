"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

min = 0
pos = 0
l = []

for i in range(100):
    l.append(random.randint(-100, 100))

for i, j in enumerate(l):
    if j < min:
        min = j
        pos = i

print(l)
print(min)
print(pos)
