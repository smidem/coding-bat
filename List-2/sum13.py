def sum13(nums):
    new = list()
    for i, num in enumerate(nums):
        if ((i and 13 not in nums[i-1:i+1] and num != 13)
            or (not i and num != 13)
        ):
            new += [num]
    return sum(new)


print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([13]))
print(sum13([13, 1, 13]))
