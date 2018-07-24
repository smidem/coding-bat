def lucky_sum(a, b, c):
    nums = [a, b, c]
    try:
        lucky = nums.index(13)
    except ValueError:
        lucky = len(nums)
    return sum(nums[:lucky])