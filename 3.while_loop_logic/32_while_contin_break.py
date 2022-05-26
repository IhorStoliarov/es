# while працює через boolean і виконується допоки змінна є True
x = 0
while x < 3:
    print(f'x = {x}')
    x += 1

# while також може працювати і з ELSE
y = 0
while y < 3:
    print(f'y = {y}')
    y += 1
else:
    print('не входить в діапазон')
