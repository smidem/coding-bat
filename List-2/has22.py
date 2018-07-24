def has22(nums):
    for i, x in enumerate(nums):
        if i and [2, 2] == nums[i-1:i+1]:
            return True
    return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
