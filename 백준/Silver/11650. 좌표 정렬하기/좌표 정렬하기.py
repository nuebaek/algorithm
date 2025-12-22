import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort()
# a.sort(key=lambda x:(x[0], x[1]))

for i in a:
    print(*i)