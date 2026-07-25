from collections import deque

def cal(words1, words2):
    # 현재 단어와 대상 단어 넣었을 때, 알파벳 하나만 차이나는지 확인하는 것
    count = 0
    if words1 == words2:
        return False
    
    for i in range(len(words1)):
        if ord(words1[i])-ord(words2[i]) != 0: # 바뀌는 알파벳 개수 카운트
            count += 1
            
    return True if count ==1 else False

            
def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = set()                       
    while q:
        now, dis = q.popleft()
        if now == target:                  
            return dis
        
        for i in words:
            if i == now or i in visited:   
                continue
            if cal(list(now), list(i)):
                visited.add(i)             
                q.append((i, dis + 1))  
                
    return 0