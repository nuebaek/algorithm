def solution(picture, k):
    answer = []
    for i in picture:
        total = ""
        # 가로 확대
        for j in i:
            total += j * k
        # 세로 확대
        for _ in range(k):
            answer.append(total)
    return answer