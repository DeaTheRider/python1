"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

l = []
s = 0
f = True

for i in range(10):
    l.append(random.randint(0, 100))
a = min(l)
b = max(l)

for i, j in enumerate(l):
    if f == True:
        if j == a or j == b:
            l1 = l[i + 1:]
            for x in l1:
                if x == b or x == a:
                    f = False
                    break

                else:
                    s += x
        else:
            continue
    else:
        break

print(a, b)
print(l)
print(s)
