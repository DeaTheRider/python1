import collections
def create():
    n = int(input("Введите колличество предприятий: "))
    l1 = []
    for i in range(n):
        company = collections.namedtuple('company', ['name', 'I', 'II', 'III', 'IV', 'profit'])
        name = input("Введите название предприятия № {} ".format(i + 1))
        l = [name, ]
        d = 0
        for j in range(4):
            c = int(input("Введите сумму за {} квартал ".format(j + 1)))
            l.append(c)
            d +=c
        l.append(d)
        e = company(l[0],l[1],l[2],l[3],l[4],l[5])
        l1.append(e)

    return l1

def average1(list):
    c = 0
    result = 0
    for i in list:
        result += i.profit
        c += 1
    average = result / c
    return average

def simile_average(list, average, b = False):
    if len(list) == 1:
        print("Вы ввели данные по одному предприятию. Его доход равен {}".format(average))
    else:
        if b == True:
            for i in list:
                if i.profit > average:
                    print("У предприятия {} доход больше среднего значения. ""Доход состовляет {} ".format(i.name,
                                                                                                           i.profit))
        else:
            for i in list:
                if i.profit < average:
                    print("У предприятия {} доход меньше среднего значения. ""Доход состовляет {} ".format(i.name,
                                                                                                           i.profit))
            simile_average(list, average, b=True)


def main():
    a = create()
    b = average1(a)
    simile_average(a,b)

if __name__ == "__main__":
    main()





