num = int(input())
d = ''
while num > 0:
    d = str(num % 2) + d
    num //= 2
print(d)
