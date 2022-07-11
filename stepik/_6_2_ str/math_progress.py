u = len(str(input()))
k = len(str(input()))
r = len(str(input()))
len_min = min(u, k, r)
len_max = max(u, k, r)
len_sr = (u + k + r) - (len_max + len_min)
if (len_max - len_sr) == (len_sr - len_min):
    print('YES')
else:
    print('NO')