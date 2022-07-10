k = int(input())
y = int(input())
v = int(input())
if y < k < v:
    print(k)
elif k < y < v:
    print(y)
elif v < y < k:
    print(y)
elif v < k < y:
    print(k)
else:
    print(v)