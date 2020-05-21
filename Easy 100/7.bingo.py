def inlt():
    return(list(map(int, input().split())))


def inp():
    return(int(input()))


A = []
for t in range(3):
    A.append(inlt())

n = inp()
for t in range(n):
    b = inp()
    # mark the position of b
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0
res = "No"
# see row wise:
for i in range(3):
    s = 0
    for j in range(3):
        s += A[i][j]
    if s == 0:
        res = "Yes"
        break
# see column wise
for i in range(3):
    s = 0
    for j in range(3):
        s += A[j][i]
    if s == 0:
        res = "Yes"
        break
# see diagonal
s = 0
for i in range(3):
    for j in range(3):
        if i == j:
            s += A[j][i]
if s == 0:
    res = "Yes"

s = 0
for i in range(3):
    for j in range(3):
        if i == j:
            s += A[j][i]
if s == 0:
    res = "Yes"

if A[0][2] == A[1][1] == A[2][0]:
    res = "Yes"

print(res)
