"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

l = []

for i in range(10):
    l.append(random.randint(-100, 100))

for i, j in enumerate(l):
    if i == 0:
        min = j
        index_min = i
        max = j
        index_max = i
    if min > j:
        min = j
        index_min = i
    if max < j:
        max = j
        index_max = i

print(l)

l[index_min], l[index_max] = l[index_max], l[index_min]

print(l)
