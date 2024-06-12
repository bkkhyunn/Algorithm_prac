# 우선순위 큐 다익스트라 -> 다익스트라는 매 순간 최소 비용만을 고려하지만 총 비용을 고려하지는 않는다.
# 즉 특정 노드에서 다른 모든 노드까지의 최소 비용을 구하지만, 그 비용들의 총합이 최소가 되는 것을 보장하지 않는다.
# 따라서 이 문제에서는 최소 신장 트리(크루스칼 혹은 프림) 알고리즘이 적절하다.
import heapq

def solution(n, costs):
    answer = 1e10
    
    graph = [[] for _ in range(n)]
    
    for start, end, cost in costs:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
        
    def dijkstra(start):
        nonlocal distance, min_cost
        queue = []
        
        heapq.heappush(queue, (0, start))
        distance[start] = 0
        min_cost[start] = 0
        
        while queue:
            
            dist, now = heapq.heappop(queue)
            
            if distance[now] < dist:
                continue
                
            for node, node_cost in graph[now]:
                cost = dist + node_cost
                
                if cost <= distance[node]:
                    distance[node] = cost
                    min_cost[node] = node_cost
                    
                    heapq.heappush(queue, (cost, node))
    
    for i in range(n):
        distance = [float('inf')] * n
        min_cost = [float('inf')] * n
        dijkstra(i)
        
        #print(distance)
        #print(min_cost)
    
        answer = min(answer, sum(min_cost))

    return answer

# 최소 신장 트리 - 크루스칼 알고리즘 (그리디의 일종)

def solution(n, costs):
    
    parent = [0] * n
    
    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges, result = [], 0
    
    for a, b, cost in costs:
        edges.append((cost, a, b))
    
    edges.sort()
    
    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i
    
    def find_parent(parent, x):
        # 루트 노드를 찾을 때까지 재귀 호출.
        if parent[x] != x:
            # 경로 압축
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    # 간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    return result