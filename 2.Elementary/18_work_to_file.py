# відкрити файл в поточній теці в режимі читання в кодуванні UTF-8!!!
file_ovk = open('../files_hw/ovk_choven.txt', encoding="utf-8")
# виводимо інфу про нього
print(file_ovk)

# вивести вміст файла і закрити його
data = file_ovk.read()
print(data)
#file_ovk.close()
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

up_letters = 0
count_let_in_first_140 = data[0:140]
for i in count_let_in_first_140:
    if i == i.isupper():
        up_letters += 1

print(f'Великих літер у перших 140 символах - {up_letters}')
print(data[0:140])