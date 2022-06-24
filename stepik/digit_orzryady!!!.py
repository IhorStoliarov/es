inp_num = int(input())
od = inp_num % 10
des = (inp_num % 100) // 10
sot = (inp_num % 1000) // 100
tys = inp_num // 1000
print(f'Цифра в позиции тысяч равна {tys}')
print(f'Цифра в позиции сотен равна {sot}')
print(f'Цифра в позиции десятков равна {des}')
print(f'Цифра в позиции единиц равна {od}')
