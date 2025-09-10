def solution(n, lost, reserve):
    lost_left = sorted(set(lost) - set(reserve))
    reserve_left = sorted(set(reserve) - set(lost))
    for r in reserve_left:
        if (r - 1) in lost_left:
            lost_left.remove(r - 1)
        elif (r + 1) in lost_left:
            lost_left.remove(r + 1)
    return n - len(lost_left)