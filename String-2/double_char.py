def double_char(str):
    return ''.join([char * 2 for char in str])


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))