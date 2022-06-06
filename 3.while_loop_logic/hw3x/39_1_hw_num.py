import random

zag = random.randint(1, 50)
print(f'Я загадав число від 0 до 50 {zag}. Спробуй відгадай. В тебе 6 спроб')
vid = int(input())
counter = 6

if vid == zag:
    print('Ти виграв')
while True:
    elif vid < zag:
        print('bilshe \n')
        counter = counter - 1
        print(int(input(f'Спроба {counter} - ')))
    elif vid > zag:
        print('menshe \n')
        counter = counter - 1
        print(int(input(f'Спроба {counter} - ')))
    if counter == 1:
        print('Ти використав всі спроби. Най щастить')
        break

#    else:
#        print('You Winner, MFCKR')
