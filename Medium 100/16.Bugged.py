def inp():
    return(int(input()))


n = inp()
scores = [0]
for i in range(n):
    scores.append(inp())
scores = sorted(scores)
d = 0
for s in scores:
    sm = sum(scores)
    if sm % 10 == 0:
        sm -= s
    if sm % 10 != 0:
        d = sm
        break
print(d)
