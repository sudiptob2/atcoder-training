import math


# For taking integer inputs.
def inp():
    return(int(input()))


# For taking List inputs.
def inlist():
    return(list(map(int, input().split())))


# For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
def instr():
    s = input()
    return(list(s[:len(s)]))


# For taking space seperated integer variable inputs.
def invr():
    return(map(int, input().split()))


def isPrime(n):
    if n < 2:
        return False
    limit = int(math.sqrt(n+1))
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


n = inp()

while True:
    if isPrime(n):
        print(n)
        break
    n += 1
