#limit=int(input('Enter number - '))
x = int(input())
sum = 0
for i in range(0, x+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
