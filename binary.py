def dec2bin(n):
    """Convert a decimal number to binary (array of 1 or 0)"""

    if n == 0:
        return [0]
    if n == 1:
        return [1]

    bin = []

    while True:
        q = n // 2
        r = n % 2
        bin.append(r)
        # print("q=",q,"r=",r)
        n = q
        if q == 0:
            break

    bin.reverse()

    return bin


assert dec2bin(11) == [1, 0, 1, 1]


def comp1(bn):
    """Give the complementary 1"""
    bin = []
    for b in bn:
        if b == 0:
            bin.append(1)
        else:
            bin.append(0)
    return bin


assert comp1(dec2bin(11)) == [0, 1, 0, 0]


def bin2dec(bin):
    """Convert a binary number (array of 1 or 0) to a decimal number"""

    dec = 0
    p = len(bin) - 1
    for b in bin:
        dec = dec + b * 2**p
        p = p - 1

    return dec


assert bin2dec([1, 0, 0, 1, 0, 1]) == 37


def addbin(bin1: list, bin2: list):

    minBin = None
    maxBin = None

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
        minBin.insert(0, 0)

    # print(minBin, maxBin)

    sbin = []
    c = 0  # carry
    i = len(minBin) - 1
    while i >= 0:
        r = minBin[i] + maxBin[i]
        if r == 0:  # les deux bits sont a 0
            if c == 0:
                sbin.append(0)
            else:
                sbin.append(1)
                c = 0  # si on a 0, on garde a carry
        elif r == 1:  # un des deux bits est a 1
            if c == 0:
                sbin.append(1)
            else:
                sbin.append(0)
                # on garde le carry
        else:  # les deux bits sont a 1
            if c == 0:
                sbin.append(0)
                c = 1
            else:
                sbin.append(1)
                # on garde le carry

        i -= 1

    if c == 1:
        sbin.append(1)

    sbin.reverse()

    return sbin


bin1 = [1, 0, 0, 1]
bin2 = [1, 0, 1]
res = addbin(bin1, bin2)
print(bin1, "+", bin2, "=", res)
print(bin2dec(bin1), "+", bin2dec(bin2), "=", bin2dec(res))
