inn = int(input())
ls = []
for i in range(1, inn + 1):
    ls.append(input() * i)
print(ls, end='')

# or

#l = []
#for i in range(ord('z') - ord('a') + 1):
#    l.append(chr(ord('a') + i) * (i + 1))
#print(l)