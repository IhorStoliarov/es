# Найголовніше те, що SET може містити тільки унікальні елементи. Всі інші подібні перезаписуються
# елементи в сеті не сортуються
my_set = set()
print(type(my_set))
print(set)

# додаємо елементи в set
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(3)
print(my_set)
my_set.add(1)
print(my_set)

# створимо лист для порівняння
my_list = [1, 1, 1, 1, 2, 2, 3, 4, 4, 5]
my2_set = set(my_list)
print(my2_set)
print(len(my2_set))
# як бачимо всі продубльовані елементи вилучені

# для того, щоб перевірити кількість входів (count) в змінну пишемо IN. Повертає булєн
print(2 in my2_set)
print(6 in my2_set)

# один сет може бути підмножиною другого сету. Тобто містити в собі всі елементи другого сету
# при порівнянні їх отримуємо або True або False
# порівняння відбувається за допомогою ISSUBSET
set_ihor1 = {1, 2, 3, 4}
set_ihor2 = {1, 2, 3, 4, 5}
print(set_ihor1.issubset(set_ihor2))


# додамо трохи перевірки на логіку та розгалудження
set_ihor3 = {1, 2, 3, 4, 8}
set_ihor4 = {1, 2, 3, 4, 5}
if set_ihor3.issubset(set_ihor4) == True:
    print('set3 повністю входить в сет 4')
else:
    print('не входить')

# перевірка на те, який сет головніший = ISSPERSET
set_ihor5 = {1, 2, 3, 4}
set_ihor6 = {1, 2, 3, 4, 5}
if set_ihor6.issuperset(set_ihor5) == True:
    print('сет 6 э суперсетом (більшим) ніж сет5')
else:
    print('сет 5 э суперсетом (більшим) ніж сет6')

# перевірка сетів на схожість між собою. Тобто на однаковість елементів. Робиться ISDISJOINT
# якщо всі елементи різні - видає True
set_ihor7 = {1, 2, 3}
set_ihor8 = {4, 5, 6}
print(set_ihor8.isdisjoint(set_ihor7))

# об'єднання (union)  сетів робиться через UNION. Робиться через новий сет
set_ihor9 = {1, 2, 3, 4, 5}
set_ihor10 = {4, 5, 6}
set_ihor11 = set_ihor9.union(set_ihor10)
print(set_ihor11)
print("це об'єднані cети " + str(set_ihor11))

# перетин двох множин сетів повертає ОДНАКОВІ елементи сетів. робиться через INTERSECTION
set_ihor12 = {1, 2, 3, 4, 5}
set_ihor13 = {3, 4, 5, 6, 7}
set_ihor14 = set_ihor12.intersection(set_ihor11)
print(set_ihor14)

# зворотній INTERSECTION є метод DIFFERENСE. повертає в новий сет РІЗНИЦЮ між cуперсетом і сетом
set_ihor15 = {1, 2, 3, 4}
set_ihor16 = {3, 4, 5, 6}
set_ihor17 = set_ihor16.difference(set_ihor15)
print(set_ihor17)

# SYMMETRIC_DIFFERENCE повертає абсолютну різницю між ДВОМА сетами. Бере із лівого сета відсутні елементи які є в
# правому і навпаки
set_ihor18 = {1, 2, 7, 6}
set_ihor19 = {1, 3, 5, 6}
set_ihor20 = set_ihor19.symmetric_difference(set_ihor18)
print(set_ihor20)

# Об'єднання сетів без створення нового. Робиться через UPDATE
set_ihor21 = {0, 1, 2, 3}
set_ihor22 = {2, 3, 4, 5}
set_ihor21.update(set_ihor22)
print(set_ihor21)

# видалення елементів з сету. Робиться через REMOVE, DISCARD, POP. При намаганні видалити неіснуючий елемент
# методом REMOVE вивалиться помилка
# remove
set_ihor23 = {0, 1, 2, 3, 4}
print(set_ihor23)
set_ihor23.remove(2)
print(set_ihor23)

# DISCARD дозволяє видаляти неіснуючий елемент без вивалення помилки
print(set_ihor23)
set_ihor23.discard(43)
print(set_ihor23)
set_ihor23.discard(3)
print(set_ihor23)

# видалення ВИПАДКОВОГО елементу за допомогою POP. При чому метод його повертає при виводі в термінал
print(set_ihor13)
popped = set_ihor13.pop()
print(popped)

# почистити сет можна за допомогою CLEAR
print(set_ihor12)
set_ihor12.clear()
print(set_ihor12)
