import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1 and scoville[0] < k:
        scv1 = heapq.heappop(scoville)
        scv2 = heapq.heappop(scoville)
        heapq.heappush(scoville, scv1+(scv2*2))
        answer += 1
    if scoville[0] < k:  
        return -1
    return answer