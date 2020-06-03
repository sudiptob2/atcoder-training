# For taking integer inputs.
import math
from decimal import Decimal
from itertools import permutations


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


def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


N = inp()
points = []
p = []
for i in range(N):
    p.append(i)
    points.append(inlist())
D = [[0 for i in range(N)] for j in range(100)]
c = 0
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        #print("p ", points[i], points[j])
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        D[i][j] = d
        D[j][i] = d
# print(D)
permut = list(permutations(p))

res = 0
for pt in permut:
    for i in range(N-1):
        res += D[pt[i]][pt[i+1]]
print(res / fact(N))
