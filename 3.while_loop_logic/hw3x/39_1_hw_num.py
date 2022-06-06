# Гра відгадай число
import random

zag = random.randint(1, 50)
print(f'Я загадав число від 0 до 50. Спробуй відгадай. В тебе 6 спроб')

counter = 0
while counter < 6:
    vid = int(input('Введи число - '))
    counter += 1

    if vid < zag:
        print('bilshe \n')
    elif vid > zag:
        print('menshe \n')
    elif counter == 1 and vid != zag:
        print('Ти використав всі спроби. Най щастить')
        break
    elif vid == zag:
        print('Ти вгадав!!!')
        break
