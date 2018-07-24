def cat_dog(str):
    ncat = 0
    ndog = 0

    for i, char in enumerate(str):
        if i <= len(str) - 3:
            if 'cat' in str[i:i + 3]:
                ncat += 1
            if 'dog' in str[i:i + 3]:
                ndog += 1

    if ncat == ndog:
        return True
    else:
        return False