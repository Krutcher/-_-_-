def x(B1,B2,C1,C2,D):
    return (C1 * B2 - C2 * B1)/ D

def y (A1,A2,C1,C2,D):
    return (A1*C2-A2*C1)/D

def D(A1, A2, B1, B2):
    return (A1 * B2 - A2 * B1)
A1, A2, B1, B2, C1, C2 = map(int, input('Введите A1, A2, B1, B2, C1, C2: ').split())
d = D(A1, A2, B1, B2)
X = x(B1, B2, C1, C2, d)
Y = y(A1, A2, C1, C2, d)
print('x = ', X, 'y = ', Y)
    
