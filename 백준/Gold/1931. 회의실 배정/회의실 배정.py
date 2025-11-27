n = int(input())
room = [list(map(int, input().split())) for i in range(n)]

room.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for s, e in room:
    if s >= end_time:
        count += 1
        end_time = e

print(count)