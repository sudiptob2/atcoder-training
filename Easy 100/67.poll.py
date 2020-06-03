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


N = inp()
count = dict()
while N:
    s = input()
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
    N -= 1
m = max(count.values())
res = []
for key, value in count.items():
    if value == m:
        res.append(key)
res = sorted(res)
for i in res:
    print(i)
