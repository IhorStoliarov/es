#На вход программе подается два натуральных числа aa и bb (a < ba< b).
# Напишите программу, которая находит натуральное число из отрезка [a; \, b][a;b]
# с максимальной суммой делителей.

a, b = int(input()), int(input())
total_maximum = 0
digit = 0

for i in range(a, b + 1):
    maximum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            maximum += j
        if maximum >= total_maximum:
            total_maximum = maximum
            digit = j
print(digit, total_maximum)
