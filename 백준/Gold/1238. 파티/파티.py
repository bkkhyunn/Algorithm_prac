import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(start):
    distance = [1e9] * (n+1)
    queue = []
    
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        
        cost, now = heapq.heappop(queue)
        
        if distance[now] < cost:
            continue
        
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