txt = 'С другой стороны рамки и место обучения кадров способствует подготовки и реализации модели развития'
words = txt.split()
long_word = max(words, key=len)
print('Длина самого длинного слова: ',words.index(long_word) + 1)
