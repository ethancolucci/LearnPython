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
