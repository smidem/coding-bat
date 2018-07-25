import re


def count_code(s):
    return sum([1 for i in range(len(s)-3) if s[i:i+2]=='co' and s[i+3]=='e'])


def count_code2(s):
    return len(re.findall(r'co.e', s))


print(count_code('codexxcode'))
print(count_code('cozexxcope'))
print(count_code('cozfxxcope'))
print(count_code('xxcozeyycop'))
print(count_code('code'))
