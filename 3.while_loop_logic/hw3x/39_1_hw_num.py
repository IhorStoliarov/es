import random

zag = random.randint(1, 50)
print(f'Я загадав число від 0 до 50 {zag}. Спробуй відгадай. В тебе 6 спроб')
vid = int(input('Спроба 6 - '))
counter = 6
tmp = int()
if vid == zag:
    print('Ти виграв')
while vid != zag or counter <= 1:

    if counter == 1:
        print('Ти використав всі спроби. Най щастить')
        break
    elif vid > zag:
        print('menshe \n')
        vid = vid // zag
        counter = counter -1
        print(int(input(f'Спроба {counter} - ')))
    elif vid < zag:
        print('bilshe \n')
        tmp = vid// zag
        counter = counter - 1
        print(int(input(f'Спроба {counter} - ')))
