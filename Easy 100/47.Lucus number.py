def inp():
    return(int(input()))


dp = [0]*87
dp[0] = 2
dp[1] = 1


def lucas(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = lucas(n-1) + lucas(n-2)
    return dp[n]


n = inp()
print(lucas(n))
