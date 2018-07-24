def caught_speeding(speed, is_birthday):
    speed -= 5 if is_birthday else 0
    return 0 if speed <= 60 else 1 if 61 <= speed <= 80 else 2


print(caught_speeding(60, False))
