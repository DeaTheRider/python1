"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""
import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

for line in matrix:
    print(line)

min_colums = []

for line in matrix:
    min_colums.append(line[0])

for line in matrix:
    for i, j in enumerate(line):
        if min_colums[i] > j:
            min_colums[i] = j

max = min_colums[0]

for i in min_colums:
    if max > i:
        max = i

print("Минимальные значения в столбцах")
print(min_colums)
print("Максимальное значение среди минимальных элементов = {}".format(max))
