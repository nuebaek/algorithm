from collections import deque

def solution(priorities, location):
    answer = 0
    que = []
    que = [(i, p) for i, p in enumerate(priorities)]
    que = deque(que)
    
    while que:
        idx, p = que.popleft()

        if any(p2 > p for idx, p2 in que):
            que.append((idx, p))  
            continue

        answer += 1
        if idx == location:
            return answer
