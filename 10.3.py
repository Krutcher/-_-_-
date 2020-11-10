n = int(input('Введите число N элементов списка: '))
import random
L = [random.randint(-10, 10) for i in range(n)]
print('Начальный список: ', L)
L_middle = len(L) // 2
print('Измененный список: ', L[L_middle:] + L[:L_middle])
