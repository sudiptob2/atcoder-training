# For taking integer inputs.
import math
import sys


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


def valid(x, y):
    if x >= 0 and x < row and y >= 0 and y < col:
        return True
    return False


fx = [0, 0, 1, -1]
fy = [1, -1, 0, 0]
row, col = invr()

a = []

for _ in range(row):
    a.append(instr())

for i in range(row):
    for j in range(col):

        if a[i][j] == "#":
            can_paint = 0
            for k in range(4):
                nx = i + fx[k]
                ny = j + fy[k]
                if valid(nx, ny) and a[nx][ny] == "#":
                    can_paint = 1
                    break
            if can_paint == 0:
                print("No")
                sys.exit()
print("Yes")
