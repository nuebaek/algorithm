from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) > 0:
        cur = prices.popleft()
        sum=0
        for i in prices:
            sum += 1
            if i < cur:
                break
        answer.append(sum)
    return answer
