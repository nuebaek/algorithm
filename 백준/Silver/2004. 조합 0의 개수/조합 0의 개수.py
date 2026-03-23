import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def solve(n, k):
    result = 0
    temp = k

    while temp <= n:
        result += n // temp
        temp *= k

    return result

two = solve(n, 2) - solve(m, 2) - solve(n-m, 2)
five = solve(n, 5) - solve(m, 5) - solve(n-m, 5)

print(min(two, five))