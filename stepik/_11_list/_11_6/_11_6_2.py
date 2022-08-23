lst = [int(i) for i in input().split()]
x = lst.index(min(lst))
y = lst.index(max(lst))
lst[x], lst[y] = max(lst), min(lst)
print(*lst)
