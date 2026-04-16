def sum(arr):
    s = 0
    for a in arr:
        s = s + a
    return s


assert sum([1, 3, 6, 2]) == 12


def even(arr):
    t = []
    for a in arr:
        if a % 2 == 0:
            t.append(a)
    return t


assert even([1, 6, 8, 9, -2]) == [6, 8, -2]
