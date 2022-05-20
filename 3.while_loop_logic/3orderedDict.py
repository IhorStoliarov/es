# звичайні словникам все одно як розташовані пари ключ/значення
# в ordered це має значення

# оголошумо три словника
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

print(d1 == d2)
print(d1 == d3)

for k, v in d1.items():
    print(k, v)

# після версії пітона 3.7 для перевірки словників на ідентичність використовується OrderedDict
# це порівнює повну ідентичність словника, включаючи розташування пар ключ/значення
from collections import OrderedDict

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = OrderedDict()
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

print(d1 == d2)
print(d1 == d3)

# з точки зору OrderedDict словники є однаковими у випадку не тільки однакових даних, а й у випадку ідентичного
# розташування пар
