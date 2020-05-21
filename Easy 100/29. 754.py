s = input()
n = len(s)
for i in range(n):
    slc = s[i:i+3]
    if i == 0:
        d = abs(753 - int(slc))
    else:
        d = min(d, abs(753 - int(slc)))
print(d)
