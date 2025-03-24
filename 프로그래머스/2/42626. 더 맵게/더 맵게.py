import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] > K:
        return answer
    
    if scoville[0] + scoville[1] == 0:
        return -1
    
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        
        if min1 >= K:
            break
        
        new_value = min1 + (min2 * 2)
        heapq.heappush(scoville, new_value)
            
        answer += 1
    
    if len(scoville) and scoville[0] < K:
        return -1
    
    return answer