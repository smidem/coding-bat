def end_other(a, b):
    min_len = min(len(a), len(b))
    small = str()
    big = str()
    if len(a) == min_len:
        small = a.lower()
        big = b.lower()
    else:
        small = b.lower()
        big = a.lower()
    i = len(big) - min_len
    if big[i:] == small:
        return True
    else:
        return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('Z', '12xz'))