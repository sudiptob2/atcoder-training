S = input()
N = len(S)
f = True
# first condition
if S[0] != "A":
    f = False
# 2nd condition
c = 0
for i in range(2, N-1):
    if S[i] == "C":
        c += 1
if c != 1:
    f = False

# 3rd cindition
for i in S:
    if i not in "AC":
        if i != i.lower():
            f = False
            break
if f:
    print("AC")
else:
    print("WA")
