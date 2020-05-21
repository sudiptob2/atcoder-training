# For taking integer inputs.
def inp():
    return(int(input()))


# For taking List inputs.
def inlt():
    return(list(map(int, input().split())))


n = inp()

arr = inlt()

arr = sorted(arr)
a = 0
b = 0
for i in range(n):
    if i % 2 == 0:
        a += arr[i]
    else:
        b += arr[i]
print(abs(a-b))
