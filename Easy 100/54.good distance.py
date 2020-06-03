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


N, D = invr()
X = []

for i in range(N):
    X.append(inlist())
c = 0
for i in range(N):
    for j in range(i+1, N):
        dis = 0
        y = X[i]
        z = X[j]
        for d in range(D):
            dis += (y[d] - z[d])**2
        dis = math.sqrt(dis)
        if dis == math.floor(dis):
            c += 1
print(c)
