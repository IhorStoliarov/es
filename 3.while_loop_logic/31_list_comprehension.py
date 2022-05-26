# List Comprehension - дозволяє ініціалізувати списки
greet = 'hello, world'
chars = []
for l in greet:
    chars.append(l)
print(chars)
# ініціалізуємо список (скорочений запис)!!!!!
chars = [l for l in greet]
print(chars)

# ще приклад
ch = [x for x in range(1, 11)]
print(ch)

# ще один
cha = [i for i in 'vsyaka hrin']
print(cha)
print(cha.count('a'))

# квадрати чисел
kv = [n*n for n in range(1, 11)]
print(kv)

# вивести квадрати непарних чисел в межах 0-10
kvn = [n*n for n in range(0, 11) if n % 2 != 0]
print(kvn)

# переводимо сантиметри в дюйми із листа
len_in_cm = [12, 15, 6, 99, 122, 34]
print(len_in_cm)
len_in_inch = [(round(cm / 2.54, 2))for cm in len_in_cm]
print(len_in_inch)

# в list comprehension можна вставляти конструкції з if/else
js = [75, 55, 90, 120, 280, 190, 300]
master = ['MG' if x > 110 else 'MS' for x in js]
print(master)

# знайти пари з двох листів які дорівнюють 0
list1 = [1, 4, -2, 5, -3, 7, -6]
list2 = [2, 6, 1, 3, -4, 3, -5]
pair = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pair.append((x, y))
print(pair)

# тепер те саме тільки через List Comprehension
pair = [(x, y) for x in list1 for y in list2 if x + y == 0]
print(pair)
