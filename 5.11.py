def func(x1,x2):
    """Вычисляет индекс массы тела по введенным массе и росту человека"""
    return (x1/((x2)**2))

a1, a2 = map(float, input('Введите  массу в килограммах и рост в метрах(например 1.80): ').split( ))
BMI = func(a1, a2)

if BMI < 16:
    print(BMI)
    print('Выраженный дефицит массы тела')
elif 16 <= BMI <18.5:
    print(round(BMI,2))
    print('Недостаточная масса тела')
    
elif 18.5 <= BMI < 25:
    print(round(BMI,2))
    print('Нормальная масса тела')
elif 25 <= BMI < 30:
    print(round(BMI,2))
    print('Предожирение')
elif 30 <= BMI < 35:
    print(round(BMI,2))
    print('Ожирение первой степени')
elif 35 <= BMI < 40:
    print(round(BMI,2))
    print('Ожирение второй степени')
elif BMI >= 40:
    print(round(BMI,2))
    print('Ожирение третьей степени')
