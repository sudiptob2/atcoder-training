# For taking integer inputs.
def inp():
    return(int(input()))


A = inp()
B = inp()
C = inp()
X = inp()
r = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            temp = i * 500 + j*100 + k * 50
            if temp == X:
                r += 1
print(r)
