n = int(input())

while n > 9:
    s = 0
    while n > 0:
        last_digit = n % 10
        s += last_digit
        n = n // 10
    n = s
print(n)
