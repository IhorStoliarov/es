step = int(input()) # крок шифрування
shifr = input() # вхідний шифрований текст
albt = 26 # кількість літер в англ абетці

for i in range(len(shifr)): # робимо цикл по довжині тексту
    de_shifr = ord(shifr[i]) - step # отримуємо код і з таблиці Юнікод із зміщенням step
    if de_shifr < 97: # якщо номер вийшов за межі рядкових літер
        de_shifr += albt # повертаємо його в межі
    print(chr(de_shifr), end='')
