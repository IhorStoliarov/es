st = input()
gl = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
count_gl = 0
count_sogl = 0

for i in st:
    if i in gl:
        count_gl += 1
    if i in sogl:
        count_sogl += 1
print(f'Количество гласных букв равно {count_gl}')
print(f'Количество согласных букв равно {count_sogl}')
