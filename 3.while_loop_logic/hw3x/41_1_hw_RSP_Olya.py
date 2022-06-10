import random

ver = 0
win = int()
while True:
    player = int(input("1- камінь, 2- ножиці, 3- папір. " "Введіть цифру: "))
    if player == 1 or player == 2 or player == 3:
        ver = 1
    comp = random.randint(1, 3)
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("Нічия!")
    if win == 1:
        print("Ви перемогли!")
    if win == 2:
        print("Переміг комп!!!")
    if player > 3:
        break
