def count_hi(str):
    hi_count = 0
    for i, char in enumerate(str):
        if i < len(str) - 1 and 'hi' in str[i:i + 2]:
            hi_count += 1
    return hi_count


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))