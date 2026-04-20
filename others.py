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
