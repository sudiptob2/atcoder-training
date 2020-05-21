# For taking integer inputs.
def inp():
    return(int(input()))


n = inp()
i = 1
while n > 1:
    n = int(n/2)
    i += 1
print(2**i - 1)
