d = input()

f = int(d[0])
res = (len(d)-1)*9 + f-1
s = 0
for i in d:
    s += int(i)

print(max(res, s))
