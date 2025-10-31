x = int(input().strip())          
change = 1000 - x               
coins = [500, 100, 50, 10, 5, 1]

ans = 0
for c in coins:
    ans += change // c
    change %= c

print(ans)