def make_bricks(small, big, goal):
    make = goal - big * 5 - small <= 0
    if big * 5 > goal:
        make = goal % 5 <= small
    if make:
        return True
    else:
        return False
