import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()
    first = 0
    result = 1

    for i in range(1, len(rank)):
        if rank[i][1] < rank[first][1]:
            first = i
            result += 1

    print(result)
