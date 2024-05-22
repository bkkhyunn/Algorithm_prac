import heapq

def solution(scoville, K):
    blending = 0
    heapq.heapify(scoville)
    
    # scoville 의 제일 작은 수와 그 다음 수가 둘 다 0 일 때
    if scoville[0] == 0 and scoville[1] == 0:
        return -1
    
    while True:
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        if len(scoville) == 1 and scoville[0] >= K:
            break
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        if first >= K and second >= K:
            break
        
        new = first + (second * 2)
        
        heapq.heappush(scoville, new)
        blending += 1
    
    return blending