def array123(nums):
    return {1, 2, 3} == set(nums) or {1, 2, 3} in set(nums)


print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
print(array123([1, 2, 3, 1, 2, 3]))
print(array123([1, 2, 3]))