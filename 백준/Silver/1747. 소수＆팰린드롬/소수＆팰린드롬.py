n = int(input())

def reverse(x):
    if x == int(str(x)[::-1]):
        return True
    return False

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

t = n

while True:
    if reverse(t) and isPrime(t):
        print(t)
        break
    t += 1