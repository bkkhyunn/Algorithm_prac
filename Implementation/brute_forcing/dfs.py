def dfs_recur(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 인접 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_recur(graph, i, visited)
            
def dfs_stack(graph, start):
    # 각 노드가 방문된 정보를 표현 (1차원 리스트)
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            # 인접 노드를 스택에 추가 (역순으로 추가하여 작은 노드부터 처리)
            for neighbor in reversed(graph[v]):
                if not visited[neighbor]:
                    stack.append(neighbor)

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

dfs_recur(graph, 1, visited)
dfs_stack(graph, 1)