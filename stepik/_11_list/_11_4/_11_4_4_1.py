st = [input() for x in range(int(input()))]
st_in = input().lower()
for i in st:
    if st_in in i.lower():
        print(i)
