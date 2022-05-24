# різниця поміж кортежами і листами полягає в тому, що в кортежах неможна змінити елементи
person = ('Olya', 'Vova', 18)
print(type(person))
print(person)

# а от цей рядок не виконається і вижасть помилку TypeError: 'tuple' object does not support item assignment
#person[1] = ('Olya', 'Vovi', 18)

# звичайний приклад листа. Тут працює все гаразд
person_list = ['Olya', 'Vovi', 22]
person_list[1] = 'Vova'
print(type(person_list))
print(person_list)

# Як і скрізь ми можемо використовувати LEN
print(len(person))

# так само і за індексом
print(person[0])
print(person[-1])

# кількість входів теж в кортежах працює
print(person.count('Vova'))

