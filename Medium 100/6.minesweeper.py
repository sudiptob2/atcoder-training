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


def valid(x, y): return True if x >= 0 and x < row and y >= 0 and y < col else False


fx = [+0, +0, +1, -1, -1, +1, -1, +1]
fy = [-1, +1, +0, +0, +1, +1, -1, -1]
row, col = invr()
mat = []
for _ in range(row):
    mat.append(instr())

for i in range(row):
    for j in range(col):
        if mat[i][j] == ".":
            count = 0
            for k in range(len(fx)):
                nx = i + fx[k]
                ny = j + fy[k]
                if valid(nx, ny):
                    if mat[nx][ny] == "#":
                        count += 1
            mat[i][j] = str(count)

for r in mat:
    for i in r:
        print(i, end="")
    print()
