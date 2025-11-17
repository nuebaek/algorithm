n = int(input())

people = [list(map(int, input().split())) for _ in range(n)]

answer = []
# 모든 사람과 비교
for i in range(n):
    rank = 1
    for j in range(n):
        if people[i] == people[j]:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    answer.append(rank)

print(*answer)