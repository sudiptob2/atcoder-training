def invr():
    return(map(int, input().split()))


A, B, C, K = invr()
res = B - A
if K % 2 == 0:
    res = A - B
if abs(res) > 1000000000000000000:
    print(" Unfair ")
else:
    print(res)
