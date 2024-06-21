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