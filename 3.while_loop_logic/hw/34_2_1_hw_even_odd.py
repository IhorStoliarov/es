# Вивести числа і позначити чи діляться вони на 2
lim = int(input('Введіть ліміт '))
for i in range(lim +1):
    if i % 2 == 0:
        print(f'{i} чотне')
    else:
        print(f'{i} не чотне')
