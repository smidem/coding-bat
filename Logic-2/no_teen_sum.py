def fix_teen(nums):
    zeros = [13, 14, 17, 18, 19]
    nums = [0 if x in zeros else x for x in nums]
    return nums


def no_teen_sum(a, b, c):
    nums = [a, b, c]
    return sum(fix_teen(nums))
