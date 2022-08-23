st = str(input())
ct = 0
for i in range(len(st)):
    if st[i].isdigit():
        ct += 1
print(ct)
