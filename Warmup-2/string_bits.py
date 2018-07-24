def string_bits(str):
    return ''.join([str[i] for i, char in enumerate(str) if i % 2 == 0])
