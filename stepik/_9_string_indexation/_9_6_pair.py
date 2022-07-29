st = input()
pair = 0

for i in range(len(st)-1):
    if st[i] == st[i + 1]:
        pair += 1
print(pair)

