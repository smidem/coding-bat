def make_chocolate(small, big, goal):
    if big * 5 > goal and small >= goal - ((goal // 5) * 5):
        return goal - ((goal // 5) * 5)
    elif big * 5 <= goal and goal - big * 5 - small <= 0:
        print('{} - {} = '.format(goal, big * 5) + str(goal - big * 5))
        return goal - big * 5
    else:
        return -1


print(make_chocolate(6, 1, 10))
print(make_chocolate(6, 1, 11))
print(make_chocolate(7, 1, 12))
