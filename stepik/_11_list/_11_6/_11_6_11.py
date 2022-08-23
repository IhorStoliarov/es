in_str = input().split()

for i in range(len(in_str)):
    in_str[i] = int(in_str[i])

in_str.sort()
print(*in_str)
in_str.sort(reverse=True)
print(*in_str)
