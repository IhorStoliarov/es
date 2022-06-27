# Геометрична прогресія

a = int(input())
b = int(input())
c = int(input())
d = (b - a) + b
e = (b + a) - b
if a < b < d:
    if c == d:
        print('YES')
    else:
        print('NO')
elif a > b > c:
    if a == e:
        print('YES')
    else:
        print('NO')
