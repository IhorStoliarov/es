# дізнатись кількість елементів
st = 'будь який текст сюди тулимо'
print(len(st))

# дізнатися кількість входів в рядок якогось символу COUNT
st_long = 'Rozbyrayus z Funktsiyamy Ryadkiv'
print(len(st_long))
print(st_long.count('a'))

# лишити тільки першу Велику літеру, всі інші малі
print(st_long.capitalize())

# все великими UPPER
print(st_long.upper())

# все малими LOWER
print(st_long.lower())

# перевірити, чи всі літери велики чи малі
print(st_long)
st_long_upper = st_long.upper()
print(st_long_upper)
print(st_long_upper.isupper())

print(st_long)
st_long_lower = st_long.lower()
print(st_long_lower)
print(st_long_lower.islower())

# повернути індекс за символом
print(st_long.find('k', 0, 26))

# перевірити чи складається рядок виключно зі слів та літер
print('123sdf'.isalnum())
print('123asd.'.isalnum())

# перевірка символів до літер
print('qewrqewr'.isalpha())

# перевірка рядка на цифри
print('123'.isdigit())

# перевірка на пробіли в рядку. Якщо присутні пробіли поверне TRUE
print(' '.isspace())
# якщо рядок реально порожній
print(''.isspace())

# видаленняна початку та вкінці рядка пробілів.
strk = ' sdfseqg ! '
print(strk)
print(strk.strip(' '))

# перевірка рядка на порожність
print(' '.strip() == '')

# ще перевірка на порожність за допомогою NOT
empty = ' '
if not empty:
    print('not space')
else:
    print('space')

# перевірка рядка на наявність певних символів на початку та в кінці startswith та endswith
h = 'ne vystachae monitora'
print(h.startswith('ne'))
print(h.endswith('a'))

# прибрати певні символи з рядка
sdf = '12; 5; 3; 2; 7; 8'
print(type(sdf))
print(sdf)
print(sdf.split(';'))
