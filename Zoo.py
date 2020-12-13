class Zoo(object):

    def __init__(self, name, hunger=0, boredom=0):
        print("Появилась на свет новая зверушка\n")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print('Привет! Меня зовут '+self.name+". Сейчас я чувствую себя"+self.mood+"!")
        self.__pass_time()

    def eat(self, food):
        print("Ням-ням")
        self.hunger-=food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Ура, играть!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom
        if unhappiness <5:
            m = "прекрасно"
        elif 5<=unhappiness<=10:
            m = "нормально"
        elif 10<unhappiness<=15:
            m = "не очень"
        else:
            m = "ужасно"
        return m


class Lev(Zoo):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появилась на свет новый Львёнок\n")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Гав-Гав! Меня зовут '+self.name+". Сейчас я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

class Keng(Zoo):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появился на свет новый Кенгурёнок\n")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Мяу! Меня зовут '+self.name+". Сейчас я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

class Popug(Zoo):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появился на свет новый Попугай\n")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Фыр-Фыр! Меня зовут '+self.name+". Сейчас я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

def main():
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\nДобро пожаловать на мой зоопарк!\n\nУ нас есть Львёнок, Кенгурёнок и Попугайчик.\nПридумай им имена, мой друг :D!\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    lev = Lev(input('Введи имя Львёнка: '))
    keng = Keng(input('Введи имя Кенгурёнка: '))
    popug = Popug(input('Введи имя Попугая: '))
    choice = None
    while choice != "0":
        print \
            ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Выберите зверюшку для взаимодействия

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Выйти
1 - Львёнок
2 - Кенгурёнок
3 - Попугай
""")
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == '1':
            choice_lev = None
            while choice_lev != '0':
                print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Вы выбрали Львёнка, выберите дальнейшее действие:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Поговорить с животным
2 - Накормить
3 - Поиграть
""")
                choice_lev = input("Ваш выбор: ")
                if choice_lev == '0':
                    break
                elif choice_lev == '1':
                    lev.talk()
                elif choice_lev == '2':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Чем хотите накормить?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Мясной соус(5 единиц)
2 - Стейк из говядины(8 единиц)
3 - Корм со вкусом курицы(7 единиц)
""")
                    choice_lev_eat = input("Ваш выбор: ")
                    if choice_lev_eat == "0":
                        break
                    elif choice_lev_eat == "1":
                        lev.eat(5)
                    elif choice_lev_eat == "2":
                        lev.eat(8)
                    elif choice_lev_eat == "3":
                        lev.eat(7)
                    elif choice_lev_eat == '4':
                        lev.eat(10)
                        print('Ура, ты нашёл дополнительный стейк! Твой '+lev.name+' очень рад!')
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_lev == '3':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

С чем хотите поиграть?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Мячик(7 единиц)
2 - Большая кость(8 единиц)
3 - Точилка для зубов(4 единицы)
""")
                    choice_lev_play = input("Ваш выбор: ")
                    if choice_lev_play == "0":
                        break
                    elif choice_lev_play == "1":
                        lev.play(7)
                    elif choice_lev_play == "2":
                        lev.play(8)
                    elif choice_lev_play == "3":
                        lev.play(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
        elif choice == '2':
            choice_keng = None
            while choice_keng != '0':
                print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Вы выбрали Кенгурёнка, выберите дальнейшее действие:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Поговорить с животным
2 - Накормить
3 - Поиграть
""")
                choice_keng = input("Ваш выбор: ")
                if choice_keng == '0':
                    break
                elif choice_keng == '1':
                    keng.talk()
                elif choice_keng == '2':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Чем хотите накормить?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Вкусная травка(5 единиц)
2 - Корни кустарников(8 единиц)
3 - Листья деревьев(7 единиц)
""")
                    choice_keng_eat = input("Ваш выбор: ")
                    if choice_keng_eat == "0":
                        break
                    elif choice_keng_eat == "1":
                        keng.eat(5)
                    elif choice_keng_eat == "2":
                        keng.eat(8)
                    elif choice_keng_eat == "3":
                        keng.eat(7)
                    elif choice_keng_eat == '4':
                        keng.eat(10)
                        print('Ура, ты нашёл cекретную Пудинг! Твой ' + keng.name + ' очень рад!')
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_keng == '3':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

С чем хотите поиграть?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Устроить спарринг(7 единиц)
2 - Большой мячик (8 единиц)
3 - Попрыгать вместе(5 единицы)
""")
                    choice_keng_play = input("Ваш выбор: ")
                    if choice_keng_play == "0":
                        break
                    elif choice_keng_play == "1":
                        keng.play(7)
                    elif choice_keng_play == "2":
                        keng.play(8)
                    elif choice_keng_play == "3":
                        keng.play(5)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
        elif choice == '3':
            choice_popu = None
            while choice_popu != '0':
                print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Вы выбрали Попугая, выберите дальнейшее действие:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Поговорить с животным
2 - Накормить
3 - Поиграть
        """)
                choice_popu = input("Ваш выбор: ")
                if choice_popu == '0':
                    break
                elif choice_popu == '1':
                    popug.talk()
                elif choice_popu == '2':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Чем хотите накормить?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Корм(5 единиц)
2 - Морковку(7 единиц)
3 - Семечки(6 единиц)
""")
                    choice_popu_eat = input("Ваш выбор: ")
                    if choice_popu_eat == "0":
                        break
                    elif choice_popu_eat == "1":
                        popug.eat(5)
                    elif choice_popu_eat == "2":
                        popug.eat(8)
                    elif choice_popu_eat == "3":
                        popug.eat(7)
                    elif choice_popu_eat == '7':
                        popug.eat(10)
                        print('Ура, ты нашёл секретное яблоко! Твой '+popug.name +' очень рад!')
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_popu== '3':
                    print \
                    ("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

С чем хотите поиграть?

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
0 - Назад
1 - Выпустить полетать(6 единиц)
2 - Поговорить с ним)(8 единиц)
3 - Шарик(7 единицы)
""")
                    choice_popu_play = input("Ваш выбор: ")
                    if choice_popu_play == "0":
                        break
                    elif choice_popu_play == "1":
                        popug.play(6)
                    elif choice_popu_play == "2":
                        popug.play(8)
                    elif choice_popu_play == "3":
                        popug.play(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
        elif choice == '4':
            print\
            ("""Ты нашёл секретный пункт меню!\n
┊┊▕╲▂▕╲▂▂┈┈┈┈┈┈┈
┊┊▕╱▋▍╲▎▋╲┈┈┈┈┈┈
┊┊╱╭▅╮▍▍╲▋╲▂┊┊┊┊ 
╱▔╱▂▔▃┃▋▋▕▍▉╲▂▂▂ 
▏▅┳╮▍▍╱▍▊▕▋▕▍▕▋▋ 
╲━╯╱▔▔╲▎▊▕▊▕▋▕▋▋ 
┊▔▔┊┊┊┊╲▋▕▋▕▋▕▍▍ 
┊┊┊┊┊┊┊┊╲▕▍▕▍▕▏▎

Это ваш новый друг Зебра :)
Он теперь живёт вместе с вами 
""")
        else:
            print("Извините, в меню игры нет такого пункта")

main()
input("\n\nНажмите Enter, чтобы выйти")
