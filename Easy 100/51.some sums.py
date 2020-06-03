# For taking space seperated integer variable inputs.
def invr():
    return(map(int, input().split()))


def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


N, A, B = invr()

S = 0
for i in range(1, N+1):
    s = sum_of_digits(i)
    if s >= A and s <= B:
        S += i
print(S)
