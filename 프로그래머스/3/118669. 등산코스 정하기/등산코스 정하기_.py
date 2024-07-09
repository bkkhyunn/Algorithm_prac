# 출입구 하나, 산봉우리 하나
# 출입구 - 산봉우리, 산봉우리 - 출입구 두 방향에서 최소 비용은 같다. 따라서 출입구 - 산봉우리 한 번만 구한다.
# 이 때 우선순위 큐 & bfs를 활용한다.
# 최소 비용으로 이동하면서 목적지에 도달했을 때, 그 중 최대값이 intensity 가 된다.
# 출입구와 산봉우리 조합이 25억개가 될 수 있으므로 DP 를 이용하여 산봉우리에서의 강도를 구한다.

import heapq

def solution(n, paths, gates, summits):
    
    # hash 화 시키기
    summits = set(summits)
    gates = set(gates)
    
    # 양방향 그래프 만들기
    graph = [[] for _ in range(n+1)]
    
    for path in paths:
        start, end, cost = path
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    # dp[i] 는 i 지점까지의 최대 강도
    dp = [1e9] * (n+1)
        
    def bfs(gates, visited):
        nonlocal graph, dp, summits
        
        # (cost(=intensity), node) 형식으로 우선순위 큐 넣기
        queue = []
        
        # 출입구 큐에 삽입
        for gate in gates:
            
            heapq.heappush(queue, (0, gate))
            dp[gate] = 0 # 출입구 dp 초기화. 출입구까지의 강도는 0
        
        while queue:
            
            cost, now = heapq.heappop(queue)
            
            # 산봉우리는 도착지점이기 때문에 넘어간다.
            if now in summits:
                continue
            
            # 여러 출입구에서 같은 지점을 지날 수 있는데 각 지점에서의 강도보다 현재 강도가 크면 무시한다.
            if dp[now] < cost:
                continue
            
            # 양방향 그래프이기 때문에 방문 처리를 한다.
            visited[now] = True
            
            for next_node, next_cost in graph[now]:
                
                # 출입구는 한개만 존재해야 한다.
                if next_node in gates:
                    continue
                
                # 이미 방문했으면 넘어간다. 
                if visited[next_node]:
                    continue
                
                # dp에 기록되는 최대 강도가 낮은 걸 구하는 것이므로 dp 에 기록된 강도보다 현재 강도가 낮을 때만 실시.
                if next_cost < dp[next_node]:
                    # 현재 지점까지의 최대강도와 다음 지점까지의 강도 중 최대값이 dp 에 기록되는 최대강도
                    # 위 최대강도를 기존의 다음 지점까지의 최대강도와 비교해서 작은 값을 기록
                    dp[next_node] = min(dp[next_node], max(dp[now], next_cost))
                    heapq.heappush(queue, (next_cost, next_node))

    visited = [False] * (n+1)
    bfs(gates, visited)
    
    intensity = 1e9
    final_summit = 1e9
    
    for summit in summits:
        if dp[summit] < intensity:
            intensity = dp[summit]
            final_summit = summit
        elif dp[summit] == intensity:
            final_summit = min(final_summit, summit)
    
    return [final_summit, intensity]