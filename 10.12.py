import random
n, m = map(int, input('Введите размер массива N*M: ').split( ))
arr = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
for i in arr:
    for j in i:
        print(j, '\t', end = " ")
    print()
qu = 0
ind_str = 0
for i in range(m):
    for j in range(n):
        qu_max = arr[i].count(arr[i][j])
        if qu_max > qu:
            qu = qu_max
            ind_str = i
print()
print('Номер строки с максимальным кол-вом одинаковых эл-тов: ', ind_str)
