import heapq
# 우선순위 큐를 이용.
# 라운드별 적의 수를 힙에 누적시키면서, 총 적의 수가 병사의 수보다 크게되는 시점에
# 적의 수가 가장 큰 라운드의 적을 힙에서 제외시키면 가장 큰 적 수에 무적권을 쓰는 것과 같다.
def solution(n, k, enemy):
    heap = []
    clear = 0
    total_enemy = 0
    
    for e in enemy:
        # max heap 동작
        heapq.heappush(heap, -e)
        total_enemy += e
        # 지금까지의 모든 적 수가 병사 수보다 많을 때
        if total_enemy > n:
            # 무적권이 없으면 라운드 리턴
            if not k:
                return clear
            # 무적권이 있으면 힙에서 가장 큰 적 수를 제거하고, 무적권 1 차감
            total_enemy += heapq.heappop(heap)
            k-=1
            
        clear += 1
                
    return clear