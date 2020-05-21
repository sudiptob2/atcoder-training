def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


n = inp()
K = inp()
X = inlt()

ans = 0
for i in range(n):
    ans += min(X[i], K-X[i])
print(ans*2)
