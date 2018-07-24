def centered_average(nums):
    nums = sorted(nums)
    centered = list()
    for i, x in enumerate(nums):
        if i and i < len(nums) - 1 and nums.count(x) < 3:
            centered += [x]
        elif nums.count(x) >= 3 and centered.count(x) < 2:
            centered += [x]
    return sum(centered)/len(centered)


print(centered_average([5, 3, 4, 0, 100]))
print(centered_average([100, 0, 5, 3, 4]))