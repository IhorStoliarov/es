num1 = int(input())
num2 = int(input())
st = str(input())
if num2 == 0 and st == '/':
    print('На ноль делить нельзя!')
elif st == '*':
    print(num1 * num2)
elif st == '/':
    print(num1 / num2)
elif st == '-':
    print(num1 - num2)
elif st == '+':
    print(num1 + num2)
elif st != '-' or st != '+' or st != '/' or st != '*':
    print('Неверная операция')
