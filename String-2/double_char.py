def double_char(str):
    new_str = ''
    for char in str:
        new_str += char * 2
    return new_str


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))