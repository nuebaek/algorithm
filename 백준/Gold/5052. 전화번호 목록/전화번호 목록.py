import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    lst = [input().strip() for _ in range(n)]
    lst.sort()
    
    for i in range(n-1):
        if lst[i+1].startswith(lst[i]):
            print("NO")
            return  
    print("YES")

t = int(input())
for _ in range(t):
    solve() 