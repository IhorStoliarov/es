st = int(input())
c = 0

for i in range(st):
    stt = input()
    if stt.count('11') >= 3:
        c += 1
print(c)