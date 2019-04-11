"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random
import timeit
import cProfile
def shellsort(a):
    def new_increment(a):
        i = int(len(a)/2)
        yield i
        while i != 1:
            if i == 2:
                i =1
            else:
                i = int(round(i/2.2))
            yield i
    for increment in new_increment(a):
        for i in range(increment,len(a)):
            for j in range(i,increment-1,-increment):
                if a[j-increment] < a[j]:
                    break
                a[j],a[j-increment] = a[j-increment],a[j]
    return a


def create_list(x):
    array = []
    for i in range(x):
        number = random.uniform(0, 50)
        number = round(number, 3)
        array.append(number)
    return array

def median(a):
    if len (a) % 2 == 1:
        return a[len(a)//2]
    else:
        b = 0.5*(a[len(a)//2-1] + a[len(a)//2])
        return b
#@profile
def main():
    m = int(input("Введите значение m: "))
    #m = 10
    a = create_list(2*m+1)
    a = shellsort(a)
    print(a)
    print(median(a))

if __name__ == "__main__":
    main()
"""
Line #    Mem usage    Increment   Line Contents
================================================
    42   36.578 MiB   36.578 MiB   @profile
    43                             def main():
    44                                 #m = int(input("Введите значение m: "))
    45   36.578 MiB    0.000 MiB       m = 10
    46   36.586 MiB    0.008 MiB       a = create_list(2*m+1)
    47   36.586 MiB    0.000 MiB       a = shellsort(a)

"""

#cProfile.run('main()')
"""
102 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 7.3.1.py:10(shellsort)
        5    0.000    0.000    0.000    0.000 7.3.1.py:11(new_increment)
        1    0.000    0.000    0.000    0.000 7.3.1.py:29(create_list)
        1    0.000    0.000    0.000    0.000 7.3.1.py:44(main)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       21    0.000    0.000    0.000    0.000 random.py:372(uniform)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       23    0.000    0.000    0.000    0.000 {built-in method builtins.round}
       21    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       21    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

"""
#print(timeit.timeit("main()", setup="from __main__ import main", number=1000000))
# 53.938937049

