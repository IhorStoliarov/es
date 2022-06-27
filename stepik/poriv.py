inp_num = int(input())
sum_plus = inp_num // 1000 + inp_num % 10
sum_minus = ((inp_num % 1000) // 100)-((inp_num % 100) // 10)
if sum_plus == sum_minus:
    print('ДА')
else:
    print('НЕТ')
