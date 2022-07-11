city1 = input()
city2 = input()
city3 = input()
lc1 = len(city1)
lc2 = len(city2)
lc3 = len(city3)
if lc1 < lc2 < lc3:
    print(city1)
    print(city3)
elif lc1 < lc3 < lc2:
    print(city1)
    print(city2)
elif lc2 < lc1 < lc3:
    print(city2)
    print(city3)
elif lc2 < lc3 < lc1:
    print(city2)
    print(city1)
elif lc3 < lc2 < lc1:
    print(city3)
    print(city1)
elif lc3 < lc1 < lc2:
    print(city3)
    print(city2)
