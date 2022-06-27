a, b, c = int(input()), int(input()), int(input())
sum_all = a + b + c
min_sum = 0
if a and b and c > 0:
    print(sum_all)
if a and b and c < 0:
    print(min_sum)

if a < 0:
    print(b + c)
elif b < 0:
    print(a + c)
elif c < 0:
    print(a + b)
