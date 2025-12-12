import sys
input = sys.stdin.readline

n = int(input())
room = [input().strip() for _ in range(n)]

w = 0
h = 0

# 가로
for r in room:
    for part in r.split('X'):
        if len(part) >= 2:
            w += 1

# 세로
for i in range(n):
    col = ""
    for j in range(n):
        col += room[j][i]
    for part in col.split('X'):
        if len(part) >= 2:
            h += 1

print(w, h)