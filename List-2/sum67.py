def sum67(nums):
    count = 0
    skip = False
    for x in nums:
        if x == 6:
            skip = True
        elif x == 7 and skip:
            skip = False
        elif not skip:
            count += x
    return count


print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
