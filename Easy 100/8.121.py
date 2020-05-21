import math


def invr():
    return(map(str, input().split()))


a, b = invr()
c = int(a+b)

sq = int(math.sqrt(c))

if sq*sq == c:
    print("Yes")
else:
    print("No")
