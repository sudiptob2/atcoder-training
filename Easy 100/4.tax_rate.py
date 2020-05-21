import math


# For taking integer inputs.
def inp():
    return(int(input()))


n = inp()
res = ":("
for i in range(1, n+1):
    temp = math.floor(i*1.08)
    if temp == n:
        res = i
print(res)
