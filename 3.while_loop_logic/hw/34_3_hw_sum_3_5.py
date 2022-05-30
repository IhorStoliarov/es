limit = int(input('Enter number - '))
x = int()
y = int()
for i in range(limit + 1):
    if i % 3 == 0:
        x = i
        i += 1
    elif i % 5 == 0:
        y = i
        i += 1
print(int(x + y))
    