import sys
input = sys.stdin.readline

n = int(input())
ans = 0

col = [False] * n
diag1 = [False] * (2 * n) 
diag2 = [False] * (2 * n) 

def solve(x):
    global ans
    
    if x == n:
        ans += 1
        return
    
    for i in range(n):
        if not col[i] and not diag1[x+i] and not diag2[x-i+n-1]:
            col[i] = diag1[x+i] = diag2[x-i+n-1] = True
            solve(x+1)
            col[i] = diag1[x+i] = diag2[x-i+n-1] = False

solve(0)
print(ans)