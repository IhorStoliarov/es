# іменний кортеж дає можливість іменувати елементи, які він має
# головна задача - робота з незмінними даними, які можна (за допомогою іменованих кортежів) клонувати і змінити
playersHome = [('Olya', 1983, 2890), ('Vova', 2004, 1508), ('Ihor', 1981, 2705)]
print(type(playersHome))
print(playersHome)
print(playersHome[2])

# ми не можемо звернутися (поки що) до якогось одного елементу
# ось такий рядок видасть помилку 'tuple' object has no attribute 'name'
# playersHome[2].name

# для того, щоб можна було звертатись до елементу необхідно імпортувати іменовані кортежі з колекцій
from collections import namedtuple
# і призначаємо змінну з великої літери (як елемент класу)
Player = namedtuple('Player', 'name age rating')
# і створюємо елемент класу з листом
players = [Player('Maman', 1950, 2000), Player('Tanya', 1970, 1700), Player('Muhomor', 1300, 100)]
print(type(players))
print(players)
print(players[1])
# тепер можемо звернутися до будь-якого елементу за індексом
print(players[0].name)
print(players[1].age)
print(players[2].rating)

# так само можемо створювати окремі змінні (без листа)
p1 = Player('OVK', 2010, 1903)
print(type(p1))
print(p1.name)
print(p1.age)
print(p1.rating)
