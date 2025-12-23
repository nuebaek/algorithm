import sys
input = sys.stdin.readline

n = int(input())
a = [input().split() for _ in range(n)]

a.sort(key = lambda x:int(x[0]))

for i in a:
    print(*i)