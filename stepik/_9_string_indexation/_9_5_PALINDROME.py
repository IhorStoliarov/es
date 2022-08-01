st = input()

perev_st = st[::-1]
if st == perev_st:
    print('YES')
else:
    print('NO')
