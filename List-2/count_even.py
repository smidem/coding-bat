def count_even(nums):
    evens = [x for x in nums if x % 2 == 0]
    return len(evens)