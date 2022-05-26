# while працює через boolean і виконується допоки змінна є True
x = 0
while x < 3:
    print(f'x = {x}')
    x += 1

# while також може працювати і з ELSE
y = 0
while y < 3:
    print(f'y = {y}')
    y += 1
else:
    print('не входить в діапазон')

# brake - дозволяє вийти з циклу заздалегідь
# continue пропуск і продовження ітерації
# pass - заповнювач для того, щоб нічого не робити
val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0

for v in val:
    if v % 2 == 0:
        continue
    else:
        sum += v
    if sum > 10:
        break
print(sum)





