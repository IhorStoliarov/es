a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
a3 = max(a1, a2)
b3 = min(b1, b2)
if a3 < b3:
    print(a3, b3)
elif a3 == b3:
    print(a3)
else:
    print('пустое множество')