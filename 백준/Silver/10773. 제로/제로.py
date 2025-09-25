import sys
n = int(input())
k = [int(sys.stdin.readline().strip()) for _ in range(n)]
res = []

def solution(n, k):
    for i in k:
        if i==0 and res:
            res.pop()
        else:
            res.append(i)
    if len(res)==0:
        return 0
    else:
        return sum(res)
        
print(solution(n, k))