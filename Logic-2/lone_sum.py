def lone_sum(a, b, c):
    nums = [a, b, c]
    y = list()
    if len(set(nums)) < len(nums):
        return sum([x for x in set(nums) if nums.count(x) == 1])
    else:
        return sum(nums)

