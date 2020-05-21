s = input()
N = len(s)
c1 = 0
c2 = 0
for i in range(N):
    if i % 2 == 0:
        if s[i] != '0':
            c1 += 1
        else:
            c2 += 1
    else:
        if s[i] != '1':
            c1 += 1
        else:
            c2 += 1
print(min(c1, c2))
