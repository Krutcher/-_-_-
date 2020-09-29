import random
x = random.randint(1, 6)
y = random.randint(1, 6)
print('Бросок 1-го игрока =',x)
print('Бросок 2-го игрока =',y)
if x > y:
    print('Победил 1-ый игрок')
else:
    print('Победил 2-ой игрок')
