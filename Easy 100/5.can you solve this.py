def inlt():
    return(list(map(int, input().split())))


def invr():
    return(map(int, input().split()))


n, m, c = invr()
B = inlt()
A = []
for t in range(n):
    A.append(inlt())
# print(A)
# print(B)

correct = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += A[i][j]*B[j]
    s += c
    if s > 0:
        correct += 1
print(correct)
