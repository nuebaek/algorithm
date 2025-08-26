def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for x in str(i):
            if x != '0' and x != '5':
                break
        else:
            answer.append(i)
    return answer if answer else [-1]