# For taking integer inputs.
import math


def inp():
    return(int(input()))


# For taking List inputs.
def inlist():
    return(list(map(int, input().split())))


# For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
def instr():
    s = input()
    return(list(s[:len(s)]))


# For taking space seperated integer variable inputs.
def invr():
    return(map(int, input().split()))


Q, H, S, D = invr()
N = inp()

Q1 = Q / 0.25
H1 = H / 0.5
S1 = S / 1
D1 = D / 2

m = min(Q1, H1, S1, D1)
res = 0
if m == D1 and N > 1:
    t1 = (N - (N % 2)) * D1
    t2 = (N % 2) * min(Q1, H1, S1)
    res = t1 + t2
elif N == 1:
    res = N * min(Q1, H1, S1)
else:
    res = N * m
print(int(res))
