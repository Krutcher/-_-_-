txt = 'Прив3т, к4к д3ла, чт0 дел4ешь?567'
nums = []
nums_sum = 0
for i in txt:
    if i in '1234567890':
        nums.append(int(i))
        nums_sum += int(i)
print('Все цифры в тексте: ', nums,'\nСумма цифр в тексте: ', nums_sum, '\nМаксимальное число в тексте: ', max(nums))
