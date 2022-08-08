n = int(input())
print([i for i in range(1, n // 2 + 1) if n % i == 0] + [n])

# or

#n = int(input())
#a = []
#for i in range(1, n + 1):
#    if n % i == 0:
#        a.append(i)
#print(a)

