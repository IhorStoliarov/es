dig = input()
flag = 0

for i in dig:
    if '0' <= i <= '9':
        # або i.isdigit()
        flag += 1
        break
    else:
        flag = 0
if flag > 0:
    print('Цифра')
if flag == 0:
    print('Цифр нет')
