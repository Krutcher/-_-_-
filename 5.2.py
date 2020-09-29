def maxx(y1, y2):
    if y1 > y2:
        return y1
    else:
        return y2

x1, x2 = map(int, input('Введите два числа: ').split( ))
print('Максимальное  из двух чисел: ', maxx(x1, x2))
