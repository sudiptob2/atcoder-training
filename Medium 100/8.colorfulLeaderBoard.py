def inp():
    return(int(input()))


def invr():
    return(map(int, input().split()))


n = inp()

ratings = invr()

flags = [0]*8
c = 0
a = 0
for r in ratings:
    if r >= 1 and r < 400 and flags[0] == 0:
        c += 1
        flags[0] = 1
    if r >= 400 and r < 800 and flags[1] == 0:
        c += 1
        flags[1] = 1
    if r >= 800 and r < 1200 and flags[2] == 0:
        c += 1
        flags[2] = 1
    if r >= 1200 and r < 1600 and flags[3] == 0:
        c += 1
        flags[3] = 1
    if r >= 1600 and r < 2000 and flags[4] == 0:
        c += 1
        flags[4] = 1
    if r >= 2000 and r < 2400 and flags[5] == 0:

        c += 1
        flags[5] = 1
    if r >= 2400 and r < 2800 and flags[6] == 0:
        c += 1
        flags[6] = 1
    if r >= 2800 and r < 3200 and flags[7] == 0:
        c += 1
        flags[7] = 1
    if r >= 3200:
        a += 1
if c == 0:
    print(1, a)
else:
    print(c, c+a)
