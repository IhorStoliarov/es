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
key = players.keys()
print(key)

# конвертування словника в лист
l = list(players1.keys())
print(type(l))
print(l)

# сортування елементів в словнику
sorted(players1.keys())
print(players1.keys())