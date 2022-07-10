num = int(input())

if num == 0:
    print('зеленый')
elif num <= 0 or num >= 37:
    print('ошибка ввода')
elif 1 <= num < 37:
    if num in range(1, 11):
        if num % 2 != 0:
            print('красный')
        else:
            print('черный')
    elif num in range(11, 19):
        if num % 2 != 0:
            print('черный')
        else:
            print('красный')
    elif num in range(19, 29):
        if num % 2 != 0:
            print('красный')
        else:
            print('черный')
    elif num in range(29, 37):
        if num % 2 != 0:
            print('черный')
        else:
            print('красный')