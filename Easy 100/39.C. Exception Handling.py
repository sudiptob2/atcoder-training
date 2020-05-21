# For taking integer inputs.
def inp():
    return(int(input()))


N = inp()
A = []
i1, i2 = 0, 0

for i in range(N):
    A.append(inp())

srt = sorted(A)
m1 = srt[-1]
m2 = srt[-2]

for i in range(N):
    if A[i] == m1:
        print(m2)
    else:
        print(m1)
