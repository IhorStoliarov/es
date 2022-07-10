a = int(input())
if 2 <= a < 6:
    if a % 2 == 0:
        print('NO')
    else:
        print('YES')
elif 6 <= a < 21:
    if a % 2 == 0:
        print('YES')
    else:
        print('NO')
elif a > 20:
    if a % 2 == 0:
        print('NO')
    else:
        print('YES')
else:
    print('YES')