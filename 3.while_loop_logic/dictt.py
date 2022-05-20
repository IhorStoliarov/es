# dictionary - лист пар "ключ - значення". Як приклад "книга контактів в телефоні"
# Головний сенс його - швидкий пошук значення по ключу!

# стоворення словника
players = {
    'Olya': 3481,
    'Vova': 2931,
    'Ihor': 1331
}
print(players)

# або ще варіант
players1 = dict(Tanya=4313, Yulya=8843, Evgen=1087)
print(players1)

# витягнути елемент зі словника
vytag = players['Olya']
print(f"топовим гравцем є {vytag}")

# або
print(players.get("Olya"))

# додавання елемента в словник або його заміна
players['Nit'] = 4921
print(players)

# видалення елементу зі словника
del players['Nit']
print(players)

# перегляд ключів словника
keys = players.keys()
print(keys)

# конвертування словника в лист
l = list(players.keys())
print(type(l))
print(l)

# сортування елементів в словнику. На виході отримуємо відсортований список
sorted(players.keys())
print(sorted(players.keys()))

# перевірка чи існує/не існує ключ в словнику (виводить True)
print('Olya' in players)
print('Olka' not in players)

# перевірка ЗНАЧЕННЯ в словнику
val = players.values()
print(val)

# конвертування словника в список і вивід значення
vall = list(players.values())
print(type(vall))
print(vall)

# зробити копію листа
playersCopy = players1.copy()
print(playersCopy)

# пройти циклом for  по словнику і вивести ключ/значення
for k, v in players1.items():
    print(k, v)

# видалити ключ та значення із словника
playersCopy.pop('Yulya')
print(playersCopy)

# додавання ключа в словник із ключем None
playersCopy.setdefault('Ira')
print(playersCopy)

# словник не дозволяє зробити два однакових ключа з однаковими значеннями!!!
