table = [[True, False, False, False],
         [False, True, False, False],
         [True, True, False, False],
         [False, False, True, False],
         [True, False, True, False],
         [False, True, True, False],
         [True, True, True, False],
         [False, False, False, True],
         [True, False, False, True],
         [False, True, False, True],
         [True, True, False, True],
         [False, False, True, True],
         [True, False, True, True],
         [False, True, True, True],
         [True, True, True, True]]

#чтение файла
def main(file):
    with open(file) as f:
        t = f.read().split("\n")
        for i in range(1, len(t)):
            temp = t[i].replace(" ", "RR")
            func(i, temp)

#обработка
def func(n, path):
    temp = ""
    flag = False
    for i in range(1, len(path)):
        mas = []
        if path[i] == "W":
            if flag == False:
                mas.append(True, True, False, False)
            elif flag == True:
                mas.append(False, False, True, True)
        elif path[i] == "L":
            if path[i-1] == "W":
                mas.append(True, False, False, True)
        else:
            if path[i-1] == "W":
                mas.append(True, False, True, False)
            elif path[i-1] == "R":
                mas.append(True, False, False, False)
        temp += block(mas, table)
        

#определение границ
def block(mas, table):
    for i in range(len(table)):
        if table[i] == mas:
            index(i)

#определение цифры или буквы
def index(i):
    if i == 10:
        return "a"
    elif i == 11:
        return "b"
    elif i == 12:
        return "c"
    elif i == 13:
        return "d"
    elif i == 14:
        return "e"
    elif i == 15:
        return "f"
    else:
        return i

#печать 
def printf(n, t):
    print('Case # ' + n)


#точка входа; задать название файла и программа отработает
#main("small-test.in.txt")
main("test.txt")
