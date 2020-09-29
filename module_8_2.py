def upper(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

if __name__ == "__main__":
    str1 = str(input('Введите строку: '))
    n1 = int(input('Введите число n: '))
    print(upper(str1,n1))
