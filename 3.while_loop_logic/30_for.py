# основна задача FOR проходити циклом по колекції елементів
number = [1, 2, 3, 4, 5, 6]
print(number)
for i in number:
    print(i)

# також можна зробити через RANGE з піднесенням в квадрат. При чому другий елемент включається до -1
num = range(1, 6)
print(type(num))
for i in num:
    print(i*i)

# вивести із діапазона всі числа, які діляться на 2
for k in range(1, 10):
    if k % 2 == 0:
        print(f'{k} ділиться на 2')
    else:
        print(f'{k} не ділиться на 2')

# ENUMERATE дозволяє добратися до кожного елементу із збереженням в нову змінну
nim = [1, 3, 5, 7, 9]
for i, item in enumerate(nim):
    nim[i] *= 2
print(nim)

# Так само ітерація можлива не тільки по  інтам, а по будь-яким типам елементів
name = 'Ihor'
for i in name:
    print(i)

# Аналог виводу в консоль повторень одного виразу без додавання тимчасових лічильників типу і
for _ in range(5):
    print('Alarm in the sky!')

# так само можна і з кортежами
pers = ['Olya', 'Lytvyn', 18]
for i in pers:
    print(i)

# named Tuple
persyk = [('Kit', 2), ('Ihor', 41), ('Vova', 19)]
print(len(persyk))
for item in persyk:
    print(item)

# щоб вивести кожний елемент іменованого кортежа  в консоль
# ще це називається unpacking tuples
for (name, age) in persyk:
    print(f'{name} йому(їй) {age} років(ка)')

# For for dict
nn = dict(Olka=18, Ihor=41, Vova=19)
for item in nn:
    print(item)
# щоб отримати набір tuples використовуємо items
for item in nn.items():
    print(item)
# unpacking tuple
for k, v in nn.items():
    print(k, v)

# щоб пройти фором і отримати значення - робимо через VALUES
for v in nn.values():
    print(v)

# задача: знайти всі пари із двох списків, сума яких дорівнює 0. Вкладені списки
list1 = [1, 2, -3, 4, -6, 8]
list2 = [5, -3, 3, 6, -8, 2]

pair = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pair.append((x, y))
print(pair)
