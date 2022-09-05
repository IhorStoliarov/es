n = int(input())


def quick_merge(n):
    return sorted([int(i) for i in range(n) for i in input().split()])


print(*quick_merge(n))
