# відкрити файл в поточній теці в режимі читання в кодуванні UTF-8!!!
file_ovk = open('../files_hw/ovk_choven.txt', encoding="utf-8")
# виводимо інфу про нього
print(file_ovk)

# вивести вміст файла і закрити його
data = file_ovk.read()
print(data)
# file_ovk.close()
print("\n")

# виводимо довжину (кількість символів) в data
print(f'Всього символів в файлі - {len(data)}')

# рахуємо кількість "входжень" літери а в файлі. При чому а (укр) і a (англ) - різні символи
count_a = data.count('а')
count_A = data.count('А')
count_space = data.count(' ')
print(f'Маленьких літер "a" - {count_a}')
print(f'Великих літер "A" - {count_A}')
print(f'Пробілів - {count_space}')

space_data_0_80 = 0
for i in data[0:80]:
    if i == ' ':
        space_data_0_80 += 1
print(f'Пробілів у перших 80 символах - {space_data_0_80}')

print('\n')

# повертаємо коретку в положення 0.
file_ovk.seek(0)

up_word = 0
print(data[0:140])
first140_in_data = data[0:140].split()
for x in first140_in_data:
    if x == x.capitalize():
        up_word += 1
        print(x)
print(f'Слів, які починаються з великих літер у перших 140 символах - {up_word}')

print('\n')

# Прибираємо пробіли
rep_space = str(data[0:110])
print(rep_space)
print('\nПрибираємо пробіли\n')
rep = rep_space.replace(' ', '')
print(rep)

print('\n')

# Реверсуємо рядок
print('Реверс рядка')
rev = str(data[0:30])
print(rev)
rev_ers = rev[::-1]
print(rev_ers)

print('\n')

# Ще один приклад
print('ще один приклад реверсу через функцію\n')


def reversed_string(text):
    result = ""
    for char in text:
        result = char + result
    return result


print(reversed_string(rev))
