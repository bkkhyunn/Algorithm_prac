def solution(routes):
    answer = 1
    routes.sort()
    
    left, right = -30000, 30000
    
    for route in routes:
        start, end = route
        
        left = start
        
        if end <= right:
            right = end
            
        if right - left < 0:
            answer += 1
            right = end
    
    return answer