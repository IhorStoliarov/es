# Задача. На вході 2 списка. З першого взяти непарні, а з другого парні. І об'єднати їх в одному списку
# Рішення моє
first_lst = [1, 5, 4, 3, 2, 6, 8, 7]
second_lst = [3, 7, 4, 5, 8, 9, 7, 6]
lst_x = []
lst_y = []
for x in first_lst:
    if x % 2 != 0:
        lst_x.append(x)
for y in second_lst:
    if y % 2 == 0:
        lst_y.append(y)
joined_list = lst_x + lst_y
print(joined_list)
