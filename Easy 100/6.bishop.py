
def invr():
    return(map(str, input().split()))


h, w = invr()

c = (int((h+1)/2)*w)
if h % 2 != 0:
    c = c - (w-1)/2
if h == 1 or w == 1:
    c = 1
print(int(c))
