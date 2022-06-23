t = int(input())
god = t // 60
hv = abs(60 - t)
if t % 60 == 0:
    print(f'{t} мин - это {god} час {hv} минут')
elif t < 60:
    print(f'{t} мин - это 0 час {t} минут.')
elif t in range(60, 119):
    print(f'{t} мин - это {god} час {hv} минут.')
