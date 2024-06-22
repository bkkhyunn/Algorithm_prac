# 가장 먼 집부터 들러서 배달과 수거를 해결하면 최소 거리로 이동 가능 (그리디)
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 맨 처음 트럭이 가야할 가장 먼 거리. 배달이든 수거든 한 개라도 있으면 가야 한다.
    for i in range(n):
        if deliveries[n-1-i] or pickups[n-1-i]:
            answer += (n-i) * 2
            break
    
    while deliveries or pickups:
        d_cap, p_cap = cap, cap
        
        # 트럭이 이동하면서 먼 거리부터 배달을 해결한다.
        while deliveries:
            if d_cap >= deliveries[-1]:
                d_cap -= deliveries[-1]
                deliveries.pop()
            # 한 번에 배달을 못하더라도 할 수 있을 만큼 배달.
            else:
                deliveries[-1] -= d_cap
                break
        
        # 트럭이 이동하면서 먼 거리부터 수거를 해결한다.
        while pickups:
            if p_cap >= pickups[-1]:
                p_cap -= pickups[-1]
                pickups.pop()
            # 한 번에 수거를 못하더라도 할 수 있을 만큼 수거.
            else:
                pickups[-1] -= p_cap
                break
        
        # 배달과 수거 중 먼 거리에 있는 집은 무조건 들러야 한다.
        answer += max(len(deliveries), len(pickups)) * 2
    
    return answer

# 개선된 방법
from itertools import zip_longest

def box_list(l):
    '''
    box에 거리를 대응시켜서 box 개수 크기의 list 를 반환
    
    ex. [1, 0, 3, 1, 2] -> [1, 3, 3, 3, 4, 5, 5]
    1번째 집에 box 1개
    3번째 집에 box 3개
    4번째 집에 box 1개
    5번째 집에 box 2개
    '''
    n = []
    for i,d in enumerate(l):
        for _ in range(d):
            n.append(i+1)
    return n

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_box = box_list(deliveries)
    p_box = box_list(pickups)
    
    # 먼 거리의 box 부터 배달/수거 하기 위해 뒤집기
    d_box.reverse()
    p_box.reverse()
    
    # cap 개 만큼 트럭에 실을 수 있기 때문에 step 으로 cap
    d_box = d_box[::cap]
    p_box = p_box[::cap]
    
    # 트럭이 한 번 움직일 때 움직이는 가장 긴 거리
    # 긴 거리부터 처리하면서 배달/수거 개수를 줄이면 그리디의 정당성이 보장된다.
    for d, p in zip_longest(d_box, p_box, fillvalue=0):
        answer += max(d, p) * 2
    
    return answer