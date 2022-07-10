color1 = str(input())
color2 = str(input())
er = 'ошибка цвета'

if color1 == 'красный':
    if color2 == 'синий':
        print('фиолетовый')
    elif color2 == 'желтый':
        print('оранжевый')
    elif color2 == 'красный':
        print('красный')
    elif color2 != 'красный' or color2 != 'синий' or color2 != 'желтый':
        print(er)
elif color1 == 'синий':
    if color2 == 'синий':
        print('синий')
    elif color2 == 'желтый':
        print('зеленый')
    elif color2 == 'красный':
        print('фиолетовый')
    elif color2 != 'красный' or color2 != 'синий' or color2 != 'желтый':
        print(er)
elif color1 == 'желтый':
    if color2 == 'красный':
        print('оранжевый')
    elif color2 == 'синий':
        print('зеленый')
    elif color2 == 'желтый':
        print('желтый')
    elif color2 != 'красный' or color2 != 'синий' or color2 != 'желтый':
        print(er)
elif color1 != 'красный' or color1 != 'синий' or color1 != 'желтый':
    print('ошибка цвета')
