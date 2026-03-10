import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    s = input().strip()

    x, y = 0, 0
    direction = 0 

    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for cmd in s:
        if cmd == 'F':
            x += dx[direction]
            y += dy[direction]
        elif cmd == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif cmd == 'L':
            direction = (direction-1)%4
        elif cmd == 'R':
            direction = (direction+1)%4

        if cmd in ('F', 'B'):
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    print((max_x-min_x) * (max_y-min_y))