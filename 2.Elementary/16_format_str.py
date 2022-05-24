# вставлення елементів в рядок. Скільки буде плейсхолдерів ({}) стільки і має бути замінників
sw = 'Ihor'
sq = 'python'
print('my name is {} and i`m learning {}'.format(sw, sq))

# скорочення розрядів до двох після крапки
pi = 3.1415
print('Number Pi = {pi:1.2f}'.format(pi=pi))
# .2f це - флоат, з округленням до двох знаків після крапки

# більш скорочений синтаксис першого прикладу
print(f'Мене звуть {sw} і я вивчаю {sq}')

# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html