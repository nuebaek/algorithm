def solution(A, B):
    answer = A
    for i in range(len(A)):
        if answer == B:
            return i
        # 오른쪽으로 한 칸 밀기
        answer = answer[-1] + answer[:-1]
    return -1