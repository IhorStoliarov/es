data = 'Background Intelligent Transfer Service'
count = 0
print(data)
data = data.split()
for i in data:
    if i == i.capitalize():
        count += 1
print(f'Upper = {count}')
