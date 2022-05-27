limit = int(input('Enter number - '))
x = int()
y = int()
for i in range(0, limit):
    if i / 3 == 0:
        x = i
        i += 1
        print(f'{x} / 3')
    elif i / 5 == 0:
        y = i
        print(f'{y} / 5')
        i += 1
print(x + y)
    