zapyt = int(input('Введіть кінцевий діапазон обрахунку. Початок буде з 0 '))
count = 1
while count <= zapyt:
    if count % 2 == 0:
        print(f'{count} ділиться на 2')
        count += 1
    else:
        print(f'{count} не ділиться на 2')
        count += 1
