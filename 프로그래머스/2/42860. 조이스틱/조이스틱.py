def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, n in enumerate(name):
        answer += min(ord(n) - ord("A"), ord("Z") - ord(n) + 1)
        next = i + 1
        
        while next < len(name) and name[next] == "A":
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
        
    answer += min_move
    return answer