# запросити у користувача ліміт в межах якого числа 3 ти 5 діляться без залишку і вивести їх в консоль
limit = int(input('Enter the limit '))
total_sum = 0
for i in range(limit + 1):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i
    else:
        continue
print(f'Total sum {total_sum}')

# та сама задача. Рішення через list Comprehension
total_sum = sum([i for i in range(limit + 1)if i % 3 == 0 or i % 5 == 0])
print(f'Total sum {total_sum}')

