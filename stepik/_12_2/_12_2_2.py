l = input().split()
m = input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))
