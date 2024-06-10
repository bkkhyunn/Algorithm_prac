# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한이 있다.
# 그렇다면 몸무게가 많이 나가는 사람부터 태우고, 가벼운 사람 중에 태울 수 있는 사람을 태우면 된다.

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    queue = deque(people)
    
    while queue:
        max_weight = queue.popleft()
        sum_weight = max_weight
        
        if queue and (sum_weight + queue[-1] <= limit):
            min_weight = queue.pop()
            sum_weight += min_weight
        
        answer += 1
        
    return answer