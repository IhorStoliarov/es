in_num = int(input())
lst = []

for i in range(in_num):
    sec = int(input())
    lst.append(sec)
lst.remove(min(lst))
lst.remove(max(lst))
print(*lst, sep='\n')
