s = str(input())
count = 0
for i in range(len(s)):
    if s[i] != s[i].upper():
        count += 1
print(count)
