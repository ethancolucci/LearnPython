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


def salutation(name):
    print("hey", name)


salutation("ethan")


def ce2fa(c):
    return c * 9 / 5 + 32


assert ce2fa(100) == 212


# ecrire la fonction comptvoy
# elle recoit un parametre qui est une chaine "ch" (pour chaine)
# elle retour un entier qui est le nombre de voyelle
# incrementer nbv (nombre de voyelles) a chaque fois qu'une lettre
# est soit : a, e, i...
VOYELLES = "aeiouyAEIOUY"


def isvoy(c: chr):
    return c.isalpha() and c in VOYELLES


def iscons(c: chr):
    return c.isalpha() and c not in VOYELLES


def comptvoy(ch: str):
    V = 0
    for c in ch:
        if isvoy(c):
            V += 1
    return V


assert comptvoy("coucou") == 4
assert comptvoy("HELLO") == 2

# for c in "hello":
#     print("c=", c)

# print("hello" in "hello everybody!")


def comptc(ch: str):
    V = 0
    for c in ch:
        if iscons(c):
            V += 1
    return V


assert comptc("hello guys") == 5

# name = input("what is your name? ")
# print("hello", name)


from random import randint


def guessnumber(max=20):
    n = randint(1, max)
    nbTurns = 1
    while True:
        p = "guess my number between 1 and " + str(max) + ": "
        r = int(input(p))
        if r < 1 or r > max:
            print("the number must be between 1 and", max)
            continue
        if r == n:
            print("GG,you won in", nbTurns, "turns")
            break
        else:
            if r < n:
                print("higher!")
            else:
                print("lower")
            nbTurns += 1


# guessnumber()


def rockPaperScissors():
    # row=us,col=player
    # order is rock (0), paper (1), scissors (2)
    # 0=same,-1=weaker,+1=stronger
    # e.g. us=paper,player=rock => mat[1][0]
    results = [[0, -1, +1], [+1, 0, -1], [-1, +1, 0]]
    scores = [0, 0]  # our score first
    while True:
        o = randint(0, 2)  # 2
        p = input(">> Rock, paper or scissors ? (r, p or s) ")
        p = p[0].lower()  # r
        if p not in "rps":
            print("\nBad choice, try again!\n")
            continue
        i = "rps".index(p)  # 0
        ourResult = results[o][i]  # -1
        print("We played", "Rock" if o == 0 else "Paper" if o == 1 else "Scissors")
        if ourResult == 0:
            print("Draw")
        elif ourResult == +1:
            print("We won! :-)")
            scores[0] += 1
        else:
            print("We lost :-(")
            scores[1] += 1

        print("We have", scores[0], "pts", "\t", "You have", scores[1], "pts")

        q = input(">> Stop the game? (y/[n]) ") or "n"
        if q[0].lower() == "y":
            break
        print("\n")


rockPaperScissors()
