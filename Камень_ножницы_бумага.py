#import libraries
import random
import enum
import os

#Define classes
class Weapon(enum.Enum):
    камень = 1
    бумага = 2
    ножницы = 3

#Define Functions
def choose_weapon_player():    
    weapon_player = 0
    while weapon_player not in [1, 2, 3]:
        try:
            weapon_player = int(input('Введите 1, если хотите выбрать камень \nВведите 2, если хотите выбрать бумагу \nВведите 3, если хотите выбрать ножницы\n\nЧто вы выбрали?: '))
        except Exception:
            weapon_player = 0
    weapon_player = Weapon(weapon_player)
    print('\nВы выбрали ' + weapon_player.name)
    return weapon_player.value

def choose_weapon_computer():
    weapon_computer = random.randint(1, 3)
    weapon_computer = Weapon(weapon_computer)
    
    if weapon_computer.value == 1:
        print('Противник выбрал камень\n')        
    elif weapon_computer.value == 2: 
        print('Противник выбрал бумагу\n') 
    elif weapon_computer.value == 3:
        print('Противник выбрал ножницы!\n')                   
    return weapon_computer.value

# 1 = rock, 2 = paper, 3 = scissors
def compare_weapons(weapon_player, weapon_computer):
    if weapon_player == weapon_computer:
        print('Ничья!')           
    elif weapon_player == 1 and weapon_computer == 2:
      print('Бумага покрывает камень\n\nВы проиграли!')
    elif weapon_player == 1 and weapon_computer == 3:
        print('Камень ломает ножницы!\n\nВы выиграли!')
    elif weapon_player == 2 and weapon_computer == 3:
      print('Ножницы режут бумагу.\n\nВы проиграли!')
    elif weapon_player == 2 and weapon_computer == 1:
        print('Бумага покрывает камень!\n\nВы выиграли!')
    elif weapon_player == 3 and weapon_computer == 1:
      print('Камень ломает ножницы.\n\nВы проиграли!')
    elif weapon_player == 3 and weapon_computer == 2:
        print('Ножницы режут бумагу!\n\nВы выиграли!')
def play_again():
    print()
    play = input('Нажмите "P" чтобы сыграть еще раз: ' )
    print()
    if play == 'p' or play == 'P':
        main()
    else:
        print('\n')




def main():
    os.system('clear')
    player_weapon = choose_weapon_player()
    computer_weapon = choose_weapon_computer()
    compare_weapons(player_weapon, computer_weapon)
    play_again()


if __name__ == '__main__':
    main()
