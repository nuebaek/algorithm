import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def check(x, y, n):
    global white, blue
    first_color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first_color:
                half = n // 2
                check(x, y, half)  
                check(x, y + half, half) 
                check(x + half, y, half) 
                check(x + half, y + half, half) 
                return

    if first_color == 0:
        white += 1
    else:
        blue += 1

check(0, 0, n)
print(white)
print(blue)