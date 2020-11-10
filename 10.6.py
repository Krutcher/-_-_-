sum_ = 0
n = 0
while n == 0:
    x = input('Введите число или стоп для выхода и вывода суммы: ')
    if str(x) == 'стоп':
        print(sum_)
        n = 1
    else:
        sum_ = sum_ + int(x)
