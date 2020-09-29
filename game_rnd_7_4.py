import random
def game():
    rand_k = random.randint(1, 10)
    f = int(input('Введите целое число от 1 до 10: '))
    if f!= rand_k:
        print('Повторите еще раз')
    else:
        print('Победа')

if __name__ == "__main__":
    game()
