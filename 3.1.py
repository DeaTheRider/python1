'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

'''
l = [x for x in range(2, 99)]
l1 = [x for x in range(2, 10)]
l2 = [0] * 8

for i in l:
    for j, x in enumerate(l1):
        if i % x == 0:
            l2[j] += 1
print(l2)

for i, j in enumerate(l2):
    print("Число {} кратно {} числам ".format(l1[i], j))
