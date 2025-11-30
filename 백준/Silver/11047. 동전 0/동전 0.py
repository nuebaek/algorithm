n, k = map(int, input().split())
price = [int(input()) for _ in range(n)]

price.sort(reverse=True)
answer = 0
current = k

for i in price:
    if current == 0:
        break
    if current >= i:
        cnt = current//i
        answer += cnt
        current -= (cnt * i)
    else:
        continue

print(answer)