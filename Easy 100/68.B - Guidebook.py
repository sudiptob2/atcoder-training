def inp():
    return(int(input()))


def invr():
    return(map(str, input().split()))


N = inp()
pos = [0] * 101
SP = dict()
for i in range(1, N+1):
    key, val = invr()
    val = int(val)
    if key in SP:
        temparr = SP[key]
        temparr.append(val)
        SP[key] = temparr
    else:
        SP[key] = [val]
    pos[val] = i

names = sorted(SP)

for key in names:
    values = SP[key]
    values = sorted(values, reverse=True)
    for i in values:

        print(pos[i])
