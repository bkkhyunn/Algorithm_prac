# 간단한 다익스트라 알고리즘 구현
# 노드의 개수 n, 간선의 개수 m
n, m = 100, 100

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단 거리 테이블
distance = [1e9] * (n+1)

# 그래프 내용 채우기(간선 정보 입력받기)
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = 1e9
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index += 1
    return index
    
# 다익스트라 최단 거리 알고리즘
def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    # 출발 노드로부터 당장 도달이 가능한 다른 노드까지의 거리를 먼저 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
        
            # 현재 선택된 노드까지의 거리(distance[now]) 값에 현재 노드와
            # 연결된 거리 값을 더해서 cost 를 만든다.
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
start = 0
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == 1e9:
        print("INFINITY")
    else:
        print(distance[i])
        

# 우선순위 큐를 활용한 개선된 다익스트라 알고리즘 구현
import heapq

# 노드의 개수 n, 간선의 개수 m

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 (무한으로 초기화)
distance = [1e9] * (n+1)

# 그래프 내용 채우기(간선 정보 입력받기)
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))
    
# 다익스트라 최단 거리 알고리즘
def dijkstra(start):
    queue = []
    
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    # queue 가 비어있지 않다면
    while queue:
    
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                
                # 값이 갱신되면 우선순위 큐에 해당 정보 기록
                heapq.heappush(queue, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == 1e9:
        print("INFINITY")
    else:
        print(distance[i])