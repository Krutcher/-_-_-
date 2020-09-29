import math
x = float(input('Введите x: '))
if x>=0.2 and x<=0.9:
    k = math.sin(x)
else: k = 1
print(k)
