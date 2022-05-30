limit = int(input('Enter number - '))
x = int()
y = int()
for i in range(0, limit + 1):
    if i % 3 == 0:
        x += i
        print(int(x))
    elif i % 5 == 0:
        y += i
        print(int(y))
print(int(x + y))
    