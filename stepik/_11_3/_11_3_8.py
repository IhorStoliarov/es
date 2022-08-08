num = int(input())
lst = []
for _ in range(num):
    lst.append(input())
k = int(input())
res = ''
for j in lst:
    if len(j) >= k:
        res += j[k-1]
print(res)
