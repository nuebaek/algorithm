import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room_map = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방향 전환
def get_d_index_turn_left(d):
    return (d + 3) % 4

# 후진
def get_d_index_go_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(n, m, r, c, d, room_map):
    count = 1
    room_map[r][c] = 2
    queue = deque([[r, c, d]])

    while queue:  # 큐가 비면 종료
        r, c, d = queue.popleft()
        cur_d = d

        for i in range(4):
            cur_d = get_d_index_turn_left(cur_d)
            cur_r, cur_c = r+dr[cur_d], c+dc[cur_d]

            if 0<=cur_d<n and 0<=cur_c<m and room_map[cur_r][cur_c]==0:  # 벽이 아니면서 청소되지 않은 경우
                count += 1
                room_map[cur_r][cur_c] = 2 # 새롭게 방문한 경우 visited 생성 대신 2로 저장
                queue.append([cur_r, cur_c, cur_d])
                break

            elif i == 3:  # 주변이 모두 청소된 경우
                cur_d = get_d_index_go_back(d) # 현재 방향 유지
                cur_r, cur_c = r+dr[get_d_index_go_back(d)], c+dc[get_d_index_go_back(d)]
                queue.append([cur_r, cur_c, d])

                if room_map[cur_r][cur_c]==1:  # 뒤가 벽인 경우
                    return count

print(get_count_of_departments_cleaned_by_robot_vacuum(n, m, r, c, d, room_map))