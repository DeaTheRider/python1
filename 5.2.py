import collections

dictionary = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "A": 10,
    "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
}


def number_list(str):
    l = collections.deque([])
    for i in str:
        l.append(i)
    return l


def transfer_10(l, dictionary):
    l.reverse()
    result = 0
    for i, j in enumerate(l):
        b = dictionary[j]
        c = b * (16 ** int(i))
        result += c
    return result


def transfer_hex(a, dictionary):
    import collections
    l = collections.deque([])
    while True:
        if a > 15:
            b = a % 16
            for key in dictionary:
                if b == dictionary[key]:
                    l.append(key)
            a = a // 16

        else:
            for key in dictionary:
                if a == dictionary[key]:
                    l.append(key)
            break

    l.reverse()
    return l


def main():
    first_number = input("Введите первое число")
    sign = input("Введите операнд(* или +)")
    second_number = input("Введите второе число")
    a = number_list(first_number)
    b = number_list(second_number)
    a = transfer_10(a, dictionary)
    b = transfer_10(b, dictionary)
    if sign == "+":
        c = a + b
    else:
        c = a * b

    print(transfer_hex(c, dictionary))


if __name__ == "__main__":
    main()
