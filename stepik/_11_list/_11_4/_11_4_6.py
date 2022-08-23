in_num = int(input())
lst = [int(input()) for i in range(in_num)]
[print(i) for i in lst if i < 0]
[print(i) for i in lst if i == 0]
[print(i) for i in lst if i > 0]
