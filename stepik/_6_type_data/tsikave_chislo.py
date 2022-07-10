num = int(input())
sot = (num % 1000) // 100
des = (num % 100) // 10
od = num % 10
if des == abs(sot - od) or des == abs(sot + od):
    print('Число интересное')
else:
    print('Число неинтересное')