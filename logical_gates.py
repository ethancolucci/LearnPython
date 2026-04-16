def f_and(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


assert f_and(0, 0) == 0
assert f_and(1, 0) == 0
assert f_and(0, 1) == 0
assert f_and(1, 1) == 1


def f_or(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


assert f_or(0, 0) == 0
assert f_or(1, 0) == 1
assert f_or(0, 1) == 1
assert f_or(1, 1) == 1
