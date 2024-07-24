import heapq

# n : 노드 개수, m : 간선 개수
n, m, x = map(int, input().split())
# 단방향
graph = [[] for _ in range(n+1)]
# 최소 거리 중 최댓값
answer = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(start):
    distance = [1e9] * (n+1)
    queue = []
    
    # (cost, node) 식으로 우선순위큐 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        
        cost, now = heapq.heappop(queue)
        
        # 방문한 적이 있으면 넘어가기
        if distance[now] < cost:
            continue
        
        # graph -> (next_node, cost)
        for i in graph[now]:
            dist = cost + i[1]
            
            if dist < distance[i[0]]:
                distance[i[0]] = dist
                heapq.heappush(queue, (dist, i[0]))
                
    return distance

to_home = dijkstra(x)
for start in range(1, n+1):
    answer = max(answer, dijkstra(start)[x] + to_home[start])
    
print(answer)