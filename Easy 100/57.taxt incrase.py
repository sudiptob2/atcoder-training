# For taking space seperated integer variable inputs.
import math


def invr():
    return(map(int, input().split()))


A, B = invr()
res = -1
for i in range(1001):
    if int(i * 0.08) == A and int(i*0.1) == B:
        res = i
        break
print(res)
