# 크루스칼 알고리즘은 간선 중심, 프림 알고리즘은 정점 중심으로 동작한다.

import heapq

def prim(v, adj):
    '''
    1. 시작 노드를 우선순위 큐에 삽입한다. 시작 노드는 간선 가중치가 0이 된다.
    2. 우선순위 큐에서 노드를 하나 빼서 그래프에 포함시킨다. 해당 노드와 연결되어 있으면서 그래프에 포함되지 않은 노드들을 우선순위 큐에 삽입한다.
    3. 우선순위 큐에서 노드를 뺐을 때 그래프에 속해 있다면 아무 작업도 하지 않는다.
    4. 우선순위 큐가 비게 되면 종료한다.
    '''
    # 그래프 (방문 처리와 같음)
    visited = [False] * (v + 1)
    min_heap = [(0, 1)]  # (cost, start_node)
    result = 0
    edges_used = 0 # 사용된 간선 개수(간선 개수는 항상 노드 개수보다 1만큼 작다)
    
    while min_heap and edges_used < v:
        cost, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        result += cost
        edges_used += 1
        
        for next_cost, next_node in adj[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_cost, next_node))
                
    return result

v = 4  # 노드의 개수
adj = {
    1: [(1, 2), (3, 3)],
    2: [(1, 1), (3, 3), (6, 4)],
    3: [(3, 1), (3, 2), (2, 4)],
    4: [(6, 2), (2, 3)]
}

print("Prim's MST cost:", prim(v, adj))