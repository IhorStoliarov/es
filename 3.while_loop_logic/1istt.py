# creat mix list

mixed_list = ['w', 2, 'red', 0, 4.03, 3, 'green', 5, 'yellow']

# просто виводимо в консоль список
print(mixed_list)

# виводимо довжину списку (кількість елементів)
print(len(mixed_list))

# друкуємо діапазон списку (з і до)
print(mixed_list[2:5])

# друкуємо діапазон списку (з і до з кроком 2)
print(mixed_list[1:9:2])

# списки, на відміну від рядків можна змінювати
# міняємо друге значення в списку
mixed_list[1] = 'zamina'
print(mixed_list)

# додавання елементу в список
mixed_list.append('dodavannya')
print(mixed_list)

# видалення останнього елементу із списка
vyd = mixed_list.pop()
print(vyd)
print(mixed_list)

# видалення елемента із списка за індексом
vyd_ind = mixed_list.pop(2)
print(vyd_ind)
print(mixed_list)

# сортування списку
int_list = [3, 6, 8, 1, 2.3]
sort1 = int_list.sort()
print(sort1)

# сортування списку за кількістю елементів в рядку
str_list = ['dsa', 'rt', 'ytrw', 'm']
print(str_list)
str_list.sort(key=len)
print(str_list)

# виведення списку в зворотньому напрямку
sort_list_revers = ['asd', 'ytr', 'mn', 'k']
print(sort_list_revers)
sort_list_revers.reverse()
print(sort_list_revers)

# зворотнє сортування списку
fl_list = [1, 4, 2, 8, 5, 7, 9, 6, 3]
print(fl_list)
fl_list.sort(reverse=True)
print(fl_list)

# додавання елемента в список за індексом (спочатку вказуємо елемент Після якого треба вставити,
# а потім, що вставляємо
add_elem_list_index = ['alex', 'bob', 'ebobo']
print(add_elem_list_index)
add_elem_list_index.insert(2, 'kit')
print(add_elem_list_index)

# поверенення індекса по елементу
pover_elem_list_index = [4, 3, 5, 9]
print(pover_elem_list_index)
print(pover_elem_list_index.index(5))

# порахувати кількість входів в список
pover_elem_list_index = [4, 3, 5, 9, 10, 14, 13, 3]
print(pover_elem_list_index)
print(pover_elem_list_index.count(3))

# копіюваяння списку в новий список
cop_list = [4, 2, 6, 1, 8, 3]
print(cop_list)
new_copy = cop_list.copy()
print(new_copy)

# очистити список повністю
new_copy.clear()
print(new_copy)
