import random as rd
import time as  ti 


class Single:
    def __init__(self):
        self.com_score = 0
        self.my = 0
        self.myscore = 0
        #vs 2
        self.player1_name = None
        self.player2_name = None
        self.player1 = 0
        self.player2 = 0
        self.player1_sco = 0
        self.player2_sco = 0

    def start(self):
        print("Выберите опцию")
        print("1.Хорошо\n2.Неплохо")
        toss = input("> ")
        t = rd.randint(1, 2)
        if (toss == t):
            print("Ты выиграл вбрасывание")
            self.myturn()
        else:
            print("Компьтер выиграл вбрасывание")
            self.Comturn()

    def myturn(self):
        self.check()
        print("-"*10)
        print("Твой ход")
        input("Нажми Enter для броска: ")
        print("Кости бросаются...")
        ti.sleep(3)
        self.my = rd.randint(1, 6)
        print("Ты получилt => ",self.my)
        self.myscore += self.my
        print(f'Твой счёт {self.myscore}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Снова ты ходишь")
            self.myturn()
        else:
            self.Comturn()

    def Comturn(self):
        self.check()
        print("-"*10)
        print("Ход комьютера")
        print("Кости бросаются...")
        ti.sleep(3)
        self.com = rd.randint(1, 6)
        print("Компьютер получил => ",self.com)
        self.com_score += self.com
        print(f'Счёт компьютера {self.com_score}/30')
        print("-"*10)
        if(self.com == 1 or self.com == 6):
            print("Ходит снова компьютер")
            self.Comturn()
        else:
            self.myturn()
    
    def check(self):
        if (self.myscore >= 30):
            print("#"*20)
            print("Ты победил...")
            print("#"*20)
            self.deall()
            d = Double()
            d.menu()
        elif (self.com_score >= 30):
            print("#"*20)
            print("Победил компьютер\nНе переживай! Повезёт в следующий раз...")
            print("#"*20)
            self.deall()
            d = Double()
            d.menu()
        
    def deall(self):
        self.com_score = 0
        self.myscore = 0
        self.player1_name = None
        self.player1_sco = 0
        self.player2_name = None
        self.player2_sco = 0

class Double(Single):
    
    def menu(self):
        print("\n_______________\n\nДобро пожаловать в игру бросание костей:)\nПобедит тот,кто первым набёрет 30 очков\nЕсли игроку выпадает 1 или 6, он ходит ещё раз:D")
        print("_"*15)
        print("\n1.Vs Компьютера\n2.vs Игрока №2")
        print("_"*15)
        x = int(input("> "))
        if(x == 1):
            self.start()
        elif (x == 2):
            self.start2()
        else:
            print("Invalid option")
            self.menu()

    def start2(self):
        
        self.player1_name = input("Введите имя игрока 1: ")
        self.player2_name = input("Введите имя игрока 2: ")
        print(self.player1_name, "Выберите опцию")
        print("1.Хорошо\n2.Неплохо")
        toss = input("> ")
        t = rd.randint(1, 2)
        if (toss == t):
            print(self.player1_name, "выйграл вбрасывание")
            self.play1()
        else:
            print(self.player2_name, "выйграл вбрасывание ")
            self.play2()

    def play1(self):
        self.chec2()
        print("-"*10)
        print(self.player1_name, " ход")
        input("Нажми Enter для броска: ")
        print("Кости бросаются...")
        ti.sleep(3)
        self.my = rd.randint(1, 6)
        print("У тебя => ",self.my)
        self.player1_sco += self.my
        print(f'Твой счёт{self.player1_sco}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Снова твой ход")
            self.play1()
        else:
            self.play2()

    def play2(self):
        self.chec2()
        print("-"*10)
        print(self.player2_name, " ход")
        input("Нажми Enter для броска:: ")
        print("Кости бросаются...")
        ti.sleep(3)
        self.my = rd.randint(1, 6)
        print("Ты получил=> ",self.my)
        self.player2_sco += self.my
        print(f'Твой счёт {self.player2_sco}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Снова твой ход")
            self.play2()
        else:
            self.play1()

    def chec2(self):
        if (self.player1_sco >= 30):
            print("#"*20)
            print(self.player1_name, " победил...")
            print("#"*20)
            self.deall()
            self.menu()
        elif (self.player2_sco >= 30):
            print("#"*20)
            print(self.player2_name," победил...")
            print("#"*20)
            self.deall()
            self.menu()

        

if __name__ == "__main__":
    d = Double()
    d.menu()
