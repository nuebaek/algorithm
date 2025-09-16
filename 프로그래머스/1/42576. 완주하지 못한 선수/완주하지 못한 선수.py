def solution(participant, completion):
    counts = {}
    for i in participant:
        counts[i] = counts.get(i, 0) + 1
    for j in completion:
        counts[j] -= 1
    for name, cnt in counts.items():
        if cnt > 0:
            return name