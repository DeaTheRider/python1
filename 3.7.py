"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

l = []
for i in range(10):
    l.append(random.randint(0, 100))
minimal1 = l[0]
minimal2 = l[0]
b = 0

for i, j in enumerate(l):
    if minimal1 > j:
        b = i
        minimal1 = j

for i, j in enumerate(l):
    if i == b:
        continue
    else:
        if minimal2 > j:
            minimal2 = j

print(l)
print(minimal2, minimal1)
