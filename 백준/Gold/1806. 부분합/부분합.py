n, s = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0
sum = a[0]
length = 100001

while True:
    if sum < s:
        end += 1
        if end == n: break
        sum += a[end]
    else:
        sum -= a[start]
        length = min(length, end - start + 1)
        start += 1

if length != 100001:
    print(length)
else:
    print(0)