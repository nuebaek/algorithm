def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i>0:
            if arr[i]==arr[i-1]:
                pass
            else:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer