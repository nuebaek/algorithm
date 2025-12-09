n, l = map(int, input().split())
place = list(map(int, input().split()))
place.sort()

tape_end = 0
count = 0

for i in place:
    if i < tape_end:
        continue
    else:
        count += 1
        tape_end = i - 0.5 + l

print(count)