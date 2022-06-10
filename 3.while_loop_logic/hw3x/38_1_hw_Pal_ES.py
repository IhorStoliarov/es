# Задача на виявлення паліндрома
numb = int(input('Введи чило - '))
# робимо реверс числа
revers_numb = 0
# кожне число з введеного інпуту зберігаємо в тимчасову змінну
tmp_numb = numb
# на кожній ітерації циклу нам необхідно позбавлятися розряд числа
# і додавати його до revers_numb за допомогою множення на 10 і будемо
# це робити допоки число не буде = 0
while tmp_numb > 0:
    revers_numb = (revers_numb * 10) + tmp_numb % 10
    tmp_numb = tmp_numb // 10
    # або tmp_numb = int(tmp_numb / 10)
if numb == revers_numb:
    print('Palindrome')
else:
    print('No palindrome')
