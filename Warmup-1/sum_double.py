def sum_double(a, b):
    return sum([x * 2 if a == b else x for x in [a, b]])


print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))
