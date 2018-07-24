def make_bricks(small, big, goal):
    return goal % 5 <= small if big * 5 > goal else goal - big * 5 - small <= 0
