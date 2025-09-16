import heapq
def solution(participant, completion):
    heapq.heapify(participant)
    heapq.heapify(completion)
    while completion:
        p = heapq.heappop(participant)
        c = heapq.heappop(completion)
        if p!=c:
            return p
    return heapq.heappop(participant)