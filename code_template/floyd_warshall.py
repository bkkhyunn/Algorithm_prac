INF = int(1e9) # 무한

# 노드의 개수 n, 간선의 개수 m
n, m = 100, 100
# 2차원 리스트(그래프 표현)를 만들고 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력받고 그 값으로 초기화
for _ in range(m):
    # A 에서 B 로 가는 비용은 C 라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행 (3중 반복문)
# k 는 거쳐가는 노드, a 는 출발 노드, b 는 도착 노드
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b])