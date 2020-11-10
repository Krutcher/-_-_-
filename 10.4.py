import random
some_int = str(random.randint(1, 10))
print('Введите число от 1 до 10')
answer = 0
while answer != some_int:
    answer = input()
    if answer == some_int:
        print('Вы угадали')
    if answer == 'Выход':
        break
