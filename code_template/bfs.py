from collections import deque

def bfs(graph, start, visited):
    # deque 라이브러리를 이용하여 큐 구현
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 모두 큐에 삽입하고 방문처리
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True
                
graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)