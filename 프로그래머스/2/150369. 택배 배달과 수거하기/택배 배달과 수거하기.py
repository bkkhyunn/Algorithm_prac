def solution(cap, n, deliveries, pickups):
    answer = 0
    
    for i in range(n):
        if deliveries[n-1-i] or pickups[n-1-i]:
            answer += (n-i) * 2
            break
    
    while deliveries or pickups:
        d_cap, p_cap = cap, cap
        
        while deliveries:
            if d_cap >= deliveries[-1]:
                d_cap -= deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= d_cap
                break
        
        while pickups:
            if p_cap >= pickups[-1]:
                p_cap -= pickups[-1]
                pickups.pop()
            else:
                pickups[-1] -= p_cap
                break
                
        answer += max(len(deliveries), len(pickups)) * 2
    
    return answer