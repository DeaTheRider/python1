"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

l = []

for i in range(100):
    l.append(random.randint(-5, 5))
max = 0
max_number = l[0]

for i in l:
    s = 0
    for x, j in enumerate(l):
        if l[i] == l[j]:
            s += 1
    if s > max:
        max = s
        max_number = i

print("В массиве чаще всего встречается число {}. Оно встречается {} раз".format(max_number, max))
