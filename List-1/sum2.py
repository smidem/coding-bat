def sum2(nums):
    return sum([x if len(nums) else 0 for x in nums[:2]])
