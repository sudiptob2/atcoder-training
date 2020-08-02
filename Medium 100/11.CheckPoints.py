n, m = map(int, input().split())
student = dict()
checkpoint = dict()
distance = dict()

for i in range(n):
    student[i] = list(map(int, input().split()))

for i in range(m):
    checkpoint[i] = list(map(int, input().split()))

for key in student:
    x1, y1 = student[key]
    minD = 10000000001
    minP = 10000000001
    for p in checkpoint:
        x2, y2 = checkpoint[p]
        d = abs(x1 - x2) + abs(y1 - y2)
        if d < minD:
            minP = p
            minD = d
    print(minP+1)
