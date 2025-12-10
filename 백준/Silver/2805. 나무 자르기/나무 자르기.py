import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    mid = (start + end)//2
    count = 0
    for i in range(n):
        if array[i] > mid:
            count += array[i] - mid
            if count >= m:
                break
    if count < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)