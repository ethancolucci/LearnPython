def AND(a: bool, b: bool) -> bool:
    return a and b


def OR(a: bool, b: bool) -> bool:
    return a or b


def NOT(a: bool) -> bool:
    return not a


def XOR(a: bool, b: bool) -> bool:
    if AND(a, b):
        return False
    return OR(a, b)
    # return AND(OR(a, b), NOT(AND(a, b)))


def halfAdder(a: bool, b: bool) -> tuple[bool, bool]:
    s = XOR(a, b)
    c = AND(a, b)
    return s, c


# def testHalfAdder(a: bool, b: bool, exps: bool, expc: bool):
#     s, c = halfAdder(a, b)
#     assert s == exps and c == expc


# testHalfAdder(False, False, False, False)
# testHalfAdder(False, True, True, False)
# testHalfAdder(True, False, True, False)
# testHalfAdder(True, True, False, True)


def fullAdder(a: bool, b: bool, cin: bool) -> tuple[bool, bool]:
    s1, c1 = halfAdder(a, b)
    s, c2 = halfAdder(s1, cin)
    c = OR(c1, c2)
    return s, c


# def testFullAdder(a: bool, b: bool, cin: bool, exps: bool, expc: bool):
#     s, c = fullAdder(a, b, cin)
#     assert s == exps and c == expc


# testFullAdder(False, False, False, False, False)
# testFullAdder(False, False, True, True, False)
# testFullAdder(False, True, False, True, False)
# testFullAdder(True, False, False, True, False)
# testFullAdder(True, True, False, False, True)
# testFullAdder(True, True, True, True, True)


def adder(bin1: list[bool], bin2: list[bool]) -> list[bool]:
    minBin: list[bool] = None
    maxBin: list[bool] = None

    lens = [len(bin1), len(bin2)]

    if lens[0] <= lens[1]:
        lenDiff = lens[1] - lens[0]
        minBin = bin1.copy()
        maxBin = bin2
    else:
        lenDiff = lens[0] - lens[1]
        minBin = bin2.copy()
        maxBin = bin1

    for _ in range(0, lenDiff):
        minBin.insert(0, False)

    # print(minBin, maxBin)

    sbin: list[bool] = []
    c = False  # carry
    i = len(minBin) - 1
    while i >= 0:
        s1, c1 = fullAdder(maxBin[i], minBin[i], c)
        sbin.append(s1)
        c = c1
        i -= 1

    if c:
        sbin.append(True)

    sbin.reverse()

    return sbin


assert adder([True, False, False], [True]) == [True, False, True]
assert adder([True, False, True], [True]) == [True, True, False]
