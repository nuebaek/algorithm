def solution(clothes):
    closet={}
    for name, kind in clothes:
        if kind not in closet:
            closet[kind] = []
        closet[kind].append(name)
        
    answer=1
    for kind in closet:
        answer *= (len(closet[kind])+1)
    return answer-1