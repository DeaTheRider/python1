#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

def binary_search(list,item):
    min = 0
    max = len(list)-1
    while min <= max:
        mid = (min + max)
        guess = list[mid]
        if mid == item :
            return guess
        elif mid > item:
            max = mid - 1
        else:
            min = mid + 1
    return None

a = string.ascii_uppercase
my_list = list(a)
print (len(a))
b = int(input("Введите номер буквы"))
print(binary_search(my_list,b))




