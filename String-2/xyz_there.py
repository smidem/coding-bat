def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and 'xyz' in str[i+1:i+4]:
            return True
        if str[0:3] == 'xyz':
            return True
    return False


print(xyz_there('1.xyz.xyz2.xyz'))
print(xyz_there('xyz'))
