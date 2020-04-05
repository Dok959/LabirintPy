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
def func(n, temp):
    print(temp)




#печать 
def printf(n, t):
    print('Case # ' + n)


#точка входа; задать название файла и программа отработает
#main("small-test.in.txt")
main("test.txt")
