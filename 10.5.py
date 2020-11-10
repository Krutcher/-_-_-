n_sum = 0
n = int(input('Введите n: '))
while n % 10 != 0:
    if n % 2 == 1:
        n_sum += n % 10
        n = n // 10
    else:
        n = n // 10
print(n_sum)
