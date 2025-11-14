n, x = map(int, input().split())
visitor = list(map(int, input().split()))

cur = sum(visitor[:x])
max_sum = cur
count = 1

for i in range(x, n): 
    cur += visitor[i] - visitor[i - x]
    if cur > max_sum:
        max_sum = cur
        count = 1
    elif cur == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)