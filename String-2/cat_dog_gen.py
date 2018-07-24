def cat_dog(str):
    ncat = 0
    ndog = 0

    for i, char in enumerate(str):
        if i <= len(str) - 3:
            gen = next(str_gen(str, start=i, end=i+3))
            try:
                if 'cat' in gen:
                    ncat += 1
                if 'dog' in gen:
                    ndog += 1
            except StopIteration:
                print('StopIteration occurred')

    if ncat == ndog:
        return True
    else:
        return False


def str_gen(str, start=0, end=0):
    if end:
        yield str[start:end]


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
