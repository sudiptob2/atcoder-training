def invr():
    return(map(int, input().split()))


A, B = invr()
c = 0
for i in range(A, B+1):
    i = str(i)
    if i == i[::-1]:
        c += 1
print(c)
