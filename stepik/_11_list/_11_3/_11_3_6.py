first = int(input())
lst = []
for i in range(first):
    sec = int(input())
    lst.append(sec)
del lst[1::2]
print(lst)
