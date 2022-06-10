import random

shut_continue = True
while shut_continue:
    vyb_player = input('Зроби вибір: [R/S/P]. R - камінь, S - ножиці, P - папір').lower()
    if vyb_player not in ['r', 's', 'p']:
        print('Читати вмієш, чи повилазило?')
        continue

# cтворюємо словник для надання "ваги" літерам
    slov = {1: 'r', 2: 's', 3: 'p'}
# генеруємо вибір компа за допомогою random.randint() від 1 до 3
    comp_vybir = slov[random.randint(1, 3)]

# або можна зробити ще простіше
# сomp_vybir = random.chois(['r', 's', 'p'])

# виводимо в консоль вибір компа
    print(f'Я вибрав {comp_vybir}')

# визначаємо переможця за допомогою кортежа. Кожен кортеж матиме 2 елемента.
# тобто перший елемент кортежа перемагає другий
    win_combination = [('p', 'r'), ('r', 's'), ('s', 'p')]
    if vyb_player == comp_vybir:
        print('Нічія')
    elif (vyb_player, comp_vybir) in win_combination:
        print('Ти виграв ')
    else:
        print('Я виграв .!.')
# тепер запитуємо чи хоче зіграти ще раз
    shut_continue = input('Ще раз? [y/n]').lower() == 'y'

