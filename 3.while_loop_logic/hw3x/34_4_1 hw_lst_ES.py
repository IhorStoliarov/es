# Задача. На вході 2 списка. З першого взяти непарні, а з другого парні. І об'єднати їх в одному списку
# Рішення ES
first_lst = [1, 5, 4, 3, 2, 6, 8, 7]
second_lst = [3, 7, 4, 5, 8, 9, 7, 6]

joined_lst = []
for x in first_lst:
    if x % 2 != 0:
        joined_lst.append(x)
for x in second_lst:
    if x % 2 == 0:
        joined_lst.append(x)
print(f'Joined list {joined_lst}')

# Те саме через List Comprehension
first_lst = [1, 2, 3, 4, 5, 6]
second_lst = [11, 12, 13, 14,15]
odds = [x for x in first_lst if x % 2 != 0]
even = [x for x in second_lst if x % 2 == 0]
joined_lst = odds + even
print(f'Joined list {joined_lst}')
