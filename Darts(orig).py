x=int(input("Введите количество игр "))
for i in range(x):
    n,k=map(int,input("Количество секторов и номер черной мишени ").split())
    max=-100
    q=0
    a = list(map(int, input().split()))
    if len(a)!=n:
        print('Введеено неверное количество секторов')
    else:
            a[k] = min(a)
            if a[k] > 0:
                a[k] = 0
            for i in range(n):
                sum = 0
                for j in range(n):
                    d = i + j
                    if d > n - 1:
                        d = d - n
                    sum = sum + a[d]
                    if sum > max:
                        max = sum
            print(max)
else:
            if (k == -1):
                for i in range(n):
                    sum = 0
                    for j in range(n):
                        d = i + j
                        if d > n - 1:
                            d = d - n
                        sum = sum + a[d]
                        if sum > max:
                            max = sum
                print(max)
