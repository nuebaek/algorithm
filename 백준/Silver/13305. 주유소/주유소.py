import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_price = cost[0]
price = 0

for i in range(len(distance)):
    price += distance[i] * min_price

    if cost[i+1] < min_price:
        min_price = cost[i+1]

print(price)