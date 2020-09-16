def sred(a=3, b=10, c=7):
    return ((a+b+c)/3)
print (sred())
x1,x2,x3= map(int,input('Введите три числа через пробел:').split())
y=sred(x1,x2,x3)
print (y)
