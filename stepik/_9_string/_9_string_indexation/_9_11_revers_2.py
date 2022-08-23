st_in = input()
ln = len(st_in)
c = ln // 2 + ln % 2
print(st_in[c:] + st_in[:c])
