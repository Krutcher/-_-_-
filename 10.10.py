import random
n, m = map(int, input('Введите размер массива N*M: ').split( ))
arr = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
for i in arr:
    for j in i:
        print(j, '\t', end = " ")
    print()
