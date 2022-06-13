# Знайти вагу карт
# Моє рішення
current_hand = ['A', 5, 4, 10, 'Q', 'K']
weight1 = [2, 3, 4, 5, 6]
weight0 = [7, 8, 9]
weight_1 = [10, 'J', 'Q', 'K', 'A']
cards_sum = []
for i in current_hand:
    if i == i in weight1:
        cards_sum.append(1)
        print('додаємо 1')
    elif i == i in weight0:
        cards_sum.append(0)
        print('додаємо 0')
    elif i == i in weight_1:
        cards_sum.append(-1)
        print('віднімаємо 1')
cards_sum = sum(cards_sum)
print(cards_sum)
