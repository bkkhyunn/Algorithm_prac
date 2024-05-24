import copy
from collections import deque

def solution(prices):
    answer = []
    queue = deque(copy.deepcopy(prices))
    for price in prices:
        queue.popleft()
        count = 0
        for val in queue:
            count += 1
            if val < price:
                break
        answer.append(count)
    return answer