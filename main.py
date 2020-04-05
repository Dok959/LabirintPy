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

def main(temp):
    with open(temp, 'r' ,encoding = 'utf-8') as f:
        mas = [line.strip() for line in f]
        print(mas)
        t = int(mas[0])
        print(t)








#задать название файла и программа отработает
main("small-test.in.txt")