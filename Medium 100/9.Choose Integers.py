A, B, C = map(int, input().split())
f = False
for i in range(1, B):
    if A*i % B == C:
        f = True
        break
if f:
    print("YES")
else:
    print("NO")
