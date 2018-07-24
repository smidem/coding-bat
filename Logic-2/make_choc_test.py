from make_chocolate import make_chocolate

try:
    assert make_chocolate(4, 1, 9) == 4
    assert make_chocolate(4, 1, 10) == 1
    assert make_chocolate(4, 1, 7) == 2
    assert make_chocolate(6, 2, 7) == 2
    assert make_chocolate(4, 1, 5) == 0
    assert make_chocolate(4, 1, 4) == 4
    assert make_chocolate(5, 4, 9) == 4
    assert make_chocolate(9, 3, 18) == 3
    assert make_chocolate(3, 1, 9) == -1
    assert make_chocolate(1, 2, 7) == -1
    assert make_chocolate(1, 2, 6) == 1
    assert make_chocolate(1, 2, 5) == 0
    assert make_chocolate(6, 1, 10) == 5
    assert make_chocolate(6, 1, 11) == 6
    assert make_chocolate(6, 1, 12) == -1
    assert make_chocolate(6, 1, 13) == -1
    assert make_chocolate(6, 2, 10) == 0
    assert make_chocolate(6, 2, 11) == 1
    assert make_chocolate(6, 2, 12) == 2
    assert make_chocolate(60, 100, 550) == 50
    assert make_chocolate(1000, 1000000, 5000006) == 6
    assert make_chocolate(7, 1, 12) == 7
    assert make_chocolate(7, 1, 13) == -1
    assert make_chocolate(7, 2, 13) == 3
except AssertionError:
    print('you fucked up')
else:
    print('success')
