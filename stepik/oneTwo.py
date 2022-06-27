# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a, b, c = int(input()), int(input()), int(input())
min_sum = 0
if a > 0 and b > 0 and c > 0:
    print(a + b + c)
if a < 0 and b < 0 and c < 0:
    print(min_sum)
if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
print(a + b + c)
