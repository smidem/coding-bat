import re


def count_code(str):
    count = 0
    for i in range(0, len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count


def count_code2(str):
    return len(re.findall(r'co.e', str))


print(count_code('codexxcode'))
print(count_code('cozexxcope'))
print(count_code('cozfxxcope'))
print(count_code('xxcozeyycop'))
print(count_code('code'))
