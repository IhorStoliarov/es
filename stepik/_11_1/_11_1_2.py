import string

nm = int(input())
a = string.ascii_lowercase
ps = []
for i in range(nm):
    ps = a[i]
    print(ps, sep=' ', end=' ')

