k, y, v = int(input()), int(input()), int(input())
if k == y == v:
    print('Равносторонний')
elif k == v or y == v or y == k:
    print('Равнобедренный')
else:
    print('Разносторонний')
