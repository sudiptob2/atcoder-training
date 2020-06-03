S = input()
T = input()

N = len(S)
res = "No"
for i in range(N+1):
    r = S[-1] + S[:N-1]
    if r == T:
        res = "Yes"
        break
    S = r

print(res)
