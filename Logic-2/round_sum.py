def round10(nums):
    return [int(round(x, -1)) for x in nums]


def round_sum(a, b, c):
    return sum(round10([a, b, c]))