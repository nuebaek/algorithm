def solution(array, commands):
    answer = []
    sorting = []
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        sorting = array[i-1:j]
        sorting.sort()
        element = sorting[k-1]
        answer.append(element)
    return answer
