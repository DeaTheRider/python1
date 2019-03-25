"""В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число."""
import random

number = random.randint(0, 100)
n = 10

while n != 0:
    a = int(input('Введите число: '))
    if number == a:
        print("Вы угадали!!!")
        break
    elif number > a:
        print("Вы не угадали ! Загаданное число больше введенного. У вас осталось {} попыток ".format(n - 1))
    else:
        print("Вы не угадали ! Загаданное число меньше введенного. У вас осталось {} попыток ".format(n - 1))
    n -= 1

if n == 0:
    print("Загаданное число равно {}".format(number))
