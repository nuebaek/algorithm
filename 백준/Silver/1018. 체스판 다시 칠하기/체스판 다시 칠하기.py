n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(input())

min_num = 64

for r in range(n-7):  # 8*8 영역의 시작점을 찾으므로 -7
    for c in range(m-7):
        count_w_start = 0  # w로 시작하는 케이스에서 칠해야할 갯수
        count_b_start = 0  # b로 시작하는 케이스에서 칠해야할 갯수
        for i in range(r, r+8):  # 8*8 영역 탐색
            for j in range(c, c+8):
                if (i+j)%2 == 0:  # (행+열)이 짝수면 W시작은 W, B시작은 B
                    if graph[i][j] != 'W':
                        count_w_start += 1
                    elif graph[i][j] != 'B':
                        count_b_start += 1
                else:  # (행+열)이 홀수면 W시작은 B, B시작은 W
                    if graph[i][j] != 'B':
                        count_w_start += 1
                    elif graph[i][j] != 'W':
                        count_b_start += 1

        current = min(count_w_start, count_b_start)  # 두 케이스에서 칠해야 하는 개수의 최소값을 구한다

        if current < min_num:
            min_num = current

print(min_num)
