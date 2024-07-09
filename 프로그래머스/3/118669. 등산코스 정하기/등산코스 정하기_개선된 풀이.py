from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    
    gates = set(gates)
    summits = set(summits)
    
    # 양방향 그래프 만들기 (해시)
    graph = defaultdict(list)
    for start, end, weight in paths:

        graph[start].append((weight, end))
        graph[end].append((weight, start))

    dp = [1e9] * (n+1) # 최소 강도(비용)로 움직였을 때, 각 지점에서 최대 강도
    queue = []
    
    for gate in gates:
        heappush(queue,(0, gate))
        dp[gate] = 0 

    while queue:
        
        intensity, now = heappop(queue)

        # 현재 노드가 산봉우리거나, 현재 intensity 가 dp 에 기록된 강도보다 크다면 종료
        if now in summits or dp[now] < intensity:
            continue

        for next_intensity, next_node in graph[now]:

            # 현재 intensity 와 next_intensity 중 최대값 계산
            max_intensity = max(intensity, next_intensity)

            # dp 에 기록된 강도보다 최대강도가 작다면
            if max_intensity < dp[next_node]:
                heappush(queue, (max_intensity, next_node))
                dp[next_node] = max_intensity


    # [summit, intensity]
    answer = [0 , 1e9]

    for summit in summits:
        if dp[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dp[summit]
        elif dp[summit] == answer[1]:
            answer[0] = min(answer[0], summit)

    return answer