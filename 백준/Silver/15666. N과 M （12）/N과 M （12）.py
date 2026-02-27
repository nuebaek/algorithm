import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

answer = [0]*m

def backtracking(k, idx):
    if k == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return

    temp = 0
    for i in range(idx, n):
        if temp != array[i]:
            answer[k] = array[i]
            temp = array[i]
            backtracking(k+1, i)

backtracking(0, 0)