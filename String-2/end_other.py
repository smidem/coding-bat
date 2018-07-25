def end_other(a, b):
    long = a if len(a) >= len(b) else b
    short = a if len(a) <= len(b) and long != a else b
    return long.lower().endswith(short.lower())


print(end_other('abcXYZ', 'abcDEF'))
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('Z', '12xz'))