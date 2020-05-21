
def invr():
    return(map(int, input().split()))


a, b = invr()
c = 0
outlet = 1
while outlet < b:
    outlet -= 1
    outlet += a
    c += 1
print(c)
