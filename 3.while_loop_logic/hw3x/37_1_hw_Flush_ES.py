# техаський флеш

table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

suites = 'CHSD'
flush = False

# масть карт на столі. Вона завжди вказана як останній елемент в списку
table_suites = [i[-1] for i in table_cards]
# так само і з мастями на руках
hand_suites = [i[-1] for i in hand_cards]
# об'єднуємо два списка з останніх елементів
suites_in_game = table_suites + hand_suites
# далі рішення через comprehension
flush = any([suites_in_game.count(suit) >= 5 for suit in suites])
if flush:
    print('Flush!')
else:
    print('No Flush!')

####
# або через цикл for
flush = False
for suit in suites:
    if suites_in_game.count(suit) >= 5:
        flush = True

if flush:
    print('Flush!')
else:
    print('No Flush!')
