# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

first_number = int(input("Введите первое число:"))
second_number = int(input("Введите второе число:"))
thirt_number = int(input("Введите третье число:"))
if first_number > second_number and first_number > thirt_number:
    if second_number > thirt_number :
        print("Число которое вы ищите", second_number)
    elif thirt_number > second_number:
        print("Число которое вы ищите", thirt_number)
    else:
        print("Имеются одинаковые числа")
elif second_number > first_number and second_number > thirt_number:
    if first_number > thirt_number :
        print("Число которое вы ищите", first_number)
    elif thirt_number > second_number:
        print("Число которое вы ищите", thirt_number)
    else:
        print("Имеются одинаковые числа")
elif thirt_number > first_number and thirt_number > second_number:
    if first_number > second_number:
        print("Число которое вы ищите", first_number)
    elif second_number > first_number:
        print("Число которое вы ищите", second_number)
    else:
        print("Имеются одинаковые числа")
else:
    print("Имеются одинаковые числа")





