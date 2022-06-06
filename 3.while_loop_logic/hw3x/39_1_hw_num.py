# Гра відгадай число
import random

zag = random.randint(1, 50)
print(f'Я загадав число від 1 до 50. Спробуй відгадай. В тебе 6 спроб')

counter = 0
while counter < 6:
    vid = int(input('Введи число - '))
    counter += 1

    if vid < zag:
        print('bilshe \n')
    if vid > zag:
        print('menshe \n')
    if vid == zag:
        print('Ти вгадав!!!')
        break
    if vid != zag and counter == 6:
        print('Ти використав всі спроби. Най щастить')
        break

