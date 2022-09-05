def find_all(target, symbol):
    return [j for j in range(len(target)) if target[j] == symbol]


s = input()
char = input()

print(find_all(s, char))
