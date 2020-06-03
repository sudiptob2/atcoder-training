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


r, c = invr()

a = []
for _ in range(r):
    a.append(instr())

for i in range(r):
    h = a[i].count("#")
    if h == 0:
        for j in range(c):
            a[i][j] = "-1"
for i in range(c):
    count = 0
    for j in range(r):
        if a[j][i] == "#":
            count += 1
    if count == 0:
        for j in range(r):
            a[j][i] = "-1"

for i in range(r):
    f = 0
    for j in range(c):
        if a[i][j] != "-1":
            f = 1
            print(a[i][j], end="")
    if f:
        print()
