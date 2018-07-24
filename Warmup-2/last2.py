def last2(str):
    return len([1 for i in range(len(str)-2) if str[i:i+2] == str[-2:]])
