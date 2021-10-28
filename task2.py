import math


def lilist(listt):
    lilist = list()
    for i in range(len(listt)):
        lilist.append(int(listt[i]))
    return lilist


def nomnom(filename):
    file1 = open(f"{filename}", "r")
    testlist = list()
    while True:
        line = file1.readline()
        if not line:
            break
        testlist.append(lilist(line.strip().split()))
    file1.close
    return testlist


def distance(a, b, a1, b1):
    c = math.sqrt((a1 - a) ** 2 + (b1 - b) ** 2)
    return c


filename = str(input('Введите первый файл: '))
firstdata = nomnom(filename)

filename = str(input('Введите первый файл: '))
seconddata = nomnom(filename)

for i in range(len(seconddata)):
    a, b, c = firstdata[0][0], firstdata[0][1], firstdata[1][0]
    f = distance(a, b, seconddata[i][0], seconddata[i][1])
    if f < float(c):
        print(1)
    elif f == float(c):
        print(0)
    else:
        print(2)
