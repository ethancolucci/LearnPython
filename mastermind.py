# https://gist.github.com/rxaviers/7360908

# colors= R,B,G,Y,O (red,blue,green,yellow and orange)

# ⚪ = good and good place
# ⚫ = good but not at the good place
# 🔴 = not good at all

# ucomb="BRYGR" scomb="RRBGO" res="⚫⚪🔴⚪⚫"


def validateLine(ucomb: str, scomb: str) -> str:
    res = ""

    for i in range(0, len(ucomb)):
        u = ucomb[i]
        s = scomb[i]
        # print(i, u, s)
        if u == s:
            res += "⚪"
        elif u in scomb:
            res += "⚫"
        else:
            res += "🔴"

    return res


print(validateLine("ORBRY", "RRBGO"))

assert validateLine("BRYGR", "RRBGO") == "⚫⚪🔴⚪⚫"
assert validateLine("YRBRG", "RRBGO") == "🔴⚪⚪⚫⚫"


def isCombValid(comb: str) -> bool:
    for n in comb:
        if n != "⚪":
            return False
    return True


assert isCombValid("🔴⚪⚪⚫⚫") == False
assert isCombValid("⚪⚪⚪⚪⚪") == True
