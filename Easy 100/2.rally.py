import math


def inp():
    return(int(input()))


def invr():
    return(map(int, input().split()))


n = inp()
arr = invr()
arr = sorted(arr)
max = arr[n-1]
min = arr[0]

cost = 100000000000
for p in range(min, max+1):
    temp_cost = 0
    for xi in arr:
        temp_cost += (xi-p)**2
    if temp_cost < cost:
        cost = temp_cost
print(cost)
