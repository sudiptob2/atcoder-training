# For taking integer inputs.
def inp():
    return(int(input()))


n = inp()

i = 0
while 2**i <= n:
    i += 1
if i > 0:
    i -= 1
print(2**(i))
