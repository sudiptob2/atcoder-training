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


n = inp()

t, a = invr()

H = inlist()
avg = []

for h in H:
    temp = t - h * 0.006
    d = abs(a-temp)
    avg.append(d)
indx = 0
for i in range(n):
    if avg[i] < avg[indx]:
        indx = i
print(indx+1)
