def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i: # answer가 존재할 때만
            answer.pop()
            k -= 1
        answer.append(i)
    if k>0:
        answer = answer[:-k]
    return ''.join(answer)