def solution(sizes):
    answer = 0
    row = []
    col = []
    for i in sizes:
        i.sort()
        row.append(i[0])
        col.append(i[1])
    answer = (max(row)*max(col))
    return answer
