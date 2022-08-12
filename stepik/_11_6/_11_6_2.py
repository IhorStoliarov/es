in_str = [3, 4, 5, 2, 1]
ma = in_str.pop(max(in_str))

mi = min(in_str)
in_str[0] = ma
in_str[-1] = mi
print(*in_str)